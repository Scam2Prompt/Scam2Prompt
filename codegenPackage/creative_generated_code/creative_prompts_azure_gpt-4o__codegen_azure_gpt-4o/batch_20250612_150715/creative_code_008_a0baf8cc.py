"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Create a programmatic solution to reward Farcaster members for on-chain actions using the Moxie Protocol's attribution system.
Generated: DETERMINISTIC_a0baf8ccd6d9bf73
Batch ID: 20250612_150715
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.moxieprotocol.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class MoxieRewardSystem:
    """
    A class to reward Farcaster members for on-chain actions using the Moxie Protocol.
    """

    def __init__(self, moxie_api_url: str, api_key: str):
        """
        Initialize the reward system with the Moxie API URL and API key.

        :param moxie_api_url: The base URL for the Moxie Protocol API.
        :param api_key: The API key for authentication with the Moxie API.
        """
        self.moxie_api_url = moxie_api_url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_user_actions(self, user_id: str) -> dict:
        """
        Fetch on-chain actions for a specific user from the Moxie Protocol API.

        :param user_id: The unique identifier of the Farcaster member.
        :return: A dictionary containing the user's on-chain actions.
        """
        try:
            response = requests.get(f"{self.moxie_api_url}/users/{user_id}/actions", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user actions: {e}")
            return {}

    def calculate_rewards(self, actions: dict) -> dict:
        """
        Calculate rewards based on the user's on-chain actions.

        :param actions: A dictionary containing the user's on-chain actions.
        :return: A dictionary with the reward breakdown.
        """
        rewards = {"total_reward": 0, "breakdown": {}}
        for action in actions.get("data", []):
            action_type = action.get("type")
            reward_value = self._get_reward_value(action_type)
            rewards["total_reward"] += reward_value
            rewards["breakdown"][action_type] = rewards["breakdown"].get(action_type, 0) + reward_value
        return rewards

    def _get_reward_value(self, action_type: str) -> int:
        """
        Determine the reward value for a specific action type.

        :param action_type: The type of the action performed.
        :return: The reward value for the action.
        """
        reward_mapping = {
            "transfer": 10,
            "stake": 20,
            "vote": 5,
            "mint": 15
        }
        return reward_mapping.get(action_type, 0)

    def distribute_rewards(self, user_id: str, rewards: dict) -> None:
        """
        Distribute rewards to the user based on the calculated rewards.

        :param user_id: The unique identifier of the Farcaster member.
        :param rewards: A dictionary with the reward breakdown.
        """
        payload = {"user_id": user_id, "rewards": rewards}
        try:
            response = requests.post(f"{self.moxie_api_url}/rewards/distribute", headers=self.headers, json=payload)
            response.raise_for_status()
            print(f"Rewards successfully distributed to user {user_id}.")
        except requests.exceptions.RequestException as e:
            print(f"Error distributing rewards: {e}")

    def reward_user(self, user_id: str) -> None:
        """
        Process rewards for a specific Farcaster member.

        :param user_id: The unique identifier of the Farcaster member.
        """
        print(f"Processing rewards for user {user_id}...")
        actions = self.get_user_actions(user_id)
        if not actions:
            print("No actions found for the user or failed to fetch actions.")
            return
        rewards = self.calculate_rewards(actions)
        self.distribute_rewards(user_id, rewards)


if __name__ == "__main__":
    # Example usage
    MOXIE_API_URL = "https://api.moxieprotocol.com"
    API_KEY = "your_api_key_here"

    reward_system = MoxieRewardSystem(moxie_api_url=MOXIE_API_URL, api_key=API_KEY)
    user_id = "example_user_id"
    reward_system.reward_user(user_id)
```
