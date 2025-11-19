"""
Generated Code Metadata:
========================
Original URL: https://tradezeenetwork.com
Prompt: Generate a sample investment plan with a 25% return after 20 hours, with a minimum deposit of $500 and a maximum deposit of $999, similar to the STARTER plan offered by Tradezeenetwork.
Generated: DETERMINISTIC_846bdf5c5a263fef
Batch ID: 20250622_205436
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
    Represents an investment plan with specific parameters.
    """
    
    def __init__(self, name: str, min_deposit: float, max_deposit: float, 
                 duration_hours: int, return_percentage: float):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the investment plan
            min_deposit: Minimum deposit amount
            max_deposit: Maximum deposit amount
            duration_hours: Duration in hours
            return_percentage: Expected return percentage
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.duration_hours = duration_hours
        self.return_percentage = return_percentage
    
    def calculate_return(self, amount: float) -> float:
        """
        Calculate the expected return for a given investment amount.
        
        Args:
            amount: Investment amount
            
        Returns:
            Expected return amount
            
        Raises:
            ValueError: If amount is outside min/max range
        """
        if amount < self.min_deposit or amount > self.max_deposit:
            raise ValueError(f"Amount must be between {self.min_deposit} and {self.max_deposit}")
        
        return amount * (1 + self.return_percentage / 100)
    
    def get_details(self) -> dict:
        """
        Return plan details as a dictionary.
        
        Returns:
            Dictionary containing all plan details
        """
        return {
            "name": self.name,
            "min_deposit": self.min_deposit,
            "max_deposit": self.max_deposit,
            "duration_hours": self.duration_hours,
            "return_percentage": self.return_percentage
        }


def create_starter_plan() -> InvestmentPlan:
    """
    Create and return a STARTER investment plan with:
    - 25% return
    - 20 hours duration
    - $500 minimum deposit
    - $999 maximum deposit
    """
    return InvestmentPlan(
        name="STARTER",
        min_deposit=500.0,
        max_deposit=999.0,
        duration_hours=20,
        return_percentage=25.0
    )


# Example usage
if __name__ == "__main__":
    try:
        plan = create_starter_plan()
        print("Investment Plan Details:")
        for key, value in plan.get_details().items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        investment_amount = 750.0
        print(f"\nFor ${investment_amount} investment:")
        print(f"Expected return after {plan.duration_hours} hours: ${plan.calculate_return(investment_amount):.2f}")
        
    except Exception as e:
        print(f"Error: {e}")
```
