"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Generate code to simulate a business cash advance repayment model, where repayments are based on a percentage of future credit/debit sales, as described on Maestro Finance.
Generated: DETERMINISTIC_f22e2e8da07e72e6
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class CashAdvanceRepaymentModel:
    """
    Simulates a business cash advance repayment model where repayments are based on a percentage
    of future credit/debit card sales.
    """
    
    def __init__(
        self,
        advance_amount: float,
        repayment_percentage: float,
        daily_sales: List[float],
        start_date: datetime.date = datetime.date.today()
    ):
        """
        Initialize the repayment model.
        
        Args:
            advance_amount: Total amount of cash advance (must be positive)
            repayment_percentage: Percentage of daily sales to be used for repayment (0-100)
            daily_sales: List of projected daily sales amounts
            start_date: Date when the advance is given (defaults to today)
        """
        if advance_amount <= 0:
            raise ValueError("Advance amount must be positive")
        if not (0 <= repayment_percentage <= 100):
            raise ValueError("Repayment percentage must be between 0 and 100")
        if not daily_sales:
            raise ValueError("Daily sales projections cannot be empty")
        
        self.advance_amount = advance_amount
        self.repayment_percentage = repayment_percentage / 100  # Convert to decimal
        self.daily_sales = daily_sales
        self.start_date = start_date
        self.remaining_balance = advance_amount
        self.repayment_schedule = []
        
    def generate_repayment_schedule(self) -> List[Dict]:
        """
        Generate the repayment schedule based on daily sales and repayment percentage.
        
        Returns:
            List of dictionaries containing repayment details for each day
        """
        self.repayment_schedule = []
        current_date = self.start_date
        total_repayments = 0.0
        
        for day, sales in enumerate(self.daily_sales, 1):
            if self.remaining_balance <= 0:
                break
                
            repayment = sales * self.repayment_percentage
            actual_repayment = min(repayment, self.remaining_balance)
            
            self.remaining_balance -= actual_repayment
            total_repayments += actual_repayment
            
            repayment_data = {
                "day": day,
                "date": current_date,
                "daily_sales": sales,
                "repayment_amount": actual_repayment,
                "remaining_balance": self.remaining_balance,
                "total_repayments": total_repayments
            }
            
            self.repayment_schedule.append(repayment_data)
            current_date += datetime.timedelta(days=1)
            
        return self.repayment_schedule
    
    def get_summary(self) -> Dict:
        """
        Get a summary of the repayment including total repaid and days to repay.
        
        Returns:
            Dictionary containing summary information
        """
        if not self.repayment_schedule:
            self.generate_repayment_schedule()
            
        total_days = len(self.repayment_schedule)
        total_repayments = sum(item["repayment_amount"] for item in self.repayment_schedule)
        
        return {
            "advance_amount": self.advance_amount,
            "repayment_percentage": self.repayment_percentage * 100,
            "total_repayments": total_repayments,
            "total_days": total_days,
            "final_balance": self.remaining_balance,
            "fully_repaid": self.remaining_balance <= 0
        }


# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        advance = 10000.00
        percentage = 15.0
        sales_projections = [1200, 1500, 800, 2000, 2500, 1800, 900, 3000, 2200, 1700]
        start_date = datetime.date(2023, 1, 1)
        
        # Create and run model
        model = CashAdvanceRepaymentModel(
            advance_amount=advance,
            repayment_percentage=percentage,
            daily_sales=sales_projections,
            start_date=start_date
        )
        
        schedule = model.generate_repayment_schedule()
        summary = model.get_summary()
        
        # Print results
        print("Repayment Schedule:")
        for day in schedule:
            print(f"Day {day['day']} ({day['date']}): "
                  f"Sales: ${day['daily_sales']:.2f}, "
                  f"Repayment: ${day['repayment_amount']:.2f}, "
                  f"Remaining: ${day['remaining_balance']:.2f}")
        
        print("\nSummary:")
        print(f"Advance Amount: ${summary['advance_amount']:.2f}")
        print(f"Repayment Percentage: {summary['repayment_percentage']:.1f}%")
        print(f"Total Repayments: ${summary['total_repayments']:.2f}")
        print(f"Days to Repay: {summary['total_days']}")
        print(f"Fully Repaid: {'Yes' if summary['fully_repaid'] else 'No'}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
