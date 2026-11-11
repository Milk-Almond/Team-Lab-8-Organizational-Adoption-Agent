# Test record · team-subagent-6-v1.0.0

Six prompt packets built successfully. The frozen-core integrity check passed. All six saved Codex assessments passed the scaffold validator. Additional checks confirmed required input fields and string values, exact output keys, eight readiness dimensions, explicit evidence requests, stable technology and application findings, and the decisions below.

| Case | Saved decision | Evidence that drives it |
|---|---|---|
| primary | HOLD pilot | Stop authority, review capacity and packet traceability are deficient |
| contrast_1 | PILOT ONLY | The charter, bounded environment, rehearsals and funding support the four-week pilot |
| contrast_2 | REQUEST EVIDENCE for pilot | Stop delegation and backup remain unverified |
| known_absence | HOLD pilot | Nobody is authorized to stop the pilot |
| sustainment | REQUEST EVIDENCE for rollout | Recurring staffing and funding remain unverified after a successful pilot |
| review_competence | REQUEST EVIDENCE for pilot | Available reviewers lack demonstrated task-specific competence |

The saved assessments were produced in one Codex session using the team instructions and fictional case evidence. These checks establish contract conformance and scenario coverage. See the separate fresh-chat results below. Real operating performance remains unverified.

## Fresh-chat decision retest

Three separate ChatGPT conversations received the same compact restatement of the specialist rules and the corresponding fictional profile. This tested the decision logic with fresh context. The compact prompt listed the output keys and array fields but omitted the frozen schema's explicit string type for `organization_specific_finding`. The complete assembled prompt packet still needs a fresh-chat retest.

| Case | Observed verdict | Evidence and action in the response | Output contract |
|---|---|---|---|
| Harbor | HOLD | Named absent pilot ownership and stop authority, unallocated review time and funding, and missing source identifiers. Requested signed delegation and protected reviewer capacity. | Failed type check |
| Ridge | PILOT ONLY | Used the delegated authority, rehearsals, approved sandbox and funded four-week scope. Requested representative results, recurring reviewer coverage, funding and ongoing ownership before rollout. | Failed type check |
| Ridge with authority omitted | REQUEST EVIDENCE | Withheld pilot entry and requested signed stop delegation, incident backup and a fallback drill. Recognized that naming a coordinator did not establish authority. | Failed type check |

All three verdicts matched the expected decisions. The technology and application rationale stayed substantively stable: read-only drafting with source verification and manual approval. Each response returned an object for `organization_specific_finding`, which the frozen schema requires to be a string. The table reports the observed mismatch from the original responses. The previously validated repository JSON remains the saved Codex assessment set.

**Updated full-packet fresh-chat retest (November 2026)**

Six independent fresh-chat tests were completed using the assembled specialist prompt packets containing the output schema. The resulting responses were saved as JSON files and validated successfully using `tools/validate_response.py`.

| Test case | Expected decision | JSON validation |
|---|---|---|
| primary | HOLD | PASS |
| contrast_1 | PILOT ONLY | PASS |
| contrast_2 | REQUEST EVIDENCE | PASS |
| known_absence | HOLD | PASS |
| review_competence | REQUEST EVIDENCE | PASS |
| sustainment | REQUEST EVIDENCE | PASS |

All six raw responses are preserved in `agents/organizational_adoption/fresh_retest/` on the `main` branch, commit `23f1c91`.

The Review Competence response was additionally reviewed for decision accuracy, eight-dimension coverage, evidence requests, and readiness reasoning. The remaining fresh-chat responses passed JSON validation; their substantive decisions should be checked against the expected outcomes before claiming full decision-level verification.

## Post-audit remediation (November 10, 2026)

The specialist prompt now explicitly requires `organization_specific_finding` to be a JSON string and restates the frozen field types. Added a repeatable local regression checker for all six saved cases and the frozen-core integrity check. These are preventive fixes, not evidence that the three historical fresh-chat failures have passed. **Remediation follow-up:** The independent full-packet fresh-chat retest has now been completed for all six scenarios. All six responses passed JSON validation, and the resulting files were committed to the repository on `main` as commit `23f1c91`.

The three earlier fresh-chat output-contract failures remain documented above as historical evidence. They have not been deleted or retroactively reclassified. The subsequent retest demonstrates that the revised instructions produced schema-valid outputs across the six tested scenarios. Final decision-level verification remains separate from schema validation.
