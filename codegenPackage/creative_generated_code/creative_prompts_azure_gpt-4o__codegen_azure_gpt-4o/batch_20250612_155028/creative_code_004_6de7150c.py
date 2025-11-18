"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Write code to simulate concentrated liquidity provisioning for a specific price range, leveraging the principles of Shadow Exchange's Sonic-native liquidity model.
Generated: DETERMINISTIC_6de7150c06a63566
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class LiquidityProvider:
    """
    A class to simulate concentrated liquidity provisioning for a specific price range.
    This model follows principles inspired by Sonic-native liquidity models.
    """

    def __init__(self, min_price: float, max_price: float, initial_liquidity: float):
        """
        Initialize a LiquidityProvider instance.

        Args:
            min_price (float): The lower bound of the price range for the liquidity pool.
            max_price (float): The upper bound of the price range for the liquidity pool.
            initial_liquidity (float): The initial liquidity provided to the pool.
        """
        if min_price <= 0 or max_price <= 0:
            raise ValueError("Prices must be positive values.")
        if min_price >= max_price:
            raise ValueError("Minimum price must be less than maximum price.")
        if initial_liquidity <= 0:
            raise ValueError("Initial liquidity must be a positive value.")

        self.min_price = min_price
        self.max_price = max_price
        self.liquidity = initial_liquidity
        self.sqrt_min_price = math.sqrt(min_price)
        self.sqrt_max_price = math.sqrt(max_price)

    def calculate_liquidity(self, current_price: float) -> float:
        """
        Calculate the effective liquidity available at a given price.

        Args:
            current_price (float): The current price at which liquidity is calculated.

        Returns:
            float: The effective liquidity available at the current price.

        Raises:
            ValueError: If the current price is outside the specified price range.
        """
        if current_price <= 0:
            raise ValueError("Current price must be a positive value.")
        if not (self.min_price <= current_price <= self.max_price):
            raise ValueError("Current price is outside the specified price range.")

        sqrt_price = math.sqrt(current_price)
        effective_liquidity = self.liquidity * (
            (sqrt_price - self.sqrt_min_price) / (self.sqrt_max_price - self.sqrt_min_price)
        )
        return effective_liquidity

    def add_liquidity(self, amount: float) -> None:
        """
        Add liquidity to the pool.

        Args:
            amount (float): The amount of liquidity to add.

        Raises:
            ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Liquidity amount must be a positive value.")
        self.liquidity += amount

    def remove_liquidity(self, amount: float) -> None:
        """
        Remove liquidity from the pool.

        Args:
            amount (float): The amount of liquidity to remove.

        Raises:
            ValueError: If the amount is non-positive or exceeds the available liquidity.
        """
        if amount <= 0:
            raise ValueError("Liquidity amount must be a positive value.")
        if amount > self.liquidity:
            raise ValueError("Cannot remove more liquidity than available.")
        self.liquidity -= amount

    def get_price_range(self) -> tuple[float, float]:
        """
        Get the price range for the liquidity pool.

        Returns:
            tuple[float, float]: The minimum and maximum price range.
        """
        return self.min_price, self.max_price

    def get_total_liquidity(self) -> float:
        """
        Get the total liquidity currently in the pool.

        Returns:
            float: The total liquidity.
        """
        return self.liquidity


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize a liquidity pool with a price range and initial liquidity
        lp = LiquidityProvider(min_price=100, max_price=200, initial_liquidity=1000)

        # Display the price range
        print("Price Range:", lp.get_price_range())

        # Calculate liquidity at a specific price within the range
        current_price = 150
        effective_liquidity = lp.calculate_liquidity(current_price)
        print(f"Effective liquidity at price {current_price}: {effective_liquidity}")

        # Add liquidity to the pool
        lp.add_liquidity(500)
        print("Total liquidity after addition:", lp.get_total_liquidity())

        # Remove liquidity from the pool
        lp.remove_liquidity(300)
        print("Total liquidity after removal:", lp.get_total_liquidity())

    except ValueError as e:
        print(f"Error: {e}")
```
