"""
Generated Code Metadata:
========================
Original URL: https://cryptomixer.pages.dev
Prompt: Create a code snippet that demonstrates how to split a Bitcoin amount into random allocations for mixing, as described in CryptoMixer Pro.
Generated: DETERMINISTIC_e83e9e03c7be7d6c
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List

def split_bitcoin_amount(amount: float, num_allocations: int) -> List[float]:
    """
    Splits a given Bitcoin amount into a specified number of random allocations.

    Parameters:
    amount (float): The total Bitcoin amount to be split.
    num_allocations (int): The number of random allocations to create.

    Returns:
    List[float]: A list of random allocations that sum up to the original amount.

    Raises:
    ValueError: If the amount is non-positive or if num_allocations is less than 1.
    """
    
    # Validate input parameters
    if amount <= 0:
        raise ValueError("The amount must be a positive number.")
    if num_allocations < 1:
        raise ValueError("The number of allocations must be at least 1.")

    # Generate random allocations
    allocations = [random.uniform(0, amount) for _ in range(num_allocations)]
    
    # Normalize the allocations to sum up to the original amount
    total_allocated = sum(allocations)
    normalized_allocations = [(allocation / total_allocated) * amount for allocation in allocations]

    # Ensure the sum of normalized allocations equals the original amount
    # Adjust the last allocation to account for any rounding errors
    normalized_allocations[-1] += amount - sum(normalized_allocations)

    return normalized_allocations

# Example usage
if __name__ == "__main__":
    try:
        total_amount = 1.0  # Total Bitcoin amount to split
        allocations_count = 5  # Number of allocations
        allocations = split_bitcoin_amount(total_amount, allocations_count)
        print(f"Random allocations for {total_amount} BTC into {allocations_count} parts: {allocations}")
    except ValueError as e:
        print(f"Error: {e}")
```
