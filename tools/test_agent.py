#!/usr/bin/env python3
"""Regression checks for saved SubAgent 6 examples; not a live model test."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "agents" / "organizational_adoption"
EXPECTED = {
    "primary": "HOLD",
    "contrast_1": "PILOT ONLY",
    "contrast_2": "REQUEST EVIDENCE",
    "known_absence": "HOLD",
    "sustainment": "REQUEST EVIDENCE",
    "review_competence": "REQUEST EVIDENCE",
}
INPUT = json.loads((ROOT / "core" / "input_schema.json").read_text())
OUTPUT = json.loads((ROOT / "core" / "output_schema.json").read_text())
DIMENSIONS = ("Leadership/sponsorship", "Skills/training", "Workflow/process",
              "Infrastructure/data", "Resources/budget", "Governance/risk",
              "Culture/change", "Operating ownership")

def check(condition, message):
    if not condition:
        raise AssertionError(message)

def validate_type(value, spec, label):
    kind = spec.get("type")
    types = {"string": str, "object": dict, "array": list}
    if kind in types:
        check(isinstance(value, types[kind]), f"{label}: expected {kind}")
    if kind == "object":
        for field in spec.get("required", []):
            check(field in value, f"{label}: missing {field}")
        if spec.get("additionalProperties") is False:
            check(set(value) <= set(spec.get("properties", {})), f"{label}: extra keys")
        for key, sub in spec.get("properties", {}).items():
            if key in value:
                validate_type(value[key], sub, f"{label}.{key}")
    if kind == "array" and "items" in spec:
        for i, item in enumerate(value):
            validate_type(item, spec["items"], f"{label}[{i}]")

def main():
    subprocess.run([sys.executable, str(ROOT / "tools" / "check_frozen_core.py")], check=True)
    baseline = None
    for case, decision in EXPECTED.items():
        source = json.loads((AGENT / "cases" / (case + ".json")).read_text())
        response = json.loads((AGENT / "responses" / (case + ".json")).read_text())
        validate_type(source, INPUT, case + ".input")
        validate_type(response, OUTPUT, case + ".response")
        check(response["recommendation_management_implication"].startswith(decision),
              f"{case}: unexpected decision")
        for dim in DIMENSIONS:
            check(dim in response["organization_specific_finding"], f"{case}: missing {dim}")
        check(response["abstention_or_more_information_needed"], f"{case}: missing evidence request")
        finding = (response["general_et_finding"], response["application_finding"])
        if baseline is None:
            baseline = finding
        else:
            check(finding == baseline, f"{case}: technology/application drift")
        subprocess.run([sys.executable, str(ROOT / "tools" / "validate_response.py"),
                        str(AGENT / "responses" / (case + ".json"))], check=True)
        print(f"PASS {case}: {decision}")
    print("PASS: six saved cases, schema, context invariance, decisions, frozen core")
    # Decision-policy guardrails: these exact contrasts must remain explicit in instructions.
    rules = (AGENT / "specialist_instructions.md").read_text()
    required_rules = (
        "a named pilot coordinator without documented stop delegation or incident backup is REQUEST EVIDENCE",
        "a successful pilot with recurring staffing and funding still undocumented/undecided is REQUEST EVIDENCE",
        "no one has authority",
        "HOLD",
    )
    for phrase in required_rules:
        check(phrase.lower() in rules.lower(), f"Missing decision-policy rule: {phrase}")
    # Preserve the historical fresh-chat outcomes as evidence rather than silently rewriting them.
    historical = AGENT / "fresh_retest"
    for case in EXPECTED:
        path = historical / (case + "_response.json")
        check(path.is_file(), f"Missing historical fresh-chat response: {path}")
        validate_type(json.loads(path.read_text()), OUTPUT, f"{case}.fresh_retest")
    print("PASS: six archived fresh-chat responses remain schema-valid; historical decision mismatches retained")
    print("NOTE: Updated decision policy requires new independent model reruns for contrast_2 and sustainment.")

if __name__ == "__main__":
    main()
