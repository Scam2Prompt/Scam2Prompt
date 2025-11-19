"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Write a code snippet that calculates the transaction fee for exchanging Bitcoin to Euro at a rate of 4.7%.
Generated: DETERMINISTIC_398281b9ed788553
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate the transaction fee for exchanging Bitcoin to Euro

def calculate_transaction_fee(bitcoin_amount, exchange_rate, fee_rate):
    """
    Calculate the transaction fee for exchanging Bitcoin to Euro.

    Parameters:
        bitcoin_amount (float): The amount of Bitcoin to be exchanged.
        exchange_rate (float): The current Bitcoin-to-Euro exchange rate.
        fee_rate (float): The transaction fee rate (as a percentage, e.g., 4.7 for 4.7%).

    Returns:
        float: The transaction fee in Euros.
    """
    try:
        # Validate inputs
        if bitcoin_amount <= 0:
            raise ValueError("Bitcoin amount must be greater than zero.")
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be greater than zero.")
        if fee_rate < 0:
            raise ValueError("Fee rate cannot be negative.")
        
        # Calculate the total Euro amount for the Bitcoin exchanged
        euro_amount = bitcoin_amount * exchange_rate

        # Calculate the transaction fee
        transaction_fee = euro_amount * (fee_rate / 100)

        return transaction_fee

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    bitcoin_amount = 0.5  # Amount of Bitcoin to be exchanged
    exchange_rate = 30000  # Current Bitcoin to Euro exchange rate
    fee_rate = 4.7  # Transaction fee rate in percentage

    fee = calculate_transaction_fee(bitcoin_amount, exchange_rate, fee_rate)
    if fee is not None:
        print(f"The transaction fee for exchanging {bitcoin_amount} BTC is €{fee:.2f}.")
```
