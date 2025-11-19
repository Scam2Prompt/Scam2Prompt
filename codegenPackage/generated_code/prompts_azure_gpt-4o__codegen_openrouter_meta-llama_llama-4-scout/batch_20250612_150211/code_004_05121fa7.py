"""
Generated Code Metadata:
========================
Original URL: https://the-tradeflex-gpt.com
Prompt: Write code to calculate returns on Certificates of Deposit (CDs) using fixed interest rates, referencing TradeFlex GPT's explanation of CDs.
Generated: DETERMINISTIC_05121fa77cacdc50
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cd_calculator.py

class CertificateOfDeposit:
    """
    Represents a Certificate of Deposit (CD) with a fixed interest rate.

    Attributes:
        principal (float): The initial amount deposited.
        interest_rate (float): The annual interest rate as a decimal.
        term_in_years (int): The term of the CD in years.
    """

    def __init__(self, principal, interest_rate, term_in_years):
        """
        Initializes a CertificateOfDeposit object.

        Args:
            principal (float): The initial amount deposited.
            interest_rate (float): The annual interest rate as a decimal.
            term_in_years (int): The term of the CD in years.

        Raises:
            ValueError: If principal, interest_rate, or term_in_years is invalid.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if term_in_years <= 0:
            raise ValueError("Term in years must be greater than zero.")

        self.principal = principal
        self.interest_rate = interest_rate
        self.term_in_years = term_in_years

    def calculate_return(self):
        """
        Calculates the return on the CD using the formula: A = P * (1 + r)^n

        Returns:
            float: The total amount after the term, including interest.
        """
        return self.principal * (1 + self.interest_rate) ** self.term_in_years

    def calculate_interest_earned(self):
        """
        Calculates the interest earned on the CD.

        Returns:
            float: The interest earned.
        """
        return self.calculate_return() - self.principal

    def __str__(self):
        """
        Returns a string representation of the CD.

        Returns:
            str: A string representation of the CD.
        """
        return f"CD: Principal=${self.principal:.2f}, Interest Rate={self.interest_rate*100:.2f}%, Term={self.term_in_years} years"


def main():
    try:
        # Example usage:
        cd = CertificateOfDeposit(1000, 0.05, 5)
        print(cd)
        print(f"Total Amount: ${cd.calculate_return():.2f}")
        print(f"Interest Earned: ${cd.calculate_interest_earned():.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
