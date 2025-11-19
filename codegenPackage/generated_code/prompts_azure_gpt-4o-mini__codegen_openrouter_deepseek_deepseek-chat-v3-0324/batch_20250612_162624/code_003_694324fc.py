"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: How can I use Excel to track expenses effectively, based on the accounting strategies suggested by Jo Dutton?
Generated: DETERMINISTIC_694324fcdd073d62
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
from datetime import datetime
import os

def create_expense_tracker(file_path):
    """
    Creates an Excel expense tracker based on Jo Dutton's accounting strategies.
    
    Args:
        file_path (str): Path where the Excel file will be saved.
    """
    try:
        # Create a new workbook
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Expense Tracker"
        
        # Define styles
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
        center_aligned = Alignment(horizontal="center")
        
        # Create headers
        headers = [
            "Date", "Category", "Description", 
            "Amount", "Payment Method", "Tax Deductible"
        ]
        
        for col_num, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col_num, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = center_aligned
        
        # Set column widths
        column_widths = [12, 20, 40, 15, 20, 15]
        for i, width in enumerate(column_widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = width
        
        # Freeze header row
        ws.freeze_panes = "A2"
        
        # Add data validation for categories
        categories = [
            "Housing", "Transportation", "Food", 
            "Utilities", "Insurance", "Healthcare",
            "Entertainment", "Personal", "Debt", 
            "Savings", "Other"
        ]
        
        dv = openpyxl.worksheet.datavalidation.DataValidation(
            type="list",
            formula1=f'"{",".join(categories)}"',
            allow_blank=True
        )
        ws.add_data_validation(dv)
        dv.add(f"B2:B1048576")  # Apply to entire column B
        
        # Add data validation for payment methods
        payment_methods = ["Cash", "Credit Card", "Debit Card", "Bank Transfer", "Other"]
        dv_payment = openpyxl.worksheet.datavalidation.DataValidation(
            type="list",
            formula1=f'"{",".join(payment_methods)}"',
            allow_blank=True
        )
        ws.add_data_validation(dv_payment)
        dv_payment.add(f"E2:E1048576")  # Apply to entire column E
        
        # Add data validation for tax deductible (Yes/No)
        dv_tax = openpyxl.worksheet.datavalidation.DataValidation(
            type="list",
            formula1='"Yes,No"',
            allow_blank=True
        )
        ws.add_data_validation(dv_tax)
        dv_tax.add(f"F2:F1048576")  # Apply to entire column F
        
        # Add current date as default in first row
        ws.cell(row=2, column=1, value=datetime.now().strftime("%Y-%m-%d"))
        
        # Save the workbook
        wb.save(file_path)
        print(f"Expense tracker created successfully at {file_path}")
        
    except Exception as e:
        print(f"Error creating expense tracker: {str(e)}")

def add_expense(file_path, date, category, description, amount, payment_method, tax_deductible):
    """
    Adds an expense entry to the tracker.
    
    Args:
        file_path (str): Path to the Excel file
        date (str): Date in YYYY-MM-DD format
        category (str): Expense category
        description (str): Expense description
        amount (float): Expense amount
        payment_method (str): Payment method used
        tax_deductible (str): "Yes" or "No"
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Expense tracker file not found")
            
        wb = openpyxl.load_workbook(file_path)
        ws = wb["Expense Tracker"]
        
        # Find the first empty row
        next_row = ws.max_row + 1
        
        # Add the expense data
        ws.cell(row=next_row, column=1, value=date)
        ws.cell(row=next_row, column=2, value=category)
        ws.cell(row=next_row, column=3, value=description)
        ws.cell(row=next_row, column=4, value=amount)
        ws.cell(row=next_row, column=5, value=payment_method)
        ws.cell(row=next_row, column=6, value=tax_deductible)
        
        # Save the workbook
        wb.save(file_path)
        print("Expense added successfully")
        
    except Exception as e:
        print(f"Error adding expense: {str(e)}")

def generate_summary_report(file_path, output_path):
    """
    Generates a summary report from the expense tracker.
    
    Args:
        file_path (str): Path to the expense tracker
        output_path (str): Path to save the summary report
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Expense tracker file not found")
            
        wb = openpyxl.load_workbook(file_path)
        ws = wb["Expense Tracker"]
        
        # Create a new sheet for the summary
        if "Summary" in wb.sheetnames:
            summary_ws = wb["Summary"]
            wb.remove(summary_ws)
        summary_ws = wb.create_sheet("Summary")
        
        # Add summary headers
        summary_headers = ["Category", "Total Amount", "Tax Deductible Amount"]
        for col_num, header in enumerate(summary_headers, 1):
            cell = summary_ws.cell(row=1, column=col_num, value=header)
            cell.font = Font(bold=True)
        
        # Get all categories from the tracker
        categories = set()
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=2, max_col=2):
            if row[0].value:
                categories.add(row[0].value)
        
        # Calculate totals by category
        row_num = 2
        for category in sorted(categories):
            total = 0
            tax_deductible_total = 0
            
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
                if row[1].value == category:  # Category column
                    amount = float(row[3].value) if row[3].value else 0  # Amount column
                    total += amount
                    
                    if row[5].value == "Yes":  # Tax Deductible column
                        tax_deductible_total += amount
            
            summary_ws.cell(row=row_num, column=1, value=category)
            summary_ws.cell(row=row_num, column=2, value=total)
            summary_ws.cell(row=row_num, column=3, value=tax_deductible_total)
            row_num += 1
        
        # Add grand totals
        summary_ws.cell(row=row_num, column=1, value="GRAND TOTAL").font = Font(bold=True)
        summary_ws.cell(row=row_num, column=2, 
                       value=f"=SUM(B2:B{row_num-1})").font = Font(bold=True)
        summary_ws.cell(row=row_num, column=3, 
                       value=f"=SUM(C2:C{row_num-1})").font = Font(bold=True)
        
        # Format columns
        summary_ws.column_dimensions['A'].width = 20
        summary_ws.column_dimensions['B'].width = 15
        summary_ws.column_dimensions['C'].width = 20
        
        # Save the summary report
        wb.save(output_path)
        print(f"Summary report generated successfully at {output_path}")
        
    except Exception as e:
        print(f"Error generating summary report: {str(e)}")

# Example usage
if __name__ == "__main__":
    tracker_path = "expense_tracker.xlsx"
    
    # Create a new tracker if it doesn't exist
    if not os.path.exists(tracker_path):
        create_expense_tracker(tracker_path)
    
    # Add sample expenses
    add_expense(
        tracker_path,
        "2023-11-15",
        "Food",
        "Groceries",
        85.50,
        "Credit Card",
        "No"
    )
    
    add_expense(
        tracker_path,
        "2023-11-16",
        "Transportation",
        "Gas",
        45.00,
        "Debit Card",
        "Yes"
    )
    
    # Generate summary report
    generate_summary_report(tracker_path, "expense_summary.xlsx")
