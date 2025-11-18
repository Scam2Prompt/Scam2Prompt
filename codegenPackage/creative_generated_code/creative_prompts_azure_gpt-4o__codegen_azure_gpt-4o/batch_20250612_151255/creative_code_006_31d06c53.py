"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Provide an example of a marketing campaign strategy for launching a crypto token like WienerAI, emphasizing community rewards and staking incentives.
Generated: DETERMINISTIC_31d06c53ff110b0f
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CryptoTokenCampaign:
    """
    A class to manage the marketing campaign strategy for launching a crypto token.
    Emphasizes community rewards and staking incentives.
    """

    def __init__(self, token_name: str, total_supply: int):
        """
        Initialize the campaign with token details.
        :param token_name: The name of the token.
        :param total_supply: The total supply of the token.
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.community_wallet = 0.2 * total_supply  # 20% allocated for community rewards
        self.staking_wallet = 0.3 * total_supply  # 30% allocated for staking incentives
        self.reward_history = []

    def distribute_community_rewards(self, user_id: str, amount: int):
        """
        Distribute rewards to community members.
        :param user_id: Unique ID of the user receiving the reward.
        :param amount: Amount of tokens to distribute as a reward.
        :raises ValueError: If the reward amount exceeds available tokens.
        """
        if amount > self.community_wallet:
            raise ValueError("Insufficient community wallet balance.")
        
        self.community_wallet -= amount
        self.reward_history.append({
            "user_id": user_id,
            "amount": amount,
            "date": datetime.datetime.now()
        })

    def allocate_staking_incentives(self, staked_amount: int, staking_duration_days: int):
        """
        Calculate and allocate staking incentives to stakers.
        :param staked_amount: Amount of tokens staked by the user.
        :param staking_duration_days: Duration of staking in days.
        :return: Incentive amount.
        :raises ValueError: If staking incentive exceeds staking wallet balance.
        """
        # Incentive formula: 5% annualized reward based on staked amount and duration
        annual_reward_rate = 0.05
        incentive = (staked_amount * annual_reward_rate * (staking_duration_days / 365))
        
        if incentive > self.staking_wallet:
            raise ValueError("Insufficient staking wallet balance.")
        
        self.staking_wallet -= incentive
        return incentive

    def get_campaign_status(self):
        """
        Retrieve the current status of the campaign wallets and reward history.
        :return: Dictionary containing wallet balances and reward history.
        """
        return {
            "community_wallet_balance": self.community_wallet,
            "staking_wallet_balance": self.staking_wallet,
            "reward_history": self.reward_history
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize campaign
        campaign = CryptoTokenCampaign(token_name="WienerAI", total_supply=1000000)

        # Distribute community rewards
        campaign.distribute_community_rewards(user_id="user123", amount=5000)
        campaign.distribute_community_rewards(user_id="user456", amount=2000)

        # Allocate staking incentives
        staking_incentive = campaign.allocate_staking_incentives(staked_amount=10000, staking_duration_days=30)
        print(f"Staking incentive allocated: {staking_incentive} tokens")

        # Check campaign status
        status = campaign.get_campaign_status()
        print("Campaign Status:", status)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
```
