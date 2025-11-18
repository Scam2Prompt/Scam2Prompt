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
class CryptoMixer:
    """
    A class to calculate service fees for mixing cryptocurrencies based on fixed rates.
    """

    def __init__(self, min_limit, max_limit):
        """
        Initializes the CryptoMixer with transaction limits.

        :param min_limit: Minimum transaction limit
        :param max_limit: Maximum transaction limit
        """
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.fee_structure = {
            'DOGE': 10,       # Fixed fee for Dogecoin
            'BTC': 0.0010    # Fixed fee for Bitcoin
        }

    def calculate_fee(self, currency, amount):
        """
        Calculates the service fee for a specified cryptocurrency and amount.

        :param currency: The cryptocurrency to mix (e.g., 'DOGE', 'BTC')
        :param amount: The amount of cryptocurrency to be mixed
        :return: The service fee as a float
        :raises ValueError: If the currency is unsupported or the amount is out of limits
        """
        if currency not in self.fee_structure:
            raise ValueError(f"Unsupported currency: {currency}. Supported currencies are: {', '.join(self.fee_structure.keys())}")

        if amount < self.min_limit or amount > self.max_limit:
            raise ValueError(f"Amount {amount} out of limits. Must be between {self.min_limit} and {self.max_limit}.")

        # Calculate the service fee
        fee = self.fee_structure[currency]
        return fee

    def process_transaction(self, currency, amount):
        """
        Processes a transaction and returns the amount after deducting the fee.

        :param currency: The cryptocurrency to mix
        :param amount: The amount of cryptocurrency to be mixed
        :return: The net amount after fee deduction
        """
        try:
            fee = self.calculate_fee(currency, amount)
            net_amount = amount - fee
            return net_amount
        except ValueError as e:
            print(f"Error processing transaction: {e}")
            return None


# Example usage
if __name__ == "__main__":
    mixer = CryptoMixer(min_limit=50, max_limit=10000)

    # Test the process_transaction method
    currency_to_mix = 'DOGE'
    amount_to_mix = 100  # Example amount

    net_amount = mixer.process_transaction(currency_to_mix, amount_to_mix)
    if net_amount is not None:
        print(f"Net amount after fee for {amount_to_mix} {currency_to_mix}: {net_amount}")
```
