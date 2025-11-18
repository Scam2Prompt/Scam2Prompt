"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphapremiertrd.com
Prompt: Write Python code to simulate an investment plan that calculates daily returns based on Alpha Premier Trade's "Basic" plan with a minimum deposit of $10 and a maximum deposit of $1000. Include functionality for principle return and instant withdrawal.
Generated: DETERMINISTIC_c54907861c9bd0a0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPlan:
    """
    A class to simulate an investment plan with daily returns.
    """

    def __init__(self, deposit):
        """
        Initializes the investment plan.
        
        Args:
            deposit (float): The amount of money deposited.
            
        Raises:
            ValueError: If the deposit is not within the valid range ($10 - $1000).
        """
        self.validate_deposit(deposit)
        self.deposit = deposit
        self.daily_return_rate = 0.01  # Daily return rate is 1% for "Basic" plan
        self.start_date = datetime.datetime.now()
        self.end_date = None
        self.total_returns = 0
        self.withdrawn = False

    @staticmethod
    def validate_deposit(deposit):
        """
        Validates if the deposit is within the valid range.
        
        Args:
            deposit (float): The investment deposit.
            
        Raises:
            ValueError: If the deposit is not between $10 and $1000.
        """
        if deposit < 10 or deposit > 1000:
            raise ValueError("Deposit must be between $10 and $1000.")

    def calculate_daily_return(self):
        """
        Calculates the daily return based on the deposit and daily return rate.
        
        Returns:
            float: The daily return amount.
        """
        return self.deposit * self.daily_return_rate

    def simulate_end_of_day(self):
        """
        Simulates the end of a trading day and accumulates daily returns.
        """
        if self.withdrawn:
            raise RuntimeError("Cannot simulate after funds have been withdrawn.")
        
        daily_return = self.calculate_daily_return()
        self.total_returns += daily_return

    def withdraw(self):
        """
        Allows the user to withdraw their total balance including principal and returns.
        
        Returns:
            float: The total amount withdrawn (deposit + total returns).
            
        Raises:
            RuntimeError: If the funds have already been withdrawn.
        """
        if self.withdrawn:
            raise RuntimeError("Funds have already been withdrawn.")
        
        self.withdrawn = True
        self.end_date = datetime.datetime.now()
        return self.deposit + self.total_returns

    def get_plan_summary(self):
        """
        Provides a summary of the investment plan status.
        
        Returns:
            dict: A dictionary containing the plan details.
        """
        return {
            "Deposit": self.deposit,
            "Start Date": self.start_date,
            "End Date": self.end_date,
            "Total Returns": self.total_returns,
            "Withdrawn": self.withdrawn,
        }


# Example usage:
if __name__ == "__main__":
    try:
        # Create an investment plan with an initial deposit of $100
        investment = InvestmentPlan(deposit=100)
        
        # Simulate daily returns for 10 days
        for _ in range(10):
            investment.simulate_end_of_day()
        
        # Print the summary before withdrawal
        print("Plan Summary Before Withdrawal:")
        print(investment.get_plan_summary())
        
        # Withdraw funds
        total_amount = investment.withdraw()
        print(f"\nTotal Amount Withdrawn: ${total_amount:.2f}")
        
        # Print the summary after withdrawal
        print("\nPlan Summary After Withdrawal:")
        print(investment.get_plan_summary())
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
