"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cellframee.pages.dev
Prompt: Write a code snippet to calculate transaction costs on the Cellframe Network using its economical transaction model.
Generated: DETERMINISTIC_33147cc683c03c95
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates transaction costs on the Cellframe Network
using its economical transaction model. The calculation considers
a base fee, per-byte fee, and additional factors for priority transactions.
"""

def calculate_transaction_cost(base_fee: float, per_byte_fee: float, transaction_size: int, priority_factor: float = 1.0) -> float:
    """
    Calculate the total transaction cost.

    Parameters:
        base_fee (float): The fixed base fee for the transaction.
        per_byte_fee (float): The fee charged per byte of transaction data.
        transaction_size (int): The size of the transaction in bytes.
        priority_factor (float): Factor to increase cost for priority transactions (default is 1.0).
        
    Returns:
        float: The total transaction cost.
    """
    try:
        # Validate inputs
        if base_fee < 0 or per_byte_fee < 0 or transaction_size < 0 or priority_factor < 1.0:
            raise ValueError("Input values must be positive, and priority_factor must be >= 1.0")

        # Calculate cost components
        size_cost = per_byte_fee * transaction_size
        total_cost = base_fee + size_cost

        # Apply priority factor if applicable
        total_cost *= priority_factor

        return total_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        return 0.0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    # Define parameters for the transaction model
    BASE_FEE = 0.01  # Base fee in native tokens
    PER_BYTE_FEE = 0.0005  # Fee per byte in native tokens
    TRANSACTION_SIZE = 150  # Transaction size in bytes
    PRIORITY_FACTOR = 1.2  # Priority multiplier (optional)

    # Calculate transaction cost
    transaction_cost = calculate_transaction_cost(BASE_FEE, PER_BYTE_FEE, TRANSACTION_SIZE, PRIORITY_FACTOR)

    if transaction_cost > 0:
        print(f"Transaction Cost: {transaction_cost:.5f} native tokens")
    else:
        print("Failed to calculate transaction cost due to errors.")
```
