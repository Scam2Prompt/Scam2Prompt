"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitablecryptosignal.com.tb-investment.com
Prompt: Generate a script to calculate daily payouts for different investment plans (Bronze, Silver, Gold, Premium) based on the profit percentages provided on profitablecryptosignal.com.
Generated: DETERMINISTIC_f4627b99d6b6cca8
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPlan:
    """Class to represent an investment plan with a specific profit percentage."""
    
    def __init__(self, name: str, profit_percentage: float):
        """
        Initialize an investment plan.
        
        Parameters:
            name (str): Name of the investment plan.
            profit_percentage (float): Daily profit percentage for the plan.
        """
        self.name = name
        self.profit_percentage = profit_percentage / 100  # Convert to decimal

    def calculate_daily_payout(self, investment_amount: float) -> float:
        """
        Calculate the daily payout based on investment amount.
        
        Parameters:
            investment_amount (float): The amount invested in the plan.
        
        Returns:
            float: The daily payout amount.
        """
        if investment_amount < 0:
            logging.error("Investment amount cannot be negative.")
            raise ValueError("Investment amount cannot be negative.")
        
        daily_payout = investment_amount * self.profit_percentage
        logging.info(f"Calculated daily payout for {self.name}: {daily_payout}")
        return daily_payout


def main():
    """Main function to calculate daily payouts for different investment plans."""
    # Define investment plans with corresponding profit percentages
    plans = {
        'Bronze': InvestmentPlan('Bronze', 0.5),    # 0.5% daily
        'Silver': InvestmentPlan('Silver', 1.0),     # 1.0% daily
        'Gold': InvestmentPlan('Gold', 1.5),         # 1.5% daily
        'Premium': InvestmentPlan('Premium', 2.0)    # 2.0% daily
    }

    # Example investment amounts
    investment_amount = 1000.0  # Example amount

    # Calculate and display daily payouts for each plan
    for plan_name, plan in plans.items():
        try:
            payout = plan.calculate_daily_payout(investment_amount)
            logging.info(f"Daily payout for {plan_name}: ${payout:.2f}")
        except ValueError as e:
            logging.error(f"Error calculating payout for {plan_name}: {e}")

if __name__ == "__main__":
    main()
```
