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
class CertificateOfDeposit:
    """
    A class to represent a Certificate of Deposit (CD) and calculate its returns.

    Attributes:
        principal (float): The initial amount of money deposited.
        annual_interest_rate (float): The annual interest rate (as a percentage).
        term_years (int): The term of the CD in years.
    """

    def __init__(self, principal: float, annual_interest_rate: float, term_years: int):
        """
        Initializes the CertificateOfDeposit with principal, interest rate, and term.

        Args:
            principal (float): The initial deposit amount.
            annual_interest_rate (float): The annual interest rate as a percentage.
            term_years (int): The duration of the CD in years.

        Raises:
            ValueError: If principal is negative, interest rate is not between 0 and 100, or term is negative.
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if not (0 <= annual_interest_rate <= 100):
            raise ValueError("Annual interest rate must be between 0 and 100.")
        if term_years < 0:
            raise ValueError("Term in years cannot be negative.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.term_years = term_years

    def calculate_returns(self) -> float:
        """
        Calculates the total returns on the Certificate of Deposit after the term.

        Returns:
            float: The total amount after the term including interest.
        """
        # Calculate the total amount using the formula for compound interest
        total_amount = self.principal * (1 + (self.annual_interest_rate / 100)) ** self.term_years
        return total_amount

    def calculate_interest_earned(self) -> float:
        """
        Calculates the interest earned on the Certificate of Deposit.

        Returns:
            float: The interest earned over the term.
        """
        total_amount = self.calculate_returns()
        interest_earned = total_amount - self.principal
        return interest_earned


# Example usage
if __name__ == "__main__":
    try:
        # Create a Certificate of Deposit instance
        cd = CertificateOfDeposit(principal=1000.0, annual_interest_rate=5.0, term_years=3)

        # Calculate total returns and interest earned
        total_returns = cd.calculate_returns()
        interest_earned = cd.calculate_interest_earned()

        # Print the results
        print(f"Total amount after {cd.term_years} years: ${total_returns:.2f}")
        print(f"Interest earned: ${interest_earned:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
