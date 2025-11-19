"""
Generated Code Metadata:
========================
Original URL: https://securecash.info
Prompt: Create a Python script to simulate a dynamic repayment schedule for business loans, as outlined by New York Savings, where payments flex with sales instead of fixed interest.
Generated: DETERMINISTIC_1f1d8d83ca18dd3c
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class DynamicRepaymentSchedule:
    """
    Simulates a dynamic repayment schedule for business loans where payments flex with sales.
    Payments are calculated as a percentage of sales instead of fixed interest.
    """
    
    def __init__(
        self,
        principal: float,
        start_date: str,
        term_months: int,
        sales_percentage: float,
        min_payment: Optional[float] = None,
        max_payment: Optional[float] = None
    ):
        """
        Initialize the repayment schedule with loan parameters.
        
        Args:
            principal: Initial loan amount.
            start_date: Loan start date in 'YYYY-MM-DD' format.
            term_months: Loan term in months.
            sales_percentage: Percentage of sales applied to repayment (0-1).
            min_payment: Optional minimum payment per period.
            max_payment: Optional maximum payment per period.
        """
        self.principal = principal
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.term_months = term_months
        self.sales_percentage = sales_percentage
        self.min_payment = min_payment
        self.max_payment = max_payment
        self.remaining_balance = principal
        self.schedule = []
        
        if not 0 <= sales_percentage <= 1:
            raise ValueError("Sales percentage must be between 0 and 1")
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if term_months <= 0:
            raise ValueError("Term must be positive")
    
    def generate_schedule(self, sales_data: List[Dict[str, float]]) -> pd.DataFrame:
        """
        Generate repayment schedule based on historical sales data.
        
        Args:
            sales_data: List of dictionaries with 'date' (YYYY-MM-DD) and 'amount' keys.
            
        Returns:
            DataFrame with repayment schedule.
        """
        if len(sales_data) != self.term_months:
            raise ValueError("Sales data length must match loan term")
        
        current_date = self.start_date
        remaining_balance = self.principal
        
        for month_data in sales_data:
            payment_date = current_date + timedelta(days=30)
            sales_amount = month_data['amount']
            
            # Calculate payment as percentage of sales
            payment = sales_amount * self.sales_percentage
            
            # Apply min/max payment constraints if specified
            if self.min_payment is not None:
                payment = max(payment, self.min_payment)
            if self.max_payment is not None:
                payment = min(payment, self.max_payment)
            
            # Ensure payment doesn't exceed remaining balance
            payment = min(payment, remaining_balance)
            
            # Update remaining balance
            remaining_balance -= payment
            
            # Record payment details
            self.schedule.append({
                'Date': payment_date.strftime('%Y-%m-%d'),
                'Sales': sales_amount,
                'Payment': payment,
                'Remaining Balance': remaining_balance
            })
            
            current_date = payment_date
            
            if remaining_balance <= 0:
                break
        
        return pd.DataFrame(self.schedule)
    
    def get_summary(self) -> Dict[str, float]:
        """
        Get summary statistics for the repayment schedule.
        
        Returns:
            Dictionary with total payments, interest equivalent, etc.
        """
        if not self.schedule:
            raise ValueError("Schedule not generated yet. Call generate_schedule() first.")
        
        total_payments = sum(payment['Payment'] for payment in self.schedule)
        total_sales = sum(payment['Sales'] for payment in self.schedule)
        
        return {
            'Total Payments': total_payments,
            'Total Sales': total_sales,
            'Effective Percentage': total_payments / total_sales if total_sales > 0 else 0,
            'Original Principal': self.principal,
            'Final Balance': self.schedule[-1]['Remaining Balance']
        }

# Example usage
if __name__ == "__main__":
    # Sample sales data (would normally come from business records)
    sales_data = [
        {'date': '2023-01-01', 'amount': 10000},
        {'date': '2023-02-01', 'amount': 12000},
        {'date': '2023-03-01', 'amount': 15000},
        {'date': '2023-04-01', 'amount': 8000},
        {'date': '2023-05-01', 'amount': 11000},
        {'date': '2023-06-01', 'amount': 13000},
    ]
    
    try:
        # Initialize loan with $50,000 principal, 6 month term, 10% of sales
        loan = DynamicRepaymentSchedule(
            principal=50000,
            start_date='2023-01-01',
            term_months=6,
            sales_percentage=0.10,
            min_payment=2000,
            max_payment=10000
        )
        
        # Generate repayment schedule
        schedule = loan.generate_schedule(sales_data)
        print("Repayment Schedule:")
        print(schedule)
        
        # Get summary
        summary = loan.get_summary()
        print("\nLoan Summary:")
        for key, value in summary.items():
            print(f"{key}: {value:,.2f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
