"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Using the bonding curve mechanism described, write a Python simulation to model the initial GHST token distribution backed by DAI.
Generated: DETERMINISTIC_dc1c13a2ef6b1b6a
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class BondingCurve:
    """
    Class to model a bonding curve mechanism for token distribution.
    GHST tokens are backed by DAI.
    """
    def __init__(self, reserve_ratio, initial_supply, initial_reserve):
        """
        Initialize the bonding curve model.
        
        :param reserve_ratio: Reserve ratio (a float between 0 and 1).
        :param initial_supply: Initial supply of GHST tokens (integer).
        :param initial_reserve: Initial reserve of DAI (float).
        """
        self.reserve_ratio = reserve_ratio
        self.token_supply = initial_supply
        self.reserve_balance = initial_reserve

    def buy_tokens(self, dai_invested):
        """
        Simulate buying GHST tokens with DAI.

        :param dai_invested: Amount of DAI used to buy GHST tokens (float).
        :return: Number of GHST tokens issued (float).
        """
        if dai_invested <= 0:
            raise ValueError("Investment amount must be positive.")
        
        # Calculate token issuance using the bonding curve formula
        tokens_issued = self.token_supply * (
            math.pow((self.reserve_balance + dai_invested) / self.reserve_balance, self.reserve_ratio) - 1
        )
        
        # Update the state
        self.token_supply += tokens_issued
        self.reserve_balance += dai_invested
        
        return tokens_issued

    def sell_tokens(self, tokens_redeemed):
        """
        Simulate selling GHST tokens to redeem DAI.

        :param tokens_redeemed: Number of GHST tokens to sell (float).
        :return: Amount of DAI redeemed (float).
        """
        if tokens_redeemed <= 0:
            raise ValueError("Redemption amount must be positive.")
        if tokens_redeemed > self.token_supply:
            raise ValueError("Cannot redeem more tokens than available supply.")
        
        # Calculate reserve redemption using the bonding curve formula
        reserve_redeemed = self.reserve_balance * (
            1 - math.pow((self.token_supply - tokens_redeemed) / self.token_supply, 1 / self.reserve_ratio)
        )
        
        # Update the state
        self.token_supply -= tokens_redeemed
        self.reserve_balance -= reserve_redeemed
        
        return reserve_redeemed


# Simulation Example
def main():
    """
    Example simulation of GHST token distribution using bonding curve mechanism.
    """
    # Initialize bonding curve: reserve_ratio=0.5, initial_supply=1000 GHST, initial_reserve=1000 DAI
    curve = BondingCurve(reserve_ratio=0.5, initial_supply=1000, initial_reserve=1000)
    print("Initial state:")
    print(f"Token Supply: {curve.token_supply}, Reserve Balance: {curve.reserve_balance} DAI")
    
    # Simulate buying tokens
    dai_invested = 500  # User invests 500 DAI
    tokens_bought = curve.buy_tokens(dai_invested)
    print(f"\nUser buys {tokens_bought:.2f} GHST tokens with {dai_invested} DAI.")
    print(f"Updated Token Supply: {curve.token_supply:.2f}, Reserve Balance: {curve.reserve_balance:.2f} DAI")
    
    # Simulate selling tokens
    tokens_to_sell = 100  # User redeems 100 GHST tokens
    dai_redeemed = curve.sell_tokens(tokens_to_sell)
    print(f"\nUser sells {tokens_to_sell:.2f} GHST tokens and redeems {dai_redeemed:.2f} DAI.")
    print(f"Updated Token Supply: {curve.token_supply:.2f}, Reserve Balance: {curve.reserve_balance:.2f} DAI")


if __name__ == "__main__":
    main()
```
