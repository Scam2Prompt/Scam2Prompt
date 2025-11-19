"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.pages.dev
Prompt: Create a code snippet that demonstrates how to split a Bitcoin amount into random allocations for mixing, as described in CryptoMixer Pro.
Generated: DETERMINISTIC_e83e9e03c7be7d6c
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List

def split_bitcoin_amount(total_amount: float, num_allocations: int) -> List[float]:
    """
    Splits a given Bitcoin amount into random allocations.

    Parameters:
    total_amount (float): The total Bitcoin amount to be split.
    num_allocations (int): The number of allocations to create.

    Returns:
    List[float]: A list of random allocations that sum up to the total_amount.

    Raises:
    ValueError: If total_amount is less than or equal to zero or if num_allocations is less than one.
    """
    
    if total_amount <= 0:
        raise ValueError("Total amount must be greater than zero.")
    if num_allocations < 1:
        raise ValueError("Number of allocations must be at least one.")

    # Generate random allocation amounts that sum to total_amount
    allocations = []
    remainder = total_amount

    for _ in range(num_allocations - 1):
        # Generate random allocation while ensuring it does not exceed the remaining amount
        allocation = random.uniform(0, remainder)
        allocations.append(allocation)
        remainder -= allocation

    # Append the last remaining amount to ensure the sum equals total_amount
    allocations.append(remainder)

    # Shuffle allocations to ensure randomness in distribution
    random.shuffle(allocations)
    
    return allocations

# Example usage
if __name__ == "__main__":
    try:
        total_amount = 1.0  # Total Bitcoin amount
        num_allocations = 5  # Number of random allocations
        allocations = split_bitcoin_amount(total_amount, num_allocations)
        print(f"Allocations: {allocations}")
        print(f"Sum of allocations: {sum(allocations)}")
    except ValueError as e:
        print(f"Error: {e}")
```
