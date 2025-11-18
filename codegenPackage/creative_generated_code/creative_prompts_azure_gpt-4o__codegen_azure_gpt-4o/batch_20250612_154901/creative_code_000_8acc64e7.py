"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write Python code to calculate cryptocurrency transaction fees on Coinbase, factoring in a 1.49% card payment fee and a 0.5% spread for a given transaction amount.
Generated: DETERMINISTIC_8acc64e7d99e828f
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for error handling
import sys

def calculate_crypto_transaction_fee(transaction_amount):
    """
    Calculate transaction fees for a cryptocurrency transaction on Coinbase.
    
    Coinbase fees:
    - 1.49% card payment fee
    - 0.5% spread fee
    
    Parameters:
    transaction_amount (float): The total transaction amount in USD.
    
    Returns:
    dict: A dictionary containing detailed breakdown of fees and final amount.
    """
    try:
        # Validate input
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than 0.")
        
        # Define fee rates
        card_payment_fee_rate = 0.0149  # 1.49%
        spread_fee_rate = 0.005  # 0.5%

        # Calculate fees
        card_payment_fee = transaction_amount * card_payment_fee_rate
        spread_fee = transaction_amount * spread_fee_rate

        # Total fees
        total_fees = card_payment_fee + spread_fee

        # Final transaction amount after fees
        final_amount = transaction_amount - total_fees

        # Return a breakdown of fees and final amount
        return {
            "transaction_amount": transaction_amount,
            "card_payment_fee": round(card_payment_fee, 2),
            "spread_fee": round(spread_fee, 2),
            "total_fees": round(total_fees, 2),
            "final_amount": round(final_amount, 2),
        }
    except ValueError as ve:
        sys.stderr.write(f"ValueError: {ve}\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

# Example usage
if __name__ == "__main__":
    try:
        # Input transaction amount
        transaction_amount = float(input("Enter the transaction amount in USD: "))
        
        # Calculate fees
        fee_details = calculate_crypto_transaction_fee(transaction_amount)
        
        # Print fee details
        if fee_details:
            print("\nTransaction Fee Breakdown:")
            print(f"Transaction Amount: ${fee_details['transaction_amount']:.2f}")
            print(f"Card Payment Fee (1.49%): ${fee_details['card_payment_fee']:.2f}")
            print(f"Spread Fee (0.5%): ${fee_details['spread_fee']:.2f}")
            print(f"Total Fees: ${fee_details['total_fees']:.2f}")
            print(f"Final Amount After Fees: ${fee_details['final_amount']:.2f}")
    except ValueError:
        print("Please enter a valid numeric transaction amount.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
