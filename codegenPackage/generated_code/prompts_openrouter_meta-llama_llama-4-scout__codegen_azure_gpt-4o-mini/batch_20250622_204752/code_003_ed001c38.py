"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Explain the concept of Protocol Owned Liquidity (PoL) in the context of the Morpheus project and how it contributes to the long-term sustainability of the protocol.
Generated: DETERMINISTIC_ed001c382be47f41
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProtocolOwnedLiquidity:
    """
    A class to represent Protocol Owned Liquidity (PoL) in the context of the Morpheus project.
    
    Attributes:
        liquidity_pool (float): The total amount of liquidity owned by the protocol.
        token_price (float): The current price of the token in the liquidity pool.
        total_supply (float): The total supply of tokens in circulation.
    """

    def __init__(self, initial_liquidity: float, initial_token_price: float, initial_supply: float):
        """
        Initializes the ProtocolOwnedLiquidity with initial values.
        
        Args:
            initial_liquidity (float): Initial liquidity owned by the protocol.
            initial_token_price (float): Initial price of the token.
            initial_supply (float): Initial total supply of tokens.
        """
        if initial_liquidity < 0 or initial_token_price <= 0 or initial_supply <= 0:
            raise ValueError("Initial values must be non-negative and token price/supply must be positive.")
        
        self.liquidity_pool = initial_liquidity
        self.token_price = initial_token_price
        self.total_supply = initial_supply

    def add_liquidity(self, amount: float):
        """
        Adds liquidity to the protocol's liquidity pool.
        
        Args:
            amount (float): The amount of liquidity to add.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        
        self.liquidity_pool += amount

    def remove_liquidity(self, amount: float):
        """
        Removes liquidity from the protocol's liquidity pool.
        
        Args:
            amount (float): The amount of liquidity to remove.
        
        Raises:
            ValueError: If the amount is negative or exceeds the current liquidity.
        """
        if amount < 0:
            raise ValueError("Amount to remove must be non-negative.")
        if amount > self.liquidity_pool:
            raise ValueError("Cannot remove more liquidity than is available in the pool.")
        
        self.liquidity_pool -= amount

    def update_token_price(self, new_price: float):
        """
        Updates the price of the token in the liquidity pool.
        
        Args:
            new_price (float): The new price of the token.
        
        Raises:
            ValueError: If the new price is non-positive.
        """
        if new_price <= 0:
            raise ValueError("Token price must be positive.")
        
        self.token_price = new_price

    def calculate_market_cap(self) -> float:
        """
        Calculates the market capitalization of the protocol based on the current token price and total supply.
        
        Returns:
            float: The market capitalization of the protocol.
        """
        return self.token_price * self.total_supply

    def __str__(self):
        """
        Returns a string representation of the ProtocolOwnedLiquidity instance.
        
        Returns:
            str: A summary of the liquidity pool, token price, and total supply.
        """
        return (f"Protocol Owned Liquidity:\n"
                f"Liquidity Pool: {self.liquidity_pool}\n"
                f"Token Price: {self.token_price}\n"
                f"Total Supply: {self.total_supply}\n"
                f"Market Cap: {self.calculate_market_cap()}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Protocol Owned Liquidity with example values
        pol = ProtocolOwnedLiquidity(initial_liquidity=100000, initial_token_price=10, initial_supply=5000)
        
        # Display initial state
        print(pol)
        
        # Add liquidity
        pol.add_liquidity(50000)
        print("\nAfter adding liquidity:")
        print(pol)
        
        # Remove liquidity
        pol.remove_liquidity(20000)
        print("\nAfter removing liquidity:")
        print(pol)
        
        # Update token price
        pol.update_token_price(12)
        print("\nAfter updating token price:")
        print(pol)

    except ValueError as e:
        print(f"Error: {e}")
```
