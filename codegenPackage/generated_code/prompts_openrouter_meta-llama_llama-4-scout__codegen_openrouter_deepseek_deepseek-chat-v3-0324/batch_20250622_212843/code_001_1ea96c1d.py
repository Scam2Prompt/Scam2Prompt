"""
Generated Code Metadata:
========================
Original URL: https://tos.hyperliquidfndn.org
Prompt: Generate a code snippet for a user agreement system that requires acceptance of terms and conditions, similar to those outlined for the Hyper Foundation's HYPE event.
Generated: DETERMINISTIC_1ea96c1db47af850
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class UserAgreement:
    """
    Represents a user agreement with terms and conditions.
    """
    version: str
    content: str
    effective_date: datetime.date
    required: bool = True


class UserAgreementSystem:
    """
    Manages user agreements and tracks user acceptances.
    """
    def __init__(self):
        self.agreements: Dict[str, UserAgreement] = {}
        self.user_acceptances: Dict[str, Dict[str, datetime.datetime]] = {}

    def add_agreement(self, agreement: UserAgreement) -> None:
        """
        Adds a new agreement to the system.
        """
        if agreement.version in self.agreements:
            raise ValueError(f"Agreement version {agreement.version} already exists")
        self.agreements[agreement.version] = agreement

    def get_current_agreement(self) -> Optional[UserAgreement]:
        """
        Returns the most recent agreement based on effective date.
        """
        if not self.agreements:
            return None
        return max(self.agreements.values(), key=lambda a: a.effective_date)

    def accept_agreement(self, user_id: str, version: str) -> None:
        """
        Records a user's acceptance of an agreement.
        """
        if version not in self.agreements:
            raise ValueError(f"Agreement version {version} does not exist")
        
        if user_id not in self.user_acceptances:
            self.user_acceptances[user_id] = {}
        
        self.user_acceptances[user_id][version] = datetime.datetime.now()

    def has_accepted(self, user_id: str, version: str) -> bool:
        """
        Checks if a user has accepted a specific agreement version.
        """
        return version in self.user_acceptances.get(user_id, {})

    def has_accepted_current(self, user_id: str) -> bool:
        """
        Checks if a user has accepted the current agreement.
        """
        current = self.get_current_agreement()
        if not current:
            return False
        return self.has_accepted(user_id, current.version)

    def get_user_acceptance_data(self, user_id: str) -> Dict[str, Any]:
        """
        Returns all acceptance data for a user.
        """
        return {
            'acceptances': self.user_acceptances.get(user_id, {}),
            'current_agreement': self.get_current_agreement(),
            'has_accepted_current': self.has_accepted_current(user_id)
        }


# Example usage
if __name__ == "__main__":
    system = UserAgreementSystem()
    
    # Add an agreement
    agreement = UserAgreement(
        version="1.0",
        content="By participating in this event, you agree to...",
        effective_date=datetime.date(2023, 1, 1)
    )
    system.add_agreement(agreement)
    
    # Simulate user acceptance
    user_id = "user123"
    system.accept_agreement(user_id, "1.0")
    
    # Check acceptance status
    print(f"User has accepted current agreement: {system.has_accepted_current(user_id)}")
    print(f"User acceptance data: {system.get_user_acceptance_data(user_id)}")
```
