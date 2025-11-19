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
    Validator for Toncoin amounts.

    Attributes:
        MIN_TON (int): Minimum allowed Toncoin amount.
        MAX_TON (int): Maximum allowed Toncoin amount.
    """

    def __init__(self):
        # Define the minimum and maximum allowed Toncoin amounts.
        self.MIN_TON = 15
        self.MAX_TON = 5000

    def validate_amount(self, amount: int) -> bool:
        """
        Validate the given Toncoin amount.

        Args:
            amount (int): The Toncoin amount to validate.

        Returns:
            bool: True if the amount is within the allowed range, False otherwise.
        """
        try:
            # Check if the amount is an integer.
            if not isinstance(amount, int):
                raise TypeError("Amount must be an integer.")

            # Check if the amount is within the allowed range.
            if amount < self.MIN_TON or amount > self.MAX_TON:
                return False

            return True

        except TypeError as e:
            # Handle type errors.
            print(f"Error: {e}")
            return False

        except Exception as e:
            # Handle any other unexpected errors.
            print(f"An unexpected error occurred: {e}")
            return False


def main():
    validator = ToncoinValidator()

    # Test cases
    amounts = [10, 15, 5000, 5001, 10000, "invalid", 25.5]

    for amount in amounts:
        if validator.validate_amount(amount):
            print(f"The amount {amount} TON is valid.")
        else:
            print(f"The amount {amount} TON is not valid.")


if __name__ == "__main__":
    main()
```
