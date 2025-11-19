"""
Generated Code Metadata:
========================
Original URL: https://leaconcapitalltd.com
Prompt: Write a Python code snippet to implement a simple cryptocurrency investment plan with daily returns, similar to Leacon Capital Ltd's 1.5% daily return plan for 7 days.
Generated: DETERMINISTIC_bbcc91a8e12ce71d
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from decimal import Decimal, getcontext

class InvestmentPlan:
    """
    A simple cryptocurrency investment plan calculator with daily returns.
    """
    
    def __init__(self, principal: float, daily_return_rate: float, investment_days: int):
        """
        Initialize the investment plan with principal amount, daily return rate, and duration.
        
        Args:
            principal: Initial investment amount
            daily_return_rate: Daily return rate as a percentage (e.g., 1.5 for 1.5%)
            investment_days: Number of days for the investment
        """
        getcontext().prec = 6  # Set precision for Decimal operations
        self.principal = Decimal(str(principal))
        self.daily_return_rate = Decimal(str(daily_return_rate)) / Decimal('100')
        self.investment_days = investment_days
        self.start_date = datetime.date.today()
        
    def calculate_returns(self) -> dict:
        """
        Calculate daily returns and total return for the investment period.
        
        Returns:
            A dictionary containing:
            - 'daily_returns': List of daily balances
            - 'total_return': Final balance after investment period
            - 'profit': Total profit earned
            - 'start_date': Investment start date
            - 'end_date': Investment end date
        """
        try:
            if self.principal <= 0:
                raise ValueError("Principal must be greater than 0")
            if self.daily_return_rate <= 0:
                raise ValueError("Daily return rate must be greater than 0")
            if self.investment_days <= 0:
                raise ValueError("Investment days must be greater than 0")
                
            daily_returns = []
            current_balance = self.principal
            
            for day in range(1, self.investment_days + 1):
                daily_return = current_balance * self.daily_return_rate
                current_balance += daily_return
                daily_returns.append(float(current_balance))
                
            end_date = self.start_date + datetime.timedelta(days=self.investment_days)
            
            return {
                'daily_returns': daily_returns,
                'total_return': float(current_balance),
                'profit': float(current_balance - self.principal),
                'start_date': self.start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d')
            }
            
        except Exception as e:
            print(f"Error calculating returns: {str(e)}")
            return None

def main():
    """
    Example usage of the InvestmentPlan class with Leacon Capital Ltd's parameters.
    """
    try:
        # Example: $1000 investment at 1.5% daily return for 7 days
        investment = InvestmentPlan(
            principal=1000.0,
            daily_return_rate=1.5,
            investment_days=7
        )
        
        results = investment.calculate_returns()
        
        if results:
            print("\nInvestment Plan Results:")
            print(f"Principal: ${investment.principal:,.2f}")
            print(f"Daily Return Rate: {investment.daily_return_rate * 100}%")
            print(f"Investment Period: {investment.investment_days} days")
            print(f"Start Date: {results['start_date']}")
            print(f"End Date: {results['end_date']}")
            print("\nDaily Returns:")
            for day, balance in enumerate(results['daily_returns'], 1):
                print(f"Day {day}: ${balance:,.2f}")
            print(f"\nTotal Return: ${results['total_return']:,.2f}")
            print(f"Total Profit: ${results['profit']:,.2f}")
            
    except Exception as e:
        print(f"Error in investment plan: {str(e)}")

if __name__ == "__main__":
    main()
```
