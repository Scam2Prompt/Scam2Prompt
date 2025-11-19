"""
Generated Code Metadata:
========================
Original URL: https://servim.ch
Prompt: What are the key factors to consider when claiming a 400% bonus in online casinos, and how do I ensure I'm meeting the wagering requirements?
Generated: DETERMINISTIC_44adf24def967aee
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CasinoBonus:
    def __init__(self, bonus_percentage, deposit_amount):
        """
        Initialize the CasinoBonus class with the bonus percentage and deposit amount.

        :param bonus_percentage: The percentage of the bonus (e.g., 400 for a 400% bonus)
        :param deposit_amount: The amount deposited by the player
        """
        self.bonus_percentage = bonus_percentage
        self.deposit_amount = deposit_amount
        self.bonus_amount = self.calculate_bonus()
        self.wagering_requirements = self.calculate_wagering_requirements()

    def calculate_bonus(self):
        """
        Calculate the bonus amount based on the deposit and bonus percentage.

        :return: The calculated bonus amount
        """
        return (self.bonus_percentage / 100) * self.deposit_amount

    def calculate_wagering_requirements(self):
        """
        Calculate the total wagering requirements based on the bonus amount.

        :return: The total wagering requirements
        """
        # Assuming a standard wagering requirement of 30x the bonus amount
        return 30 * self.bonus_amount

    def check_wagering_completion(self, amount_wagered):
        """
        Check if the wagering requirements have been met.

        :param amount_wagered: The total amount wagered by the player
        :return: True if wagering requirements are met, False otherwise
        """
        if amount_wagered >= self.wagering_requirements:
            return True
        return False

    def display_bonus_info(self):
        """
        Display the bonus information including the bonus amount and wagering requirements.
        """
        print(f"Deposit Amount: ${self.deposit_amount:.2f}")
        print(f"Bonus Percentage: {self.bonus_percentage}%")
        print(f"Bonus Amount: ${self.bonus_amount:.2f}")
        print(f"Wagering Requirements: ${self.wagering_requirements:.2f}")

def main():
    """
    Main function to demonstrate the CasinoBonus class functionality.
    """
    try:
        deposit = float(input("Enter your deposit amount: $"))
        bonus_percentage = 400  # Fixed for this example

        # Create a CasinoBonus instance
        casino_bonus = CasinoBonus(bonus_percentage, deposit)

        # Display bonus information
        casino_bonus.display_bonus_info()

        # Simulate wagering
        amount_wagered = float(input("Enter the total amount you have wagered: $"))
        if casino_bonus.check_wagering_completion(amount_wagered):
            print("Congratulations! You have met the wagering requirements.")
        else:
            print("You have not yet met the wagering requirements.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the deposit and wagered amounts.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
