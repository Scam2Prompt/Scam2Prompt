"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.to
Prompt: Generate a code snippet that calculates the service fee for mixing Bitcoin using CryptoMixer based on the amount and selected options.
Generated: DETERMINISTIC_8d1bd7305c19673d
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CryptoMixer:
    """
    A class to represent the CryptoMixer service, calculating service fees
    based on the amount of Bitcoin and selected options.
    """
    def __init__(self):
        # Base service fee percentage (default fee for all transactions)
        self.base_fee_percent = 0.005  # 0.5% base fee
        # Additional fee percentages for optional features
        self.additional_option_fees = {
            'fast_processing': 0.002,  # 0.2% fee for faster processing
            'extra_security': 0.004,   # 0.4% fee for enhanced security
        }

    def calculate_fee(self, amount_btc, options=None):
        """
        Calculate the total service fee for mixing Bitcoin.

        :param amount_btc: float, Amount of Bitcoin to mix.
        :param options: list of str, Selected options (e.g., 'fast_processing', 'extra_security').
        :return: float, Total service fee in Bitcoin.
        """
        if amount_btc <= 0:
            raise ValueError("Amount of Bitcoin must be greater than zero.")

        # Start with the base fee
        total_fee_percent = self.base_fee_percent

        # Add fees for selected options
        if options:
            for option in options:
                if option in self.additional_option_fees:
                    total_fee_percent += self.additional_option_fees[option]
                else:
                    raise ValueError(f"Invalid option selected: {option}")

        # Calculate total fee in Bitcoin
        total_fee_btc = amount_btc * total_fee_percent
        return total_fee_btc


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the CryptoMixer service
        mixer = CryptoMixer()

        # Example inputs
        amount = 1.5  # Bitcoin amount
        selected_options = ['fast_processing', 'extra_security']  # Options selected by the user

        # Calculate the service fee
        fee = mixer.calculate_fee(amount, selected_options)

        # Display the results
        print(f"Total service fee for mixing {amount} BTC with options {selected_options}: {fee:.8f} BTC")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
