"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoinweb.pages.dev
Prompt: How can I implement a staking mechanism for the Green Bitcoin ($GBTC) token that allows users to earn rewards based on their predictions of Bitcoin price trends?
Generated: DETERMINISTIC_a31ef64762b8f382
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class GBTCStakingMechanism:
    """
    A class to implement a Green Bitcoin ($GBTC) staking mechanism 
    where users earn rewards based on their predictions of Bitcoin price trends.
    """

    def __init__(self):
        # Initialize the staking mechanism with empty records
        self.stakers = {}  # Format: {user_id: {'amount': float, 'start_time': datetime, 'prediction': str}}
        self.reward_pool = 0.0  # Available reward pool for staking
        self.bitcoin_price = 0.0  # Simulated Bitcoin price (real-world implementation would use a price oracle)
    
    def set_bitcoin_price(self, price):
        """
        Set the current Bitcoin price (typically from an external price oracle).
        """
        if price <= 0:
            raise ValueError("Bitcoin price must be greater than zero.")
        self.bitcoin_price = price

    def add_to_reward_pool(self, amount):
        """
        Add funds to the reward pool. This is typically done by the platform.
        """
        if amount <= 0:
            raise ValueError("Reward pool amount must be greater than zero.")
        self.reward_pool += amount

    def stake_tokens(self, user_id, amount, prediction):
        """
        Stake $GBTC tokens with a prediction on the Bitcoin price trend.
        Prediction must be either 'up' or 'down'.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if prediction not in ['up', 'down']:
            raise ValueError("Prediction must be either 'up' or 'down'.")
        
        # Record the user's staking details
        self.stakers[user_id] = {
            'amount': amount,
            'start_time': datetime.now(),
            'prediction': prediction
        }

    def evaluate_rewards(self):
        """
        Evaluate rewards for all stakers based on the Bitcoin price trend.
        Rewards are distributed proportionally based on the staked amount.
        """
        if not self.stakers:
            raise ValueError("No stakers found to evaluate rewards.")

        # Simulate price change (in real-world, fetch the price from a price oracle)
        new_price = self.bitcoin_price * 1.05  # Example: Bitcoin price increased by 5%
        price_trend = 'up' if new_price > self.bitcoin_price else 'down'
        
        total_correct_predictions = 0
        for staker in self.stakers.values():
            if staker['prediction'] == price_trend:
                total_correct_predictions += staker['amount']
        
        if total_correct_predictions == 0:
            print("No correct predictions. Reward pool remains unallocated.")
            return
        
        # Allocate rewards to stakers with correct predictions
        for user_id, staker in self.stakers.items():
            if staker['prediction'] == price_trend:
                user_reward = (staker['amount'] / total_correct_predictions) * self.reward_pool
                print(f"User {user_id} receives reward: {user_reward:.2f} $GBTC")
        
        # Reset the reward pool and stakers
        self.reward_pool = 0.0
        self.stakers = {}

    def simulate_time_passage(self, days):
        """
        Simulate passage of time for testing purposes. Increment the start_time of all stakers.
        """
        for staker in self.stakers.values():
            staker['start_time'] += timedelta(days=days)


# Example Usage
if __name__ == "__main__":
    staking_mech = GBTCStakingMechanism()
    
    # Simulate initial setup
    staking_mech.set_bitcoin_price(50000)  # Set initial Bitcoin price
    staking_mech.add_to_reward_pool(1000)  # Add reward pool funds
    
    # Users stake tokens with predictions
    staking_mech.stake_tokens(user_id="user1", amount=50, prediction="up")
    staking_mech.stake_tokens(user_id="user2", amount=100, prediction="down")
    staking_mech.stake_tokens(user_id="user3", amount=200, prediction="up")
    
    # Simulate a price change and evaluate rewards
    staking_mech.evaluate_rewards()
```
