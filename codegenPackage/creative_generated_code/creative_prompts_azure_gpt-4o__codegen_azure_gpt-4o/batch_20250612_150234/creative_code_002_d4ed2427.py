"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoinmixer.com
Prompt: Generate code to calculate the service fees for mixing cryptocurrencies using fixed rates, such as 10 DOGE for Dogecoin or 0.0010 BTC for Bitcoin, based on the minimum and maximum transaction limits.
Generated: DETERMINISTIC_d4ed24275ebb142d
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the service fees for cryptocurrency mixing based on fixed rates per coin.
It supports multiple cryptocurrencies with minimum and maximum transaction limits.
"""

class CryptoMixerService:
    def __init__(self):
        """
        Initializes supported cryptocurrencies, their fixed rates, and transaction limits.
        """
        self.supported_currencies = {
            "BTC": {
                "fixed_rate": 0.0010,  # Fixed rate in BTC
                "min_limit": 0.01,     # Minimum transaction limit
                "max_limit": 10.0      # Maximum transaction limit
            },
            "DOGE": {
                "fixed_rate": 10.0,    # Fixed rate in DOGE
                "min_limit": 100.0,    # Minimum transaction limit
                "max_limit": 100000.0  # Maximum transaction limit
            }
        }

    def calculate_fee(self, currency: str, amount: float) -> float:
        """
        Calculates service fee for a given cryptocurrency and transaction amount.

        Parameters:
            currency (str): The cryptocurrency (e.g., "BTC", "DOGE").
            amount (float): The transaction amount.

        Returns:
            float: The calculated service fee.

        Raises:
            ValueError: If the currency is unsupported or the amount is out of range.
        """
        # Validate if the currency is supported
        if currency not in self.supported_currencies:
            raise ValueError(f"Unsupported currency: {currency}")
        
        # Get the cryptocurrency details
        crypto_details = self.supported_currencies[currency]
        fixed_rate = crypto_details["fixed_rate"]
        min_limit = crypto_details["min_limit"]
        max_limit = crypto_details["max_limit"]
        
        # Validate transaction limits
        if not (min_limit <= amount <= max_limit):
            raise ValueError(
                f"Transaction amount for {currency} must be between {min_limit} and {max_limit}."
            )
        
        # Calculate the fee
        return fixed_rate

# Example usage
if __name__ == "__main__":
    try:
        mixer_service = CryptoMixerService()
        currency = "BTC"
        amount = 0.05  # Example transaction amount in BTC

        fee = mixer_service.calculate_fee(currency, amount)
        print(f"Service fee for {amount} {currency}: {fee} {currency}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
