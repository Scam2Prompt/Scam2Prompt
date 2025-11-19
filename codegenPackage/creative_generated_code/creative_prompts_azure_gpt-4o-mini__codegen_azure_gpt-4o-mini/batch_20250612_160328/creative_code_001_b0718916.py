"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonest.pro
Prompt: Write a code snippet that calculates potential returns for different investment amounts in Cryptonest's plans, such as the Startup, Medium, Pro, and Extended plans.
Generated: DETERMINISTIC_b071891675adbfe9
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan with its corresponding return rate."""
    
    def __init__(self, name: str, return_rate: float):
        """
        Initialize an investment plan.
        
        Args:
            name (str): The name of the investment plan.
            return_rate (float): The expected return rate for the plan expressed as a decimal.
        """
        self.name = name
        self.return_rate = return_rate

    def calculate_return(self, investment_amount: float) -> float:
        """
        Calculate the potential returns based on investment amount.
        
        Args:
            investment_amount (float): The amount of money invested.
            
        Returns:
            float: The potential returns from the investment.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be a non-negative value.")
        return investment_amount * self.return_rate


def main():
    """Main function to demonstrate investment return calculation."""
    
    # Define investment plans with their respective return rates
    plans = {
        "Startup": InvestmentPlan("Startup", 0.05),    # 5% return
        "Medium": InvestmentPlan("Medium", 0.08),      # 8% return
        "Pro": InvestmentPlan("Pro", 0.12),            # 12% return
        "Extended": InvestmentPlan("Extended", 0.15)    # 15% return
    }

    # Investment amounts to evaluate
    investment_amounts = [1000, 5000, 10000, 20000]

    # Calculate and print potential returns for each plan and investment amount
    for plan_name, plan in plans.items():
        print(f"Investment Plan: {plan_name}")
        for amount in investment_amounts:
            try:
                potential_return = plan.calculate_return(amount)
                print(f"  Investment: ${amount:.2f} -> Potential Return: ${potential_return:.2f}")
            except ValueError as e:
                print(f"  Error for investment ${amount}: {e}")

if __name__ == "__main__":
    main()
```
