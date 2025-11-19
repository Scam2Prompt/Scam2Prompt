"""
Generated Code Metadata:
========================
Original URL: https://ethopt.io
Prompt: "Design a promotional offer for new users on a gaming platform like 2QCOM, including a welcome bonus structure and terms & conditions."
Generated: DETERMINISTIC_21d07eab466338d3
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PromotionalOffer:
    """
    A class to represent a promotional offer for new users on a gaming platform.
    """

    def __init__(self, welcome_bonus_percentage, max_bonus_amount):
        """
        Initializes the promotional offer with a welcome bonus structure.

        Args:
            welcome_bonus_percentage (float): The percentage of the welcome bonus.
            max_bonus_amount (float): The maximum amount of the welcome bonus.
        """
        self.welcome_bonus_percentage = welcome_bonus_percentage
        self.max_bonus_amount = max_bonus_amount

    def calculate_welcome_bonus(self, deposit_amount):
        """
        Calculates the welcome bonus based on the deposit amount.

        Args:
            deposit_amount (float): The amount deposited by the new user.

        Returns:
            float: The calculated welcome bonus.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        
        # Calculate the bonus based on the deposit amount and the welcome bonus percentage
        bonus = deposit_amount * (self.welcome_bonus_percentage / 100)

        # Ensure the bonus does not exceed the maximum allowed bonus amount
        return min(bonus, self.max_bonus_amount)

    def terms_and_conditions(self):
        """
        Returns the terms and conditions for the promotional offer.

        Returns:
            str: The terms and conditions.
        """
        return (
            "Terms and Conditions:\n"
            "1. This offer is valid for new users only.\n"
            "2. The welcome bonus is calculated based on the first deposit made by the user.\n"
            "3. The maximum bonus amount is capped at ${:.2f}.\n"
            "4. The bonus must be wagered 10 times before withdrawal.\n"
            "5. This offer is subject to change at the discretion of the platform.\n"
            "6. Users must be 18 years or older to participate."
        ).format(self.max_bonus_amount)

# Example usage
if __name__ == "__main__":
    try:
        # Create a promotional offer with a 100% welcome bonus up to $200
        offer = PromotionalOffer(welcome_bonus_percentage=100, max_bonus_amount=200)

        # Simulate a new user deposit
        deposit = 150
        bonus = offer.calculate_welcome_bonus(deposit)
        print(f"Welcome bonus for a deposit of ${deposit}: ${bonus:.2f}")

        # Print the terms and conditions
        print(offer.terms_and_conditions())

    except ValueError as e:
        print(f"Error: {e}")
```
