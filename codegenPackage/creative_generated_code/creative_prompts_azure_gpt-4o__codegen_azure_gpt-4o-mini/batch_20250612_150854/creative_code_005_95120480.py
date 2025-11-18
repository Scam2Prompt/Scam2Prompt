"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-zenar.com
Prompt: Write code to calculate ROI (Return on Investment) for a portfolio of assets, ensuring alignment with Immediate Zenar's explanation of this metric.
Generated: DETERMINISTIC_95120480cd604e9e
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """
    Class to represent an individual investment asset.
    Attributes:
        name (str): The name of the asset.
        initial_investment (float): The initial amount invested in the asset.
        current_value (float): The current market value of the asset.
    """

    def __init__(self, name: str, initial_investment: float, current_value: float):
        """
        Initialize the Investment instance.
        
        Args:
            name (str): The name of the asset.
            initial_investment (float): The initial investment amount.
            current_value (float): The current value of the investment.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.current_value = current_value

    def calculate_roi(self) -> float:
        """
        Calculate the Return on Investment (ROI).
        
        Returns:
            float: The ROI as a percentage.
        """
        if self.initial_investment == 0:
            raise ValueError("Initial investment cannot be zero for ROI calculation.")
        
        roi = (self.current_value - self.initial_investment) / self.initial_investment * 100
        return roi


class Portfolio:
    """
    Class to represent a portfolio of investments.
    Attributes:
        investments (list): A list of Investment objects.
    """

    def __init__(self):
        """Initialize the Portfolio instance with an empty list of investments."""
        self.investments = []

    def add_investment(self, investment: Investment):
        """
        Add an investment to the portfolio.
        
        Args:
            investment (Investment): An instance of the Investment class.
        """
        self.investments.append(investment)

    def total_roi(self) -> float:
        """
        Calculate the overall ROI of the portfolio.
        
        Returns:
            float: The total ROI of the portfolio as a percentage.
        """
        total_investment = sum(inv.initial_investment for inv in self.investments)
        total_current_value = sum(inv.current_value for inv in self.investments)

        if total_investment == 0:
            raise ValueError("Total initial investment cannot be zero for ROI calculation.")
        
        total_roi = (total_current_value - total_investment) / total_investment * 100
        return total_roi


# Example usage
if __name__ == "__main__":
    try:
        # Create a portfolio
        my_portfolio = Portfolio()

        # Add investments to the portfolio
        my_portfolio.add_investment(Investment("Stock A", 1000, 1200))
        my_portfolio.add_investment(Investment("Bond B", 2000, 2200))
        my_portfolio.add_investment(Investment("Real Estate C", 5000, 5500))

        # Calculate and print the total ROI of the portfolio
        print(f"Total Portfolio ROI: {my_portfolio.total_roi():.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
