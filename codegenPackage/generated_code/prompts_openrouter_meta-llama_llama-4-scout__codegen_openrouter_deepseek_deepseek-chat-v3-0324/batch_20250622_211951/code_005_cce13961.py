"""
Generated Code Metadata:
========================
Original URL: https://megapromining.live
Prompt: Develop a basic investment plan algorithm that could be used on a platform like Megapromining, taking into account daily payouts and profit percentages.
Generated: DETERMINISTIC_cce1396165d47ded
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, Optional, Union
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InvestmentPlan:
    """
    A class representing an investment plan with daily payouts and profit calculations.
    """
    
    def __init__(
        self,
        initial_investment: float,
        daily_profit_percent: float,
        duration_days: int,
        payout_frequency_days: int = 1
    ):
        """
        Initialize the investment plan.
        
        Args:
            initial_investment: Initial investment amount in USD
            daily_profit_percent: Daily profit percentage (e.g., 1.5 for 1.5%)
            duration_days: Total duration of the investment in days
            payout_frequency_days: Frequency of payouts in days (default: daily)
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive")
        if daily_profit_percent <= 0:
            raise ValueError("Daily profit percentage must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        if payout_frequency_days <= 0:
            raise ValueError("Payout frequency must be positive")
            
        self.initial_investment = initial_investment
        self.daily_profit_percent = daily_profit_percent
        self.duration_days = duration_days
        self.payout_frequency_days = payout_frequency_days
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration_days)
        
    def calculate_projection(self) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate the investment projection with daily payouts.
        
        Returns:
            Dictionary containing:
                - total_invested: Total amount invested
                - total_profit: Total profit earned
                - total_payouts: Sum of all payouts
                - final_balance: Final balance after all payouts
                - payouts: Dictionary of payout dates and amounts
        """
        try:
            current_balance = self.initial_investment
            total_profit = 0.0
            payouts = {}
            
            for day in range(1, self.duration_days + 1):
                # Calculate daily profit
                daily_profit = current_balance * (self.daily_profit_percent / 100)
                total_profit += daily_profit
                
                # Update balance with compounded profit
                current_balance += daily_profit
                
                # Process payout if it's a payout day
                if day % self.payout_frequency_days == 0:
                    payout_date = self.start_date + timedelta(days=day)
                    payout_amount = daily_profit * self.payout_frequency_days
                    payouts[payout_date.strftime("%Y-%m-%d")] = round(payout_amount, 2)
                    current_balance -= payout_amount
            
            return {
                "total_invested": round(self.initial_investment, 2),
                "total_profit": round(total_profit, 2),
                "total_payouts": round(sum(payouts.values()), 2),
                "final_balance": round(current_balance, 2),
                "payouts": payouts
            }
            
        except Exception as e:
            logger.error(f"Error calculating projection: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Create an investment plan with $1000, 1.5% daily profit for 30 days
        plan = InvestmentPlan(
            initial_investment=1000.0,
            daily_profit_percent=1.5,
            duration_days=30
        )
        
        # Calculate and print the projection
        projection = plan.calculate_projection()
        print("Investment Projection:")
        print(f"Total Invested: ${projection['total_invested']}")
        print(f"Total Profit: ${projection['total_profit']}")
        print(f"Total Payouts: ${projection['total_payouts']}")
        print(f"Final Balance: ${projection['final_balance']}")
        print("\nPayout Schedule:")
        for date, amount in projection['payouts'].items():
            print(f"{date}: ${amount}")
            
    except ValueError as ve:
        logger.error(f"Invalid input: {ve}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
```
