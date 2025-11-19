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
# dynamic_repayment_schedule.py

class BusinessLoan:
    def __init__(self, loan_amount, sales_projection, repayment_percentage):
        """
        Initialize a BusinessLoan object.

        Args:
            loan_amount (float): The initial loan amount.
            sales_projection (list[float]): A list of projected sales for each period.
            repayment_percentage (float): The percentage of sales to allocate towards repayment.
        """
        self.loan_amount = loan_amount
        self.sales_projection = sales_projection
        self.repayment_percentage = repayment_percentage / 100  # Convert to decimal
        self.outstanding_balance = loan_amount
        self.repayment_schedule = []

    def calculate_repayment(self):
        """
        Calculate the dynamic repayment schedule based on sales projections.
        """
        for sales in self.sales_projection:
            repayment = sales * self.repayment_percentage
            if self.outstanding_balance > 0:
                if repayment > self.outstanding_balance:
                    repayment = self.outstanding_balance
                self.outstanding_balance -= repayment
                self.repayment_schedule.append({
                    'sales': sales,
                    'repayment': repayment,
                    'outstanding_balance': self.outstanding_balance
                })
            else:
                self.repayment_schedule.append({
                    'sales': sales,
                    'repayment': 0,
                    'outstanding_balance': self.outstanding_balance
                })

    def print_repayment_schedule(self):
        """
        Print the dynamic repayment schedule.
        """
        print("Dynamic Repayment Schedule:")
        print("--------------------------------")
        for i, repayment in enumerate(self.repayment_schedule):
            print(f"Period {i+1}:")
            print(f"  Sales: ${repayment['sales']:.2f}")
            print(f"  Repayment: ${repayment['repayment']:.2f}")
            print(f"  Outstanding Balance: ${repayment['outstanding_balance']:.2f}")
            print("--------------------------------")


def main():
    try:
        loan_amount = float(input("Enter the loan amount: $"))
        num_periods = int(input("Enter the number of periods: "))
        sales_projection = []
        for i in range(num_periods):
            sales = float(input(f"Enter sales projection for period {i+1}: $"))
            sales_projection.append(sales)
        repayment_percentage = float(input("Enter repayment percentage (%): "))

        loan = BusinessLoan(loan_amount, sales_projection, repayment_percentage)
        loan.calculate_repayment()
        loan.print_repayment_schedule()

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
