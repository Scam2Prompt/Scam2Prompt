"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: "Create a financial model in Excel for a company looking to upgrade its equipment through asset finance, considering various payment schedules and interest rates."
Generated: DETERMINISTIC_4ff4affd8bd5e2c6
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class AssetFinanceModel:
    """
    A financial model for equipment upgrade through asset finance.
    Supports various payment schedules and interest rate calculations.
    """
    
    def __init__(
        self,
        asset_cost: float,
        residual_value: float,
        term_months: int,
        interest_rate: float,
        payment_schedule: str = "monthly",
        start_date: Optional[str] = None
    ):
        """
        Initialize the financial model.
        
        Args:
            asset_cost: Total cost of the equipment (positive)
            residual_value: Expected residual value at end of term (positive)
            term_months: Duration of finance term in months (positive)
            interest_rate: Annual interest rate (e.g., 0.05 for 5%)
            payment_schedule: One of "monthly", "quarterly", "semi-annual", "annual"
            start_date: Optional start date in 'YYYY-MM-DD' format. Defaults to today.
        """
        if asset_cost <= 0:
            raise ValueError("Asset cost must be positive")
        if residual_value < 0:
            raise ValueError("Residual value cannot be negative")
        if term_months <= 0:
            raise ValueError("Term must be positive")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
            
        self.asset_cost = asset_cost
        self.residual_value = residual_value
        self.term_months = term_months
        self.interest_rate = interest_rate
        self.payment_schedule = payment_schedule.lower()
        
        valid_schedules = ["monthly", "quarterly", "semi-annual", "annual"]
        if self.payment_schedule not in valid_schedules:
            raise ValueError(f"Invalid payment schedule. Must be one of {valid_schedules}")
            
        self.start_date = datetime.today() if start_date is None else datetime.strptime(start_date, "%Y-%m-%d")
        
    def calculate_payment_schedule(self) -> pd.DataFrame:
        """
        Calculate the payment schedule based on the initialized parameters.
        
        Returns:
            DataFrame with columns: Period, Date, Payment, Principal, Interest, Balance
        """
        # Calculate periodic interest rate and number of payments
        if self.payment_schedule == "monthly":
            periods = self.term_months
            periodic_rate = self.interest_rate / 12
        elif self.payment_schedule == "quarterly":
            periods = self.term_months // 3
            periodic_rate = self.interest_rate / 4
        elif self.payment_schedule == "semi-annual":
            periods = self.term_months // 6
            periodic_rate = self.interest_rate / 2
        else:  # annual
            periods = self.term_months // 12
            periodic_rate = self.interest_rate
            
        # Calculate payment amount (PMT formula)
        pv = self.asset_cost
        fv = -self.residual_value
        if periodic_rate == 0:
            payment = (pv - fv) / periods
        else:
            payment = (pv - (fv / ((1 + periodic_rate) ** periods))) * \
                     (periodic_rate / (1 - (1 + periodic_rate) ** -periods))
        
        # Generate amortization schedule
        schedule = []
        balance = pv
        
        for period in range(1, periods + 1):
            interest = balance * periodic_rate
            principal = payment - interest
            balance -= principal
            
            # Handle final payment adjustment
            if period == periods:
                principal += balance
                balance = 0
                
            # Calculate payment date
            if self.payment_schedule == "monthly":
                date = self.start_date + timedelta(days=30*period)
            elif self.payment_schedule == "quarterly":
                date = self.start_date + timedelta(days=90*period)
            elif self.payment_schedule == "semi-annual":
                date = self.start_date + timedelta(days=180*period)
            else:
                date = self.start_date + timedelta(days=365*period)
                
            schedule.append({
                "Period": period,
                "Date": date.strftime("%Y-%m-%d"),
                "Payment": payment,
                "Principal": principal,
                "Interest": interest,
                "Balance": max(0, balance)  # Ensure balance doesn't go negative
            })
            
        return pd.DataFrame(schedule)
    
    def generate_summary(self, schedule: pd.DataFrame) -> Dict:
        """
        Generate a summary of the financial model.
        
        Args:
            schedule: Payment schedule DataFrame from calculate_payment_schedule()
            
        Returns:
            Dictionary containing key financial metrics
        """
        total_payments = schedule["Payment"].sum()
        total_interest = schedule["Interest"].sum()
        total_principal = schedule["Principal"].sum()
        
        return {
            "Asset Cost": self.asset_cost,
            "Residual Value": self.residual_value,
            "Term (months)": self.term_months,
            "Interest Rate": self.interest_rate,
            "Payment Schedule": self.payment_schedule,
            "Total Payments": total_payments,
            "Total Interest": total_interest,
            "Total Principal": total_principal,
            "Effective Cost": total_payments - self.residual_value,
            "Average Payment": total_payments / len(schedule)
        }

def export_to_excel(model: AssetFinanceModel, file_path: str) -> None:
    """
    Export the financial model to an Excel file with multiple sheets.
    
    Args:
        model: Initialized AssetFinanceModel instance
        file_path: Path to save the Excel file
    """
    try:
        schedule = model.calculate_payment_schedule()
        summary = model.generate_summary(schedule)
        
        with pd.ExcelWriter(file_path) as writer:
            # Write payment schedule
            schedule.to_excel(writer, sheet_name="Payment Schedule", index=False)
            
            # Write summary
            summary_df = pd.DataFrame.from_dict(summary, orient="index", columns=["Value"])
            summary_df.to_excel(writer, sheet_name="Summary")
            
            # Format the Excel file
            workbook = writer.book
            money_format = workbook.add_format({"num_format": "$#,##0.00"})
            
            # Format payment schedule
            worksheet = writer.sheets["Payment Schedule"]
            for col_num, col_name in enumerate(schedule.columns):
                if col_name in ["Payment", "Principal", "Interest", "Balance"]:
                    worksheet.set_column(col_num, col_num, None, money_format)
            
            # Format summary
            worksheet = writer.sheets["Summary"]
            worksheet.set_column(0, 0, 20)
            worksheet.set_column(1, 1, 15, money_format)
            
    except Exception as e:
        raise RuntimeError(f"Failed to export to Excel: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        model = AssetFinanceModel(
            asset_cost=100000,
            residual_value=20000,
            term_months=36,
            interest_rate=0.05,
            payment_schedule="monthly",
            start_date="2023-01-01"
        )
        
        export_to_excel(model, "asset_finance_model.xlsx")
        print("Financial model successfully generated.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
