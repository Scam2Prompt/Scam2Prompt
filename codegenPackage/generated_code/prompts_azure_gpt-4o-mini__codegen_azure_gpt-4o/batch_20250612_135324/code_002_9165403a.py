"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: Create a function that calculates potential losses from high transaction fees in cryptocurrency trading, referencing the example of the 8.18 BTC fee incident shared on the CryptoBro site.
Generated: DETERMINISTIC_9165403aae380fa2
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

def calculate_transaction_fee_loss(transaction_amount_btc, fee_rate_percent):
    """
    Calculate potential losses from high transaction fees in cryptocurrency trading.

    Args:
        transaction_amount_btc (float): The amount of cryptocurrency being transacted in BTC.
        fee_rate_percent (float): The transaction fee rate as a percentage.

    Returns:
        float: The calculated transaction fee loss in BTC.

    Raises:
        ValueError: If transaction_amount_btc or fee_rate_percent is negative.
    """
    try:
        # Validate inputs
        if transaction_amount_btc < 0:
            raise ValueError("Transaction amount cannot be negative.")
        if fee_rate_percent < 0:
            raise ValueError("Fee rate cannot be negative.")

        # Calculate the fee loss
        fee_loss_btc = (transaction_amount_btc * fee_rate_percent) / 100
        return fee_loss_btc

    except ValueError as e:
        # Log the error and re-raise it
        logging.error(f"Input validation error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        # Example transaction: 8.18 BTC with a fee rate of 10%
        transaction_amount = 8.18
        fee_rate = 10.0

        # Calculate the fee loss
        loss = calculate_transaction_fee_loss(transaction_amount, fee_rate)
        logging.info(f"Transaction amount: {transaction_amount} BTC")
        logging.info(f"Fee rate: {fee_rate}%")
        logging.info(f"Potential fee loss: {loss:.8f} BTC")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
