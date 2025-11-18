"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonmixers.com
Prompt: Generate code to check the minimum and maximum Toncoin amounts (15 TON to 5000 TON) allowed for mixing and validate user input accordingly.
Generated: DETERMINISTIC_7bd6eeae6a1d8ff5
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ToncoinValidator:
    """
    A class to validate Toncoin amounts for mixing.
    Minimum and maximum allowed amounts are defined as constants.
    """

    MIN_AMOUNT = 15   # Minimum allowed amount of Toncoin
    MAX_AMOUNT = 5000  # Maximum allowed amount of Toncoin

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """
        Validate the Toncoin amount.

        Args:
            amount (float): The amount of Toncoin to validate.

        Returns:
            bool: True if the amount is valid, False otherwise.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")

        if amount < ToncoinValidator.MIN_AMOUNT:
            raise ValueError(f"Amount must be at least {ToncoinValidator.MIN_AMOUNT} TON.")
        elif amount > ToncoinValidator.MAX_AMOUNT:
            raise ValueError(f"Amount must not exceed {ToncoinValidator.MAX_AMOUNT} TON.")
        
        return True

def main():
    """
    Main function to run the Toncoin validation process.
    """
    user_input = input("Enter the amount of Toncoin for mixing: ")

    try:
        amount = float(user_input)  # Convert input to float
        if ToncoinValidator.validate_amount(amount):
            print(f"Valid amount: {amount} TON")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
