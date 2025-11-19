"""
Generated Code Metadata:
========================
Original URL: https://tos.hyperliquidfndn.org
Prompt: Write a Python function that checks if a user has agreed to the terms of service and privacy policy before allowing participation in an event, based on the structure seen in the Hyper Foundation's terms.
Generated: DETERMINISTIC_f5338b96d70ae76e
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional

class UserAgreement:
    """Represents a user's agreement to terms of service and privacy policy."""

    def __init__(self, 
                 user_id: str, 
                 terms_of_service_version: str, 
                 privacy_policy_version: str, 
                 agreed_at: Optional[datetime] = None):
        """
        Initializes a UserAgreement instance.

        Args:
        - user_id (str): Unique identifier for the user.
        - terms_of_service_version (str): Version of the terms of service agreed to.
        - privacy_policy_version (str): Version of the privacy policy agreed to.
        - agreed_at (Optional[datetime]): Timestamp when the user agreed. Defaults to None.
        """
        self.user_id = user_id
        self.terms_of_service_version = terms_of_service_version
        self.privacy_policy_version = privacy_policy_version
        self.agreed_at = agreed_at

    def has_agreed(self) -> bool:
        """Checks if the user has agreed to the terms."""
        return self.agreed_at is not None

    def agree(self, terms_of_service_version: str, privacy_policy_version: str) -> None:
        """
        Records the user's agreement to the terms of service and privacy policy.

        Args:
        - terms_of_service_version (str): Version of the terms of service.
        - privacy_policy_version (str): Version of the privacy policy.

        Raises:
        - ValueError: If the terms of service or privacy policy version is empty.
        """
        if not terms_of_service_version or not privacy_policy_version:
            raise ValueError("Terms of service and privacy policy versions are required.")

        self.terms_of_service_version = terms_of_service_version
        self.privacy_policy_version = privacy_policy_version
        self.agreed_at = datetime.now()

class EventParticipationChecker:
    """Checks if a user can participate in an event based on their agreement status."""

    def __init__(self, 
                 current_terms_of_service_version: str, 
                 current_privacy_policy_version: str):
        """
        Initializes an EventParticipationChecker instance.

        Args:
        - current_terms_of_service_version (str): Current version of the terms of service.
        - current_privacy_policy_version (str): Current version of the privacy policy.
        """
        self.current_terms_of_service_version = current_terms_of_service_version
        self.current_privacy_policy_version = current_privacy_policy_version

    def can_participate(self, user_agreement: UserAgreement) -> bool:
        """
        Checks if a user can participate in an event.

        Args:
        - user_agreement (UserAgreement): User's agreement status.

        Returns:
        - bool: True if the user can participate, False otherwise.
        """
        if not user_agreement.has_agreed():
            return False

        return (user_agreement.terms_of_service_version == self.current_terms_of_service_version and
                user_agreement.privacy_policy_version == self.current_privacy_policy_version)

def main():
    try:
        # Example usage
        user_agreement = UserAgreement("user123", "", "", None)
        event_checker = EventParticipationChecker("v1.0", "v2.0")

        print("User has agreed:", user_agreement.has_agreed())  # Should print: False
        print("Can participate:", event_checker.can_participate(user_agreement))  # Should print: False

        user_agreement.agree("v1.0", "v2.0")
        print("User has agreed:", user_agreement.has_agreed())  # Should print: True
        print("Can participate:", event_checker.can_participate(user_agreement))  # Should print: True

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
