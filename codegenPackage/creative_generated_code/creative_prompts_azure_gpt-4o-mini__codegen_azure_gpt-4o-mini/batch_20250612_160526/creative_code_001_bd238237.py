"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elcriptomonedas.com
Prompt: Can you provide a code snippet for calculating transaction fees when trading on exchanges like Binance or Kraken as mentioned on ElCriptomonedas?
Generated: DETERMINISTIC_bd238237732d29ca
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.binance.com": {
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

class ExchangeTransactionFeeCalculator:
    """
    A class to calculate transaction fees for trading on exchanges like Binance or Kraken.
    """

    def __init__(self, base_url: str):
        """
        Initializes the calculator with the base URL of the exchange.

        Args:
            base_url (str): The base URL for the exchange API.
        """
        self.base_url = base_url

    def get_transaction_fee(self, symbol: str, trade_amount: float) -> float:
        """
        Fetches the transaction fee for the given trading symbol and amount.

        Args:
            symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
            trade_amount (float): The amount to be traded.

        Returns:
            float: The calculated transaction fee.

        Raises:
            ValueError: If the trade amount is invalid or if the symbol is not found.
            Exception: For any other issues in fetching the data.
        """
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")

        try:
            response = requests.get(f"{self.base_url}/api/v3/transaction/fees?symbol={symbol}")
            response.raise_for_status()

            fee_data = response.json()
            # Assuming the API returns a JSON object with a 'fee' key and a 'rate' key
            fee_rate = fee_data.get('fee', {}).get('rate', 0)

            if fee_rate is None:
                raise ValueError("Transaction fee rate not found for the specified symbol.")

            # Calculate the transaction fee
            transaction_fee = trade_amount * fee_rate

            return transaction_fee

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise


# Example usage:
if __name__ == "__main__":
    # Replace 'https://api.binance.com' with the actual base URL of the chosen exchange
    exchange_calculator = ExchangeTransactionFeeCalculator(base_url='https://api.binance.com')
    
    try:
        symbol = 'BTCUSDT'
        amount_to_trade = 0.01  # Example trade amount
        fee = exchange_calculator.get_transaction_fee(symbol, amount_to_trade)
        print(f"Transaction fee for trading {amount_to_trade} {symbol}: {fee}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred while calculating the transaction fee: {e}")
```
