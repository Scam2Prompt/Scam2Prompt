"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradeflex-gpt.com
Prompt: Write code to calculate returns on Certificates of Deposit (CDs) using fixed interest rates, referencing TradeFlex GPT's explanation of CDs.
Generated: DETERMINISTIC_05121fa77cacdc50
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CertificateOfDeposit:
    """
    A class to represent a Certificate of Deposit (CD) investment.

    Attributes
    ----------
    principal : float
        The initial amount of money invested in the CD.
    interest_rate : float
        The annual fixed interest rate (as a percentage).
    term_years : int
        The duration of the CD in years.

    Methods
    -------
    calculate_returns():
        Calculates the total amount after the term, including interest earned.
    """

    def __init__(self, principal: float, interest_rate: float, term_years: int):
        """
        Constructs all the necessary attributes for the CD object.

        Parameters
        ----------
        principal : float
            The principal amount invested.
        interest_rate : float
            The annual interest rate (in percentage).
        term_years : int
            The term duration of the CD in years.
        """
        
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if interest_rate <= 0:
            raise ValueError("Interest rate must be greater than 0.")
        if term_years <= 0:
            raise ValueError("Term must be greater than 0 years.")
        
        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.term_years = term_years

    def calculate_returns(self) -> float:
        """
        Calculate the total returns on the CD after the specified term.

        Returns
        -------
        float
            The total amount after interest has been applied.
        """
        # Calculate the total amount using the formula for compound interest
        total_amount = self.principal * (1 + self.interest_rate) ** self.term_years
        return total_amount

# Example usage
if __name__ == "__main__":
    try:
        # Creating a CD instance with principal amount, interest rate, and term
        cd = CertificateOfDeposit(principal=1000.0, interest_rate=5.0, term_years=3)

        # Calculating the returns on the CD
        total_returns = cd.calculate_returns()
        print(f"Total amount after {cd.term_years} years: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
