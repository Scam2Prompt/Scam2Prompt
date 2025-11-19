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
import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def create_inspection_report(report_title, inspection_date, inspector_name, findings, recommendations, output_path):
    """
    Generates a customizable inspection report in Word format.

    Parameters:
        report_title (str): The title of the inspection report.
        inspection_date (str): The date when the inspection was conducted.
        inspector_name (str): Name of the inspector who conducted the inspection.
        findings (list): A list of findings from the inspection.
        recommendations (list): A list of recommendations based on the findings.
        output_path (str): The file path where the report will be saved.

    Raises:
        ValueError: If any required parameter is empty.
        Exception: For other unforeseen errors during report creation.
    """
    
    # Validate input parameters
    if not all([report_title, inspection_date, inspector_name, findings, recommendations, output_path]):
        raise ValueError("All parameters must be provided and cannot be empty.")
    
    try:
        # Create a new Document
        doc = Document()
        
        # Add title to the document
        title_paragraph = doc.add_heading(report_title, level=1)
        title_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
        # Add inspection details
        doc.add_paragraph(f"Inspection Date: {inspection_date}")
        doc.add_paragraph(f"Inspector Name: {inspector_name}\n")
        
        # Add Findings section
        doc.add_heading('Findings', level=2)
        for finding in findings:
            doc.add_paragraph(f"- {finding}")
        
        # Add Recommendations section
        doc.add_heading('Recommendations', level=2)
        for recommendation in recommendations:
            doc.add_paragraph(f"- {recommendation}")
        
        # Save the document
        doc.save(output_path)
        print(f"Inspection report saved successfully at: {output_path}")
    
    except Exception as e:
        print(f"An error occurred while creating the report: {str(e)}")

# Example usage
if __name__ == "__main__":
    title = "Annual Safety Inspection Report"
    date = "2023-10-15"
    inspector = "John Doe"
    findings = ["Fire extinguisher expired", "Exit signs not illuminated"]
    recommendations = ["Replace fire extinguisher", "Install new exit signs"]
    path = os.path.join(os.getcwd(), "inspection_report.docx")
    
    create_inspection_report(title, date, inspector, findings, recommendations, path)
```
