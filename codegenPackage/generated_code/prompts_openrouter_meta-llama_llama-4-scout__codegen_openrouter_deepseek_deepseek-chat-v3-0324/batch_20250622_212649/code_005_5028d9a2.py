"""
Generated Code Metadata:
========================
Original URL: https://spark.fishersclubs.com
Prompt: "Design a bug bounty program for a DeFi platform like Spark, including guidelines for reporting vulnerabilities and rewards for white hat hackers."
Generated: DETERMINISTIC_5028d9a275989c67
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DeFi Bug Bounty Program Implementation for Spark Platform

This module implements a bug bounty program system for a DeFi platform,
including vulnerability reporting guidelines and reward structures.
"""

from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime
import hashlib
import json
from dataclasses import dataclass, field
import re

class SeverityLevel(Enum):
    """Enum representing the severity levels of reported vulnerabilities."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class VulnerabilityReport:
    """Class representing a vulnerability report submitted by a white hat hacker."""
    reporter_id: str
    title: str
    description: str
    steps_to_reproduce: str
    impact: str
    severity: SeverityLevel
    proof_of_concept: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    status: str = "pending"
    report_id: str = field(init=False)

    def __post_init__(self):
        """Generate a unique report ID using SHA-256 hash."""
        report_data = f"{self.reporter_id}{self.title}{self.timestamp}"
        self.report_id = hashlib.sha256(report_data.encode()).hexdigest()

class BugBountyProgram:
    """Class representing the bug bounty program with reporting and reward logic."""
    
    def __init__(self):
        self.reports: Dict[str, VulnerabilityReport] = {}
        self.reward_structure = {
            SeverityLevel.LOW: 500,
            SeverityLevel.MEDIUM: 2000,
            SeverityLevel.HIGH: 10000,
            SeverityLevel.CRITICAL: 50000
        }
        self.guidelines = """
        Spark DeFi Bug Bounty Program Guidelines:
        
        1. Scope:
           - All smart contracts deployed by Spark
           - Web applications and APIs
           - Mobile applications
        
        2. Out of Scope:
           - Theoretical vulnerabilities without proof
           - UI/UX issues without security impact
           - Third-party services
        
        3. Reporting Requirements:
           - Detailed description of vulnerability
           - Steps to reproduce
           - Impact analysis
           - Proof of Concept (preferred)
        
        4. Eligibility:
           - First reporter of a unique vulnerability
           - Good faith effort to avoid damage
           - Compliance with all program rules
        """

    def submit_report(self, report: VulnerabilityReport) -> str:
        """Submit a vulnerability report to the bounty program."""
        if not self._validate_report(report):
            raise ValueError("Invalid report submission")
        
        self.reports[report.report_id] = report
        return report.report_id

    def _validate_report(self, report: VulnerabilityReport) -> bool:
        """Validate the report meets all requirements."""
        if not report.title or not report.description:
            return False
        if not report.steps_to_reproduce or not report.impact:
            return False
        if not isinstance(report.severity, SeverityLevel):
            return False
        return True

    def evaluate_report(self, report_id: str, valid: bool, notes: str = "") -> None:
        """Evaluate a submitted report and update its status."""
        if report_id not in self.reports:
            raise ValueError("Report not found")
        
        report = self.reports[report_id]
        if valid:
            report.status = "accepted"
        else:
            report.status = "rejected"
            report.proof_of_concept = None  # Remove sensitive data

    def calculate_reward(self, report_id: str) -> float:
        """Calculate the reward amount based on severity."""
        if report_id not in self.reports:
            raise ValueError("Report not found")
        
        report = self.reports[report_id]
        if report.status != "accepted":
            raise ValueError("Report not accepted")
        
        return self.reward_structure[report.severity]

    def get_guidelines(self) -> str:
        """Return the program guidelines."""
        return self.guidelines

    def get_report(self, report_id: str) -> VulnerabilityReport:
        """Retrieve a specific report by ID."""
        return self.reports.get(report_id)

    def get_all_reports(self, status_filter: Optional[str] = None) -> List[VulnerabilityReport]:
        """Retrieve all reports, optionally filtered by status."""
        if status_filter:
            return [r for r in self.reports.values() if r.status == status_filter]
        return list(self.reports.values())

class Reporter:
    """Class representing a white hat hacker participating in the program."""
    
    def __init__(self, email: str, name: str):
        if not self._validate_email(email):
            raise ValueError("Invalid email format")
        
        self.email = email
        self.name = name
        self.reporter_id = hashlib.sha256(email.encode()).hexdigest()
        self.submitted_reports: List[str] = []
        self.total_rewards: float = 0.0

    def _validate_email(self, email: str) -> bool:
        """Validate email format using regex."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def submit_vulnerability(self, bounty_program: BugBountyProgram, report: VulnerabilityReport) -> str:
        """Submit a vulnerability report to the bounty program."""
        if report.reporter_id != self.reporter_id:
            raise ValueError("Reporter ID mismatch")
        
        report_id = bounty_program.submit_report(report)
        self.submitted_reports.append(report_id)
        return report_id

    def receive_reward(self, bounty_program: BugBountyProgram, report_id: str) -> float:
        """Receive reward for an accepted vulnerability report."""
        if report_id not in self.submitted_reports:
            raise ValueError("Report not submitted by this reporter")
        
        reward = bounty_program.calculate_reward(report_id)
        self.total_rewards += reward
        return reward

def save_program_state(program: BugBountyProgram, filename: str) -> None:
    """Save the program state to a JSON file."""
    state = {
        "reports": {
            rid: {
                "reporter_id": r.reporter_id,
                "title": r.title,
                "status": r.status,
                "severity": r.severity.name,
                "timestamp": r.timestamp.isoformat()
            }
            for rid, r in program.reports.items()
        }
    }
    
    with open(filename, 'w') as f:
        json.dump(state, f, indent=2)

def load_program_state(filename: str) -> BugBountyProgram:
    """Load the program state from a JSON file."""
    program = BugBountyProgram()
    
    try:
        with open(filename, 'r') as f:
            state = json.load(f)
            
            # Note: In a real implementation, you would reconstruct full reports
            # This is simplified for demonstration
            for rid, r in state.get("reports", {}).items():
                dummy_report = VulnerabilityReport(
                    reporter_id=r["reporter_id"],
                    title=r["title"],
                    description="",
                    steps_to_reproduce="",
                    impact="",
                    severity=SeverityLevel[r["severity"]]
                )
                dummy_report.report_id = rid
                dummy_report.status = r["status"]
                program.reports[rid] = dummy_report
                
    except FileNotFoundError:
        pass  # No existing state
    
    return program
```
