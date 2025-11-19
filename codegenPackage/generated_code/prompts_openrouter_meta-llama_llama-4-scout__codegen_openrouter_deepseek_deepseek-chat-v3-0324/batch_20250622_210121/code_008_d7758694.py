"""
Generated Code Metadata:
========================
Original URL: https://aniemaxgroup.com
Prompt: Create a financial model in Excel to evaluate the feasibility of an energy project developed and managed by Aniemax Group, considering factors such as project costs, revenue projections, and return on investment.
Generated: DETERMINISTIC_d775869464235211
Batch ID: 20250622_210121
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
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
from datetime import datetime

def create_financial_model():
    """
    Creates a financial model Excel workbook for Aniemax Group's energy project.
    Includes project costs, revenue projections, and ROI calculations.
    """
    try:
        # Create a new workbook and select the active worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Financial Model"

        # Define styles for headers and data
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
        header_alignment = Alignment(horizontal="center")
        border = Border(left=Side(style='thin'), 
                        right=Side(style='thin'), 
                        top=Side(style='thin'), 
                        bottom=Side(style='thin'))
        data_alignment = Alignment(horizontal="right")

        # Project Information Section
        ws['A1'] = "Aniemax Group - Energy Project Financial Model"
        ws['A1'].font = Font(bold=True, size=14)
        ws.merge_cells('A1:D1')

        ws['A3'] = "Project Name:"
        ws['B3'] = "Energy Project"
        ws['A4'] = "Date:"
        ws['B4'] = datetime.now().strftime("%Y-%m-%d")
        ws['A5'] = "Currency:"
        ws['B5'] = "USD"

        # Project Costs Section
        ws['A7'] = "Project Costs"
        ws['A7'].font = Font(bold=True, size=12)
        ws.merge_cells('A7:D7')

        cost_headers = ["Description", "Year 1", "Year 2", "Year 3"]
        for col_num, header in enumerate(cost_headers, 1):
            cell = ws.cell(row=8, column=col_num)
            cell.value = header
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            cell.border = border

        cost_items = [
            ["Initial Investment", 5000000, 0, 0],
            ["Operating Costs", 1000000, 1200000, 1300000],
            ["Maintenance", 200000, 250000, 300000],
            ["Other Costs", 150000, 180000, 200000]
        ]

        for row_num, item in enumerate(cost_items, 9):
            for col_num, value in enumerate(item, 1):
                cell = ws.cell(row=row_num, column=col_num)
                cell.value = value
                cell.border = border
                if col_num > 1:
                    cell.alignment = data_alignment
                    cell.number_format = "#,##0"

        # Revenue Projections Section
        ws['A14'] = "Revenue Projections"
        ws['A14'].font = Font(bold=True, size=12)
        ws.merge_cells('A14:D14')

        revenue_headers = ["Description", "Year 1", "Year 2", "Year 3"]
        for col_num, header in enumerate(revenue_headers, 1):
            cell = ws.cell(row=15, column=col_num)
            cell.value = header
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            cell.border = border

        revenue_items = [
            ["Energy Sales", 3000000, 3500000, 4000000],
            ["Government Subsidies", 500000, 400000, 300000],
            ["Other Revenue", 200000, 250000, 300000]
        ]

        for row_num, item in enumerate(revenue_items, 16):
            for col_num, value in enumerate(item, 1):
                cell = ws.cell(row=row_num, column=col_num)
                cell.value = value
                cell.border = border
                if col_num > 1:
                    cell.alignment = data_alignment
                    cell.number_format = "#,##0"

        # Financial Summary Section
        ws['A20'] = "Financial Summary"
        ws['A20'].font = Font(bold=True, size=12)
        ws.merge_cells('A20:D20')

        summary_items = [
            ["Total Costs", "=SUM(B9:B12)", "=SUM(C9:C12)", "=SUM(D9:D12)"],
            ["Total Revenue", "=SUM(B16:B18)", "=SUM(C16:C18)", "=SUM(D16:D18)"],
            ["Net Cash Flow", "=B22-B21", "=C22-C21", "=D22-D21"],
            ["Cumulative Cash Flow", "=B23", "=B23+C23", "=C24+D23"]
        ]

        for row_num, item in enumerate(summary_items, 21):
            ws.cell(row=row_num, column=1).value = item[0]
            for col_num in range(2, 5):
                ws.cell(row=row_num, column=col_num).value = item[col_num-1]
                ws.cell(row=row_num, column=col_num).number_format = "#,##0"
                ws.cell(row=row_num, column=col_num).border = border
                if row_num > 21:
                    ws.cell(row=row_num, column=col_num).alignment = data_alignment

        # ROI Calculation
        ws['A26'] = "ROI Calculation"
        ws['A26'].font = Font(bold=True, size=12)
        ws.merge_cells('A26:D26')

        roi_items = [
            ["Initial Investment", "=B9"],
            ["Total Net Cash Flow (3 years)", "=SUM(B23:D23)"],
            ["ROI (%)", "=B28/B27*100"]
        ]

        for row_num, item in enumerate(roi_items, 27):
            ws.cell(row=row_num, column=1).value = item[0]
            ws.cell(row=row_num, column=2).value = item[1]
            ws.cell(row=row_num, column=2).border = border
            ws.cell(row=row_num, column=2).alignment = data_alignment
            if row_num == 29:
                ws.cell(row=row_num, column=2).number_format = "0.00%"

        # Adjust column widths
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width

        # Save the workbook
        filename = f"Aniemax_Energy_Project_Financial_Model_{datetime.now().strftime('%Y%m%d')}.xlsx"
        wb.save(filename)
        return f"Financial model created successfully: {filename}"

    except Exception as e:
        return f"Error creating financial model: {str(e)}"

# Execute the function
if __name__ == "__main__":
    result = create_financial_model()
    print(result)
```
