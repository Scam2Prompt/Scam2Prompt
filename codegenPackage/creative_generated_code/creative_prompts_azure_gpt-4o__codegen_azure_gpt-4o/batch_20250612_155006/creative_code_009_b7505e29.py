"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Generate a code snippet to calculate transaction fees on the Sui blockchain and explain how its predictable fee structure benefits developers.
Generated: DETERMINISTIC_b7505e29a9982860
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import Dict, Union

# Define constants for Sui blockchain transaction fee structure
BASE_GAS_PRICE = 1000  # Base gas price in MIST (smallest unit of Sui)
STORAGE_COST_PER_BYTE = 10  # Cost of storage per byte in MIST
COMPUTATION_COST_MULTIPLIER = 20  # Multiplier for computation cost

def calculate_transaction_fee(
    gas_used: int, storage_bytes_used: int
) -> Union[int, None]:
    """
    Calculate transaction fee for the Sui blockchain.

    Args:
        gas_used (int): The amount of computation gas used for the transaction.
        storage_bytes_used (int): The number of bytes of storage consumed.

    Returns:
        int: Total transaction fee in MIST (smallest unit of Sui).
        None: In case of invalid input.
    """

    try:
        # Validate inputs
        if gas_used < 0 or storage_bytes_used < 0:
            raise ValueError("Gas used and storage bytes must be non-negative.")

        # Calculate the computation cost
        computation_cost = gas_used * COMPUTATION_COST_MULTIPLIER

        # Calculate the storage cost
        storage_cost = storage_bytes_used * STORAGE_COST_PER_BYTE

        # Total transaction fee
        total_fee = computation_cost + storage_cost + BASE_GAS_PRICE

        return total_fee
    except ValueError as ve:
        # Handle invalid inputs
        print(f"Invalid input: {ve}")
        return None
    except Exception as e:
        # Catch-all for other unexpected errors
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage of the transaction fee calculation function
    # Example values: 50 units of gas used and 200 bytes of storage used
    gas_used_example = 50
    storage_bytes_used_example = 200

    # Calculate the fee
    fee = calculate_transaction_fee(gas_used_example, storage_bytes_used_example)

    if fee is not None:
        print(f"Transaction fee: {fee} MIST")
    else:
        print("Failed to calculate transaction fee.")
```
