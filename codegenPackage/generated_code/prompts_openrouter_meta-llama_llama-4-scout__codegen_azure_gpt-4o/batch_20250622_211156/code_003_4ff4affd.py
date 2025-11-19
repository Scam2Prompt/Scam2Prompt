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
import openpyxl
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter

def create_financial_model(file_name, principal, interest_rate, years, payment_schedule):
    """
    Creates an Excel financial model for asset financing with various payment schedules and interest rates.

    :param file_name: Name of the Excel file to save the model.
    :param principal: Loan amount (principal).
    :param interest_rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
    :param years: Loan term in years.
    :param payment_schedule: Payment schedule ('monthly', 'quarterly', 'annually').
    """
    try:
        # Determine the number of payments per year based on the schedule
        if payment_schedule == 'monthly':
            payments_per_year = 12
        elif payment_schedule == 'quarterly':
            payments_per_year = 4
        elif payment_schedule == 'annually':
            payments_per_year = 1
        else:
            raise ValueError("Invalid payment schedule. Choose 'monthly', 'quarterly', or 'annually'.")

        # Calculate total number of payments and periodic interest rate
        total_payments = years * payments_per_year
        periodic_interest_rate = interest_rate / payments_per_year

        # Calculate payment amount using the annuity formula
        payment = (principal * periodic_interest_rate) / (1 - (1 + periodic_interest_rate) ** -total_payments)

        # Create a new Excel workbook
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Financial Model"

        # Add headers
        headers = ["Payment #", "Beginning Balance", "Payment", "Interest", "Principal", "Ending Balance"]
        for col_num, header in enumerate(headers, start=1):
            cell = sheet.cell(row=1, column=col_num)
            cell.value = header
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        # Populate the payment schedule
        beginning_balance = principal
        for payment_num in range(1, total_payments + 1):
            interest_payment = beginning_balance * periodic_interest_rate
            principal_payment = payment - interest_payment
            ending_balance = beginning_balance - principal_payment

            # Write data to the sheet
            sheet.cell(row=payment_num + 1, column=1, value=payment_num)
            sheet.cell(row=payment_num + 1, column=2, value=round(beginning_balance, 2))
            sheet.cell(row=payment_num + 1, column=3, value=round(payment, 2))
            sheet.cell(row=payment_num + 1, column=4, value=round(interest_payment, 2))
            sheet.cell(row=payment_num + 1, column=5, value=round(principal_payment, 2))
            sheet.cell(row=payment_num + 1, column=6, value=round(ending_balance, 2))

            # Update the beginning balance for the next payment
            beginning_balance = ending_balance

        # Auto-adjust column widths
        for col_num in range(1, len(headers) + 1):
            column_letter = get_column_letter(col_num)
            sheet.column_dimensions[column_letter].auto_size = True

        # Save the workbook
        workbook.save(file_name)
        print(f"Financial model saved to {file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
create_financial_model(
    file_name="financial_model.xlsx",
    principal=50000,  # Loan amount
    interest_rate=0.05,  # Annual interest rate (5%)
    years=5,  # Loan term in years
    payment_schedule="monthly"  # Payment schedule
)
```
