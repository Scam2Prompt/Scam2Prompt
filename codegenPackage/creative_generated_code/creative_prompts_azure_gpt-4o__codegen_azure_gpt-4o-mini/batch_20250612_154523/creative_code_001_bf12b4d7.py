"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Generate a script to automate the conversion of monetary values into text format, referencing the "Convertir de números a letras" tool mentioned on AulaContable.
Generated: DETERMINISTIC_bf12b4d76bff1911
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import inflect

class CurrencyConverter:
    def __init__(self):
        """Initialize the CurrencyConverter with English language support."""
        self.p = inflect.engine()

    def convert_number_to_words(self, amount):
        """
        Convert a number to its word representation.
        
        Parameters:
        amount (float): The monetary amount to convert.

        Returns:
        str: The word representation of the number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount should be a numeric value.")

        # Split the amount into whole and fractional parts
        whole_part = int(amount)
        fractional_part = round((amount - whole_part) * 100)

        # Convert the whole part and fractional part to words
        words = self.p.number_to_words(whole_part)

        # Append the cents (if any)
        if fractional_part > 0:
            cents_words = self.p.number_to_words(fractional_part)
            words += f" and {cents_words} cent{'s' if fractional_part != 1 else ''}"

        return words.capitalize()

    def convert_currency(self, amount):
        """
        Convert the given amount to text format and handle errors.

        Parameters:
        amount (float): The monetary amount to convert.

        Returns:
        str: The string representation of the amount in words.
        """
        try:
            words = self.convert_number_to_words(amount)
            return words
        except ValueError as e:
            return str(e)

if __name__ == "__main__":
    converter = CurrencyConverter()
    # Example usage:
    try:
        amount = float(input("Enter the amount to convert: "))
        result = converter.convert_currency(amount)
        print(f"The amount in words is: {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
```
