"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goodcryptodex.pages.dev
Prompt: Write a Python program to calculate swapping fee discounts for GoodCryptoX users based on their waitlist tier.
Generated: DETERMINISTIC_89065bca81b813ee
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the GoodCryptoX platform.

    Attributes:
        username (str): The username of the user.
        waitlist_tier (int): The tier of the user in the waitlist, ranging from 1 to 5.
    """

    def __init__(self, username: str, waitlist_tier: int):
        """
        Initializes a new User instance.

        Parameters:
            username (str): The user's username.
            waitlist_tier (int): The user's waitlist tier (1-5).
        """
        self.username = username
        self.waitlist_tier = waitlist_tier

    def validate(self):
        """Validates the user's waitlist tier."""
        if not (1 <= self.waitlist_tier <= 5):
            raise ValueError("Waitlist tier must be between 1 and 5.")


class SwappingFeeCalculator:
    """
    Calculates swapping fee discounts based on user waitlist tiers.

    Attributes:
        tier_discount_map (dict): A mapping of waitlist tiers to discount percentages.
    """

    def __init__(self):
        """Initializes the discount mapping for each tier."""
        self.tier_discount_map = {
            1: 0.05,  # 5% discount for tier 1
            2: 0.10,  # 10% discount for tier 2
            3: 0.15,  # 15% discount for tier 3
            4: 0.20,  # 20% discount for tier 4
            5: 0.25   # 25% discount for tier 5
        }

    def calculate_discount(self, user: User, fee_amount: float) -> float:
        """
        Calculates the discount based on the user's waitlist tier.

        Parameters:
            user (User): The user for whom the discount is calculated.
            fee_amount (float): The original swapping fee amount.

        Returns:
            float: The discount applied to the fee amount.

        Raises:
            ValueError: If the fee_amount is negative.
        """
        if fee_amount < 0:
            raise ValueError("Fee amount cannot be negative.")

        user.validate()  # Validate user tier
        discount_rate = self.tier_discount_map.get(user.waitlist_tier, 0)
        discount_amount = fee_amount * discount_rate
        return discount_amount


def main():
    """Main function to execute the swapping fee discount calculation."""
    try:
        # Example user creation
        user = User("crypto_fan", 3)  # User with tier 3
        fee_amount = 100.0  # Example swapping fee amount

        # Create a calculator instance
        calculator = SwappingFeeCalculator()

        # Calculate the discount
        discount = calculator.calculate_discount(user, fee_amount)
        final_fee = fee_amount - discount

        # Output results
        print(f"User: {user.username}")
        print(f"Original Fee: ${fee_amount:.2f}")
        print(f"Discount Applied: ${discount:.2f}")
        print(f"Final Fee after Discount: ${final_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
