"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsecure.pages.dev
Prompt: Provide a solution for handling high transaction fees in a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_e4d30dde674d3c52
Batch ID: 20250612_161617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YOUR_API_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from decimal import Decimal

# Constants
MAX_TRANSACTION_FEE_PERCENTAGE = Decimal("5.0")  # Maximum allowed transaction fee percentage
GAS_PRICE_API_URL = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YOUR_API_KEY"

class TransactionError(Exception):
    """Custom exception for transaction-related errors."""
    pass

def fetch_current_gas_price():
    """
    Fetch the current gas price from a reliable source.
    Returns:
        Decimal: Current gas price in Gwei.
    Raises:
        TransactionError: If unable to fetch gas price.
    """
    try:
        response = requests.get(GAS_PRICE_API_URL)
        response.raise_for_status()
        data = response.json()
        return Decimal(data['result']['ProposeGasPrice'])
    except (requests.RequestException, KeyError) as e:
        raise TransactionError(f"Failed to fetch current gas price: {str(e)}")

def calculate_transaction_fee(gas_price, gas_limit):
    """
    Calculate the estimated transaction fee in ETH.
    Args:
        gas_price (Decimal): Current gas price in Gwei.
        gas_limit (int): Maximum amount of gas the transaction can consume.
    Returns:
        Decimal: Estimated transaction fee in ETH.
    """
    # Convert gas price from Gwei to ETH
    gas_price_in_eth = gas_price / Decimal("1000000000")
    return gas_price_in_eth * Decimal(gas_limit)

def validate_transaction_fee(transaction_amount, transaction_fee):
    """
    Validate if the transaction fee is within acceptable limits.
    Args:
        transaction_amount (Decimal): Amount to be transacted in ETH.
        transaction_fee (Decimal): Estimated transaction fee in ETH.
    Raises:
        TransactionError: If the transaction fee exceeds allowable percentage.
    """
    fee_percentage = (transaction_fee / transaction_amount) * Decimal("100")
    if fee_percentage > MAX_TRANSACTION_FEE_PERCENTAGE:
        raise TransactionError(
            f"Transaction fee ({fee_percentage:.2f}%) exceeds the maximum allowed ({MAX_TRANSACTION_FEE_PERCENTAGE}%)."
        )

def handle_transaction(transaction_amount, gas_limit):
    """
    Handle the transaction, ensuring fees are acceptable.
    Args:
        transaction_amount (Decimal): Amount to be transacted in ETH.
        gas_limit (int): Maximum amount of gas the transaction can consume.
    Returns:
        str: Confirmation that the transaction is processed.
    Raises:
        TransactionError: If transaction cannot be processed due to high fees.
    """
    try:
        # Fetch current gas price
        gas_price = fetch_current_gas_price()

        # Calculate transaction fee
        transaction_fee = calculate_transaction_fee(gas_price, gas_limit)

        # Validate transaction fee
        validate_transaction_fee(transaction_amount, transaction_fee)

        # If validation passes, proceed with the transaction (placeholder logic)
        return f"Transaction processed successfully with fee: {transaction_fee:.8f} ETH"
    except TransactionError as e:
        return f"Transaction failed: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        transaction_amount = Decimal("0.5")  # Transacting 0.5 ETH
        gas_limit = 21000  # Typical gas limit for a basic ETH transfer

        result = handle_transaction(transaction_amount, gas_limit)
        print(result)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
