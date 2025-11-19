"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internationalconversionethereumfunds.weebly.com
Prompt: Generate a script that calculates the service fee for converting funds as described on the Ethereum International Conversion Funds webpage.
Generated: DETERMINISTIC_637441d77416aaf5
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
currency_converter.py
A script that calculates the service fee for converting funds based on
the Ethereum International Conversion Funds fee structure.
"""

class CurrencyConverter:
    """A class to handle currency conversion calculations."""

    def __init__(self, conversion_rate, service_fee_percentage):
        """
        Initializes the CurrencyConverter with a given conversion rate
        and service fee percentage.

        Args:
            conversion_rate (float): The rate at which to convert currency.
            service_fee_percentage (float): The percentage fee applied to the conversion.
        """
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be greater than zero.")
        if not (0 <= service_fee_percentage <= 100):
            raise ValueError("Service fee percentage must be between 0 and 100.")

        self.conversion_rate = conversion_rate
        self.service_fee_percentage = service_fee_percentage

    def calculate_conversion(self, amount):
        """
        Calculates the converted amount and the service fee.

        Args:
            amount (float): The amount of currency to convert.

        Returns:
            dict: A dictionary containing the converted amount and service fee.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Amount to convert must be greater than zero.")

        # Calculate the service fee
        service_fee = amount * (self.service_fee_percentage / 100)

        # Calculate the converted amount after applying the service fee
        converted_amount = (amount - service_fee) * self.conversion_rate

        return {
            "converted_amount": converted_amount,
            "service_fee": service_fee
        }

def main():
    """Main function to execute the currency conversion process."""
    try:
        # Example values (these can be modified or received as input)
        conversion_rate = 1.5  # Example conversion rate
        service_fee_percentage = 2.5  # Example service fee percentage

        # Create a CurrencyConverter instance
        converter = CurrencyConverter(conversion_rate, service_fee_percentage)

        # Amount to convert (example input)
        amount_to_convert = float(input("Enter the amount to convert: "))

        # Calculate the conversion
        result = converter.calculate_conversion(amount_to_convert)

        # Display the results
        print(f"Converted Amount: {result['converted_amount']:.2f}")
        print(f"Service Fee: {result['service_fee']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
