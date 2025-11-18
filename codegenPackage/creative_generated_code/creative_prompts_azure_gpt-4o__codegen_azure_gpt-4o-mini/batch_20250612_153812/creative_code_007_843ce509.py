"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-neurongate.xyz
Prompt: Write code to implement a welcome bonus system for an online casino, including features like €450 and 250 free spins, as described on the Zeus Fortune webpage.
Generated: DETERMINISTIC_843ce509cd2886ba
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WelcomeBonus:
    def __init__(self, bonus_amount=450, free_spins=250):
        """
        Initialize the WelcomeBonus class with default values.

        :param bonus_amount: The monetary bonus amount (default is €450)
        :param free_spins: The number of free spins granted (default is 250)
        """
        self.bonus_amount = bonus_amount  # Monetary bonus
        self.free_spins = free_spins  # Number of free spins

    def apply_bonus(self, user_balance):
        """
        Apply the welcome bonus to the user's balance.

        :param user_balance: The current balance of the user
        :return: Updated balance after applying the bonus
        """
        if user_balance < 0:
            raise ValueError("User balance cannot be negative.")
        
        updated_balance = user_balance + self.bonus_amount
        return updated_balance

    def get_free_spins(self):
        """
        Get the total number of free spins granted.

        :return: Number of free spins
        """
        return self.free_spins

    def validate_user(self, user):
        """
        Validate the user eligibility for the welcome bonus.

        :param user: A dictionary containing user details
        :return: Boolean indicating whether the user is eligible
        """
        if "age" in user and user["age"] >= 18:
            return True
        else:
            raise PermissionError("User must be at least 18 years old.")

def main():
    """
    Main function to demonstrate the welcome bonus functionality.
    """
    # Sample user data
    user = {
        "username": "player1",
        "age": 25,
        "balance": 100  # User's current balance
    }

    try:
        # Create a WelcomeBonus instance
        welcome_bonus = WelcomeBonus()

        # Validate user eligibility
        if welcome_bonus.validate_user(user):
            # Apply bonus to user balance
            new_balance = welcome_bonus.apply_bonus(user["balance"])
            free_spins = welcome_bonus.get_free_spins()

            print(f"Welcome Bonus Applied! New Balance: €{new_balance}")
            print(f"Total Free Spins Granted: {free_spins}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except PermissionError as pe:
        print(f"Error: {pe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
