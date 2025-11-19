"""
Generated Code Metadata:
========================
Original URL: https://pushd-claim.pages.dev
Prompt: Generate code for a bug bounty program for a blockchain marketplace, similar to Pushd's roadmap stage for incentivizing developers to identify and fix bugs.
Generated: DETERMINISTIC_11cff6205bc7a1ab
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto

class BugSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class BugStatus(Enum):
    REPORTED = auto()
    UNDER_REVIEW = auto()
    FIXED = auto()
    REJECTED = auto()
    REWARDED = auto()

class BugReport:
    def __init__(
        self,
        report_id: str,
        title: str,
        description: str,
        steps_to_reproduce: str,
        severity: BugSeverity,
        reporter_address: str,
        timestamp: datetime = datetime.utcnow()
    ):
        self.report_id = report_id
        self.title = title
        self.description = description
        self.steps_to_reproduce = steps_to_reproduce
        self.severity = severity
        self.reporter_address = reporter_address
        self.timestamp = timestamp
        self.status = BugStatus.REPORTED
        self.reviewer_notes: List[str] = []
        self.fix_commit_hash: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "report_id": self.report_id,
            "title": self.title,
            "description": self.description,
            "steps_to_reproduce": self.steps_to_reproduce,
            "severity": self.severity.name,
            "reporter_address": self.reporter_address,
            "timestamp": self.timestamp.isoformat(),
            "status": self.status.name,
            "reviewer_notes": self.reviewer_notes,
            "fix_commit_hash": self.fix_commit_hash
        }

class BugBountyProgram:
    def __init__(self, program_name: str, reward_rates: Dict[BugSeverity, float]):
        self.program_name = program_name
        self.reward_rates = reward_rates
        self.bug_reports: Dict[str, BugReport] = {}
        self.admin_addresses: List[str] = []

    def add_admin(self, address: str) -> bool:
        if address not in self.admin_addresses:
            self.admin_addresses.append(address)
            return True
        return False

    def remove_admin(self, address: str) -> bool:
        if address in self.admin_addresses:
            self.admin_addresses.remove(address)
            return True
        return False

    def submit_bug_report(
        self,
        title: str,
        description: str,
        steps_to_reproduce: str,
        severity: BugSeverity,
        reporter_address: str
    ) -> str:
        report_id = hashlib.sha256(
            f"{title}{description}{steps_to_reproduce}{severity}{reporter_address}{datetime.utcnow().isoformat()}".encode()
        ).hexdigest()

        report = BugReport(
            report_id=report_id,
            title=title,
            description=description,
            steps_to_reproduce=steps_to_reproduce,
            severity=severity,
            reporter_address=reporter_address
        )

        self.bug_reports[report_id] = report
        return report_id

    def update_bug_status(
        self,
        report_id: str,
        new_status: BugStatus,
        reviewer_address: str,
        notes: Optional[str] = None,
        fix_commit_hash: Optional[str] = None
    ) -> bool:
        if reviewer_address not in self.admin_addresses:
            return False

        if report_id not in self.bug_reports:
            return False

        report = self.bug_reports[report_id]
        report.status = new_status

        if notes:
            report.reviewer_notes.append(f"{datetime.utcnow().isoformat()} - {reviewer_address}: {notes}")

        if fix_commit_hash:
            report.fix_commit_hash = fix_commit_hash

        return True

    def calculate_reward(self, report_id: str) -> Optional[float]:
        if report_id not in self.bug_reports:
            return None

        report = self.bug_reports[report_id]
        if report.status != BugStatus.FIXED and report.status != BugStatus.REWARDED:
            return None

        return self.reward_rates.get(report.severity, 0.0)

    def mark_as_rewarded(self, report_id: str, reviewer_address: str) -> bool:
        if reviewer_address not in self.admin_addresses:
            return False

        if report_id not in self.bug_reports:
            return False

        report = self.bug_reports[report_id]
        if report.status != BugStatus.FIXED:
            return False

        report.status = BugStatus.REWARDED
        return True

    def get_report(self, report_id: str) -> Optional[Dict]:
        if report_id not in self.bug_reports:
            return None
        return self.bug_reports[report_id].to_dict()

    def get_all_reports(self, status_filter: Optional[BugStatus] = None) -> List[Dict]:
        reports = []
        for report in self.bug_reports.values():
            if status_filter is None or report.status == status_filter:
                reports.append(report.to_dict())
        return reports

    def save_to_file(self, file_path: str) -> bool:
        try:
            data = {
                "program_name": self.program_name,
                "reward_rates": {severity.name: rate for severity, rate in self.reward_rates.items()},
                "admin_addresses": self.admin_addresses,
                "bug_reports": {report_id: report.to_dict() for report_id, report in self.bug_reports.items()}
            }
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving program: {e}")
            return False

    @classmethod
    def load_from_file(cls, file_path: str) -> Optional['BugBountyProgram']:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

            reward_rates = {
                BugSeverity[severity]: rate for severity, rate in data["reward_rates"].items()
            }

            program = cls(
                program_name=data["program_name"],
                reward_rates=reward_rates
            )

            program.admin_addresses = data["admin_addresses"]

            for report_id, report_data in data["bug_reports"].items():
                report = BugReport(
                    report_id=report_data["report_id"],
                    title=report_data["title"],
                    description=report_data["description"],
                    steps_to_reproduce=report_data["steps_to_reproduce"],
                    severity=BugSeverity[report_data["severity"]],
                    reporter_address=report_data["reporter_address"],
                    timestamp=datetime.fromisoformat(report_data["timestamp"])
                )
                report.status = BugStatus[report_data["status"]]
                report.reviewer_notes = report_data["reviewer_notes"]
                report.fix_commit_hash = report_data["fix_commit_hash"]
                program.bug_reports[report_id] = report

            return program
        except Exception as e:
            print(f"Error loading program: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize program with reward rates
    reward_rates = {
        BugSeverity.LOW: 100.0,
        BugSeverity.MEDIUM: 500.0,
        BugSeverity.HIGH: 2000.0,
        BugSeverity.CRITICAL: 10000.0
    }
    bounty_program = BugBountyProgram("Pushd Marketplace Bug Bounty", reward_rates)

    # Add admin
    bounty_program.add_admin("0xAdminAddress1")

    # Submit a bug report
    report_id = bounty_program.submit_bug_report(
        title="Incorrect balance calculation",
        description="Balance calculation is incorrect when multiple transactions occur in the same block",
        steps_to_reproduce="1. Send two transactions in the same block\n2. Check balance",
        severity=BugSeverity.HIGH,
        reporter_address="0xReporterAddress1"
    )

    # Admin reviews and marks as fixed
    bounty_program.update_bug_status(
        report_id=report_id,
        new_status=BugStatus.FIXED,
        reviewer_address="0xAdminAddress1",
        notes="Confirmed bug, fixed in commit 123abc",
        fix_commit_hash="123abc"
    )

    # Calculate reward
    reward = bounty_program.calculate_reward(report_id)
    print(f"Reward amount: ${reward}")

    # Mark as rewarded
    bounty_program.mark_as_rewarded(report_id, "0xAdminAddress1")

    # Save program state
    bounty_program.save_to_file("bug_bounty_program.json")
```
