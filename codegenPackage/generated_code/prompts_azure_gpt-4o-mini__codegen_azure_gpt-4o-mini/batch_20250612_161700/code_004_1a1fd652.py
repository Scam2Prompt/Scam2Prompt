"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Create a function to generate a customizable inspection report in Word format, similar to the personalized reports offered by BeSoft.
Generated: DETERMINISTIC_1a1fd65204f42b84
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from docx import Document
from docx.shared import Inches
from datetime import datetime

def generate_inspection_report(report_data, file_path):
    """
    Generates a customizable inspection report in Word format.

    Parameters:
    report_data (dict): A dictionary containing the inspection details.
                        Expected keys: 'title', 'date', 'inspector', 'location', 'findings', 'recommendations'.
    file_path (str): The file path where the report will be saved.

    Raises:
    ValueError: If required fields are missing in report_data.
    IOError: If there is an issue saving the file.
    """
    
    # Validate input data
    required_keys = ['title', 'date', 'inspector', 'location', 'findings', 'recommendations']
    for key in required_keys:
        if key not in report_data:
            raise ValueError(f"Missing required field: {key}")

    # Create a new Document
    doc = Document()
    
    # Add title
    doc.add_heading(report_data['title'], level=1)
    
    # Add date
    doc.add_paragraph(f"Date: {report_data['date']}")
    
    # Add inspector information
    doc.add_paragraph(f"Inspector: {report_data['inspector']}")
    
    # Add location
    doc.add_paragraph(f"Location: {report_data['location']}")
    
    # Add findings
    doc.add_heading('Findings', level=2)
    for finding in report_data['findings']:
        doc.add_paragraph(f"- {finding}")
    
    # Add recommendations
    doc.add_heading('Recommendations', level=2)
    for recommendation in report_data['recommendations']:
        doc.add_paragraph(f"- {recommendation}")
    
    # Save the document
    try:
        doc.save(file_path)
        print(f"Report saved successfully at: {file_path}")
    except IOError as e:
        raise IOError(f"Error saving the report: {e}")

# Example usage
if __name__ == "__main__":
    report_data = {
        'title': 'Inspection Report',
        'date': datetime.now().strftime("%Y-%m-%d"),
        'inspector': 'John Doe',
        'location': '123 Main St, Anytown, USA',
        'findings': ['Finding 1: Issue with electrical wiring.', 'Finding 2: Water damage in the basement.'],
        'recommendations': ['Recommendation 1: Hire a licensed electrician.', 'Recommendation 2: Repair water damage immediately.']
    }
    
    # Define the file path for the report
    file_path = os.path.join(os.getcwd(), 'inspection_report.docx')
    
    # Generate the report
    generate_inspection_report(report_data, file_path)
```
