"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Create a function to generate a customizable inspection report in Word format, similar to the personalized reports offered by BeSoft.
Generated: DETERMINISTIC_1a1fd65204f42b84
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from docx import Document
from datetime import datetime

def generate_inspection_report(file_name, title, inspector_name, inspection_date, sections):
    """
    Generates a customizable inspection report in Word format.

    Parameters:
        file_name (str): The name of the output Word file (e.g., 'inspection_report.docx').
        title (str): The title of the inspection report.
        inspector_name (str): Name of the inspector creating the report.
        inspection_date (str): Date of inspection, formatted as 'YYYY-MM-DD'.
        sections (list of dict): A list of sections, each represented as a dictionary containing:
            - 'heading' (str): The heading for the section.
            - 'content' (str): The content for the section.

    Returns:
        str: The path to the generated Word file.
    """
    try:
        # Create a new Word document
        document = Document()

        # Add the report title
        document.add_heading(title, level=1)

        # Add inspector details and inspection date
        document.add_paragraph(f"Inspector Name: {inspector_name}")
        document.add_paragraph(f"Inspection Date: {inspection_date}")

        # Add a horizontal line for separation
        document.add_paragraph("—" * 30)

        # Add sections to the document
        for section in sections:
            if 'heading' in section and 'content' in section:
                # Add section heading
                document.add_heading(section['heading'], level=2)
                # Add section content
                document.add_paragraph(section['content'])
                # Add space between sections
                document.add_paragraph()
            else:
                raise ValueError("Each section must contain 'heading' and 'content' keys.")

        # Save the document to the specified file name
        document.save(file_name)

        return f"Inspection report generated successfully: {file_name}"

    except Exception as e:
        # Handle errors gracefully
        return f"An error occurred while generating the report: {str(e)}"


# Example usage of the function
if __name__ == "__main__":
    # Sample data for the report
    report_title = "Building Inspection Report"
    report_inspector = "John Doe"
    report_date = datetime.now().strftime("%Y-%m-%d")  # Today's date
    report_sections = [
        {"heading": "Structural Integrity", "content": "The building structure is stable and shows no signs of damage."},
        {"heading": "Electrical Systems", "content": "All electrical systems are functioning properly and meet safety standards."},
        {"heading": "Plumbing", "content": "No leaks detected in pipes or fixtures. Water pressure is adequate."}
    ]

    # Generate the report
    output_file = "inspection_report.docx"
    result_message = generate_inspection_report(output_file, report_title, report_inspector, report_date, report_sections)
    print(result_message)
```
