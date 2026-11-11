# Team Lab 8 — Organizational Adoption Agent
Version: team-subagent-6-v1.0.0  
Prepared: November 10, 2026  
Status: synthesis for team review; approval, workshop participation, and posting are not evidenced.

## Workshop sequence

| Time | What the team does | What to record |
|---|---|---|
| 0–8 min | Give each member about 90 seconds to state their individual judgment, dominant gap, action and evidence request. Use section 1 as the starting point. | Five individual positions, including any disagreement. |
| 8–23 min | Compare each candidate against the eight dimensions in section 2. Decide what evidence should count for each stage. | Which rules the team retains and why. |
| 23–37 min | Run cases A and B in separate chats using the same specialist instructions and frozen common prompt. Run C for the missing-authority test. Use D–F if time allows. | Save raw outputs. Check that the application assessment stays stable, the action changes with the profile, and C asks for proof before recommending launch. |
| 37–49 min | Agree on decision labels and edit the specialist instructions. Check that each proposed action closes an observed gap or resolves an unknown. | Agreed owner, completion evidence and decision gate for the most consequential actions. |
| 49–56 min | Validate saved outputs with the scaffold validator. Review decision quality separately, record one unresolved limitation, and update section 5. | Actual results, any unexpected output, dissent, approval and the agreed version. |
| 56–60 min | Rehearse section 6 using the team’s actual judgments and evidence. | Report-out and final intake fields. |

Use the workshop for the decisions, tests and approval. Use the post-class window to apply agreed edits, consolidate the record and post it.

## 1. Candidate comparison and synthesis decision

Reviewed all five linked repositories at the snapshots in section 7, specialist instructions, case files, saved responses and records where present. Repository-reported validation is historical evidence, not a new validation run.

| Candidate | Substantive contribution | Limitation / synthesis treatment |
|---|---|---|
| mp7240-sudo / Meilin | Separates synthetic evaluation, real-client pilot and sustained operation. Requires task-specific evidence of reviewer competence, error detection, correction, escalation and workload. | Saved v0.2 follow-ups corrected an unsupported skills rating. They reused the original conversations, which limits repeatability evidence. |
| yanisimova / Yulia Anisimova | Eight dimensions; small/large consulting contrast; precise confidentiality hold; actions tied to observed gaps; maximum defensible scope | Uses conditional readiness terminology. Preserve explicit scope and data permissions; standardize stage-specific decisions. Record says not committed, although reviewed files now exist at the pinned snapshot; distinguish historical record from current availability. |
| Harry-max264 / Shenghao Ma | Explicit HOLD versus REQUEST EVIDENCE; stop delegation and backup coverage; pilot versus recurring capacity; saved before/after missing-authority test | Strong decision backbone. Do not impose every procurement-specific control on every technology. |
| sawulya / Alexandra Chsherbinina | Gap → action → owner → evidence → gate; failed load/access tests; multi-period maintenance funding | Require recurring funding before sustained operation; require it before a pilot only when pilot continuity or consequences make it a pilot gate. Earlier weak response is a diagnostic critique, not a separately executed test. |
| yicrry777 / Shuoying Wang | Detailed profile, end-to-end workflow evidence, culture/workload, explicit incomplete-information case and output mapping | Replace numeric 0–3 ratings with categorical status: unknown is not a lower capability score. Media-specific rights/disclosure controls apply only where relevant. |

Proposed synthesis: Harry’s decision gates + all five agents’ eight dimensions + Yulia’s bounded scope + Alexandra’s sustainment conditions + Shuoying’s evidence/action structure + Meilin’s distinction between reviewer availability and demonstrated competence. This is an analytical recommendation, not a recorded team vote.

## 2. Ready-to-use specialist instructions

You are SubAgent 6, the Organizational Adoption Agent. Answer: Even if adoption is strategically appropriate, can this organization absorb, govern and sustain the specified application, and what must change before it can?

### Boundaries and method

1. Separate technology generally, fit for the exact application, and readiness of this organization. Organizational weakness must never lower the underlying technology’s maturity. Preserve uncertainty about actual application performance.
2. State the decision stage and exact scope: discovery, bounded pilot, operational rollout, or sustained operation. A narrower scope needs its own readiness assessment; do not silently substitute a sandbox for the requested deployment.
3. Assess all eight dimensions using Strength, Partial, Gap, or Unknown. For each, record evidence/assumption, strength, gap or unknown, consequence, severity, and supported accountable role. Unknown describes evidence sufficiency, not poor capability. Never average away a critical gate.
4. Derive gates from the application’s consequences and requested stage. Do not copy a universal control checklist. State why each gate is necessary for this scope.
5. Apply one decision label:
   - HOLD: a known material blocker prevents the requested stage. Still request consequential missing evidence.
   - REQUEST EVIDENCE: no established blocker already decides the case, but a critical unknown prevents a defensible judgment. Withhold a positive recommendation for that stage.
   - PILOT ONLY: evidence supports the specific bounded pilot and its gates, including accountable authority, necessary reviewer/operator capacity, approved inputs/environment, fallback and incident response where applicable. This is readiness advice; management retains approval.
   - ROLLOUT ELIGIBLE: representative pilot results meet agreed use-specific criteria and recurring capacity, funding, controls, ownership and risk acceptance support rollout and continued operation. Eligibility is not final approval.
6. Identify the single most consequential gap or unknown and explain the failure mechanism. Rank no more than four actions in dependency order. Every action includes observed gap, P0 stage gate / P1 pilot learning / P2 scale condition, action, supported or explicitly proposed owner, decision point, completion evidence, and decision unlocked.
7. Do not infer authority from a title or sponsorship. Where material, request a named person with stop authority, delegation evidence and incident backup. Assess reviewer availability and demonstrated task competence separately. Where human review is a critical control, request representative evidence of material error detection, correction, escalation and review time, using error-seeded exercises where appropriate. Training attendance and willingness do not establish competence. Verify recurring capacity separately from pilot funding.
8. Ask direct, targeted evidence questions: what fact is missing, which artifact or test would resolve it, who should supply it, and which decision it blocks. Never fabricate permissions, vendor terms, skills, infrastructure, staffing, budget, user acceptance or performance.
9. Distinguish supplied facts, hypothetical assumptions, external evidence and inference. Date material evidence. Verify current laws, standards, vendor capabilities and organizational-practice claims against relevant primary sources before using them to drive a decision. If verification is unavailable, state the unresolved dependency and withhold that part of the judgment.
10. Set scope, entry/exit criteria, pause triggers, fallback, monitoring owner and reassessment events. Label numerical thresholds as proposed until management adopts them.
11. Check context sensitivity: when only organizational capabilities change, technology/application findings stay stable; readiness, bottleneck and actions change when warranted. Identical recommendations are acceptable only if a shared binding constraint explains them.
12. Do not certify law, security, procurement or strategic desirability. Route those judgments to their accountable specialists.

### Eight-dimension framework

| Dimension | Required evidence focus |
|---|---|
| Leadership/sponsorship | Sponsor commitment, scope, priority, decision rights and escalation support |
| Skills/training | Demonstrated operator/reviewer ability, evaluation and exception-handling rehearsal, refresh plan |
| Process/workflow | Input checks, verification, handoffs, approvals, exceptions, records and fallback |
| Infrastructure/data | Approved environment, access, source quality/rights, integration, load and logging evidence relevant to scope |
| Resources/budget | Protected staff time, full control cost, pilot funding, recurring staffing/funding horizon |
| Governance/risk | Permitted use, risk acceptance, monitoring, incident response, vendor/data review where relevant |
| Culture/change | Staff feedback, workload, incentives, willingness to challenge outputs and safe error reporting |
| Operating ownership | Service/control owners, stop delegation, incident backup, change/metrics ownership and continuity |

### Output mapping — retain the common contract

Use the existing 13 required top-level fields; add none. Put the three analytical levels in general_et_finding, application_finding and organization_specific_finding. Put the eight-dimension profile and dominant blocker in organization_specific_finding. Start recommendation_management_implication with the decision label, stage and permitted scope, then prioritized gap/action/owner/evidence/gate entries. Put direct evidence requests in abstention_or_more_information_needed; put reassessment triggers and responses in change_monitoring_triggers. Populate agent, analytical_question, evidence, contrary_evidence_or_limitations, confidence_and_uncertainty, value_opportunity_implication and risk_governance_implication as defined by the common schema.

## 3. Common context tests and worked expectations

These are fictional instructional cases adapted from Harry’s matched procurement cases. Worked expectations and saved JSON assessments were produced in one Codex session.

Constant technology/application: one LLM in a read-only assistant drafting source-linked packaging RFQ comparisons from the same sanitized historical packets and approved supplier records. Buyers verify material claims. Sourcing approval remains manual. No messaging, supplier selection or writes to procurement systems. Same risk, moderate fast-follower posture, four-week pilot and 90-day rollout question. No measured model accuracy or savings supplied.

Stable general finding: selected-model reliability is unmeasured; generated claims require evaluation.
Stable application finding: conditional fit for evidence-linked drafting with buyer verification and manual sourcing decisions; actual quality and net time savings remain unproven.

| Dimension | A: Harbor | B: Ridge |
|---|---|---|
| Leadership | Partial: director endorses concept, no delegated authority | Strength for pilot: signed charter and delegated stop authority |
| Skills | Gap: buyers have not rehearsed AI verification | Strength for pilot: two buyers completed source-check/escalation rehearsal |
| Workflow | Gap: manual sign-off exists, AI error route absent | Strength for pilot: manual approval, rehearsed reporting and fallback |
| Infrastructure/data | Gap: approved sandbox/data, but IDs and revision labels missing in some packets | Strength for pilot: approved sandbox/data; analyst verified all 20 packet identifiers |
| Resources | Gap: no protected reviewer time or pilot budget | Strength for pilot: funded four-week charter, four review hours/week; sustained capacity unknown |
| Governance | Gap: no authorized pause/incident route | Strength for pilot: stop delegation, tested reporting and IT/security escalation |
| Culture | Unknown/Partial: buyers ask how reported errors will be handled | Partial: rehearsal supports reporting; sustained uptake/workload unmeasured |
| Ownership | Gap: no pilot owner or stop decision-maker | Strength for pilot: procurement operations owns log/review/escalation; long-term coverage unknown |

### Worked result A

HOLD the pilot. Dominant gap: no accountable operating/stop authority, compounded by unfunded review capacity and incomplete source traceability. Conditional application fit remains unchanged.

| Priority | Gap → action | Owner | Completion evidence / gate |
|---|---|---|---|
| P0 | Absent authority → appoint owner, delegate pause power and incident coverage | Procurement director (supported role; appointment still needed) | Signed delegation and backup route before pilot |
| P0 | No review capacity/AI exception workflow → fund protected time and rehearse verification/fallback | Proposed procurement operations owner; director approves capacity | Funded allocation and passed representative rehearsal |
| P0 | Missing identifiers → reconcile supplier IDs and bid revisions | Proposed procurement analyst | Admission log links every pilot packet to approved source/revision |

Missing-information request: “Director, provide the pilot charter or equivalent naming the stop decision-maker and incident backup. This blocks pilot eligibility; endorsement alone does not establish authority.”

### Worked result B

PILOT ONLY for the funded four-week historical-data scope. Most consequential remaining readiness unknown: recurring operating capacity and funding beyond the pilot. Actual quality and review burden are pilot learning dependencies. No rollout recommendation yet.

| Priority | Gap → action | Owner | Completion evidence / gate |
|---|---|---|---|
| P1 | Performance/workload unmeasured → measure defects, omissions, buyer time, rework and total cost | Procurement operations manager with buyers | Representative baseline comparison against pre-agreed quality/value criteria before rollout |
| P2 | Recurring capacity/funding unknown → document ongoing staffing, backup, budget and operating horizon | Director with finance; proposed finance role | Approved support plan before operational rollout |
| P1 | Long-term reporting/culture unmeasured → collect buyer feedback and review workload | Procurement operations manager | Pilot review records and resolved workload/error-reporting issues |

Do not demand that Ridge create a sandbox, train from scratch or appoint a pilot owner already supplied in the case.

### Test C — missing-information mutation

Use B unchanged except replace explicit stop delegation with “operations manager is coordinator” and omit incident coverage. Expected: REQUEST EVIDENCE for the pilot. Ask for signed delegation or equivalent and named incident backup; do not infer absent authority or allow launch while it is unresolved.

### Test D — known absent control mutation

Use C but explicitly state “no person is authorized to pause the pilot.” Expected: HOLD rather than REQUEST EVIDENCE. Known absence and missing evidence must produce different reasoning.

### Test E — sustainment mutation

Use B with representative pilot results stipulated to meet management-approved quality/value criteria, but recurring funding still unknown. Expected: REQUEST EVIDENCE for rollout; pilot evidence does not establish sustained capacity.

### Test F — reviewer competence mutation

Use B with the same funded review hours, ownership and data approvals, but remove evidence that buyers passed the source-check rehearsal. The file only says buyers are assigned and available. Expected: REQUEST EVIDENCE for pilot entry. Ask Procurement Operations for a representative exercise with seeded price, terms and omission errors, plus detection, correction, escalation and review-time results. Keep staffing availability as a strength and classify task-specific review competence as unknown. This adapts Meilin’s observed v0.1 failure to the common test.

### Validation record

Manual rule review: A→HOLD; B→PILOT ONLY; C→REQUEST EVIDENCE; D→HOLD; E→REQUEST EVIDENCE for rollout; F→REQUEST EVIDENCE for pilot entry. General/application baseline remains constant. A’s immediate blocker-removal actions differ from B’s measurement and sustainment actions. All six prompts built successfully. The six saved Codex assessments passed the scaffold response validator and the decision and contract checks listed in TEST_RECORD.md. Three separate ChatGPT runs using a compact prompt matched the expected decisions. All three returned an object where the frozen schema requires a string. See TEST_RECORD.md for the observed results and the remaining exact-packet retest.

## 4. Organizational intake for final MoE integration

Retain the common 11 required string fields: emerging_technology, intended_application, organization, industry_sector, business_need, users_stakeholders, adoption_posture, capabilities_constraints, risk_consequence_context, management_question, time_horizon. The inspected schema also allows optional additional_context. Encode specialist details in capabilities_constraints and additional_context as readable structured text; do not change the frozen schemas.

| Intake detail | Minimum useful content |
|---|---|
| Decision stage/scope | Pilot versus rollout, users, data, action permissions, volume, timing, exclusions |
| Sponsor/authority | Named sponsor, decision-maker, operating owner, stop delegation artifact, incident backup |
| Skills/capacity | Operators/reviewers, task-specific ability, protected hours, representative error detection/correction, escalation and review-time evidence |
| Workflow | Current process, checks, approvals, exceptions, fallback, retained records |
| Infrastructure/data | Tool/environment approval, access, source quality/rights, relevant load/integration tests |
| Funding/sustainment | Pilot funds, total control workload/cost, recurring staff/funding, horizon and approving authority |
| Governance | Risk boundary/acceptance, vendor/data terms where relevant, incident and change process |
| Culture | Staff feedback, workload, incentives, reporting and challenge mechanisms |
| Measurement | Baseline, representative evaluation results, agreed acceptance/stop criteria, metrics owner |
| Evidence metadata | Artifact reference, date, scope, supplied fact versus assumption, unresolved questions |

Missing details must trigger targeted requests rather than filled-in defaults.

## 5. Team Agent Record and inventory

| Record field | Entry |
|---|---|
| Agent | SubAgent 6 — Organizational Adoption Agent |
| Version | team-subagent-6-v1.0.0 |
| Governing question | Can this organization absorb, govern and sustain the application? |
| Build status | Runnable prompt package and integration mapping prepared |
| Team approval | Pending; no approval vote or signatories supplied |
| Readiness finding | Context dependent; no real organization has been assessed |
| Dominant gap in common primary test | Accountable operating/stop authority, alongside review capacity and traceability blockers |
| Evidence request | Delegation/backup artifact before pilot; recurring capacity/funding before rollout |
| Tests | A–F above; saved Codex assessments validated, three compact fresh-chat decisions matched, exact-packet schema retest pending |
| Source record | Five pinned repository snapshots below, including Meilin’s Assignment 7 branch |
| Remaining limitation | Hypothetical profiles and saved examples do not establish real control effectiveness or repeatability |
| New commit | See repository history for the exact commit |
| Final-project destination | Organizational-readiness expert, implementation gates and required intake fields |

### Evidence/dissent record

No actual team disagreement was provided. Preserve these unresolved design choices for discussion rather than inventing consensus:
- Whether signed recurring funding is required before every pilot or only when the pilot’s exposure/continuity demands it. Proposed rule: stage-specific gates with explicit rationale.
- Whether to use numeric ratings or categorical states. Proposed rule: categorical states, with Unknown separate from Gap.
- Whether a “conditional pilot” means permission now or permission after gates close. Proposed rule: explicit scope plus HOLD/REQUEST EVIDENCE/PILOT ONLY/ROLLOUT ELIGIBLE.
- Whether a training rehearsal is sufficient evidence at each stage. Proposed rule: match the review exercise to the consequences and scale of the stage, and request measured performance before real-client use when review is a critical control.

Team completion fields: approval date ___; participants ___; agreed revisions ___; dissent/minority view ___; approved version/commit ___; model-run evidence ___; posting location ___.

## 6. Report-out draft

“Our synthesized SubAgent 6 separates application fit from organizational readiness and uses eight evidence-based dimensions. In the common hypothetical test, Harbor is on HOLD because operating authority, review capacity and source traceability are missing. Ridge is PILOT ONLY because those pilot controls exist, while performance and recurring capacity remain unproven. Removing authority evidence triggers REQUEST EVIDENCE rather than an invented answer. The key intake additions are accountable owners and stop authority, demonstrated review capacity, workflow/data evidence, recurring funding, staff feedback and measurable gates. Version team-subagent-6-v1.0.0 is packaged for team review; approval remains pending.”

## 7. Source snapshot register

Snapshots retrieved during this session. References establish repository contents and reported test history, not external regulatory, vendor or performance facts. Commit SHAs pin the reviewed snapshots.

| Repository snapshot | SHA |
|---|---|
| [mp7240-sudo / assignment-7-organizational-adoption](https://github.com/mp7240-sudo/MASY1800-Organizational-Adoption-Agent/tree/6d752b457a39a5cfe96218acd0c7c02b2e8f5720/agents/organizational_adoption_agent) | `6d752b457a39a5cfe96218acd0c7c02b2e8f5720` |
| [yanisimova/Implementing-Agent](https://github.com/yanisimova/Implementing-Agent/tree/026b0a7fe4d6853c98abac8d331dd28668595a01) | `026b0a7fe4d6853c98abac8d331dd28668595a01` |
| [Harry-max264/LAB7-Harry](https://github.com/Harry-max264/LAB7-Harry/tree/72f6823c5daa86d185feb1c89058a65523f527ed) | `72f6823c5daa86d185feb1c89058a65523f527ed` |
| [sawulya/Lab-7---SubAgent-6-Implementing](https://github.com/sawulya/Lab-7---SubAgent-6-Implementing/tree/2b8d590ea4f33fc11c6b266c0a4ee4e58d608993) | `2b8d590ea4f33fc11c6b266c0a4ee4e58d608993` |
| [yicrry777/1800lab7](https://github.com/yicrry777/1800lab7/tree/b119f5fda90fde2286ccd92250e5c4bd001965b5) | `b119f5fda90fde2286ccd92250e5c4bd001965b5` |

Substantive paths: mp7240-sudo: agents/organizational_adoption_agent/ on its Assignment 7 branch; yanisimova: MASY1800_ET_Agent_Scaffold_v1_0-2/agents/organizational_adoption_agent/; Harry: agents/organizational_adoption/; sawulya: MASY1800_ET_Agent_Scaffold_v1_0 9/agents/organizational_adoption_agent/; yicrry777: agents/organizational_adoption_agent/. Read specialist_instructions.md, case/response JSON and available Markdown records in these paths. Common input/output schemas inspected in Harry’s pinned snapshot.

No current legal/platform/vendor claim is used to decide the new worked cases. The source agents’ cited NIST, platform, C2PA and vendor assertions are not independently reverified here and must be checked if used for a real implementation decision. AI assisted comparison, drafting and manual rule application; human workshop work and team approval must be recorded by the team.

