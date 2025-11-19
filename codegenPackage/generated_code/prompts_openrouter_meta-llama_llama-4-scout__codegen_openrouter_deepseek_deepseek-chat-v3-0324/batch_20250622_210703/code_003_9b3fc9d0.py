"""
Generated Code Metadata:
========================
Original URL: https://wrapstickfoods.com
Prompt: Develop a code snippet to calculate the Return on Investment (ROI) for a Wrapstick Foods franchise, considering factors like initial investment, revenue, and profit margins.
Generated: DETERMINISTIC_9b3fc9d01cc8f386
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ROI_Calculator:
    """
    A class to calculate Return on Investment (ROI) for a Wrapstick Foods franchise.
    Takes into account initial investment, revenue, and profit margins.
    """
    
    def __init__(self):
        """
        Initialize the ROI calculator with default values.
        """
        self.initial_investment = 0.0
        self.annual_revenue = 0.0
        self.profit_margin = 0.0  # as a decimal (e.g., 0.15 for 15%)
        self.time_period = 1  # in years
    
    def set_parameters(self, initial_investment: float, annual_revenue: float, 
                       profit_margin: float, time_period: int = 1) -> None:
        """
        Set the calculation parameters.
        
        Args:
            initial_investment (float): Initial franchise investment cost
            annual_revenue (float): Expected annual revenue
            profit_margin (float): Profit margin as decimal (0.0-1.0)
            time_period (int, optional): Time period in years. Defaults to 1.
        
        Raises:
            ValueError: If any parameter is invalid
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive")
        if annual_revenue < 0:
            raise ValueError("Annual revenue cannot be negative")
        if not 0 <= profit_margin <= 1:
            raise ValueError("Profit margin must be between 0 and 1")
        if time_period <= 0:
            raise ValueError("Time period must be at least 1 year")
            
        self.initial_investment = initial_investment
        self.annual_revenue = annual_revenue
        self.profit_margin = profit_margin
        self.time_period = time_period
    
    def calculate_net_profit(self) -> float:
        """
        Calculate total net profit over the time period.
        
        Returns:
            float: Total net profit
        """
        return self.annual_revenue * self.profit_margin * self.time_period
    
    def calculate_roi(self) -> float:
        """
        Calculate ROI as a percentage.
        
        Returns:
            float: ROI percentage (e.g., 15.5 for 15.5%)
        
        Raises:
            ZeroDivisionError: If initial investment is zero
        """
        net_profit = self.calculate_net_profit()
        return (net_profit / self.initial_investment) * 100
    
    def calculate_break_even(self) -> float:
        """
        Calculate break-even point in years.
        
        Returns:
            float: Years to break even
        """
        annual_net = self.annual_revenue * self.profit_margin
        if annual_net <= 0:
            return float('inf')  # Never breaks even
        return self.initial_investment / annual_net


# Example usage
if __name__ == "__main__":
    try:
        calculator = ROI_Calculator()
        calculator.set_parameters(
            initial_investment=250000,
            annual_revenue=500000,
            profit_margin=0.20,
            time_period=3
        )
        
        print(f"Net Profit: ${calculator.calculate_net_profit():,.2f}")
        print(f"ROI: {calculator.calculate_roi():.2f}%")
        print(f"Break-even: {calculator.calculate_break_even():.2f} years")
        
    except ValueError as e:
        print(f"Error in input parameters: {e}")
    except ZeroDivisionError:
        print("Error: Cannot calculate ROI with zero initial investment")
```
