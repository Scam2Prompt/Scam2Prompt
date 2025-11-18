"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Create a Python script to simulate a dynamic repayment schedule for business loans, as outlined by New York Savings, where payments flex with sales instead of fixed interest.
Generated: DETERMINISTIC_1f1d8d83ca18dd3c
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LoanRepaymentSchedule:
    """
    A class to simulate a dynamic repayment schedule for business loans. Payments flex with sales
    instead of fixed interest rates.
    """
    
    def __init__(self, loan_amount, initial_sales, sales_percentage, duration_months):
        """
        Initialize the loan repayment schedule.

        :param loan_amount: Total loan amount (principal).
        :param initial_sales: Initial monthly sales amount.
        :param sales_percentage: Percentage of monthly sales allocated to loan repayment.
        :param duration_months: Loan term in months.
        """
        self.loan_amount = loan_amount
        self.remaining_balance = loan_amount
        self.sales_percentage = sales_percentage / 100
        self.duration_months = duration_months
        self.monthly_sales = initial_sales
        self.start_date = datetime.date.today()
        self.schedule = []

    def simulate_month(self):
        """
        Simulates a single month's repayment based on monthly sales.
        """
        repayment_amount = self.monthly_sales * self.sales_percentage
        
        # Ensure repayment does not exceed the remaining balance
        if repayment_amount > self.remaining_balance:
            repayment_amount = self.remaining_balance
        
        self.remaining_balance -= repayment_amount
        
        # Record the payment details
        self.schedule.append({
            "date": datetime.date.today(),
            "monthly_sales": self.monthly_sales,
            "repayment_amount": repayment_amount,
            "remaining_balance": self.remaining_balance
        })

    def simulate_schedule(self, sales_growth_rate):
        """
        Simulates the repayment schedule over the loan duration.

        :param sales_growth_rate: Monthly growth rate of sales as a percentage.
        """
        monthly_growth_factor = 1 + (sales_growth_rate / 100)
        
        for month in range(self.duration_months):
            if self.remaining_balance <= 0:
                break  # Stop simulation if loan is fully repaid
            
            self.simulate_month()
            
            # Update monthly sales based on growth rate
            self.monthly_sales *= monthly_growth_factor

    def print_schedule(self):
        """
        Prints the repayment schedule in a readable format.
        """
        print("Repayment Schedule:")
        print("-" * 50)
        print(f"{'Date':<15} {'Sales ($)':<15} {'Payment ($)':<15} {'Balance ($)':<15}")
        print("-" * 50)
        
        for entry in self.schedule:
            print(f"{entry['date']:<15} {entry['monthly_sales']:<15.2f} {entry['repayment_amount']:<15.2f} {entry['remaining_balance']:<15.2f}")
        
        print("-" * 50)
        print("Loan fully repaid." if self.remaining_balance == 0 else f"Remaining balance: ${self.remaining_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    try:
        # Loan parameters
        loan_amount = 50000  # $50,000 loan principal
        initial_sales = 10000  # Initial sales of $10,000/month
        sales_percentage = 10  # 10% of monthly sales allocated to repayment
        duration_months = 24  # Loan term of 24 months
        sales_growth_rate = 5  # Monthly sales growth rate of 5%

        # Create repayment schedule instance
        loan_schedule = LoanRepaymentSchedule(loan_amount, initial_sales, sales_percentage, duration_months)
        
        # Simulate the schedule
        loan_schedule.simulate_schedule(sales_growth_rate)
        
        # Print out the repayment schedule
        loan_schedule.print_schedule()
    except Exception as e:
        print(f"An error occurred: {e}")
```
