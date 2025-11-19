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
# bug_bounty_program.py

import datetime

class BugBountyProgram:
    """
    A class to manage a bug bounty program for a decentralized lending protocol.
    Inspired by Silo Finance's security measures and audit reports.
    """

    def __init__(self, protocol_name, reward_pool):
        """
        Initialize the bug bounty program.

        :param protocol_name: Name of the decentralized lending protocol.
        :param reward_pool: Total reward pool allocated for the bug bounty program.
        """
        self.protocol_name = protocol_name
        self.reward_pool = reward_pool
        self.submissions = []
        self.rewards_distributed = 0

    def submit_bug_report(self, reporter_name, bug_description, severity_level):
        """
        Submit a bug report to the program.

        :param reporter_name: Name of the person submitting the bug report.
        :param bug_description: Description of the bug.
        :param severity_level: Severity level of the bug (e.g., "low", "medium", "high", "critical").
        :return: Confirmation message.
        """
        if severity_level not in ["low", "medium", "high", "critical"]:
            raise ValueError("Invalid severity level. Must be one of: 'low', 'medium', 'high', 'critical'.")

        report = {
            "reporter_name": reporter_name,
            "bug_description": bug_description,
            "severity_level": severity_level,
            "submission_date": datetime.datetime.now(),
            "status": "pending"
        }
        self.submissions.append(report)
        return f"Bug report submitted successfully by {reporter_name}."

    def evaluate_bug_report(self, report_index, is_valid, reward_amount):
        """
        Evaluate a bug report and distribute rewards if valid.

        :param report_index: Index of the bug report in the submissions list.
        :param is_valid: Boolean indicating whether the bug report is valid.
        :param reward_amount: Amount to reward the reporter if the bug is valid.
        :return: Evaluation result message.
        """
        if report_index < 0 or report_index >= len(self.submissions):
            raise IndexError("Invalid report index.")

        report = self.submissions[report_index]

        if report["status"] != "pending":
            return f"Bug report at index {report_index} has already been evaluated."

        if not is_valid:
            report["status"] = "rejected"
            return f"Bug report at index {report_index} has been rejected."

        if reward_amount > self.reward_pool - self.rewards_distributed:
            raise ValueError("Insufficient reward pool to distribute the specified amount.")

        report["status"] = "accepted"
        report["reward_amount"] = reward_amount
        self.rewards_distributed += reward_amount
        return f"Bug report at index {report_index} has been accepted. Reward of {reward_amount} distributed."

    def get_program_summary(self):
        """
        Get a summary of the bug bounty program.

        :return: Summary dictionary.
        """
        return {
            "protocol_name": self.protocol_name,
            "reward_pool": self.reward_pool,
            "rewards_distributed": self.rewards_distributed,
            "remaining_pool": self.reward_pool - self.rewards_distributed,
            "total_submissions": len(self.submissions),
            "pending_reports": len([r for r in self.submissions if r["status"] == "pending"]),
            "accepted_reports": len([r for r in self.submissions if r["status"] == "accepted"]),
            "rejected_reports": len([r for r in self.submissions if r["status"] == "rejected"])
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the bug bounty program
        program = BugBountyProgram(protocol_name="Decentralized Lending Protocol", reward_pool=100000)

        # Submit bug reports
        print(program.submit_bug_report("Alice", "Critical vulnerability in smart contract", "critical"))
        print(program.submit_bug_report("Bob", "Minor UI bug in dashboard", "low"))

        # Evaluate bug reports
        print(program.evaluate_bug_report(0, is_valid=True, reward_amount=50000))
        print(program.evaluate_bug_report(1, is_valid=False, reward_amount=0))

        # Get program summary
        summary = program.get_program_summary()
        print("Bug Bounty Program Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")
```
