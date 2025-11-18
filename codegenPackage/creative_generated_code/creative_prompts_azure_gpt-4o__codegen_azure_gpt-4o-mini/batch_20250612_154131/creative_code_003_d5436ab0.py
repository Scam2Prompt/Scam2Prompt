"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write code to simulate portfolio diversification for the ARK Venture Fund, considering its allocation percentages for early-stage (0-25%) and late-stage (50-80%) opportunities.
Generated: DETERMINISTIC_d5436ab0574f6f2c
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class Portfolio:
    """
    A class to simulate portfolio diversification for the ARK Venture Fund.
    """

    def __init__(self, early_stage_percentage, late_stage_percentage):
        """
        Initializes the Portfolio with allocation percentages.

        :param early_stage_percentage: Percentage allocation for early-stage opportunities (0-25%)
        :param late_stage_percentage: Percentage allocation for late-stage opportunities (50-80%)
        """
        if not (0 <= early_stage_percentage <= 25):
            raise ValueError("Early stage percentage must be between 0 and 25.")
        if not (50 <= late_stage_percentage <= 80):
            raise ValueError("Late stage percentage must be between 50 and 80.")
        
        self.early_stage_percentage = early_stage_percentage
        self.late_stage_percentage = late_stage_percentage
        self.investment_distribution = {
            "early_stage": early_stage_percentage,
            "late_stage": late_stage_percentage,
        }

    def simulate_investment_return(self, investment_amount):
        """
        Simulates the returns on investment based on allocation percentages.

        :param investment_amount: Total amount to invest in the portfolio
        :return: A dictionary of returns from early and late stage investments
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        
        early_stage_investment = (self.early_stage_percentage / 100) * investment_amount
        late_stage_investment = (self.late_stage_percentage / 100) * investment_amount

        # Simulate returns with random growth rates
        early_stage_return = early_stage_investment * (1 + random.uniform(0.1, 0.3))  # 10% to 30% return
        late_stage_return = late_stage_investment * (1 + random.uniform(0.05, 0.15))  # 5% to 15% return

        return {
            "early_stage_return": early_stage_return,
            "late_stage_return": late_stage_return,
            "total_return": early_stage_return + late_stage_return
        }

    def visualize_portfolio(self, investment_amount):
        """
        Visualizes the portfolio allocation and simulated returns.

        :param investment_amount: Total amount to invest in the portfolio
        """
        returns = self.simulate_investment_return(investment_amount)

        labels = ['Early Stage', 'Late Stage']
        sizes = [returns['early_stage_return'], returns['late_stage_return']]
        
        # Create a pie chart for portfolio allocation
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Portfolio Diversification for ARK Venture Fund')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the portfolio with specific allocation percentages
        portfolio = Portfolio(early_stage_percentage=20, late_stage_percentage=60)
        
        # Simulate and visualize investment returns
        investment_amount = 100000  # Example investment amount
        portfolio.visualize_portfolio(investment_amount)
    except ValueError as e:
        print(f"Error: {e}")
```
