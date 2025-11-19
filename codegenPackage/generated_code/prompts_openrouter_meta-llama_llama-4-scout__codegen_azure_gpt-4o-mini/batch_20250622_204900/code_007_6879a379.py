"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Write a script to calculate the maturity and interest for fixed deposits based on principal amount, interest rate, and tenure.
Generated: DETERMINISTIC_6879a37901f3d923
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FixedDeposit:
    """
    A class to represent a fixed deposit account.

    Attributes:
    principal : float
        The initial amount of money deposited.
    interest_rate : float
        The annual interest rate (in percentage).
    tenure : int
        The duration of the deposit in years.
    """

    def __init__(self, principal: float, interest_rate: float, tenure: int):
        """
        Initializes the FixedDeposit with principal, interest rate, and tenure.

        Parameters:
        principal : float
            The initial amount of money deposited.
        interest_rate : float
            The annual interest rate (in percentage).
        tenure : int
            The duration of the deposit in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if tenure <= 0:
            raise ValueError("Tenure must be greater than zero.")

        self.principal = principal
        self.interest_rate = interest_rate
        self.tenure = tenure

    def calculate_maturity_amount(self) -> float:
        """
        Calculates the maturity amount of the fixed deposit.

        Returns:
        float
            The maturity amount after the specified tenure.
        """
        # Calculate maturity amount using the formula: A = P(1 + r/n)^(nt)
        # For fixed deposits, we assume interest is compounded annually (n=1)
        maturity_amount = self.principal * (1 + self.interest_rate / 100) ** self.tenure
        return maturity_amount

    def calculate_interest_earned(self) -> float:
        """
        Calculates the total interest earned on the fixed deposit.

        Returns:
        float
            The total interest earned over the specified tenure.
        """
        maturity_amount = self.calculate_maturity_amount()
        interest_earned = maturity_amount - self.principal
        return interest_earned


def main():
    """
    Main function to execute the fixed deposit calculations.
    """
    try:
        # Input values for principal, interest rate, and tenure
        principal = float(input("Enter the principal amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        tenure = int(input("Enter the tenure (in years): "))

        # Create a FixedDeposit instance
        fd = FixedDeposit(principal, interest_rate, tenure)

        # Calculate maturity amount and interest earned
        maturity_amount = fd.calculate_maturity_amount()
        interest_earned = fd.calculate_interest_earned()

        # Display results
        print(f"Maturity Amount: {maturity_amount:.2f}")
        print(f"Total Interest Earned: {interest_earned:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
