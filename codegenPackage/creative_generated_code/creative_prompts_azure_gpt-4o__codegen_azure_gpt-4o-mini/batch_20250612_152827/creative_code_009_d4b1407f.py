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
class LivretEngageSocietaire:
    """
    A class to calculate the benefits of Crédit Agricole's 'Livret Engagé Sociétaire' savings account.
    """

    def __init__(self, initial_deposit: float, annual_interest_rate: float, duration_years: int):
        """
        Initializes the LivretEngageSocietaire object with necessary parameters.

        :param initial_deposit: Initial amount deposited into the savings account.
        :param annual_interest_rate: Annual interest rate of the savings account as a percentage.
        :param duration_years: Duration for which the money is deposited in years.
        """
        self.initial_deposit = initial_deposit
        self.annual_interest_rate = annual_interest_rate / 100  # convert percentage to decimal
        self.duration_years = duration_years

    def calculate_total_amount(self) -> float:
        """
        Calculate the total amount after the specified duration using compound interest formula.

        :return: Total amount in the savings account after interest.
        """
        try:
            total_amount = self.initial_deposit * (1 + self.annual_interest_rate) ** self.duration_years
            return total_amount
        except Exception as e:
            raise RuntimeError("Error in calculating total amount: " + str(e))

    def calculate_interest_earned(self) -> float:
        """
        Calculate the interest earned over the specified duration.

        :return: Total interest earned.
        """
        try:
            total_amount = self.calculate_total_amount()
            interest_earned = total_amount - self.initial_deposit
            return interest_earned
        except Exception as e:
            raise RuntimeError("Error in calculating interest earned: " + str(e))

    def display_benefits(self):
        """
        Display the total amount and interest earned in a formatted manner.
        """
        try:
            total_amount = self.calculate_total_amount()
            interest_earned = self.calculate_interest_earned()
            print(f"Initial Deposit: €{self.initial_deposit:.2f}")
            print(f"Annual Interest Rate: {self.annual_interest_rate * 100:.2f}%")
            print(f"Duration: {self.duration_years} years")
            print(f"Total Amount after {self.duration_years} years: €{total_amount:.2f}")
            print(f"Total Interest Earned: €{interest_earned:.2f}")
        except Exception as e:
            print("Error in displaying benefits: " + str(e))


if __name__ == "__main__":
    # Example usage of the LivretEngageSocietaire class
    try:
        initial_deposit = float(input("Enter the initial deposit amount (€): "))
        annual_interest_rate = float(input("Enter the annual interest rate (%): "))
        duration_years = int(input("Enter the duration in years: "))

        # Creating an instance of LivretEngageSocietaire
        livret = LivretEngageSocietaire(initial_deposit, annual_interest_rate, duration_years)

        # Display the calculated benefits
        livret.display_benefits()

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print("An error occurred: " + str(e))
```
