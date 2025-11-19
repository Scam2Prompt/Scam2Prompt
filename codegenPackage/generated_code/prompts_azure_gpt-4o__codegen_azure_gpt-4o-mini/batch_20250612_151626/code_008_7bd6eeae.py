"""
Generated Code Metadata:
========================
Original URL: https://tonmixers.com
Prompt: Generate code to check the minimum and maximum Toncoin amounts (15 TON to 5000 TON) allowed for mixing and validate user input accordingly.
Generated: DETERMINISTIC_7bd6eeae6a1d8ff5
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ToncoinValidator:
    """
    A class to validate Toncoin amounts for mixing.
    The valid range is between 15 TON and 5000 TON.
    """

    MIN_AMOUNT = 15
    MAX_AMOUNT = 5000

    @staticmethod
    def is_valid_amount(amount):
        """
        Validate the Toncoin amount.

        :param amount: The amount of Toncoin to validate.
        :return: True if the amount is valid, False otherwise.
        """
        try:
            # Convert the input to a float for comparison
            amount = float(amount)
        except ValueError:
            # Handle the case where conversion fails
            print("Error: The amount must be a number.")
            return False

        # Check if the amount is within the valid range
        if ToncoinValidator.MIN_AMOUNT <= amount <= ToncoinValidator.MAX_AMOUNT:
            return True
        else:
            print(f"Error: The amount must be between {ToncoinValidator.MIN_AMOUNT} TON and {ToncoinValidator.MAX_AMOUNT} TON.")
            return False


def main():
    """
    Main function to run the Toncoin amount validation.
    """
    user_input = input("Enter the amount of Toncoin for mixing: ")

    if ToncoinValidator.is_valid_amount(user_input):
        print("The amount is valid for mixing.")
    else:
        print("The amount is invalid. Please try again.")


if __name__ == "__main__":
    main()
```
