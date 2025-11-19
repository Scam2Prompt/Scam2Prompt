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

def split_bitcoin_amount(amount, num_splits, min_split=0.0001):
    """
    Splits a Bitcoin amount into random allocations for mixing.
    
    Args:
        amount (float): Total Bitcoin amount to split.
        num_splits (int): Number of allocations to create.
        min_split (float): Minimum allocation size for each split.
        
    Returns:
        list of float: Randomly allocated amounts that sum up to the original `amount`.
        
    Raises:
        ValueError: If the amount or num_splits are invalid (e.g., insufficient amount for splits).
    """
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if num_splits <= 0:
        raise ValueError("Number of splits must be positive.")
    if amount < num_splits * min_split:
        raise ValueError("Amount too small for the number of splits with the minimum allocation size.")

    allocations = []
    remaining_amount = amount

    # Generate random allocations while ensuring minimum split size and final sum
    for i in range(num_splits - 1):
        max_split = remaining_amount - (num_splits - len(allocations) - 1) * min_split
        split = round(random.uniform(min_split, max_split), 8)  # BTC precision is up to 8 decimal places
        allocations.append(split)
        remaining_amount -= split

    # Add the remaining amount as the final allocation
    allocations.append(round(remaining_amount, 8))

    return allocations


# Example usage
if __name__ == "__main__":
    try:
        total_amount = 0.05  # Example total Bitcoin amount
        splits = 5          # Number of random allocations
        min_allocation = 0.0001

        allocations = split_bitcoin_amount(total_amount, splits, min_allocation)
        print(f"Total Amount: {total_amount} BTC")
        print(f"Allocations: {allocations}")
        print(f"Sum of Allocations: {sum(allocations)} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
