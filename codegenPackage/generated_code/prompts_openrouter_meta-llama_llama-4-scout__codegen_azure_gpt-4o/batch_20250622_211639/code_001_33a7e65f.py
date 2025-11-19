"""
Generated Code Metadata:
========================
Original URL: https://memes-index.pages.dev
Prompt: How does the $MEMEX presale work, and what are the rewards for buying and staking $MEMEX tokens, considering the current price and market capitalization of meme coins like DOGE, SHIB, and PEPE?
Generated: DETERMINISTIC_33a7e65f8deafb81
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class MemexPresale:
    """
    A class to simulate the $MEMEX presale and rewards system.
    """

    def __init__(self, token_price, total_supply, staking_reward_rate):
        """
        Initialize the presale with token price, total supply, and staking reward rate.

        :param token_price: Price of one $MEMEX token in USD.
        :param total_supply: Total supply of $MEMEX tokens available for presale.
        :param staking_reward_rate: Annual reward rate for staking $MEMEX tokens (percentage).
        """
        self.token_price = token_price
        self.total_supply = total_supply
        self.staking_reward_rate = staking_reward_rate
        self.tokens_sold = 0
        self.buyers = {}

    def buy_tokens(self, buyer_name, amount_usd):
        """
        Allows a buyer to purchase $MEMEX tokens during the presale.

        :param buyer_name: Name of the buyer.
        :param amount_usd: Amount in USD the buyer wants to spend.
        :return: Number of tokens purchased.
        """
        try:
            tokens_to_buy = amount_usd / self.token_price
            if tokens_to_buy > self.total_supply - self.tokens_sold:
                raise ValueError("Not enough tokens available for purchase.")
            
            self.tokens_sold += tokens_to_buy
            self.buyers[buyer_name] = self.buyers.get(buyer_name, 0) + tokens_to_buy
            return tokens_to_buy
        except Exception as e:
            print(f"Error during token purchase: {e}")
            return 0

    def stake_tokens(self, buyer_name, tokens_to_stake, staking_duration_days):
        """
        Allows a buyer to stake their $MEMEX tokens and earn rewards.

        :param buyer_name: Name of the buyer.
        :param tokens_to_stake: Number of tokens the buyer wants to stake.
        :param staking_duration_days: Duration of staking in days.
        :return: Staking reward earned.
        """
        try:
            if buyer_name not in self.buyers or self.buyers[buyer_name] < tokens_to_stake:
                raise ValueError("Insufficient tokens to stake.")
            
            # Calculate staking rewards
            annual_reward = tokens_to_stake * (self.staking_reward_rate / 100)
            daily_reward = annual_reward / 365
            total_reward = daily_reward * staking_duration_days

            # Update buyer's token balance
            self.buyers[buyer_name] -= tokens_to_stake
            return total_reward
        except Exception as e:
            print(f"Error during staking: {e}")
            return 0

    def get_presale_status(self):
        """
        Returns the current status of the presale.

        :return: Dictionary containing presale status.
        """
        return {
            "token_price": self.token_price,
            "total_supply": self.total_supply,
            "tokens_sold": self.tokens_sold,
            "tokens_remaining": self.total_supply - self.tokens_sold,
            "buyers": self.buyers
        }


# Example usage
if __name__ == "__main__":
    # Initialize presale with token price, total supply, and staking reward rate
    memex_presale = MemexPresale(token_price=0.01, total_supply=1000000, staking_reward_rate=10)

    # Simulate token purchase
    print("Buying tokens...")
    tokens_purchased = memex_presale.buy_tokens(buyer_name="Alice", amount_usd=100)
    print(f"Alice purchased {tokens_purchased} tokens.")

    # Simulate staking
    print("Staking tokens...")
    staking_reward = memex_presale.stake_tokens(buyer_name="Alice", tokens_to_stake=5000, staking_duration_days=30)
    print(f"Alice earned {staking_reward} tokens as staking reward.")

    # Get presale status
    print("Presale status:")
    print(json.dumps(memex_presale.get_presale_status(), indent=4))
```
