"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr2.pages.dev
Prompt: Write a Python script to stake SYNTH tokens for veSYNTH and calculate boosted farming rewards based on gauge weights for syASSET/ASSET LP incentives.
Generated: DETERMINISTIC_761b54774c461425
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from decimal import Decimal

class TokenStaking:
    """
    A class to handle SYNTH token staking for veSYNTH and calculate boosted farming rewards.
    """

    def __init__(self, total_gauge_weight=1000):
        """
        Initialize the staking instance with default gauge weights.
        Args:
            total_gauge_weight (int): Total gauge weight for reward calculation (default: 1000 units).
        """
        self.staked_tokens = Decimal("0")
        self.veSYNTH_balance = Decimal("0")
        self.total_gauge_weight = Decimal(total_gauge_weight)
        self.gauge_weights = {}

    def stake_tokens(self, token_amount):
        """
        Stake SYNTH tokens and mint veSYNTH.
        Args:
            token_amount (Decimal): Amount of SYNTH tokens to stake.
        """
        try:
            token_amount = Decimal(token_amount)
            if token_amount <= 0:
                raise ValueError("Token amount must be greater than zero.")
            self.staked_tokens += token_amount
            # Mint veSYNTH at a 1:1 ratio; adjust if necessary
            self.veSYNTH_balance += token_amount
            print(f"Successfully staked {token_amount} SYNTH tokens.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error during staking: {e}")
            sys.exit(1)

    def set_gauge_weights(self, weights):
        """
        Set gauge weights for syASSET/ASSET LP incentives.
        Args:
            weights (dict): A dictionary with asset pairs as keys and weights as values.
        """
        try:
            total_weight = sum(weights.values())
            if total_weight != self.total_gauge_weight:
                raise ValueError(
                    f"Total gauge weight must be {self.total_gauge_weight}, but got {total_weight}."
                )
            self.gauge_weights = {k: Decimal(v) for k, v in weights.items()}
            print("Gauge weights successfully updated.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error during gauge weight update: {e}")
            sys.exit(1)

    def calculate_boosted_rewards(self, asset_pair):
        """
        Calculate boosted farming rewards for a specific syASSET/ASSET LP pair.
        Args:
            asset_pair (str): The asset pair to calculate rewards for.
        Returns:
            Decimal: Boosted farming rewards for the specified asset pair.
        """
        try:
            if asset_pair not in self.gauge_weights:
                raise ValueError(f"Gauge weights not defined for asset pair: {asset_pair}")
            # Example formula for boosted rewards based on veSYNTH balance and gauge weight
            gauge_weight = self.gauge_weights[asset_pair]
            boosted_rewards = self.veSYNTH_balance * (gauge_weight / self.total_gauge_weight)
            return boosted_rewards
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error during reward calculation: {e}")
            sys.exit(1)


if __name__ == "__main__":
    # Example usage
    staking = TokenStaking(total_gauge_weight=1000)

    # Stake SYNTH Tokens
    staking.stake_tokens("1000")

    # Set Gauge Weights
    gauge_weights = {
        "syASSET1/ASSET1": 500,
        "syASSET2/ASSET2": 300,
        "syASSET3/ASSET3": 200,
    }
    staking.set_gauge_weights(gauge_weights)

    # Calculate Boosted Farming Rewards
    asset_pair = "syASSET1/ASSET1"
    rewards = staking.calculate_boosted_rewards(asset_pair)
    print(f"Boosted farming rewards for {asset_pair}: {rewards}")
```
