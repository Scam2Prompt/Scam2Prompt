"""
Generated Code Metadata:
========================
Original URL: https://adrop.one
Prompt: Design a system to handle airdrop events on the TON blockchain, including user eligibility and reward calculation.
Generated: DETERMINISTIC_2c33b3e7b1212a65
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

class AirdropEvent:
    def __init__(self, event_id: str, total_rewards: float, eligibility_criteria: Dict[str, Any]):
        """
        Initialize an AirdropEvent instance.

        :param event_id: Unique identifier for the airdrop event
        :param total_rewards: Total rewards available for the airdrop
        :param eligibility_criteria: Criteria to determine user eligibility
        """
        self.event_id = event_id
        self.total_rewards = total_rewards
        self.eligibility_criteria = eligibility_criteria
        self.participants = {}

    def register_participant(self, user_id: str, user_data: Dict[str, Any]) -> None:
        """
        Register a participant for the airdrop if they meet eligibility criteria.

        :param user_id: Unique identifier for the user
        :param user_data: Dictionary containing user data for eligibility check
        :raises ValueError: If the user does not meet eligibility criteria
        """
        if self.is_eligible(user_data):
            self.participants[user_id] = user_data
            logging.info(f"User {user_id} registered for airdrop {self.event_id}.")
        else:
            logging.warning(f"User {user_id} is not eligible for airdrop {self.event_id}.")
            raise ValueError(f"User {user_id} does not meet eligibility criteria.")

    def is_eligible(self, user_data: Dict[str, Any]) -> bool:
        """
        Check if a user meets the eligibility criteria.

        :param user_data: Dictionary containing user data
        :return: True if eligible, False otherwise
        """
        # Example eligibility check based on criteria
        for key, value in self.eligibility_criteria.items():
            if user_data.get(key) != value:
                return False
        return True

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculate rewards for each participant based on their eligibility.

        :return: Dictionary mapping user_id to their calculated reward
        """
        if not self.participants:
            logging.warning("No participants registered for reward calculation.")
            return {}

        reward_per_participant = self.total_rewards / len(self.participants)
        rewards = {user_id: reward_per_participant for user_id in self.participants}
        logging.info(f"Calculated rewards for airdrop {self.event_id}: {rewards}")
        return rewards

    def to_json(self) -> str:
        """
        Convert the airdrop event to a JSON string.

        :return: JSON representation of the airdrop event
        """
        return json.dumps({
            "event_id": self.event_id,
            "total_rewards": self.total_rewards,
            "eligibility_criteria": self.eligibility_criteria,
            "participants": list(self.participants.keys())
        }, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Define eligibility criteria
        criteria = {
            "is_verified": True,
            "min_balance": 100
        }

        # Create an airdrop event
        airdrop = AirdropEvent(event_id="AIRDROP_001", total_rewards=1000.0, eligibility_criteria=criteria)

        # Register participants
        airdrop.register_participant("user_1", {"is_verified": True, "min_balance": 100})
        airdrop.register_participant("user_2", {"is_verified": True, "min_balance": 50})  # This will raise an error

        # Calculate rewards
        rewards = airdrop.calculate_rewards()
        print(rewards)

        # Output the airdrop event details
        print(airdrop.to_json())

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
