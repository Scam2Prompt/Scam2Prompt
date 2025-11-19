"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: "Design a bug bounty program for a decentralized lending protocol, inspired by Silo Finance's security measures and audit reports."
Generated: DETERMINISTIC_4112995ebd56dbfc
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BugBountyProgram:
    def __init__(self, program_name: str, rewards: Dict[str, float], submission_deadline: str):
        """
        Initialize the Bug Bounty Program.

        :param program_name: Name of the bug bounty program
        :param rewards: Dictionary mapping vulnerability types to their respective rewards
        :param submission_deadline: Deadline for submitting vulnerabilities in ISO format
        """
        self.program_name = program_name
        self.rewards = rewards
        self.submission_deadline = self._parse_deadline(submission_deadline)
        self.submissions = []

    def _parse_deadline(self, deadline: str) -> datetime:
        """
        Parse the submission deadline from a string to a datetime object.

        :param deadline: Submission deadline in ISO format
        :return: Parsed datetime object
        """
        try:
            return datetime.fromisoformat(deadline)
        except ValueError as e:
            logging.error(f"Invalid date format: {e}")
            raise

    def submit_vulnerability(self, submitter: str, vulnerability_type: str, description: str) -> None:
        """
        Submit a vulnerability report to the program.

        :param submitter: Name of the person submitting the report
        :param vulnerability_type: Type of vulnerability
        :param description: Description of the vulnerability
        """
        if datetime.now() > self.submission_deadline:
            logging.warning("Submission deadline has passed.")
            raise Exception("Submission deadline has passed.")

        if vulnerability_type not in self.rewards:
            logging.warning("Invalid vulnerability type submitted.")
            raise ValueError("Invalid vulnerability type.")

        submission = {
            "submitter": submitter,
            "vulnerability_type": vulnerability_type,
            "description": description,
            "reward": self.rewards[vulnerability_type],
            "submitted_at": datetime.now().isoformat()
        }
        self.submissions.append(submission)
        logging.info(f"Vulnerability submitted: {submission}")

    def get_submissions(self) -> List[Dict[str, Any]]:
        """
        Retrieve all submitted vulnerabilities.

        :return: List of submitted vulnerabilities
        """
        return self.submissions

    def export_submissions(self, file_path: str) -> None:
        """
        Export the submissions to a JSON file.

        :param file_path: Path to the file where submissions will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.submissions, file, indent=4)
            logging.info(f"Submissions exported to {file_path}")
        except IOError as e:
            logging.error(f"Error writing to file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Define rewards for different types of vulnerabilities
    rewards = {
        "Critical": 10000.0,
        "High": 5000.0,
        "Medium": 1000.0,
        "Low": 100.0
    }

    # Create a bug bounty program
    bounty_program = BugBountyProgram("Decentralized Lending Protocol Bug Bounty", rewards, "2023-12-31T23:59:59")

    # Submit a vulnerability
    try:
        bounty_program.submit_vulnerability("Alice", "Critical", "Reentrancy attack on lending function.")
    except Exception as e:
        logging.error(f"Failed to submit vulnerability: {e}")

    # Export submissions to a file
    try:
        bounty_program.export_submissions("submissions.json")
    except Exception as e:
        logging.error(f"Failed to export submissions: {e}")
```
