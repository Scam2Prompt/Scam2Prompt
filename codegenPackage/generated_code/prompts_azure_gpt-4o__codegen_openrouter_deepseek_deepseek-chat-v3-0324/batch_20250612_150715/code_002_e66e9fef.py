"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Provide an example of how to use Moxie Bonding Curves to emphasize utility over speculation for Fan Tokens.
Generated: DETERMINISTIC_e66e9fefc520691d
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List, Tuple
from dataclasses import dataclass
import math

@dataclass
class FanToken:
    """
    Represents a Fan Token with utility features.
    """
    name: str
    total_supply: float
    utility_score: float  # Measures actual usage (0-1 scale)
    price: float
    reserve_balance: float

class MoxieBondingCurve:
    """
    Implements a bonding curve that emphasizes utility over speculation.
    """
    def __init__(self, base_price: float, k: float):
        """
        Initialize bonding curve parameters.
        
        Args:
            base_price: Starting price when supply is 0
            k: Curve steepness parameter (higher = more utility-sensitive)
        """
        self.base_price = base_price
        self.k = k
    
    def calculate_price(self, token: FanToken) -> float:
        """
        Calculate token price based on utility and supply.
        
        Args:
            token: FanToken instance
            
        Returns:
            float: Calculated price
        """
        # Price increases with utility and decreases with supply
        utility_factor = 1 + (token.utility_score * self.k)
        supply_factor = 1 / (1 + math.log(1 + token.total_supply))
        return self.base_price * utility_factor * supply_factor
    
    def buy_tokens(self, token: FanToken, amount: float, eth_amount: float) -> Tuple[float, float]:
        """
        Buy tokens through the bonding curve.
        
        Args:
            token: FanToken instance
            amount: Amount of tokens to buy
            eth_amount: ETH sent for purchase
            
        Returns:
            Tuple[float, float]: (tokens_received, eth_refund)
            
        Raises:
            ValueError: If inputs are invalid
        """
        if amount <= 0 or eth_amount <= 0:
            raise ValueError("Amount and ETH must be positive")
            
        # Calculate price and required ETH
        price_per_token = self.calculate_price(token)
        required_eth = price_per_token * amount
        
        if eth_amount < required_eth:
            raise ValueError("Insufficient ETH for purchase")
            
        # Update token metrics
        token.total_supply += amount
        token.reserve_balance += required_eth
        token.price = self.calculate_price(token)  # Recalculate price
        
        return amount, eth_amount - required_eth
    
    def sell_tokens(self, token: FanToken, amount: float) -> float:
        """
        Sell tokens back through the bonding curve.
        
        Args:
            token: FanToken instance
            amount: Amount of tokens to sell
            
        Returns:
            float: ETH received from sale
            
        Raises:
            ValueError: If inputs are invalid or insufficient tokens
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > token.total_supply:
            raise ValueError("Insufficient token supply")
            
        # Calculate price and ETH to return
        price_per_token = self.calculate_price(token)
        eth_returned = price_per_token * amount * 0.95  # 5% fee to discourage speculation
        
        # Update token metrics
        token.total_supply -= amount
        token.reserve_balance -= eth_returned
        token.price = self.calculate_price(token)  # Recalculate price
        
        return eth_returned
    
    def update_utility(self, token: FanToken, utility_score: float) -> None:
        """
        Update the utility score of a token.
        
        Args:
            token: FanToken instance
            utility_score: New utility score (0-1)
            
        Raises:
            ValueError: If utility score is invalid
        """
        if not 0 <= utility_score <= 1:
            raise ValueError("Utility score must be between 0 and 1")
        token.utility_score = utility_score
        token.price = self.calculate_price(token)  # Recalculate price

# Example usage
if __name__ == "__main__":
    # Initialize a fan token with low initial utility
    fan_token = FanToken(
        name="FCB Fan Token",
        total_supply=1000,
        utility_score=0.2,
        price=0,
        reserve_balance=0
    )
    
    # Create bonding curve with parameters
    bonding_curve = MoxieBondingCurve(base_price=0.1, k=2.0)
    
    # Initial price calculation
    fan_token.price = bonding_curve.calculate_price(fan_token)
    print(f"Initial price: {fan_token.price:.4f} ETH")
    
    # Simulate utility increase (e.g., from actual fan engagement)
    bonding_curve.update_utility(fan_token, utility_score=0.8)
    print(f"Price after utility increase: {fan_token.price:.4f} ETH")
    
    # Buy tokens
    try:
        tokens_received, eth_refund = bonding_curve.buy_tokens(fan_token, amount=100, eth_amount=20)
        print(f"Bought {tokens_received} tokens, refunded {eth_refund:.4f} ETH")
        print(f"New price: {fan_token.price:.4f} ETH")
    except ValueError as e:
        print(f"Error buying tokens: {e}")
    
    # Sell tokens
    try:
        eth_received = bonding_curve.sell_tokens(fan_token, amount=50)
        print(f"Sold 50 tokens, received {eth_received:.4f} ETH")
        print(f"New price: {fan_token.price:.4f} ETH")
    except ValueError as e:
        print(f"Error selling tokens: {e}")
```
