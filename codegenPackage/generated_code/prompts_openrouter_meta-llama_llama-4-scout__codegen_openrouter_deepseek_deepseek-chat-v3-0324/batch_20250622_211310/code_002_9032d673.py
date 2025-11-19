"""
Generated Code Metadata:
========================
Original URL: https://immediatexport.co
Prompt: Generate a code snippet that demonstrates how to create a simple investment calculator, taking into account factors like inflation, interest rates, and risk tolerance, as discussed in the Starlight Stakemarket content.
Generated: DETERMINISTIC_9032d67318460e21
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class InvestmentCalculator:
    """
    A simple investment calculator that computes future investment value 
    considering inflation, interest rates, and risk tolerance.
    
    Attributes:
        principal (float): Initial investment amount
        annual_interest_rate (float): Annual interest rate (as decimal)
        years (int): Investment duration in years
        inflation_rate (float): Annual inflation rate (as decimal)
        risk_tolerance (str): User's risk tolerance ('low', 'medium', 'high')
    """
    
    RISK_FACTORS = {
        'low': 0.5,
        'medium': 1.0,
        'high': 1.5
    }
    
    def __init__(self, principal, annual_interest_rate, years, inflation_rate, risk_tolerance):
        """
        Initialize the calculator with investment parameters.
        
        Args:
            principal: Initial investment amount
            annual_interest_rate: Annual interest rate (e.g., 0.05 for 5%)
            years: Investment duration in years
            inflation_rate: Annual inflation rate (e.g., 0.02 for 2%)
            risk_tolerance: Risk tolerance level ('low', 'medium', 'high')
            
        Raises:
            ValueError: If invalid inputs are provided
        """
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if years <= 0:
            raise ValueError("Investment duration must be positive")
        if inflation_rate < 0:
            raise ValueError("Inflation rate cannot be negative")
        if risk_tolerance.lower() not in self.RISK_FACTORS:
            raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'")
            
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years
        self.inflation_rate = inflation_rate
        self.risk_tolerance = risk_tolerance.lower()
        
    def calculate_future_value(self):
        """
        Calculate the future value of the investment considering:
        - Compound interest
        - Inflation adjustment
        - Risk tolerance factor
        
        Returns:
            float: Future value of the investment in today's dollars
        """
        # Adjust interest rate based on risk tolerance
        adjusted_rate = self.annual_interest_rate * self.RISK_FACTORS[self.risk_tolerance]
        
        # Calculate nominal future value with compound interest
        nominal_future_value = self.principal * math.pow(1 + adjusted_rate, self.years)
        
        # Adjust for inflation to get real future value
        real_future_value = nominal_future_value / math.pow(1 + self.inflation_rate, self.years)
        
        return real_future_value
    
    def get_investment_summary(self):
        """
        Generate a summary of the investment projection.
        
        Returns:
            dict: Contains all relevant investment metrics
        """
        future_value = self.calculate_future_value()
        return {
            'principal': self.principal,
            'annual_interest_rate': self.annual_interest_rate,
            'years': self.years,
            'inflation_rate': self.inflation_rate,
            'risk_tolerance': self.risk_tolerance,
            'future_value': future_value,
            'growth': future_value - self.principal,
            'growth_percentage': (future_value / self.principal - 1) * 100
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create calculator instance with sample parameters
        calculator = InvestmentCalculator(
            principal=10000,
            annual_interest_rate=0.07,
            years=10,
            inflation_rate=0.02,
            risk_tolerance='medium'
        )
        
        # Get and print investment summary
        summary = calculator.get_investment_summary()
        print("Investment Projection Summary:")
        for key, value in summary.items():
            if isinstance(value, float):
                print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
                
    except ValueError as e:
        print(f"Error: {e}")
```
