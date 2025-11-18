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
"""
Bug Bounty Program for Blockchain Marketplace
This script implements a bug bounty program where developers can submit bug reports, 
get them reviewed, and receive rewards for valid submissions.
"""

from typing import List, Dict
import uuid

# Constants
BUG_STATUS_PENDING = "Pending"
BUG_STATUS_REVIEWED = "Reviewed"
BUG_STATUS_APPROVED = "Approved"
BUG_STATUS_REJECTED = "Rejected"

REWARD_AMOUNT = 0.05  # Reward per approved bug in cryptocurrency (e.g., Ethereum)

class BugReport:
    """
    Represents a bug report submitted by developers.
    """
    def __init__(self, reporter_name: str, description: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the bug report
        self.reporter_name = reporter_name
        self.description = description
        self.status = BUG_STATUS_PENDING
    
    def update_status(self, new_status: str):
        """
        Updates the status of the bug report.
        """
        valid_statuses = [BUG_STATUS_PENDING, BUG_STATUS_REVIEWED, BUG_STATUS_APPROVED, BUG_STATUS_REJECTED]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status

class BugBountyProgram:
    """
    Manages the bug bounty program for the blockchain marketplace.
    """
    def __init__(self):
        self.bug_reports: List[BugReport] = []  # List of submitted bug reports
        self.approved_reports: List[BugReport] = []  # List of approved bug reports
        self.rejected_reports: List[BugReport] = []  # List of rejected bug reports
    
    def submit_bug_report(self, reporter_name: str, description: str) -> str:
        """
        Allows a developer to submit a bug report.
        """
        if not reporter_name or not description:
            raise ValueError("Both reporter_name and description are required.")
        
        bug_report = BugReport(reporter_name, description)
        self.bug_reports.append(bug_report)
        return bug_report.id  # Return the unique ID for tracking
    
    def review_bug_report(self, report_id: str, approve: bool):
        """
        Reviews a bug report and updates its status accordingly.
        """
        bug_report = self._find_bug_report(report_id)
        if approve:
            bug_report.update_status(BUG_STATUS_APPROVED)
            self.approved_reports.append(bug_report)
        else:
            bug_report.update_status(BUG_STATUS_REJECTED)
            self.rejected_reports.append(bug_report)
        self.bug_reports.remove(bug_report)
    
    def list_reports(self, filter_status: str = None) -> List[Dict[str, str]]:
        """
        Lists all bug reports with optional filtering by status.
        """
        reports_to_list = self.bug_reports if filter_status is None else [
            report for report in self.bug_reports if report.status == filter_status
        ]
        return [
            {
                "id": report.id,
                "reporter_name": report.reporter_name,
                "description": report.description,
                "status": report.status,
            }
            for report in reports_to_list
        ]
    
    def calculate_rewards(self) -> float:
        """
        Calculates the total reward amount for all approved reports.
        """
        return len(self.approved_reports) * REWARD_AMOUNT

    def _find_bug_report(self, report_id: str) -> BugReport:
        """
        Helper method to find a bug report by its ID.
        """
        for report in self.bug_reports:
            if report.id == report_id:
                return report
        raise ValueError(f"Bug report with ID {report_id} not found.")

# Example usage
if __name__ == "__main__":
    try:
        program = BugBountyProgram()
        
        # Submit bug reports
        report_id_1 = program.submit_bug_report("Alice", "Critical vulnerability in smart contract.")
        report_id_2 = program.submit_bug_report("Bob", "UI glitch during transaction confirmation.")
        
        # Review bug reports
        program.review_bug_report(report_id_1, approve=True)
        program.review_bug_report(report_id_2, approve=False)
        
        # List all reports
        print("Pending Reports:", program.list_reports(filter_status=BUG_STATUS_PENDING))
        print("Approved Reports:", program.list_reports(filter_status=BUG_STATUS_APPROVED))
        print("Rejected Reports:", program.list_reports(filter_status=BUG_STATUS_REJECTED))
        
        # Calculate rewards
        print("Total Rewards in Crypto:", program.calculate_rewards())
    
    except Exception as e:
        print(f"Error: {e}")
```
