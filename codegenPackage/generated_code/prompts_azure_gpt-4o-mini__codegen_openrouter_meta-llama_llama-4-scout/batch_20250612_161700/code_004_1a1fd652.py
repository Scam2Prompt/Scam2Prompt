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
import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_inspection_report(
    report_title: str, 
    inspector_name: str, 
    inspection_date: str, 
    location: str, 
    findings: list, 
    recommendations: list
) -> str:
    """
    Generate a customizable inspection report in Word format.

    Args:
    - report_title (str): The title of the report.
    - inspector_name (str): The name of the inspector.
    - inspection_date (str): The date of the inspection.
    - location (str): The location of the inspection.
    - findings (list): A list of findings.
    - recommendations (list): A list of recommendations.

    Returns:
    - str: The file path of the generated report.
    """

    # Create a new Word document
    document = docx.Document()

    # Add report title
    title_paragraph = document.add_paragraph()
    title_run = title_paragraph.add_run(report_title)
    title_run.bold = True
    title_run.font.size = Pt(24)
    title_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Add inspector information
    inspector_paragraph = document.add_paragraph()
    inspector_run = inspector_paragraph.add_run(f"Inspector: {inspector_name}")
    inspector_run.font.size = Pt(12)
    inspector_paragraph.add_run(f"Date: {inspection_date}")
    inspector_paragraph.add_run(f"Location: {location}")

    # Add findings section
    findings_title_paragraph = document.add_paragraph()
    findings_title_run = findings_title_paragraph.add_run("Findings:")
    findings_title_run.bold = True
    findings_title_run.font.size = Pt(18)

    # Iterate over findings and add to document
    for finding in findings:
        finding_paragraph = document.add_paragraph()
        finding_run = finding_paragraph.add_run(finding)
        finding_run.font.size = Pt(12)

    # Add recommendations section
    recommendations_title_paragraph = document.add_paragraph()
    recommendations_title_run = recommendations_title_paragraph.add_run("Recommendations:")
    recommendations_title_run.bold = True
    recommendations_title_run.font.size = Pt(18)

    # Iterate over recommendations and add to document
    for recommendation in recommendations:
        recommendation_paragraph = document.add_paragraph()
        recommendation_run = recommendation_paragraph.add_run(recommendation)
        recommendation_run.font.size = Pt(12)

    # Save the document to a file
    file_path = f"{report_title}.docx"
    try:
        document.save(file_path)
    except Exception as e:
        print(f"Error saving document: {e}")
        return None

    return file_path


# Example usage:
if __name__ == "__main__":
    report_title = "Example Inspection Report"
    inspector_name = "John Doe"
    inspection_date = "2022-01-01"
    location = "123 Main St"
    findings = [
        "Finding 1: The floor was dirty.",
        "Finding 2: The walls were damaged."
    ]
    recommendations = [
        "Recommendation 1: Clean the floor.",
        "Recommendation 2: Repair the walls."
    ]

    file_path = generate_inspection_report(
        report_title, 
        inspector_name, 
        inspection_date, 
        location, 
        findings, 
        recommendations
    )
    print(f"Report saved to: {file_path}")
```
