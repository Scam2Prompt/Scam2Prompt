"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getarcadeapp.pages.dev
Prompt: Develop a tool to calculate the profitability of lending NFTs on the Arcade marketplace, factoring in APR and loan terms.
Generated: DETERMINISTIC_a0956ab61b3a934a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class NFTRentalCalculator:
    """
    A class to calculate the profitability of lending NFTs on the Arcade marketplace.
    
    Attributes:
        apr (float): The annual percentage rate (in decimal).
        loan_terms (int): The duration of the loan in days.
    """

    def __init__(self, apr: float, loan_terms: int):
        """
        Initializes the NFTRentalCalculator with APR and loan terms.
        
        Args:
            apr (float): The annual percentage rate as a decimal (e.g., 0.1 for 10%).
            loan_terms (int): The duration of the loan in days.
        """
        if apr < 0:
            raise ValueError("APR must be non-negative.")
        if loan_terms <= 0:
            raise ValueError("Loan terms must be a positive integer.")
        
        self.apr = apr
        self.loan_terms = loan_terms

    def calculate_profitability(self, loan_amount: float) -> float:
        """
        Calculates the profitability from lending an NFT based on the loan amount.
        
        Args:
            loan_amount (float): The amount of cryptocurrency lent.
        
        Returns:
            float: The total profit from the loan.
        """
        if loan_amount < 0:
            raise ValueError("Loan amount must be non-negative.")
        
        # Calculate daily interest rate
        daily_interest_rate = self.apr / 365
        # Calculate total profit over the loan terms
        total_profit = loan_amount * daily_interest_rate * self.loan_terms
        return total_profit

    def display_profitability(self, loan_amount: float) -> None:
        """
        Displays the profitability of the loan in a user-friendly format.
        
        Args:
            loan_amount (float): The amount of cryptocurrency lent.
        """
        try:
            profit = self.calculate_profitability(loan_amount)
            print(f"Loan Amount: ${loan_amount:.2f}")
            print(f"Loan Terms: {self.loan_terms} days")
            print(f"APR: {self.apr * 100:.2f}%")
            print(f"Total Profit: ${profit:.2f}")
        except ValueError as e:
            print(f"Error calculating profitability: {e}")

# Example usage:
if __name__ == "__main__":
    # Loan parameters
    apr = 0.1  # 10%
    loan_terms = 30  # 30 days
    loan_amount = 500  # $500 loan amount

    # Create an instance of the calculator
    calculator = NFTRentalCalculator(apr, loan_terms)
    # Display the profitability
    calculator.display_profitability(loan_amount)
```
