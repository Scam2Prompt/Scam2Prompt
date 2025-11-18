"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Write code to design and export a calendar layout suitable for offset printing, incorporating features similar to Ram Digi's calendar printing services.
Generated: DETERMINISTIC_d43bfb561c11e0a9
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import calendar
from datetime import datetime
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle


def generate_calendar(year, output_file='calendar.pdf'):
    """
    Generates a printable calendar layout for the specified year and exports it as a PDF file.
    
    Args:
        year (int): The year for which the calendar will be generated.
        output_file (str): The name of the output PDF file (default: 'calendar.pdf').
    """
    try:
        # Validate the year
        if year < 1 or year > 9999:
            raise ValueError("Year must be between 1 and 9999.")

        # Create a PDF canvas
        c = canvas.Canvas(output_file, pagesize=A4)
        width, height = A4  # Dimensions for A4 page size (595 x 842 points)

        # Title section
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, height - 50, f"Calendar for {year}")

        # Iterate through all months
        for month in range(1, 13):
            c.setFont("Helvetica-Bold", 16)

            # Draw the month name
            c.drawCentredString(width / 2, height - 100, calendar.month_name[month])

            # Fetch month calendar as a list of weeks
            month_calendar = calendar.monthcalendar(year, month)

            # Prepare table data
            table_data = [["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]]  # Days header
            for week in month_calendar:
                # Fill week data, replace 0 (empty days) with blank strings
                table_data.append([str(day) if day != 0 else "" for day in week])

            # Create table
            table = Table(table_data, colWidths=[width / 7.5] * 7, rowHeights=[25] * len(table_data))
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Header background color
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),       # Header text color
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),              # Align text to center
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),    # Bold font for header
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),        # Regular font for cells
                ('FONTSIZE', (0, 0), (-1, -1), 10),                 # Text size
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),      # Grid lines
            ])
            table.setStyle(style)

            # Draw table
            table.wrapOn(c, width, height)
            table.drawOn(c, 50, height - 200)

            # Move to the next page for the next month
            c.showPage()

        # Save the PDF
        c.save()
        print(f"Calendar for {year} saved successfully as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        # Prompt user for year input
        year_input = input("Enter the year for the calendar (e.g., 2023): ")
        year = int(year_input)

        # Generate calendar and export to PDF
        generate_calendar(year)

    except ValueError:
        print("Invalid year input. Please enter a valid integer year.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
