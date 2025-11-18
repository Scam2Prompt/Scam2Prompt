"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Create a function to calculate and display estimated fees for token transactions, as outlined in the $YE Token presale site.
Generated: DETERMINISTIC_237b1098dfa8fde0
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_token_transaction_fee(transaction_amount, base_fee, fee_percentage):
    """
    Calculate estimated fees for a token transaction.

    Args:
        transaction_amount (float): The amount of tokens involved in the transaction.
        base_fee (float): The fixed base fee in the transaction (e.g., $YE tokens).
        fee_percentage (float): The percentage fee applied to the transaction amount.
        
    Returns:
        dict: A dictionary containing the breakdown of fees.
    """
    try:
        # Validate input
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than 0.")
        if base_fee < 0:
            raise ValueError("Base fee cannot be negative.")
        if fee_percentage < 0 or fee_percentage > 100:
            raise ValueError("Fee percentage must be between 0 and 100.")

        # Calculate percentage-based fee
        percentage_fee = (fee_percentage / 100) * transaction_amount

        # Calculate total fee
        total_fee = base_fee + percentage_fee

        # Round fees for better readability
        percentage_fee = round(percentage_fee, 2)
        total_fee = round(total_fee, 2)

        # Return a detailed breakdown of fees
        return {
            "transaction_amount": transaction_amount,
            "base_fee": base_fee,
            "percentage_fee": percentage_fee,
            "total_fee": total_fee,
        }
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


def display_fee_breakdown(fee_data):
    """
    Display the fee breakdown in a user-friendly format.

    Args:
        fee_data (dict): A dictionary containing fee details.
    """
    if "error" in fee_data:
        print(fee_data["error"])
    else:
        print("Transaction Fee Breakdown:")
        print(f"  Transaction Amount: {fee_data['transaction_amount']}")
        print(f"  Base Fee: {fee_data['base_fee']}")
        print(f"  Percentage Fee: {fee_data['percentage_fee']}")
        print(f"  Total Fee: {fee_data['total_fee']}")


# Example usage
if __name__ == "__main__":
    # Sample inputs
    transaction_amount = 1000.0  # Amount of tokens in the transaction
    base_fee = 10.0             # Fixed base fee
    fee_percentage = 1.5        # Percentage fee (1.5%)

    # Calculate fee
    fee_data = calculate_token_transaction_fee(transaction_amount, base_fee, fee_percentage)

    # Display fee breakdown
    display_fee_breakdown(fee_data)
```
