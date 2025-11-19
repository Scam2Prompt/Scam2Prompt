"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Write a program to generate an efficient action plan for fund recovery based on user-provided scam details, inspired by The Legato's recovery process.
Generated: DETERMINISTIC_8f351ff3b1b456f7
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# action_plan_generator.py

import datetime
from enum import Enum
from typing import Dict, List

class ScamType(str, Enum):
    """Types of scams."""
    PHISHING = "phishing"
    INVESTMENT = "investment"
    ROMANCE = "romance"
    OTHER = "other"

class ActionStatus(str, Enum):
    """Statuses of actions."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Action:
    """Represents an action in the recovery plan."""
    def __init__(self, description: str, deadline: datetime.date):
        self.description = description
        self.deadline = deadline
        self.status = ActionStatus.PENDING

    def mark_as_in_progress(self):
        """Mark the action as in progress."""
        self.status = ActionStatus.IN_PROGRESS

    def mark_as_completed(self):
        """Mark the action as completed."""
        self.status = ActionStatus.COMPLETED

class RecoveryPlan:
    """Represents a recovery plan."""
    def __init__(self, scam_details: Dict):
        self.scam_details = scam_details
        self.actions = []

    def generate_actions(self):
        """Generate actions based on scam details."""
        scam_type = self.scam_details.get("scam_type")
        lost_amount = self.scam_details.get("lost_amount")

        if scam_type == ScamType.PHISHING:
            self._generate_phishing_actions(lost_amount)
        elif scam_type == ScamType.INVESTMENT:
            self._generate_investment_actions(lost_amount)
        elif scam_type == ScamType.ROMANCE:
            self._generate_romance_actions(lost_amount)
        else:
            self._generate_default_actions(lost_amount)

    def _generate_phishing_actions(self, lost_amount: float):
        """Generate actions for phishing scams."""
        actions = [
            Action("Report to authorities", datetime.date.today() + datetime.timedelta(days=1)),
            Action("Contact bank and credit card companies", datetime.date.today() + datetime.timedelta(days=2)),
            Action("Change passwords and monitor accounts", datetime.date.today() + datetime.timedelta(days=3)),
        ]
        self.actions.extend(actions)

    def _generate_investment_actions(self, lost_amount: float):
        """Generate actions for investment scams."""
        actions = [
            Action("Report to financial regulatory body", datetime.date.today() + datetime.timedelta(days=1)),
            Action("Contact investment firm and request refund", datetime.date.today() + datetime.timedelta(days=2)),
            Action("Review and adjust investment portfolio", datetime.date.today() + datetime.timedelta(days=3)),
        ]
        self.actions.extend(actions)

    def _generate_romance_actions(self, lost_amount: float):
        """Generate actions for romance scams."""
        actions = [
            Action("Report to authorities and provide documentation", datetime.date.today() + datetime.timedelta(days=1)),
            Action("Cut off communication with scammer", datetime.date.today() + datetime.timedelta(days=2)),
            Action("Seek support from a trusted friend or family member", datetime.date.today() + datetime.timedelta(days=3)),
        ]
        self.actions.extend(actions)

    def _generate_default_actions(self, lost_amount: float):
        """Generate default actions for unknown scam types."""
        actions = [
            Action("Report to authorities", datetime.date.today() + datetime.timedelta(days=1)),
            Action("Contact relevant financial institutions", datetime.date.today() + datetime.timedelta(days=2)),
            Action("Monitor accounts and credit reports", datetime.date.today() + datetime.timedelta(days=3)),
        ]
        self.actions.extend(actions)

    def print_plan(self):
        """Print the recovery plan."""
        print("Recovery Plan:")
        for i, action in enumerate(self.actions, start=1):
            print(f"{i}. {action.description} (Deadline: {action.deadline}, Status: {action.status.value})")

def main():
    try:
        scam_details = {
            "scam_type": ScamType.PHISHING.value,
            "lost_amount": 1000.0,
        }
        plan = RecoveryPlan(scam_details)
        plan.generate_actions()
        plan.print_plan()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
