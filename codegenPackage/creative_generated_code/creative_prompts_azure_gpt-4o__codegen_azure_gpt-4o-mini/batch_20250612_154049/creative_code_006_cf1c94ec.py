"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guapzenith.com
Prompt: Create a recurring deposit system for cryptocurrency investments that aligns with the features described on guapzenith.com.
Generated: DETERMINISTIC_cf1c94ecaccbf09a
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Investment:
    """Represents an investment in a recurring deposit for cryptocurrency."""
    
    def __init__(self, amount: float, frequency_days: int):
        self.amount = amount
        self.frequency_days = frequency_days
        self.start_date = datetime.datetime.now()
        self.investments: List[datetime.datetime] = []
    
    def add_investment(self):
        """Adds a new investment to the current date, based on the frequency."""
        self.investments.append(datetime.datetime.now())
    
    def get_next_investment_date(self) -> datetime.datetime:
        """Calculates the next investment date based on the last investment made."""
        if not self.investments:
            return self.start_date
        else:
            return self.investments[-1] + datetime.timedelta(days=self.frequency_days)

    def get_investment_schedule(self, total_months: int) -> List[datetime.datetime]:
        """Generates a schedule of future investment dates for a given number of months."""
        schedule = []
        for month in range(total_months):
            next_investment_date = self.get_next_investment_date()
            while next_investment_date < (self.start_date + datetime.timedelta(days=30 * month)):
                schedule.append(next_investment_date)
                next_investment_date += datetime.timedelta(days=self.frequency_days)
        return schedule


class RecurringDepositSystem:
    """Handles the recurring deposit system for cryptocurrency investments."""
    
    def __init__(self):
        self.investments = []
    
    def create_investment(self, amount: float, frequency_days: int) -> Investment:
        """Creates a new investment and adds it to the system."""
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if frequency_days <= 0:
            raise ValueError("Frequency in days must be greater than zero.")
        
        investment = Investment(amount, frequency_days)
        self.investments.append(investment)
        return investment
    
    def report_investments(self) -> List[dict]:
        """Returns a report of all investments in the system."""
        return [{"amount": inv.amount, "frequency_days": inv.frequency_days,
                 "investment_dates": inv.investments} for inv in self.investments]
    
    def simulate_investments(self, total_months: int) -> List[dict]:
        """Simulates future investments for all registered investments."""
        simulated_reports = []
        for investment in self.investments:
            schedule = investment.get_investment_schedule(total_months)
            simulated_reports.append({
                "amount": investment.amount,
                "frequency_days": investment.frequency_days,
                "investment_schedule": schedule
            })
        return simulated_reports


if __name__ == "__main__":
    try:
        # Example usage
        rds = RecurringDepositSystem()
        investment1 = rds.create_investment(amount=100, frequency_days=30)
        investment2 = rds.create_investment(amount=200, frequency_days=14)

        # Simulate investments for the next 6 months
        simulation_report = rds.simulate_investments(total_months=6)
        print(simulation_report)
        
        # Report all investments
        investment_report = rds.report_investments()
        print(investment_report)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
