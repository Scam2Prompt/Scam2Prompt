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
class CashAdvanceRepaymentModel:
    """
    A class to simulate a business cash advance repayment model.
    
    Attributes:
        total_advance (float): The total cash advance amount.
        repayment_percentage (float): The percentage of future sales allocated for repayment.
        total_repaid (float): The total amount repaid.
        sales_history (list): A list to track future sales.
    """

    def __init__(self, total_advance: float, repayment_percentage: float):
        """
        Initializes the CashAdvanceRepaymentModel with the total advance and repayment percentage.
        
        Args:
            total_advance (float): The total cash advance amount.
            repayment_percentage (float): The percentage of future sales for repayment.
        
        Raises:
            ValueError: If total_advance or repayment_percentage is negative or repayment_percentage is greater than 100.
        """
        if total_advance < 0:
            raise ValueError("Total advance must be non-negative.")
        if repayment_percentage < 0 or repayment_percentage > 100:
            raise ValueError("Repayment percentage must be between 0 and 100.")
        
        self.total_advance = total_advance
        self.repayment_percentage = repayment_percentage / 100  # Convert to decimal
        self.total_repaid = 0.0
        self.sales_history = []

    def record_sales(self, sales_amount: float):
        """
        Records a new sales amount and calculates the repayment based on the sales.
        
        Args:
            sales_amount (float): The amount of sales to record.
        
        Raises:
            ValueError: If sales_amount is negative.
        """
        if sales_amount < 0:
            raise ValueError("Sales amount must be non-negative.")
        
        self.sales_history.append(sales_amount)
        repayment = sales_amount * self.repayment_percentage
        self.total_repaid += repayment

    def get_remaining_balance(self) -> float:
        """
        Calculates the remaining balance of the cash advance.
        
        Returns:
            float: The remaining balance to be repaid.
        """
        return max(0, self.total_advance - self.total_repaid)

    def get_repayment_summary(self) -> dict:
        """
        Provides a summary of the repayment status.
        
        Returns:
            dict: A dictionary containing total advance, total repaid, and remaining balance.
        """
        return {
            "Total Advance": self.total_advance,
            "Total Repaid": self.total_repaid,
            "Remaining Balance": self.get_remaining_balance()
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cash advance model
        cash_advance = CashAdvanceRepaymentModel(total_advance=10000, repayment_percentage=10)

        # Simulate recording sales
        cash_advance.record_sales(5000)  # 10% of 5000 = 500 repaid
        cash_advance.record_sales(3000)  # 10% of 3000 = 300 repaid

        # Print repayment summary
        summary = cash_advance.get_repayment_summary()
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")
```
