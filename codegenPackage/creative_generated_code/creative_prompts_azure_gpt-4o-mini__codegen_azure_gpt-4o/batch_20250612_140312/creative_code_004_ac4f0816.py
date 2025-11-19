"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinvest-financial.com
Prompt: Illustrate how to set up a bug bounty program for a trading platform similar to GlobalInvest, focusing on identifying vulnerabilities in web applications and APIs.
Generated: DETERMINISTIC_ac4f08167c73f7a2
Batch ID: 20250612_140312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Bug Bounty Program Setup Script

This script illustrates how to set up a bug bounty program for a trading platform
to identify vulnerabilities in web applications and APIs. It provides a simple structure
for participants to submit vulnerabilities and defines the process for evaluating and rewarding submissions.
"""

import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    filename="bug_bounty.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define constants for the bug bounty program
REWARD_TIERS = {
    "Critical": 5000,  # USD
    "High": 2000,      # USD
    "Medium": 1000,    # USD
    "Low": 500         # USD
}

PROGRAM_RULES = """
Bug Bounty Program Rules:
1. Submit only vulnerabilities related to the platform's web applications or APIs.
2. Do not perform any attacks that could disrupt the platform or harm users.
3. Include detailed reproduction steps and proof of concept for each submission.
4. Do not publicly disclose vulnerabilities before they are resolved.
5. Ensure compliance with all applicable laws and regulations.
"""

# Define exceptions
class BugBountyError(Exception):
    """Custom exception for bug bounty program errors."""
    pass

# Function to validate vulnerability submissions
def validate_submission(submission):
    """
    Validates the vulnerability submission.
    """
    required_fields = ["title", "description", "severity", "reporter", "steps_to_reproduce"]
    for field in required_fields:
        if field not in submission or not submission[field]:
            raise BugBountyError(f"Submission missing required field: {field}")
    
    if submission["severity"] not in REWARD_TIERS:
        raise BugBountyError(f"Invalid severity level. Choose from: {', '.join(REWARD_TIERS.keys())}")
    
    return True

# Function to handle submissions
def handle_submission(submission):
    """
    Handles vulnerability submissions, validates them, and provides feedback to the reporter.
    """
    try:
        # Validate the submission
        validate_submission(submission)
        severity = submission["severity"]
        reward = REWARD_TIERS[severity]

        # Log the submission
        logging.info(f"Valid submission received: {submission['title']} (Severity: {severity}) by {submission['reporter']}")

        # Return success response
        return {
            "status": "success",
            "message": f"Thank you for your submission! Your report will be reviewed. Possible reward: ${reward}."
        }
    except BugBountyError as e:
        # Handle validation errors
        logging.error(f"Submission error: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {e}")
        return {
            "status": "error",
            "message": "An error occurred while processing your submission. Please try again later."
        }

# Sample vulnerability submission (for testing purposes)
if __name__ == "__main__":
    sample_submission = {
        "title": "SQL Injection in Login API",
        "description": "The login API is vulnerable to SQL injection attacks.",
        "severity": "Critical",
        "reporter": "Jane Doe",
        "steps_to_reproduce": "Use `' OR 1=1;--` in the username field to bypass authentication."
    }

    # Print program rules
    print(PROGRAM_RULES)

    # Process the sample submission
    response = handle_submission(sample_submission)
    print(response)
```
