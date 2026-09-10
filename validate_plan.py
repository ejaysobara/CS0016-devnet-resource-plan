"""Validate the Module 2 DevNet resource plan.

Usage:
    1. Copy student_plan_template.json as student_plan.json.
    2. Complete student_plan.json.
    3. Run: python validate_plan.py

The validator performs no network connections and never reads credentials.
"""

import json
import re
from pathlib import Path
from urllib.parse import urlparse


PLAN_FILE = Path("student_plan.json")
EXPECTED = {
    "UC1": "always-on-sandbox",
    "UC2": "reservation-sandbox",
    "UC3": "learning-lab",
    "UC4": "code-exchange",
}
ALLOWED_STATUS = {"verified", "partially-verified", "rejected"}
SENSITIVE_KEYWORDS = {"password", "token", "secret", "api_key", "apikey", "credential"}


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield str(key).lower()
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def is_official_cisco_url(value):
    try:
        parsed = urlparse(value)
    except (TypeError, ValueError):
        return False
    return parsed.scheme == "https" and parsed.hostname == "developer.cisco.com"


def check(condition, message, errors):
    if condition:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")
        errors.append(message)


def main():
    errors = []
    try:
        data = json.loads(PLAN_FILE.read_text(encoding="utf-8"))
        loaded = True
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"FAIL: JSON file loaded ({exc})")
        raise SystemExit(1)

    check(loaded, "JSON file loaded", errors)
    check(
        bool(str(data.get("student_name", "")).strip())
        and bool(str(data.get("section", "")).strip())
        and bool(str(data.get("ai_tool", "")).strip()),
        "student and AI disclosure completed",
        errors,
    )

    entries = data.get("entries", [])
    by_id = {
        entry.get("use_case_id"): entry
        for entry in entries
        if isinstance(entry, dict) and entry.get("use_case_id")
    }
    check(set(by_id) == set(EXPECTED), "all four scenario IDs present", errors)
    check(
        all(by_id.get(case_id, {}).get("selected_resource_type") == expected
            for case_id, expected in EXPECTED.items()),
        "resource classifications match scenario requirements",
        errors,
    )
    check(
        all(is_official_cisco_url(by_id.get(case_id, {}).get("official_evidence_url", ""))
            for case_id in EXPECTED),
        "official Cisco evidence URLs supplied",
        errors,
    )
    check(
        all(by_id.get(case_id, {}).get("verification_status") in ALLOWED_STATUS
            for case_id in EXPECTED),
        "AI verification statuses are valid",
        errors,
    )
    check(
        all(len(str(by_id.get(case_id, {}).get("rationale", "")).split()) >= 12
            for case_id in EXPECTED),
        "rationales are sufficiently detailed",
        errors,
    )
    check(
        all(len(str(by_id.get(case_id, {}).get("ai_recommendation_summary", "")).split()) >= 6
            for case_id in EXPECTED),
        "AI recommendations are summarized in the student's own words",
        errors,
    )
    sensitive_keys = {
        key for key in walk_keys(data)
        if any(keyword in re.sub(r"[^a-z0-9_]", "", key) for keyword in SENSITIVE_KEYWORDS)
    }
    check(not sensitive_keys, "no credential-like fields detected", errors)

    if errors:
        print(f"\nVALIDATION INCOMPLETE: {9 - len(errors)}/9 checks passed.")
        raise SystemExit(1)
    print("\nVALIDATION COMPLETE: 9/9 checks passed.")


if __name__ == "__main__":
    main()
