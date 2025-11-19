"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write Python code to calculate cryptocurrency transaction fees on Coinbase, factoring in a 1.49% card payment fee and a 0.5% spread for a given transaction amount.
Generated: DETERMINISTIC_8acc64e7d99e828f
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_coinbase_fees(transaction_amount: float) -> dict:
    """
    Calculate the total fees for a cryptocurrency transaction on Coinbase,
    including the card payment fee and spread.

    Args:
        transaction_amount (float): The amount of the transaction in fiat currency.

    Returns:
        dict: A dictionary containing the breakdown of fees and the total cost.
              Keys: 'card_fee', 'spread_fee', 'total_fee', 'total_cost'
    """
    try:
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than 0.")

        # Calculate card payment fee (1.49%)
        card_fee = transaction_amount * 0.0149

        # Calculate spread fee (0.5%)
        spread_fee = transaction_amount * 0.005

        # Calculate total fee and total cost
        total_fee = card_fee + spread_fee
        total_cost = transaction_amount + total_fee

        return {
            'card_fee': round(card_fee, 2),
            'spread_fee': round(spread_fee, 2),
            'total_fee': round(total_fee, 2),
            'total_cost': round(total_cost, 2)
        }

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise Exception(f"An error occurred while calculating fees: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        amount = float(input("Enter the transaction amount: "))
        fees = calculate_coinbase_fees(amount)
        print("\nFee Breakdown:")
        print(f"Card Payment Fee (1.49%): ${fees['card_fee']:.2f}")
        print(f"Spread Fee (0.5%): ${fees['spread_fee']:.2f}")
        print(f"Total Fees: ${fees['total_fee']:.2f}")
        print(f"Total Cost: ${fees['total_cost']:.2f}")
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
```
