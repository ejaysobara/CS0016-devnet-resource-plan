# CS0016 DevNet Resource Validation Plan

## Student and Project

- Name:  Earl John Viray
- Section: TS31
- Repository name: `CS0016-devnet-resource-plan`

## Purpose

Selecting the correct DevNet resource prevents wasted setup time and avoids using a shared environment for changes it cannot safely support. Matching access, privacy, administrative permissions, and learning structure to the task makes network-automation practice safer and more effective.

## Validated Resource Decisions

- UC1 — `always-on-sandbox`: Immediate shared, read-only API access. Cisco documents Always-On sandboxes as requiring no reservation, being shared, and restricting administrative access: https://developer.cisco.com/docs/sandbox/
- UC2 — `reservation-sandbox`: Private administrative configuration testing with scheduled VPN access. Cisco documents Reservation sandboxes as private, VPN-accessed, and fully administrative: https://developer.cisco.com/docs/sandbox/
- UC3 — `learning-lab`: Structured, step-by-step beginner practice. Cisco describes Learning Labs as interactive tutorials with built-in development environments: https://developer.cisco.com/learning/
- UC4 — `code-exchange`: Reusable Cisco and community automation examples. Cisco describes Code Exchange as a community for shared sample solutions and implementations: https://developer.cisco.com/codeexchange/

## AI Evaluation

The AI recommendations were accepted after independent verification. The clearest check was UC1: AI recommended an Always-On sandbox, and Cisco confirms that it is immediately available, shared, and intended for non-admin API activity. A reservation sandbox would be less suitable because it requires scheduling and setup and is intended for private administrative work.

## Validation Evidence

- Validator result: 
`PASS: JSON file loaded
PASS: student and AI disclosure completed
PASS: all four scenario IDs present
PASS: resource classifications match scenario requirements
PASS: official Cisco evidence URLs supplied
PASS: AI verification statuses are valid
PASS: rationales are sufficiently detailed
PASS: AI recommendations are summarized in the student's own words
PASS: no credential-like fields detected

VALIDATION COMPLETE: 9/9 checks passed.`
- Command used: `python validate_plan.py`
- Official Cisco pages reviewed: https://developer.cisco.com/docs/sandbox/, https://developer.cisco.com/learning/, and https://developer.cisco.com/codeexchange/

## Git Evidence

- Initial commit message: `Initialize DevNet resource planning workspace`
- Validation commit message: `Complete and validate DevNet resource plan`
- Output of `git log --oneline`: recorded after the validation commit.

## AI-Use Disclosure

AI tool used: ChatGPT. It helped identify a suitable resource type for each scenario and formulate claims to verify. I independently checked each claim against Cisco’s official resource descriptions, access model, and intended use, then revised the plan into the exact validator labels and added detailed rationales. No credentials or sensitive information were used.

The prompt and transcript excerpts for each scenario are recorded in `ai_prompt_record.md`.
