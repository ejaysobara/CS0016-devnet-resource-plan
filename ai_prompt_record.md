# AI Prompt Record

The following prompt was used for each scenario. The placeholder is shown here with a made-up example classroom scenario:

> I am selecting a Cisco DevNet resource for a fictional classroom use case.
> Use case: A group of students wants to look up basic information from a Cisco device right away. They only need to read the information, and they do not need to change anything.
> Choose exactly one: learning-lab, always-on-sandbox, reservation-sandbox, or code-exchange.
> Explain which requirement drove your choice. State any access, isolation, setup, or privilege claim that I should verify in official Cisco documentation.
> Do not invent a sandbox product name, URL, account, or credential.

## UC1

AI recommendation: `always-on-sandbox`. The decisive requirement was immediate shared read-only API access without provisioning. Verify that Always-On access is immediate, shared, requires no reservation, and restricts administrative access.

## UC2

AI recommendation: `reservation-sandbox`. The decisive requirement was private configuration testing with administrative access. Verify that Reservation sandboxes are private, scheduled, VPN-accessed, and provide administrative access, with setup time.

## UC3

AI recommendation: `learning-lab`. The decisive requirement was structured, step-by-step beginner practice. Verify that Learning Labs provide guided interactive learning content and an appropriate practice environment.

## UC4

AI recommendation: `code-exchange`. The decisive requirement was examining reusable community and Cisco-maintained automation code. Verify that Code Exchange provides shared sample solutions and implementations.
