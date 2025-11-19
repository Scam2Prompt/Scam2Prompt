"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Design a bug bounty program for the Venus Protocol, including guidelines for reporting vulnerabilities and rewards for successful submissions.
Generated: DETERMINISTIC_1b5dd98fb5a308ab
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bug_bounty_program.py

"""
Bug Bounty Program for Venus Protocol

This script defines the structure and guidelines for a bug bounty program.
It includes functionality for reporting vulnerabilities, evaluating submissions,
and rewarding successful reports. The program is designed to ensure security
and incentivize responsible disclosure of vulnerabilities.
"""

from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    filename="bug_bounty.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BugBountyProgram:
    """
    Class representing the Venus Protocol Bug Bounty Program.
    """

    def __init__(self):
        """
        Initialize the bug bounty program with default reward tiers and an empty list of submissions.
        """
        self.reward_tiers = {
            "critical": 10000,  # USD
            "high": 5000,       # USD
            "medium": 2000,     # USD
            "low": 500          # USD
        }
        self.submissions = []

    def report_vulnerability(self, reporter_name, email, description, severity):
        """
        Allows a user to report a vulnerability.

        Args:
            reporter_name (str): Name of the person reporting the vulnerability.
            email (str): Email address of the reporter.
            description (str): Detailed description of the vulnerability.
            severity (str): Severity level of the vulnerability (critical, high, medium, low).

        Returns:
            dict: Confirmation of the submission.
        """
        if severity not in self.reward_tiers:
            raise ValueError("Invalid severity level. Must be one of: critical, high, medium, low.")

        submission = {
            "reporter_name": reporter_name,
            "email": email,
            "description": description,
            "severity": severity,
            "timestamp": datetime.now(),
            "status": "pending"
        }

        self.submissions.append(submission)
        logging.info(f"New vulnerability reported by {reporter_name} ({email}). Severity: {severity}.")
        return {
            "message": "Vulnerability reported successfully.",
            "submission_id": len(self.submissions) - 1
        }

    def evaluate_submission(self, submission_id, is_valid):
        """
        Evaluates a reported vulnerability and determines the reward.

        Args:
            submission_id (int): ID of the submission to evaluate.
            is_valid (bool): Whether the submission is valid.

        Returns:
            dict: Evaluation result and reward details.
        """
        if submission_id < 0 or submission_id >= len(self.submissions):
            raise IndexError("Invalid submission ID.")

        submission = self.submissions[submission_id]

        if submission["status"] != "pending":
            raise ValueError("Submission has already been evaluated.")

        if is_valid:
            reward = self.reward_tiers[submission["severity"]]
            submission["status"] = "approved"
            submission["reward"] = reward
            logging.info(f"Submission ID {submission_id} approved. Reward: ${reward}.")
            return {
                "message": "Submission approved.",
                "reward": reward
            }
        else:
            submission["status"] = "rejected"
            logging.info(f"Submission ID {submission_id} rejected.")
            return {
                "message": "Submission rejected.",
                "reward": 0
            }

    def get_submissions(self):
        """
        Retrieves all submissions.

        Returns:
            list: List of all submissions.
        """
        return self.submissions


# Example usage
if __name__ == "__main__":
    # Initialize the bug bounty program
    program = BugBountyProgram()

    try:
        # Report a vulnerability
        report = program.report_vulnerability(
            reporter_name="Alice",
            email="alice@example.com",
            description="SQL injection vulnerability in login endpoint.",
            severity="critical"
        )
        print(report)

        # Evaluate the submission
        evaluation = program.evaluate_submission(submission_id=0, is_valid=True)
        print(evaluation)

        # Retrieve all submissions
        submissions = program.get_submissions()
        print(submissions)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"Error: {e}")
```
