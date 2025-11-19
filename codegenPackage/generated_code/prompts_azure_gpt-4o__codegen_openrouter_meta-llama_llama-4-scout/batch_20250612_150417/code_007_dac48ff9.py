"""
Generated Code Metadata:
========================
Original URL: https://vfatio.com
Prompt: Write a program to calculate the price range and APR for a new position in the "CL1-WETH/superOETHb" pool, using the min price of 0.99990 and max price of 1.00000.
Generated: DETERMINISTIC_dac48ff9e5de89ec
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Tuple

def calculate_price_range_and_apr(
    pool_name: str, 
    min_price: float, 
    max_price: float, 
    liquidity: float, 
    borrow_rate: float, 
    utilization_rate: float
) -> Tuple[float, float, float]:
    """
    Calculate the price range and APR for a new position in a given pool.

    Args:
    - pool_name (str): The name of the pool (e.g., "CL1-WETH/superOETHb").
    - min_price (float): The minimum price.
    - max_price (float): The maximum price.
    - liquidity (float): The liquidity of the pool.
    - borrow_rate (float): The borrow rate of the pool.
    - utilization_rate (float): The utilization rate of the pool.

    Returns:
    - Tuple[float, float, float]: A tuple containing the price range, APR, and the utilization rate.
    """

    try:
        # Check for valid input values
        if min_price >= max_price:
            raise ValueError("min_price must be less than max_price")

        if liquidity <= 0:
            raise ValueError("liquidity must be greater than zero")

        if borrow_rate < 0 or utilization_rate < 0:
            raise ValueError("borrow_rate and utilization_rate must be non-negative")

        # Calculate the price range
        price_range = max_price - min_price

        # Calculate the APR
        apr = (borrow_rate * utilization_rate) / (1 - utilization_rate)

        return price_range, apr, utilization_rate

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Define the pool parameters
    pool_name = "CL1-WETH/superOETHb"
    min_price = 0.99990
    max_price = 1.00000
    liquidity = 1000000.0  # Example liquidity
    borrow_rate = 0.05  # Example borrow rate (5%)
    utilization_rate = 0.7  # Example utilization rate (70%)

    # Calculate the price range and APR
    result = calculate_price_range_and_apr(
        pool_name, 
        min_price, 
        max_price, 
        liquidity, 
        borrow_rate, 
        utilization_rate
    )

    if result:
        price_range, apr, utilization_rate = result
        print(f"Pool Name: {pool_name}")
        print(f"Price Range: {price_range}")
        print(f"APR: {apr * 100}%")
        print(f"Utilization Rate: {utilization_rate * 100}%")

if __name__ == "__main__":
    main()
```
