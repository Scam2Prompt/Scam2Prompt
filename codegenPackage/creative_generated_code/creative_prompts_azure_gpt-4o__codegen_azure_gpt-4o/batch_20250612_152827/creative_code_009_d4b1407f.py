"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Develop a tool to calculate the benefits of Crédit Agricole's "Livret Engagé Sociétaire" savings account based on its unique features.
Generated: DETERMINISTIC_d4b1407f21715a35
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class LivretEngageSocietaireCalculator:
    """
    A tool for calculating the benefits of Crédit Agricole's "Livret Engagé Sociétaire" savings account.
    """

    def __init__(self, principal, annual_interest_rate, duration_years):
        """
        Initialize the calculator with the principal amount, annual interest rate, and duration.

        :param principal: Initial deposit amount (in euros)
        :param annual_interest_rate: Annual interest rate (as a percentage)
        :param duration_years: Duration of the savings in years
        """
        if principal <= 0 or annual_interest_rate <= 0 or duration_years <= 0:
            raise ValueError("Principal, annual interest rate, and duration must be positive values.")
        
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_total_amount(self):
        """
        Calculate the total amount in the account at the end of the specified duration.

        :return: Total amount accumulated in the account (in euros)
        """
        # Formula for compound interest: A = P * (1 + r)^t
        total_amount = self.principal * (1 + self.annual_interest_rate) ** self.duration_years
        return round(total_amount, 2)

    def calculate_total_interest(self):
        """
        Calculate the total interest earned at the end of the specified duration.

        :return: Total interest earned (in euros)
        """
        total_amount = self.calculate_total_amount()
        total_interest = total_amount - self.principal
        return round(total_interest, 2)


def main():
    """
    Main function to interact with the user and perform calculations.
    """
    try:
        print("Welcome to the Livret Engagé Sociétaire Benefits Calculator!")
        
        # Prompt user for inputs
        principal = float(input("Enter the initial deposit amount (in euros): "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        duration_years = int(input("Enter the duration (in years): "))

        # Create an instance of the calculator
        calculator = LivretEngageSocietaireCalculator(principal, annual_interest_rate, duration_years)

        # Perform calculations
        total_amount = calculator.calculate_total_amount()
        total_interest = calculator.calculate_total_interest()

        # Display results
        print("\nResults:")
        print(f"Total amount in the account after {duration_years} years: €{total_amount}")
        print(f"Total interest earned over {duration_years} years: €{total_interest}")

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Input Error: {ve}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
