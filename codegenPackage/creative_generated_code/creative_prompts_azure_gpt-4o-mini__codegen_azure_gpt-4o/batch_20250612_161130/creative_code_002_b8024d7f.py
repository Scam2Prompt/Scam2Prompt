"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molly-4uy.pages.dev
Prompt: Create a function that calculates the total fees for buying and selling Molly Tokens based on the provided fee structure.
Generated: DETERMINISTIC_b8024d7f77a63a06
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_molly_token_fees(transaction_type, amount, buy_fee_percentage, sell_fee_percentage):
    """
    Calculate the total fees for buying or selling Molly Tokens.

    Args:
        transaction_type (str): The type of transaction ('buy' or 'sell').
        amount (float): The amount of Molly Tokens involved in the transaction.
        buy_fee_percentage (float): The fee percentage applied for buying Molly Tokens.
        sell_fee_percentage (float): The fee percentage applied for selling Molly Tokens.

    Returns:
        float: The calculated fee for the transaction.

    Raises:
        ValueError: If the transaction_type is invalid or amount is negative.
    """
    try:
        # Validate input
        if transaction_type not in ('buy', 'sell'):
            raise ValueError("Invalid transaction type. Must be 'buy' or 'sell'.")
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")
        
        # Calculate the fee based on transaction type
        if transaction_type == 'buy':
            fee = amount * (buy_fee_percentage / 100)
        elif transaction_type == 'sell':
            fee = amount * (sell_fee_percentage / 100)
        
        return fee

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Define fee percentages
    buy_fee = 2.5  # 2.5% fee for buying
    sell_fee = 3.0  # 3.0% fee for selling

    # Calculate fees for example transactions
    buy_transaction_fee = calculate_molly_token_fees('buy', 1000, buy_fee, sell_fee)
    print(f"Buy Transaction Fee: {buy_transaction_fee}")

    sell_transaction_fee = calculate_molly_token_fees('sell', 1000, buy_fee, sell_fee)
    print(f"Sell Transaction Fee: {sell_transaction_fee}")
```
