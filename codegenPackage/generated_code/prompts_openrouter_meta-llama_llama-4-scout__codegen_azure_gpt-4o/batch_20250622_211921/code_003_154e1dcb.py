"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Create a template for a planilla electrónica (electronic payroll) in Excel, including formulas and formatting for easy use by Peruvian employers."
Generated: DETERMINISTIC_154e1dcb9d08a49f
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

def create_payroll_template(file_name="Planilla_Electronica_Peru.xlsx"):
    try:
        # Create a new workbook and select the active worksheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Planilla Electrónica"

        # Define header titles
        headers = [
            "Nombres y Apellidos", "DNI", "Cargo", "Sueldo Básico", "Horas Extras",
            "Bonificaciones", "Descuentos", "Sueldo Neto", "AFP/ONP", "Essalud"
        ]

        # Apply header formatting
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
        header_alignment = Alignment(horizontal="center", vertical="center")
        border_style = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin")
        )

        # Write headers to the first row
        for col_num, header in enumerate(headers, start=1):
            cell = sheet.cell(row=1, column=col_num)
            cell.value = header
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            cell.border = border_style

        # Set column widths for better readability
        column_widths = [25, 12, 20, 15, 15, 15, 15, 15, 15, 15]
        for col_num, width in enumerate(column_widths, start=1):
            sheet.column_dimensions[openpyxl.utils.get_column_letter(col_num)].width = width

        # Add formulas for payroll calculations (example formulas for demonstration)
        for row in range(2, 101):  # Template for up to 100 employees
            # Sueldo Neto = Sueldo Básico + Horas Extras + Bonificaciones - Descuentos
            sheet.cell(row=row, column=8).value = f"=D{row}+E{row}+F{row}-G{row}"
            # AFP/ONP = Sueldo Básico * 0.10 (10% contribution)
            sheet.cell(row=row, column=9).value = f"=D{row}*0.10"
            # Essalud = Sueldo Básico * 0.09 (9% contribution)
            sheet.cell(row=row, column=10).value = f"=D{row}*0.09"

        # Save the workbook to the specified file
        workbook.save(file_name)
        print(f"Payroll template '{file_name}' created successfully.")

    except Exception as e:
        print(f"An error occurred while creating the payroll template: {e}")

# Call the function to create the payroll template
create_payroll_template()
```
