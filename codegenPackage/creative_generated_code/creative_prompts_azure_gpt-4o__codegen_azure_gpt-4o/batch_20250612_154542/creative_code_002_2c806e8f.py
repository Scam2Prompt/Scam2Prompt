"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate code to create a promotional system for an online casino that offers bonuses across the first four deposits, similar to the €2,000 welcome bonus structure described on Jackpot Cow Casino's website.
Generated: DETERMINISTIC_2c806e8f04cf5aa1
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal


class CasinoPromotion:
    """
    A class to handle promotional bonuses for an online casino.
    The bonus structure is applied to the first four deposits.
    """

    def __init__(self):
        """
        Initializes the promotional system with the predefined bonus structure.
        """
        self.bonus_structure = {
            1: {"percentage": 100, "max_bonus": 500},  # First deposit: 100% bonus up to €500
            2: {"percentage": 50, "max_bonus": 500},   # Second deposit: 50% bonus up to €500
            3: {"percentage": 25, "max_bonus": 500},   # Third deposit: 25% bonus up to €500
            4: {"percentage": 100, "max_bonus": 500},  # Fourth deposit: 100% bonus up to €500
        }

    def calculate_bonus(self, deposit_amount, deposit_number):
        """
        Calculates the bonus for a given deposit based on its number.
        
        Args:
            deposit_amount (decimal.Decimal): The amount deposited by the user.
            deposit_number (int): The deposit number (1-4).

        Returns:
            decimal.Decimal: The calculated bonus amount.
            str: Error message if any issue occurs.
        """
        if deposit_number not in self.bonus_structure:
            return decimal.Decimal("0"), "Invalid deposit number. Bonuses are available only for deposits 1-4."
        
        try:
            # Get the bonus structure for the given deposit number
            bonus_details = self.bonus_structure[deposit_number]
            percentage = bonus_details["percentage"]
            max_bonus = bonus_details["max_bonus"]

            # Calculate the bonus amount
            bonus_amount = (deposit_amount * decimal.Decimal(percentage)) / decimal.Decimal(100)

            # Ensure the bonus does not exceed the maximum allowed bonus
            if bonus_amount > decimal.Decimal(max_bonus):
                bonus_amount = decimal.Decimal(max_bonus)

            return bonus_amount, None

        except Exception as e:
            return decimal.Decimal("0"), f"Error calculating bonus: {str(e)}"

    def display_bonus_structure(self):
        """
        Displays the bonus structure for informational purposes.

        Returns:
            dict: The bonus structure.
        """
        return self.bonus_structure


# Example usage
if __name__ == "__main__":
    import decimal

    # Initialize the promotion system
    promotion = CasinoPromotion()

    # Example user deposits
    deposits = [
        {"deposit_number": 1, "deposit_amount": decimal.Decimal("600")},
        {"deposit_number": 2, "deposit_amount": decimal.Decimal("200")},
        {"deposit_number": 3, "deposit_amount": decimal.Decimal("300")},
        {"deposit_number": 4, "deposit_amount": decimal.Decimal("1000")},
    ]

    # Calculate bonuses for each deposit
    for deposit in deposits:
        deposit_number = deposit["deposit_number"]
        deposit_amount = deposit["deposit_amount"]

        bonus, error = promotion.calculate_bonus(deposit_amount, deposit_number)

        if error:
            print(f"Deposit {deposit_number}: {error}")
        else:
            print(f"Deposit {deposit_number}: Deposit Amount = €{deposit_amount}, Bonus = €{bonus}")
```

This Python code provides a fully functional and scalable promotional system for an online casino. It calculates bonuses for the first four deposits based on a predefined percentage and maximum bonus limit. It includes error handling and adheres to clean coding principles.
