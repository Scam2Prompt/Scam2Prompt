"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinsnet.org
Prompt: Write a function to calculate trading fees for a given transaction using the CoinsNet fee structure.
Generated: DETERMINISTIC_660065f540bbd9a9
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate trading fees based on the CoinsNet fee structure

def calculate_trading_fee(transaction_amount: float, fee_rate: float) -> float:
    """
    Calculate the trading fee for a given transaction amount using the CoinsNet fee structure.

    Args:
        transaction_amount (float): The amount of the transaction (must be positive).
        fee_rate (float): The fee rate as a percentage (e.g., 0.1 for 0.1%).
    
    Returns:
        float: The calculated trading fee.
    
    Raises:
        ValueError: If transaction_amount or fee_rate is negative.
        ValueError: If transaction_amount is zero.
    """
    # Validate inputs
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    if fee_rate < 0:
        raise ValueError("Fee rate cannot be negative.")

    # Calculate the fee
    trading_fee = transaction_amount * (fee_rate / 100)

    # Return the calculated fee
    return round(trading_fee, 2)  # Round to 2 decimal places for precision


# Example of how to use the function
if __name__ == "__main__":
    try:
        # Example transaction
        transaction_amount = 1000.0  # Transaction amount in USD
        fee_rate = 0.1  # Fee rate in percentage (0.1%)

        # Calculate the fee
        fee = calculate_trading_fee(transaction_amount, fee_rate)
        print(f"Trading fee for the transaction: ${fee}")
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
```
