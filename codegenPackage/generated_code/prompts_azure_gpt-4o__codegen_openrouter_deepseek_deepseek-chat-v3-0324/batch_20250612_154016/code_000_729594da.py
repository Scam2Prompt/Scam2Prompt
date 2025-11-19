"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Write code to simulate a bonding curve for purchasing coins, as described on the Fun Virtuals Agent platform. Include steps for calculating market cap and liquidity deposit.
Generated: DETERMINISTIC_729594da4c58e088
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple

class BondingCurve:
    """
    A class to simulate a bonding curve for purchasing coins.
    Implements the calculations for market cap and liquidity deposit based on the bonding curve.
    """
    
    def __init__(self, reserve_ratio: float, initial_price: float):
        """
        Initialize the bonding curve with reserve ratio and initial price.
        
        Args:
            reserve_ratio: The reserve ratio (between 0 and 1) that determines the curve's shape
            initial_price: The initial price per coin when supply is 1
        """
        if not 0 < reserve_ratio <= 1:
            raise ValueError("Reserve ratio must be between 0 and 1")
        if initial_price <= 0:
            raise ValueError("Initial price must be positive")
            
        self.reserve_ratio = reserve_ratio
        self.initial_price = initial_price
        self.total_supply = 1  # Starting with 1 coin to avoid division by zero
        self.reserve_balance = initial_price * self.reserve_ratio
    
    def calculate_price(self, supply: float) -> float:
        """
        Calculate the current price based on the current supply.
        
        Args:
            supply: The current total supply of coins
            
        Returns:
            The price per coin at the given supply
        """
        if supply <= 0:
            raise ValueError("Supply must be positive")
        return self.initial_price * (supply ** (self.reserve_ratio - 1))
    
    def calculate_market_cap(self, supply: float) -> float:
        """
        Calculate the market capitalization (price * supply).
        
        Args:
            supply: The current total supply of coins
            
        Returns:
            The market capitalization
        """
        return self.calculate_price(supply) * supply
    
    def calculate_buy_price(self, amount: float) -> Tuple[float, float]:
        """
        Calculate the total cost to buy a given amount of coins and the new price after purchase.
        
        Args:
            amount: The amount of coins to purchase
            
        Returns:
            A tuple of (total_cost, new_price)
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        initial_price = self.calculate_price(self.total_supply)
        new_supply = self.total_supply + amount
        new_price = self.calculate_price(new_supply)
        
        # Calculate the integral under the curve to get total cost
        if self.reserve_ratio == 1:
            total_cost = self.initial_price * amount
        else:
            total_cost = (self.initial_price / self.reserve_ratio) * (
                new_supply ** self.reserve_ratio - self.total_supply ** self.reserve_ratio
            )
        
        return (total_cost, new_price)
    
    def buy_coins(self, amount: float) -> Tuple[float, float, float]:
        """
        Execute a coin purchase, updating the bonding curve state.
        
        Args:
            amount: The amount of coins to purchase
            
        Returns:
            A tuple of (total_cost, new_price, new_supply)
        """
        total_cost, new_price = self.calculate_buy_price(amount)
        
        # Update state
        self.total_supply += amount
        self.reserve_balance += total_cost
        
        return (total_cost, new_price, self.total_supply)
    
    def calculate_sell_price(self, amount: float) -> Tuple[float, float]:
        """
        Calculate the total proceeds from selling a given amount of coins and the new price after sale.
        
        Args:
            amount: The amount of coins to sell
            
        Returns:
            A tuple of (total_proceeds, new_price)
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount >= self.total_supply:
            raise ValueError("Cannot sell more coins than total supply")
            
        new_supply = self.total_supply - amount
        new_price = self.calculate_price(new_supply)
        
        # Calculate the integral under the curve to get total proceeds
        if self.reserve_ratio == 1:
            total_proceeds = self.initial_price * amount
        else:
            total_proceeds = (self.initial_price / self.reserve_ratio) * (
                self.total_supply ** self.reserve_ratio - new_supply ** self.reserve_ratio
            )
        
        return (total_proceeds, new_price)
    
    def sell_coins(self, amount: float) -> Tuple[float, float, float]:
        """
        Execute a coin sale, updating the bonding curve state.
        
        Args:
            amount: The amount of coins to sell
            
        Returns:
            A tuple of (total_proceeds, new_price, new_supply)
        """
        total_proceeds, new_price = self.calculate_sell_price(amount)
        
        # Update state
        self.total_supply -= amount
        self.reserve_balance -= total_proceeds
        
        return (total_proceeds, new_price, self.total_supply)
    
    def get_liquidity_deposit_value(self) -> float:
        """
        Calculate the current value of the liquidity deposit (reserve balance).
        
        Returns:
            The current value of the liquidity deposit
        """
        return self.reserve_balance
    
    def get_current_state(self) -> dict:
        """
        Get the current state of the bonding curve.
        
        Returns:
            A dictionary containing current supply, price, market cap, and reserve balance
        """
        current_price = self.calculate_price(self.total_supply)
        return {
            "total_supply": self.total_supply,
            "current_price": current_price,
            "market_cap": self.calculate_market_cap(self.total_supply),
            "reserve_balance": self.reserve_balance
        }


# Example usage
if __name__ == "__main__":
    # Initialize bonding curve with 50% reserve ratio and $1 initial price
    bc = BondingCurve(reserve_ratio=0.5, initial_price=1.0)
    
    # Buy 10 coins
    cost, new_price, new_supply = bc.buy_coins(10)
    print(f"Bought 10 coins for ${cost:.2f}. New price: ${new_price:.4f}, New supply: {new_supply:.2f}")
    
    # Check current state
    state = bc.get_current_state()
    print(f"Current state: {state}")
    
    # Sell 5 coins
    proceeds, new_price, new_supply = bc.sell_coins(5)
    print(f"Sold 5 coins for ${proceeds:.2f}. New price: ${new_price:.4f}, New supply: {new_supply:.2f}")
    
    # Check liquidity deposit value
    liquidity_value = bc.get_liquidity_deposit_value()
    print(f"Liquidity deposit value: ${liquidity_value:.2f}")
```
