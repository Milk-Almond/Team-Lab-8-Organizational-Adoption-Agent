# Team Lab 8 · Organizational Adoption Agent

SubAgent 6 assesses whether an organization can implement, govern and sustain a proposed technology application. Version **team-subagent-6-v1.0.0** is packaged for team review.

1. Read the [Team Agent Record](TEAM_AGENT_RECORD.md) for the five-source comparison, readiness framework, workshop steps, intake fields and report-out.
2. Build a prompt from the repository root:
   ```sh
   python3 tools/build_prompt.py --agent agents/organizational_adoption --case agents/organizational_adoption/cases/primary.json
   ```
3. Run the packet in a fresh chat and save the JSON. Repeat with the other [case files](agents/organizational_adoption/cases).
4. Validate the JSON and compare it with the [test record](TEST_RECORD.md).
   ```sh
   python3 tools/validate_response.py agents/organizational_adoption/responses/primary.json
   python3 tools/check_frozen_core.py
   ```
5. Record team decisions, dissent and approval in the Team Agent Record.

The [specialist instructions](agents/organizational_adoption/specialist_instructions.md) and frozen common contract are ready for final MoE integration. Saved responses are fictional scenario assessments produced in one Codex session.
