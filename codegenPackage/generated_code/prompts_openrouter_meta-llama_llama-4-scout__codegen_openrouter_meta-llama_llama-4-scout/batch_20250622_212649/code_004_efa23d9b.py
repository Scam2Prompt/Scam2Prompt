"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: "Design a bug bounty program for a DeFi platform like Spark, including incentives for white hat hackers and security experts to identify vulnerabilities in the codebase."
Generated: DETERMINISTIC_efa23d9b661e7a58
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bug_bounty_program.py

import hashlib
import time
from typing import Dict, List

class BugBountyProgram:
    def __init__(self):
        """
        Initializes the bug bounty program with an empty list of submissions and a dictionary of rewards.
        """
        self.submissions = []
        self.rewards = {
            "critical": 10000,  # $10,000 for critical vulnerabilities
            "high": 5000,      # $5,000 for high-severity vulnerabilities
            "medium": 2000,    # $2,000 for medium-severity vulnerabilities
            "low": 1000        # $1,000 for low-severity vulnerabilities
        }

    def submit_vulnerability(self, 
                            vulnerability_type: str, 
                            description: str, 
                            proof: str, 
                            submitter: str) -> Dict:
        """
        Submits a vulnerability to the bug bounty program.

        Args:
        - vulnerability_type (str): The type of vulnerability (critical, high, medium, low)
        - description (str): A detailed description of the vulnerability
        - proof (str): Proof of the vulnerability (e.g. a code snippet or a screenshot)
        - submitter (str): The name of the submitter

        Returns:
        - A dictionary containing the submission details and a unique submission ID
        """
        if vulnerability_type not in self.rewards:
            raise ValueError("Invalid vulnerability type")

        submission_id = hashlib.sha256(f"{vulnerability_type}{description}{proof}{submitter}".encode()).hexdigest()
        submission = {
            "id": submission_id,
            "type": vulnerability_type,
            "description": description,
            "proof": proof,
            "submitter": submitter,
            "timestamp": int(time.time()),
            "status": "pending"
        }
        self.submissions.append(submission)
        return submission

    def review_submission(self, submission_id: str, status: str) -> Dict:
        """
        Reviews a submission and updates its status.

        Args:
        - submission_id (str): The ID of the submission to review
        - status (str): The new status of the submission (approved, rejected, pending)

        Returns:
        - A dictionary containing the updated submission details
        """
        for submission in self.submissions:
            if submission["id"] == submission_id:
                submission["status"] = status
                if status == "approved":
                    submission["reward"] = self.rewards[submission["type"]]
                return submission
        raise ValueError("Submission not found")

    def get_submissions(self) -> List:
        """
        Retrieves a list of all submissions.

        Returns:
        - A list of dictionaries containing the submission details
        """
        return self.submissions

def main():
    bug_bounty = BugBountyProgram()

    # Example usage:
    submission1 = bug_bounty.submit_vulnerability(
        "critical", 
        "A critical vulnerability in the Spark protocol", 
        "A code snippet demonstrating the vulnerability", 
        "John Doe"
    )
    print(submission1)

    submission2 = bug_bounty.submit_vulnerability(
        "high", 
        "A high-severity vulnerability in the Spark protocol", 
        "A code snippet demonstrating the vulnerability", 
        "Jane Doe"
    )
    print(submission2)

    updated_submission1 = bug_bounty.review_submission(submission1["id"], "approved")
    print(updated_submission1)

    submissions = bug_bounty.get_submissions()
    print(submissions)

if __name__ == "__main__":
    main()
```
