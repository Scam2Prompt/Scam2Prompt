"""
Generated Code Metadata:
========================
Original URL: https://accesslinklimited.com
Prompt: Write code to simulate the investment process, including plan selection, deposit tracking, and interest accumulation, as described on Access Link Limited's platform.
Generated: DETERMINISTIC_f3fdb92911974a4e
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    Class to represent an investment plan.
    Attributes:
        name (str): The name of the investment plan.
        interest_rate (float): The annual interest rate of the plan.
        duration_years (int): The duration of the investment in years.
    """

    def __init__(self, name: str, interest_rate: float, duration_years: int):
        self.name = name
        self.interest_rate = interest_rate
        self.duration_years = duration_years

    def calculate_interest(self, principal: float) -> float:
        """
        Calculate the total interest earned over the investment duration.
        
        Args:
            principal (float): The initial amount of money invested.
        
        Returns:
            float: The total interest earned.
        """
        return principal * (self.interest_rate / 100) * self.duration_years


class InvestmentAccount:
    """
    Class to represent an investment account.
    Attributes:
        plan (InvestmentPlan): The investment plan selected.
        principal (float): The initial amount of money deposited.
    """

    def __init__(self, plan: InvestmentPlan, principal: float):
        self.plan = plan
        self.principal = principal

    def deposit(self, amount: float):
        """
        Deposit an additional amount into the investment account.
        
        Args:
            amount (float): The amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.principal += amount

    def total_value(self) -> float:
        """
        Calculate the total value of the investment account after interest.
        
        Returns:
            float: The total value including principal and interest.
        """
        interest = self.plan.calculate_interest(self.principal)
        return self.principal + interest


def main():
    """
    Main function to simulate the investment process.
    """
    try:
        # Define investment plans
        plan1 = InvestmentPlan("Growth Plan", 5.0, 10)
        plan2 = InvestmentPlan("Conservative Plan", 3.0, 5)

        # User selects a plan
        selected_plan = plan1  # Example selection

        # User makes an initial deposit
        initial_deposit = 10000.0  # Example initial deposit
        account = InvestmentAccount(selected_plan, initial_deposit)

        # User makes additional deposits
        account.deposit(5000.0)  # Example additional deposit

        # Calculate total value after interest
        total_investment_value = account.total_value()
        print(f"Total investment value after {selected_plan.duration_years} years: ${total_investment_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
