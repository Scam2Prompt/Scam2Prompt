"""
Generated Code Metadata:
========================
Original URL: https://idegensolutionmeme.pages.dev
Prompt: Create a function that simulates the price updates for a token based on purchase activity, inspired by the iDEGEN presale auction mechanics.
Generated: DETERMINISTIC_510ce69ae3e6bf57
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Tuple

def calculate_token_price(
    total_raised: float,
    total_supply: float,
    initial_price: float,
    price_increment: float,
    max_price: float
) -> float:
    """
    Calculate the current token price based on the total raised and auction parameters.
    
    Args:
        total_raised: Total amount raised in the presale (in base currency)
        total_supply: Total number of tokens available in the presale
        initial_price: Starting price per token
        price_increment: Price increase per increment step
        max_price: Maximum price the token can reach
    
    Returns:
        Current price per token
    
    Raises:
        ValueError: If any input parameter is invalid (negative or zero where not allowed)
    """
    # Validate input parameters
    if total_raised < 0:
        raise ValueError("Total raised cannot be negative")
    if total_supply <= 0:
        raise ValueError("Total supply must be positive")
    if initial_price <= 0:
        raise ValueError("Initial price must be positive")
    if price_increment <= 0:
        raise ValueError("Price increment must be positive")
    if max_price <= initial_price:
        raise ValueError("Max price must be greater than initial price")
    
    # Calculate how much of the supply has been allocated
    allocated_supply = (total_raised / initial_price) if initial_price > 0 else 0
    
    # Calculate the number of price increments that have occurred
    increment_steps = math.floor(allocated_supply / (total_supply / ((max_price - initial_price) / price_increment)))
    
    # Calculate the current price with increments, capped at max_price
    current_price = min(initial_price + (increment_steps * price_increment), max_price)
    
    return current_price

def simulate_purchases(
    purchase_amounts: List[float],
    total_supply: float,
    initial_price: float,
    price_increment: float,
    max_price: float
) -> List[Tuple[float, float]]:
    """
    Simulate a series of purchases and return the price after each purchase.
    
    Args:
        purchase_amounts: List of purchase amounts (in base currency)
        total_supply: Total number of tokens available in the presale
        initial_price: Starting price per token
        price_increment: Price increase per increment step
        max_price: Maximum price the token can reach
    
    Returns:
        List of tuples (total_raised, current_price) after each purchase
    
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if any(amount <= 0 for amount in purchase_amounts):
        raise ValueError("All purchase amounts must be positive")
    if total_supply <= 0:
        raise ValueError("Total supply must be positive")
    if initial_price <= 0:
        raise ValueError("Initial price must be positive")
    if price_increment <= 0:
        raise ValueError("Price increment must be positive")
    if max_price <= initial_price:
        raise ValueError("Max price must be greater than initial price")
    
    results = []
    total_raised = 0.0
    
    for amount in purchase_amounts:
        total_raised += amount
        current_price = calculate_token_price(
            total_raised,
            total_supply,
            initial_price,
            price_increment,
            max_price
        )
        results.append((total_raised, current_price))
    
    return results

# Example usage
if __name__ == "__main__":
    try:
        # Presale parameters
        TOTAL_SUPPLY = 1_000_000.0  # 1 million tokens
        INITIAL_PRICE = 0.01        # $0.01 per token
        PRICE_INCREMENT = 0.001     # $0.001 increment per step
        MAX_PRICE = 0.05            # $0.05 maximum price
        
        # Simulate purchases
        purchases = [1000.0, 5000.0, 2000.0, 10000.0, 50000.0]
        results = simulate_purchases(
            purchases,
            TOTAL_SUPPLY,
            INITIAL_PRICE,
            PRICE_INCREMENT,
            MAX_PRICE
        )
        
        # Print results
        print("Purchase Simulation Results:")
        print("Total Raised | Token Price")
        for total_raised, price in results:
            print(f"${total_raised:,.2f} | ${price:.4f}")
            
    except ValueError as e:
        print(f"Error in simulation: {e}")
```
