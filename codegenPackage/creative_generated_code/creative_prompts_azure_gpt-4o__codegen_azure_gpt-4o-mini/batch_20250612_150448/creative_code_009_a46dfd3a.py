"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-venus-protocol.vercel.app
Prompt: Generate code to simulate borrowing scenarios on Venus Protocol, including varying collateral and interest rate conditions.
Generated: DETERMINISTIC_a46dfd3acc8128f4
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for simulation
import random

class BorrowingScenario:
    """
    A class to simulate borrowing scenarios on the Venus Protocol.
    
    Attributes:
        collateral (float): The amount of collateral provided.
        interest_rate (float): The interest rate for the borrowing.
        loan_amount (float): The amount of loan taken.
        duration (int): Duration for which the loan is taken, in days.
    """

    def __init__(self, collateral: float, interest_rate: float, loan_amount: float, duration: int):
        """
        Initializes the BorrowingScenario with the given parameters.
        
        Args:
            collateral (float): The amount of collateral.
            interest_rate (float): The interest rate for the loan.
            loan_amount (float): The amount of loan.
            duration (int): Duration for the loan in days.
        """
        self.collateral = collateral
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.duration = duration

    def calculate_total_repayment(self) -> float:
        """
        Calculates the total repayment amount including interest.

        Returns:
            float: Total repayment amount.
        """
        try:
            total_repayment = self.loan_amount * (1 + self.interest_rate / 100) ** (self.duration / 365)
            return total_repayment
        except Exception as e:
            raise RuntimeError(f"Error calculating total repayment: {str(e)}")

    def evaluate_scenario(self) -> None:
        """
        Evaluates the borrowing scenario and prints the results.
        """
        try:
            total_repayment = self.calculate_total_repayment()
            print(f"Borrowing Scenario Evaluation:")
            print(f"Collateral: {self.collateral}")
            print(f"Loan Amount: {self.loan_amount}")
            print(f"Interest Rate: {self.interest_rate}%")
            print(f"Duration: {self.duration} days")
            print(f"Total Repayment Amount: {total_repayment:.2f}")
            print(f"Collateral to Loan Ratio: {self.collateral / self.loan_amount:.2f}")
        except RuntimeError as e:
            print(e)

def simulate_borrowing_scenarios():
    """
    Simulates various borrowing scenarios with random parameters.
    """
    try:
        # Simulate 5 borrowing scenarios
        for _ in range(5):
            collateral = round(random.uniform(1000, 5000), 2)  # Random collateral between $1,000 and $5,000
            interest_rate = round(random.uniform(3, 15), 2)     # Random interest rate between 3% and 15%
            loan_amount = round(random.uniform(500, 2500), 2)   # Random loan amount between $500 and $2,500
            duration = random.randint(30, 365)                  # Random duration between 30 and 365 days
            
            scenario = BorrowingScenario(collateral, interest_rate, loan_amount, duration)
            scenario.evaluate_scenario()
            print("-" * 60)  # Separator for clarity
    except Exception as e:
        print(f"Error during simulation: {str(e)}")

if __name__ == "__main__":
    # Run the simulation of borrowing scenarios
    simulate_borrowing_scenarios()
```
