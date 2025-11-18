"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://08pf.cn
Prompt: Provide a Python script to calculate transaction fees for trades on the OKX platform, considering the low-cost structure described.
Generated: DETERMINISTIC_51b0eba0d885fe0d
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to calculate transaction fees for trades on the OKX platform.
This script considers OKX's low-cost structure, with varying fees for makers and takers.
"""

# Import necessary libraries
from typing import Union

# Define constants for fee structure (example values, adjust according to OKX's actual fee structure)
MAKER_FEE_RATE = 0.0008  # Maker fee rate (0.08%)
TAKER_FEE_RATE = 0.0010  # Taker fee rate (0.10%)

def calculate_transaction_fee(trade_amount: Union[float, int], is_maker: bool) -> float:
    """
    Calculate the transaction fee for a trade based on its type (maker/taker).

    Parameters:
        trade_amount (Union[float, int]): The total trade amount in the traded currency.
        is_maker (bool): True if the trade is a maker trade, False if it's a taker trade.

    Returns:
        float: The calculated transaction fee.
    """
    try:
        # Validate trade_amount
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")

        # Determine the applicable fee rate
        fee_rate = MAKER_FEE_RATE if is_maker else TAKER_FEE_RATE

        # Calculate the fee
        transaction_fee = trade_amount * fee_rate

        return transaction_fee
    except ValueError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Example trade details
        trade_amount = 10000.0  # Trade amount in USD
        trade_type_is_maker = True  # True for maker trade, False for taker trade

        # Calculate fee
        fee = calculate_transaction_fee(trade_amount, trade_type_is_maker)

        # Print result
        trade_type = "Maker" if trade_type_is_maker else "Taker"
        print(f"Trade Type: {trade_type}")
        print(f"Trade Amount: ${trade_amount}")
        print(f"Transaction Fee: ${fee:.2f}")
    except Exception:
        print("Failed to calculate transaction fee.")
```
