"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Develop a function that simulates a cash exchange transaction for cryptocurrencies, incorporating a minimum amount of 250 PLN.
Generated: DETERMINISTIC_31a200da4aacaf69
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def simulate_crypto_exchange(fiat_amount_pln, crypto_rate, transaction_fee_percent=0.5):
    """
    Simulates a cryptocurrency exchange transaction given an amount in PLN.
    
    Parameters:
        fiat_amount_pln (float or Decimal): The amount in PLN to exchange (must be >= 250 PLN).
        crypto_rate (float or Decimal): The exchange rate for the cryptocurrency (PLN to Crypto).
        transaction_fee_percent (float): The transaction fee as a percentage (default is 0.5%).

    Returns:
        dict: A dictionary containing:
            - 'crypto_received': The amount of cryptocurrency received.
            - 'transaction_fee': The transaction fee deducted.
            - 'fiat_amount': The fiat amount (PLN) provided.
            - 'crypto_rate': The exchange rate used.

    Raises:
        ValueError: If the fiat amount is less than the minimum required (250 PLN).
        ValueError: If any input is invalid or non-positive.
    """
    # Ensure all inputs are valid and above minimum constraints
    MIN_PLN_AMOUNT = 250
    try:
        fiat_amount_pln = decimal.Decimal(fiat_amount_pln)
        crypto_rate = decimal.Decimal(crypto_rate)
        transaction_fee_percent = decimal.Decimal(transaction_fee_percent)

        if fiat_amount_pln < MIN_PLN_AMOUNT:
            raise ValueError(f"Fiat amount must be at least {MIN_PLN_AMOUNT} PLN.")
        if fiat_amount_pln <= 0 or crypto_rate <= 0 or transaction_fee_percent < 0:
            raise ValueError("Input values must be positive.")
    except decimal.InvalidOperation:
        raise ValueError("Invalid numerical input provided.")

    # Calculate transaction fee
    transaction_fee = fiat_amount_pln * (transaction_fee_percent / 100)

    # Calculate the final cryptocurrency received after deducting the fee
    net_fiat_amount = fiat_amount_pln - transaction_fee
    crypto_received = net_fiat_amount / crypto_rate

    # Construct the result dictionary
    result = {
        "fiat_amount": float(fiat_amount_pln),
        "crypto_rate": float(crypto_rate),
        "transaction_fee": float(transaction_fee),
        "crypto_received": float(crypto_received),
    }

    return result


# Example usage
if __name__ == "__main__":
    try:
        fiat_amount = 300  # Amount in PLN
        crypto_exchange_rate = 50  # PLN to Crypto rate
        fee_percent = 0.5  # Fee percentage

        transaction_result = simulate_crypto_exchange(fiat_amount, crypto_exchange_rate, fee_percent)
        print("Transaction Result:", transaction_result)
    except ValueError as e:
        print(f"Error: {e}")
```
