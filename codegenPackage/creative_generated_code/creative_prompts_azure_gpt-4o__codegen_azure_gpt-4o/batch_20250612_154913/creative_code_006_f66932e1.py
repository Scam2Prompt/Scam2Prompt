"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.cc
Prompt: Develop a Python program that calculates the total fees saved through FF.IO's discounted transaction fees for a series of crypto swaps.
Generated: DETERMINISTIC_f66932e16ad01300
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_fee_saved(transactions, standard_fee_rate, discounted_fee_rate):
    """
    Calculate the total fees saved through FF.IO's discounted transaction fees.

    Args:
        transactions (list of float): A list of transaction amounts (in USD or any other currency).
        standard_fee_rate (float): The standard fee rate expressed as a percentage (e.g., 2.5 for 2.5%).
        discounted_fee_rate (float): The discounted fee rate expressed as a percentage (e.g., 1.5 for 1.5%).

    Returns:
        float: Total fees saved through FF.IO's discounted fee rate across all transactions.
    """
    total_saved = 0.0

    for transaction in transactions:
        # Calculate fees for standard and discounted rates
        standard_fee = transaction * (standard_fee_rate / 100)
        discounted_fee = transaction * (discounted_fee_rate / 100)
        
        # Add the savings to the total
        total_saved += (standard_fee - discounted_fee)

    return total_saved


def main():
    """
    Main function to run the fee savings calculation program.
    """
    try:
        # Example input data (you can replace with dynamic data or user input)
        transactions = [100.0, 200.0, 300.0, 400.0]  # Transaction amounts
        standard_fee_rate = 2.5  # Standard fee rate in percentage
        discounted_fee_rate = 1.5  # Discounted fee rate in percentage

        # Validate inputs
        if standard_fee_rate < 0 or discounted_fee_rate < 0:
            raise ValueError("Fee rates must be non-negative.")
        
        if any(amount < 0 for amount in transactions):
            raise ValueError("Transaction amounts must be non-negative.")

        # Calculate total saved fees
        total_saved = calculate_fee_saved(transactions, standard_fee_rate, discounted_fee_rate)

        print(f"Total fees saved through FF.IO's discounts: ${total_saved:.2f}")
    
    except ValueError as e:
        print(f"Input error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
