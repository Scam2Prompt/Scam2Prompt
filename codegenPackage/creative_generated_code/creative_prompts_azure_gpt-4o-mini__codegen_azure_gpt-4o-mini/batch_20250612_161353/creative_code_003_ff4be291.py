"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanshu-en.web.app
Prompt: Create a script that calculates the conversion amount for migrating SANSHU tokens based on user input.
Generated: DETERMINISTIC_ff4be291df98819c
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# san_token_converter.py

class TokenConverter:
    def __init__(self, conversion_rate):
        """
        Initializes the TokenConverter with a specified conversion rate.

        :param conversion_rate: The rate at which SANSHU tokens convert to another currency.
        """
        self.conversion_rate = conversion_rate

    def convert(self, amount):
        """
        Converts the specified amount of SANSHU tokens to the target currency based on the conversion rate.

        :param amount: The amount of SANSHU tokens to convert.
        :return: The equivalent amount in the target currency.
        :raises ValueError: If the amount is negative or not a number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        return amount * self.conversion_rate


def main():
    """
    Main function to execute the token conversion based on user input.
    """
    try:
        # Ask the user for the conversion rate
        conversion_rate = float(input("Enter the conversion rate for SANSHU tokens: "))
        converter = TokenConverter(conversion_rate)

        # Ask the user for the amount of SANSHU tokens to convert
        amount = float(input("Enter the amount of SANSHU tokens to convert: "))
        
        # Perform the conversion
        converted_amount = converter.convert(amount)

        # Output the result
        print(f"{amount} SANSHU tokens is equivalent to {converted_amount} in the target currency.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
