"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.at
Prompt: Generate code to calculate the service fee for a Bitcoin mixing transaction using the fee structure provided by CryptoMixer.at (0.5% + 0.0005 BTC) and apply discounts for repeated usage with the same code.
Generated: DETERMINISTIC_84dee722d50334ba
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMixingService:
    """
    A class to calculate the service fee for Bitcoin mixing transactions
    based on the fee structure provided by CryptoMixer.at.
    """

    BASE_FEE_PERCENTAGE = 0.005  # 0.5%
    BASE_FEE_FLAT = 0.0005  # Flat fee in BTC

    def __init__(self):
        """
        Initializes the BitcoinMixingService with no previous usage count.
        """
        self.usage_count = 0

    def calculate_fee(self, amount_btc):
        """
        Calculate the service fee for the given amount in BTC.

        :param amount_btc: The amount in BTC for which to calculate the service fee.
        :return: The calculated service fee in BTC.
        :raises ValueError: If the provided amount is non-positive.
        """
        if amount_btc <= 0:
            raise ValueError("The amount must be greater than zero.")

        # Calculate the base fee
        percentage_fee = amount_btc * self.BASE_FEE_PERCENTAGE
        total_fee = percentage_fee + self.BASE_FEE_FLAT

        # Apply discount for repeated usage
        discount = self._calculate_discount()
        total_fee -= discount

        # Ensure total fee does not go below zero
        return max(total_fee, 0)

    def _calculate_discount(self):
        """
        Calculate the discount based on the number of previous usages.

        :return: The discount amount in BTC.
        """
        # Example discount: 10% off the fee for each use after the first
        discount_rate = 0.10  # 10% discount
        if self.usage_count > 0:
            # Calculate discount based on the current fee
            return (self.calculate_fee(amount_btc) * discount_rate)
        return 0

    def use_service(self, amount_btc):
        """
        Use the service to calculate the fee and increment usage count.

        :param amount_btc: The amount in BTC for which to calculate the service fee.
        :return: The service fee in BTC.
        """
        fee = self.calculate_fee(amount_btc)
        self.usage_count += 1  # Increment usage count after service is used
        return fee


# Example usage
if __name__ == "__main__":
    try:
        mixer = BitcoinMixingService()
        
        # Example transaction amounts
        transaction_amounts = [0.1, 0.5, 0.2]

        for amount in transaction_amounts:
            fee = mixer.use_service(amount)
            print(f"Transaction amount: {amount} BTC | Service fee: {fee} BTC")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
