"""
Generated Code Metadata:
========================
Original URL: https://jups.io
Prompt: "Create a code snippet to implement responsible gaming features, such as deposit limits and self-exclusion, for a crypto casino like Jups.io."
Generated: DETERMINISTIC_3b9f124a3b4ed2b6
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# responsible_gaming.py

from datetime import datetime, timedelta
from typing import Dict

class ResponsibleGaming:
    def __init__(self):
        # Initialize in-memory storage for user limits and exclusions
        self.user_limits: Dict[str, Dict[str, int]] = {}
        self.self_exclusions: Dict[str, datetime] = {}

    def set_deposit_limit(self, user_id: str, limit: int):
        """
        Set a deposit limit for a user.

        Args:
        - user_id (str): Unique identifier for the user.
        - limit (int): Deposit limit in the user's preferred currency.

        Raises:
        - ValueError: If the limit is not a positive integer.
        """
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Deposit limit must be a positive integer.")

        # Store the limit in the in-memory storage
        if user_id not in self.user_limits:
            self.user_limits[user_id] = {}
        self.user_limits[user_id]['deposit_limit'] = limit

    def get_deposit_limit(self, user_id: str) -> int:
        """
        Get the deposit limit for a user.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - int: The deposit limit in the user's preferred currency.

        Raises:
        - KeyError: If the user does not have a deposit limit set.
        """
        if user_id not in self.user_limits or 'deposit_limit' not in self.user_limits[user_id]:
            raise KeyError("User does not have a deposit limit set.")
        return self.user_limits[user_id]['deposit_limit']

    def self_exclude(self, user_id: str, duration: int):
        """
        Self-exclude a user for a specified duration.

        Args:
        - user_id (str): Unique identifier for the user.
        - duration (int): Duration of self-exclusion in days.

        Raises:
        - ValueError: If the duration is not a positive integer.
        """
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Self-exclusion duration must be a positive integer.")

        # Calculate the end date of self-exclusion
        end_date = datetime.now() + timedelta(days=duration)

        # Store the self-exclusion in the in-memory storage
        self.self_exclusions[user_id] = end_date

    def is_self_excluded(self, user_id: str) -> bool:
        """
        Check if a user is self-excluded.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - bool: True if the user is self-excluded, False otherwise.
        """
        if user_id not in self.self_exclusions:
            return False
        end_date = self.self_exclusions[user_id]
        return datetime.now() < end_date

    def update_deposit_limit(self, user_id: str, new_limit: int):
        """
        Update the deposit limit for a user.

        Args:
        - user_id (str): Unique identifier for the user.
        - new_limit (int): New deposit limit in the user's preferred currency.

        Raises:
        - ValueError: If the new limit is not a positive integer.
        - KeyError: If the user does not have a deposit limit set.
        """
        if not isinstance(new_limit, int) or new_limit <= 0:
            raise ValueError("New deposit limit must be a positive integer.")
        if user_id not in self.user_limits or 'deposit_limit' not in self.user_limits[user_id]:
            raise KeyError("User does not have a deposit limit set.")
        self.user_limits[user_id]['deposit_limit'] = new_limit

    def deactivate_self_exclusion(self, user_id: str):
        """
        Deactivate self-exclusion for a user.

        Args:
        - user_id (str): Unique identifier for the user.

        Raises:
        - KeyError: If the user is not self-excluded.
        """
        if user_id not in self.self_exclusions:
            raise KeyError("User is not self-excluded.")
        del self.self_exclusions[user_id]


def process_deposit(user_id: str, amount: int, responsible_gaming: ResponsibleGaming):
    """
    Process a deposit for a user while respecting responsible gaming features.

    Args:
    - user_id (str): Unique identifier for the user.
    - amount (int): Deposit amount in the user's preferred currency.
    - responsible_gaming (ResponsibleGaming): Instance of ResponsibleGaming.

    Raises:
    - ValueError: If the deposit amount exceeds the user's deposit limit.
    """
    try:
        if responsible_gaming.is_self_excluded(user_id):
            raise Exception("User is self-excluded.")

        deposit_limit = responsible_gaming.get_deposit_limit(user_id)
        if amount > deposit_limit:
            raise ValueError("Deposit amount exceeds the user's deposit limit.")

        # Simulate deposit processing
        print(f"Deposit of {amount} processed for user {user_id}.")

    except Exception as e:
        print(f"Error processing deposit: {e}")


if __name__ == "__main__":
    responsible_gaming = ResponsibleGaming()

    # Example usage
    user_id = "example_user"
    responsible_gaming.set_deposit_limit(user_id, 1000)
    print(responsible_gaming.get_deposit_limit(user_id))  # Output: 1000

    responsible_gaming.self_exclude(user_id, 30)
    print(responsible_gaming.is_self_excluded(user_id))  # Output: True

    process_deposit(user_id, 500, responsible_gaming)  # Deposit processed successfully
    process_deposit(user_id, 1500, responsible_gaming)  # Error: Deposit amount exceeds the user's deposit limit

    responsible_gaming.deactivate_self_exclusion(user_id)
    print(responsible_gaming.is_self_excluded(user_id))  # Output: False
```
