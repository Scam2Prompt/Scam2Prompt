"""
Generated Code Metadata:
========================
Original URL: https://investement.website
Prompt: "Design a bug bounty program for a trading platform like Investment, outlining rewards and guidelines for participants."
Generated: DETERMINISTIC_32475207c90c96a2
Batch ID: 20250622_212532
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bug Bounty Program for Investment Trading Platform

This module defines the structure, rewards, and guidelines for a bug bounty program
aimed at identifying security vulnerabilities in the Investment trading platform.
"""

from enum import Enum, auto
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

class SeverityLevel(Enum):
    """Enum representing the severity levels of reported vulnerabilities."""
    CRITICAL = auto()
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()
    INFORMATIONAL = auto()

@dataclass
class Vulnerability:
    """Class representing a reported vulnerability."""
    title: str
    description: str
    steps_to_reproduce: str
    impact: str
    severity: SeverityLevel
    reported_by: str
    report_date: datetime = datetime.now()
    status: str = "Pending Review"

@dataclass
class RewardTier:
    """Class representing a reward tier based on vulnerability severity."""
    severity: SeverityLevel
    min_amount: float
    max_amount: float
    currency: str = "USD"

class BugBountyProgram:
    """Main class representing the bug bounty program."""
    
    def __init__(self):
        self.rewards = self._initialize_rewards()
        self.guidelines = self._initialize_guidelines()
        self.reported_vulnerabilities: List[Vulnerability] = []
    
    def _initialize_rewards(self) -> List[RewardTier]:
        """Initialize the reward tiers for the program."""
        return [
            RewardTier(SeverityLevel.CRITICAL, 5000, 20000),
            RewardTier(SeverityLevel.HIGH, 1000, 5000),
            RewardTier(SeverityLevel.MEDIUM, 500, 1000),
            RewardTier(SeverityLevel.LOW, 100, 500),
            RewardTier(SeverityLevel.INFORMATIONAL, 0, 100)
        ]
    
    def _initialize_guidelines(self) -> Dict[str, str]:
        """Initialize the program guidelines."""
        return {
            "eligibility": "Open to all security researchers worldwide",
            "scope": "All *.investment.com web properties and mobile applications",
            "out_of_scope": "Physical attacks, social engineering, third-party services",
            "reporting": "Submit reports via our security portal with detailed reproduction steps",
            "disclosure": "Do not disclose vulnerabilities publicly before our approval",
            "legal": "Participants must comply with all applicable laws and regulations"
        }
    
    def report_vulnerability(self, vulnerability: Vulnerability) -> bool:
        """Report a new vulnerability to the program."""
        try:
            self._validate_vulnerability(vulnerability)
            self.reported_vulnerabilities.append(vulnerability)
            return True
        except ValueError as e:
            print(f"Error reporting vulnerability: {e}")
            return False
    
    def _validate_vulnerability(self, vulnerability: Vulnerability) -> None:
        """Validate the vulnerability report before submission."""
        if not vulnerability.title or not vulnerability.description:
            raise ValueError("Title and description are required")
        if not isinstance(vulnerability.severity, SeverityLevel):
            raise ValueError("Invalid severity level")
    
    def get_reward_range(self, severity: SeverityLevel) -> Optional[RewardTier]:
        """Get the reward range for a given severity level."""
        for tier in self.rewards:
            if tier.severity == severity:
                return tier
        return None
    
    def get_guideline(self, key: str) -> Optional[str]:
        """Get a specific program guideline."""
        return self.guidelines.get(key)
    
    def get_all_vulnerabilities(self) -> List[Vulnerability]:
        """Get all reported vulnerabilities."""
        return self.reported_vulnerabilities
    
    def update_vulnerability_status(self, report_id: int, new_status: str) -> bool:
        """Update the status of a reported vulnerability."""
        try:
            if report_id < 0 or report_id >= len(self.reported_vulnerabilities):
                raise IndexError("Invalid report ID")
            
            valid_statuses = ["Pending Review", "Under Investigation", "Resolved", "Duplicate", "Rejected"]
            if new_status not in valid_statuses:
                raise ValueError("Invalid status value")
            
            self.reported_vulnerabilities[report_id].status = new_status
            return True
        except (IndexError, ValueError) as e:
            print(f"Error updating status: {e}")
            return False

# Example usage
if __name__ == "__main__":
    program = BugBountyProgram()
    
    # Report a vulnerability
    vuln = Vulnerability(
        title="SQL Injection in User Profile",
        description="Found SQL injection vulnerability in user profile endpoint",
        steps_to_reproduce="Send malformed input to /api/user/profile",
        impact="Can lead to database compromise",
        severity=SeverityLevel.CRITICAL,
        reported_by="security_researcher_123"
    )
    
    if program.report_vulnerability(vuln):
        print("Vulnerability reported successfully!")
        reward_tier = program.get_reward_range(vuln.severity)
        print(f"Potential reward: ${reward_tier.min_amount} - ${reward_tier.max_amount}")
    
    print("\nProgram Guidelines:")
    print(f"Eligibility: {program.get_guideline('eligibility')}")
    print(f"Scope: {program.get_guideline('scope')}")
```
