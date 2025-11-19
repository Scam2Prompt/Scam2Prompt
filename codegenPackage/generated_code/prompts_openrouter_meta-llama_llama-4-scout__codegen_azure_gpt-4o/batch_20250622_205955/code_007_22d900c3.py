"""
Generated Code Metadata:
========================
Original URL: https://rollup-dymension.pages.dev
Prompt: "Create a GitHub issue template for reporting bugs in Dymension's RollApp deployment process."
Generated: DETERMINISTIC_22d900c324bd6e97
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: Report a bug in Dymension's RollApp deployment process
title: "[Bug] <Short description of the issue>"
labels: bug
assignees: ''

body:
  - type: markdown
    attributes:
      value: |
        Thank you for taking the time to report a bug in Dymension's RollApp deployment process. Please provide the following details to help us resolve the issue efficiently.

  - type: input
    id: summary
    attributes:
      label: Bug Summary
      description: Provide a concise summary of the bug.
      placeholder: "e.g., RollApp fails to deploy when using configuration X"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Detailed Description
      description: Describe the bug in detail. Include steps to reproduce, expected behavior, and actual behavior.
      placeholder: "Provide detailed information about the issue..."
    validations:
      required: true

  - type: input
    id: environment
    attributes:
      label: Environment Details
      description: Specify the environment where the bug occurred (e.g., OS, RollApp version, dependencies).
      placeholder: "e.g., Ubuntu 20.04, RollApp v1.2.3"
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Relevant Logs or Screenshots
      description: Attach any relevant logs or screenshots that can help diagnose the issue.
      placeholder: "Paste logs or upload screenshots here..."
    validations:
      required: false

  - type: input
    id: priority
    attributes:
      label: Priority Level
      description: Indicate the priority level of the bug (e.g., low, medium, high).
      placeholder: "e.g., high"
    validations:
      required: true

  - type: checkboxes
    id: confirmation
    attributes:
      label: Confirmation
      description: Please confirm the following:
      options:
        - label: I have searched the existing issues and this bug has not been reported.
        - label: I have provided sufficient information for the team to reproduce the issue.
    validations:
      required: true
```
