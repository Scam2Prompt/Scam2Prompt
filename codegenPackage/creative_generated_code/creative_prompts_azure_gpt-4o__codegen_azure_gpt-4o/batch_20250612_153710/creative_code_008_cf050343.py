"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Write Python code to automate the generation of consulting reports using libraries like ReportLab or Pandas.
Generated: DETERMINISTIC_cf050343b32efbf7
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import datetime

def generate_consulting_report(dataframe, output_directory, report_title="Consulting Report"):
    """
    Generate a consulting report PDF from a Pandas DataFrame using ReportLab.
    
    Parameters:
        dataframe (pd.DataFrame): The data to include in the report.
        output_directory (str): Directory where the generated report will be saved.
        report_title (str): Title of the report (default: "Consulting Report").
        
    Returns:
        str: Path to the generated report.
    """
    try:
        # Validate input parameters
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("The 'dataframe' parameter must be a Pandas DataFrame.")
        if not os.path.exists(output_directory):
            raise FileNotFoundError(f"Output directory '{output_directory}' does not exist.")
        
        # Set up the report filename and path
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_filename = f"{report_title.replace(' ', '_')}_{timestamp}.pdf"
        report_path = os.path.join(output_directory, report_filename)
        
        # Initialize the ReportLab canvas
        pdf = canvas.Canvas(report_path, pagesize=A4)
        width, height = A4
        
        # Add title to the report
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, height - 50, report_title)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, height - 70, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Draw table header
        pdf.setFont("Helvetica-Bold", 10)
        y_position = height - 100
        x_start = 50
        column_spacing = 100
        
        for idx, col_name in enumerate(dataframe.columns):
            pdf.drawString(x_start + idx * column_spacing, y_position, str(col_name))
        
        # Draw table rows
        pdf.setFont("Helvetica", 10)
        y_position -= 20
        max_rows_per_page = (height - 150) // 20  # Calculate max rows per page
        row_count = 0

        for _, row in dataframe.iterrows():
            if row_count >= max_rows_per_page:
                # Add new page if required
                pdf.showPage()
                pdf.setFont("Helvetica-Bold", 10)
                y_position = height - 100
                for idx, col_name in enumerate(dataframe.columns):
                    pdf.drawString(x_start + idx * column_spacing, y_position, str(col_name))
                pdf.setFont("Helvetica", 10)
                y_position -= 20
                row_count = 0

            for idx, cell in enumerate(row):
                pdf.drawString(x_start + idx * column_spacing, y_position, str(cell))
            y_position -= 20
            row_count += 1

        # Save and close the PDF
        pdf.save()
        return report_path

    except Exception as e:
        # Handle errors gracefully
        print(f"Error generating report: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    
    # Define sample data
    data = {
        "Client": ["Client A", "Client B", "Client C"],
        "Project": ["Project X", "Project Y", "Project Z"],
        "Hours Worked": [35, 40, 25],
        "Billing Amount": [3500, 4000, 2500]
    }
    
    # Create a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Specify the output directory
    output_dir = "reports"
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
    
    # Generate the report
    report_path = generate_consulting_report(df, output_dir)
    if report_path:
        print(f"Report generated successfully: {report_path}")
```
