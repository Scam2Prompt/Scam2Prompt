"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Generate code to simulate a business cash advance repayment model, where repayments are based on a percentage of future credit/debit sales, as described on Maestro Finance.
Generated: DETERMINISTIC_f22e2e8da07e72e6
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CashAdvanceRepayment:
    """
    Simulates a business cash advance repayment model.
    Repayments are based on a fixed percentage of future credit/debit sales.
    """

    def __init__(self, advance_amount, daily_sales, repayment_percentage):
        """
        Initialize the cash advance repayment model.

        :param advance_amount: Total cash advance provided to the business.
        :param daily_sales: List of daily credit/debit sales amounts.
        :param repayment_percentage: Fixed percentage of daily sales used for repayment.
        """
        if advance_amount <= 0 or repayment_percentage <= 0 or repayment_percentage > 100:
            raise ValueError("Advance amount and repayment percentage must be positive. Percentage must be <= 100.")
        
        if not all(sales >= 0 for sales in daily_sales):
            raise ValueError("Daily sales must be non-negative.")
        
        self.advance_amount = advance_amount
        self.daily_sales = daily_sales
        self.repayment_percentage = repayment_percentage / 100  # Convert to decimal
        self.remaining_balance = advance_amount
        self.total_repaid = 0
        self.repayment_schedule = []

    def simulate_repayment(self):
        """
        Simulates the repayment process based on daily sales and repayment percentage.
        """
        for day, sales in enumerate(self.daily_sales, start=1):
            # Calculate daily repayment based on sales
            daily_repayment = sales * self.repayment_percentage
            daily_repayment = min(daily_repayment, self.remaining_balance)  # Ensure no overpayment
            
            # Update repayment details
            self.remaining_balance -= daily_repayment
            self.total_repaid += daily_repayment
            self.repayment_schedule.append({
                "day": day,
                "daily_sales": sales,
                "daily_repayment": daily_repayment,
                "remaining_balance": self.remaining_balance
            })

            # Stop the simulation when the advance is fully repaid
            if self.remaining_balance <= 0:
                break

    def print_repayment_schedule(self):
        """
        Prints the repayment schedule in a user-friendly format.
        """
        print(f"Repayment Schedule for Cash Advance of ${self.advance_amount:.2f}")
        print("-" * 50)
        for entry in self.repayment_schedule:
            print(f"Day {entry['day']:2}: Sales: ${entry['daily_sales']:.2f}, "
                  f"Repayment: ${entry['daily_repayment']:.2f}, "
                  f"Remaining Balance: ${entry['remaining_balance']:.2f}")
        print("-" * 50)
        print(f"Total Repaid: ${self.total_repaid:.2f}")

if __name__ == "__main__":
    try:
        # Simulated data: cash advance amount, daily sales, and repayment percentage
        cash_advance_amount = 2000.00  # Example cash advance amount
        daily_sales = [random.uniform(100, 500) for _ in range(30)]  # Generate random daily sales for 30 days
        repayment_percentage = 10.0  # Business agrees to repay 10% of daily sales

        # Initialize the repayment model
        repayment_model = CashAdvanceRepayment(cash_advance_amount, daily_sales, repayment_percentage)

        # Simulate repayment
        repayment_model.simulate_repayment()

        # Print the repayment schedule
        repayment_model.print_repayment_schedule()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
