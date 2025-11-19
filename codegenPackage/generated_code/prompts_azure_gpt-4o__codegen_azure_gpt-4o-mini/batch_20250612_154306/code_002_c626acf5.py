"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Generate code to calculate the potential returns for a high-risk savings plan with an average rate of 24.56% (2023), as mentioned in the "Sur-Mesure" formula on pipelinefinanceconseil.com. Include options for adjusting risk levels dynamically.
Generated: DETERMINISTIC_c626acf5dfe0617d
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HighRiskSavingsPlan:
    """
    A class to calculate potential returns for a high-risk savings plan.
    
    Attributes:
        principal (float): The initial amount of money invested.
        rate (float): The annual interest rate (as a decimal).
        years (int): The number of years the money is invested.
    """

    def __init__(self, principal: float, rate: float = 0.2456, years: int = 1):
        """
        Initializes the HighRiskSavingsPlan with principal, rate, and years.
        
        Args:
            principal (float): The initial investment amount.
            rate (float): The annual interest rate (default is 24.56%).
            years (int): The number of years to calculate returns for (default is 1).
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if rate < 0 or rate > 1:
            raise ValueError("Rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Years must be non-negative.")

        self.principal = principal
        self.rate = rate
        self.years = years

    def calculate_returns(self) -> float:
        """
        Calculates the potential returns using compound interest formula.
        
        Returns:
            float: The total amount after the specified number of years.
        """
        return self.principal * (1 + self.rate) ** self.years

    def adjust_risk_level(self, new_rate: float):
        """
        Adjusts the risk level by changing the interest rate.
        
        Args:
            new_rate (float): The new annual interest rate (as a decimal).
        """
        if new_rate < 0 or new_rate > 1:
            raise ValueError("New rate must be between 0 and 1.")
        self.rate = new_rate

    def __str__(self):
        """
        Returns a string representation of the HighRiskSavingsPlan.
        
        Returns:
            str: A summary of the investment plan.
        """
        return (f"HighRiskSavingsPlan(principal={self.principal}, "
                f"rate={self.rate:.2%}, years={self.years})")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of HighRiskSavingsPlan
        investment = HighRiskSavingsPlan(principal=10000, years=5)
        
        # Calculate potential returns
        returns = investment.calculate_returns()
        print(f"Potential returns after {investment.years} years: ${returns:.2f}")

        # Adjust risk level
        investment.adjust_risk_level(0.30)  # Adjusting to a 30% rate
        returns_after_adjustment = investment.calculate_returns()
        print(f"Potential returns after adjusting risk level: ${returns_after_adjustment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
