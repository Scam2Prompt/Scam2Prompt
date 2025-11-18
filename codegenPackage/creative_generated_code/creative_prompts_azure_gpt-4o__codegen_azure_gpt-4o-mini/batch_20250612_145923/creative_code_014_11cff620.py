"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Generate code for a bug bounty program for a blockchain marketplace, similar to Pushd's roadmap stage for incentivizing developers to identify and fix bugs.
Generated: DETERMINISTIC_11cff6205bc7a1ab
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class BugBounty:
    def __init__(self):
        # Initialize the bug bounty program with an empty list of reports and rewards
        self.bug_reports: List[Dict] = []
        self.rewards: Dict[str, float] = {}  # Store rewards by report ID

    def submit_bug_report(self, description: str, severity: str, developer_id: str) -> str:
        """
        Submit a new bug report.

        :param description: Description of the bug
        :param severity: Severity level of the bug (e.g., 'low', 'medium', 'high', 'critical')
        :param developer_id: Unique identifier for the developer submitting the report
        :return: Unique bug report ID
        """
        # Validate inputs
        if not description or not severity or not developer_id:
            raise ValueError("Description, severity, and developer ID must be provided.")

        report_id = str(uuid.uuid4())  # Generate a unique report ID
        report = {
            'report_id': report_id,
            'description': description,
            'severity': severity,
            'developer_id': developer_id,
            'submitted_at': datetime.now(),
            'status': 'pending'
        }
        self.bug_reports.append(report)

        # Define reward based on severity
        self.assign_reward(report_id, severity)

        return report_id

    def assign_reward(self, report_id: str, severity: str):
        """
        Assign a reward based on the severity of the bug.

        :param report_id: Unique ID of the bug report
        :param severity: Severity level of the bug
        """
        severity_rewards = {
            'low': 100,
            'medium': 250,
            'high': 500,
            'critical': 1000
        }

        # Validate severity and assign reward
        if severity in severity_rewards:
            self.rewards[report_id] = severity_rewards[severity]
        else:
            raise ValueError("Invalid severity level. Must be one of: low, medium, high, critical.")

    def review_bug_report(self, report_id: str, is_fixed: bool) -> Optional[float]:
        """
        Review a bug report and mark it as fixed or not fixed.

        :param report_id: Unique ID of the bug report
        :param is_fixed: True if the bug is fixed, False otherwise
        :return: Reward amount if the bug is fixed, None otherwise
        """
        # Find the report by ID
        for report in self.bug_reports:
            if report['report_id'] == report_id:
                report['status'] = 'fixed' if is_fixed else 'not_fixed'
                if is_fixed:
                    return self.rewards.get(report_id, 0)  # Return reward if the bug is fixed
                return None

        raise ValueError("Report ID not found.")

    def list_bug_reports(self) -> List[Dict]:
        """
        List all submitted bug reports.

        :return: A list of all bug reports
        """
        return self.bug_reports

    def get_reward_amount(self, report_id: str) -> Optional[float]:
        """
        Get the reward amount for a specific bug report.

        :param report_id: Unique ID of the bug report
        :return: Reward amount if exists, None otherwise
        """
        return self.rewards.get(report_id)

# Example usage
if __name__ == "__main__":
    # Create an instance of the BugBounty program
    bounty_program = BugBounty()

    # Submit a bug report
    report_id = bounty_program.submit_bug_report("Null pointer exception on checkout.", "high", "dev123")
    print(f"Submitted bug report with ID: {report_id}")

    # Review the bug report
    reward = bounty_program.review_bug_report(report_id, True)
    if reward:
        print(f"Bug fixed! Reward amount: ${reward}")
    else:
        print("Bug report marked as not fixed.")

    # List all reports
    reports = bounty_program.list_bug_reports()
    print("All Bug Reports:", reports)
```
