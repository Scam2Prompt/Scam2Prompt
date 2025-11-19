"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinzat.com
Prompt: Create a function that calculates potential losses from high transaction fees in cryptocurrency trading, referencing the example of the 8.18 BTC fee incident shared on the CryptoBro site.
Generated: DETERMINISTIC_9165403aae380fa2
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

def calculate_transaction_fee_loss(transaction_value_btc, fee_btc, btc_to_usd_rate):
    """
    Calculate potential loss from high transaction fees in cryptocurrency trading.

    Args:
        transaction_value_btc (float): The value of the transaction in BTC.
        fee_btc (float): The transaction fee in BTC.
        btc_to_usd_rate (float): Current exchange rate of BTC to USD.

    Returns:
        dict: A dictionary containing the following keys:
            - 'fee_percentage': Percentage of the transaction lost to fees.
            - 'loss_in_usd': The loss in USD caused by the transaction fee.
    Raises:
        ValueError: If any of the inputs are negative or zero.
    """

    # Input validation
    if transaction_value_btc <= 0:
        raise ValueError("Transaction value (BTC) must be greater than zero.")
    if fee_btc <= 0:
        raise ValueError("Transaction fee (BTC) must be greater than zero.")
    if btc_to_usd_rate <= 0:
        raise ValueError("BTC to USD rate must be greater than zero.")

    # Calculate the percentage of the transaction lost to fees
    fee_percentage = (fee_btc / transaction_value_btc) * 100

    # Calculate the loss in USD caused by the transaction fee
    loss_in_usd = fee_btc * btc_to_usd_rate

    result = {
        "fee_percentage": round(fee_percentage, 2),    # Rounded to two decimal places
        "loss_in_usd": round(loss_in_usd, 2)          # Rounded to two decimal places
    }

    return result


# Example usage:
if __name__ == "__main__":
    try:
        # Example values
        transaction_value_btc = 10.0  # Transaction value in BTC
        fee_btc = 8.18               # Fee in BTC (Example: 8.18 BTC fee incident)
        btc_to_usd_rate = 20000.0    # Current BTC to USD exchange rate

        # Calculate the loss
        loss_details = calculate_transaction_fee_loss(transaction_value_btc, fee_btc, btc_to_usd_rate)

        # Output the results
        print(f"Fee Percentage: {loss_details['fee_percentage']}%")
        print(f"Loss in USD: ${loss_details['loss_in_usd']}")

    except ValueError as e:
        logging.error(f"Input error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
