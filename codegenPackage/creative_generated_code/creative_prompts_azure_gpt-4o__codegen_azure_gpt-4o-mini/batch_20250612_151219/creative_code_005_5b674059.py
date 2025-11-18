"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbbag.com
Prompt: Generate code to calculate the conversion rate of $MBAG tokens based on the current presale stage price (e.g., 1 MBAG = 0.0005 USDT) and payment method.
Generated: DETERMINISTIC_5b6740590f1fe283
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MBAGTokenConverter:
    """
    A class to convert MBAG tokens to USDT based on the current presale stage price.
    """

    def __init__(self, price_per_mbag: float):
        """
        Initializes the converter with the price of MBAG tokens.

        :param price_per_mbag: The price of one MBAG token in USDT.
        """
        if price_per_mbag <= 0:
            raise ValueError("Price per MBAG must be greater than zero.")
        self.price_per_mbag = price_per_mbag

    def convert(self, amount_of_mbag: float, payment_method: str) -> float:
        """
        Converts MBAG tokens to USDT based on the amount and payment method.

        :param amount_of_mbag: The amount of MBAG tokens to convert.
        :param payment_method: The payment method being used (e.g., "USDT", "ETH").
        :return: The equivalent amount in USDT.
        """
        if amount_of_mbag <= 0:
            raise ValueError("Amount of MBAG must be greater than zero.")
        if payment_method not in ["USDT", "ETH"]:
            raise ValueError("Unsupported payment method. Supported methods are 'USDT' and 'ETH'.")

        # Calculate total in USDT
        total_usdt = amount_of_mbag * self.price_per_mbag
        
        return total_usdt

def main():
    """
    Main function to demonstrate the MBAGTokenConverter functionality.
    """
    try:
        # Example price per MBAG token in USDT
        price_per_mbag = 0.0005  # Current presale price
        converter = MBAGTokenConverter(price_per_mbag)

        # Example amount of MBAG tokens to convert
        amount_of_mbag = 1000  # Number of tokens to convert
        payment_method = "USDT"  # Payment method used

        # Perform conversion
        converted_amount = converter.convert(amount_of_mbag, payment_method)
        print(f"{amount_of_mbag} MBAG tokens are equivalent to {converted_amount:.4f} USDT.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
