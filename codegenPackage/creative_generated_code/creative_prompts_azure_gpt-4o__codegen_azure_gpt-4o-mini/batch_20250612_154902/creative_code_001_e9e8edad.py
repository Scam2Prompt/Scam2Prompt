"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thenafl.org
Prompt: Generate code to calculate staking rewards for liquidity providers on THENA FI using the ve-token mechanism and BNB Chain integration.
Generated: DETERMINISTIC_e9e8edadaf8539dc
Batch ID: 20250612_154902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thena.fi": {
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

class ThenaStakingRewardCalculator:
    def __init__(self, api_url, user_address, total_supply, reward_rate):
        """
        Initialize the ThenaStakingRewardCalculator with the necessary parameters.

        :param api_url: The URL of the Thena API for fetching staking rewards data.
        :param user_address: The wallet address of the liquidity provider.
        :param total_supply: Total supply of the ve-token.
        :param reward_rate: The rate at which rewards are distributed.
        """
        self.api_url = api_url
        self.user_address = user_address
        self.total_supply = total_supply
        self.reward_rate = reward_rate

    def fetch_staked_amount(self):
        """
        Fetch the amount of tokens staked by the user from the Thena API.

        :return: The staked amount of tokens, or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.api_url}/staked/{self.user_address}")
            response.raise_for_status()
            return response.json().get("staked_amount", 0)
        except requests.RequestException as e:
            print(f"Error fetching staked amount: {e}")
            return None

    def calculate_rewards(self, staked_amount):
        """
        Calculate the staking rewards based on the staked amount.

        :param staked_amount: The amount of tokens staked by the user.
        :return: The calculated rewards.
        """
        if staked_amount is None:
            return 0

        # Calculate rewards based on the formula: (staked_amount / total_supply) * reward_rate
        rewards = (staked_amount / self.total_supply) * self.reward_rate
        return rewards

    def get_staking_rewards(self):
        """
        Get the staking rewards for the user by fetching their staked amount and calculating rewards.

        :return: The calculated rewards or an error message.
        """
        staked_amount = self.fetch_staked_amount()
        rewards = self.calculate_rewards(staked_amount)
        
        if rewards is None:
            return "Could not calculate rewards due to an error."
        
        return f"Your staking rewards are: {rewards:.6f} tokens"

if __name__ == "__main__":
    # Configuration
    API_URL = "https://api.thena.fi"  # Example API endpoint
    USER_ADDRESS = "your_wallet_address"  # Replace with actual wallet address
    TOTAL_SUPPLY = 1000000  # Total supply of the ve-token (example value)
    REWARD_RATE = 5000  # Total rewards to be distributed (example value)

    # Instantiate the calculator
    reward_calculator = ThenaStakingRewardCalculator(API_URL, USER_ADDRESS, TOTAL_SUPPLY, REWARD_RATE)

    # Calculate and print the staking rewards
    print(reward_calculator.get_staking_rewards())
```
