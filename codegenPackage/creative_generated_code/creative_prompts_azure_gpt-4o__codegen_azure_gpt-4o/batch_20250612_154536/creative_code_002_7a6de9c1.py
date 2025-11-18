"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xxcw51.com
Prompt: Recommend libraries or APIs to programmatically generate formatted reports similar to the "汽修毕业实习报告6篇" examples on xxcw51.com.
Generated: DETERMINISTIC_7a6de9c171cb4a8e
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code that fulfills your request. It uses the `ReportLab` library to programmatically generate formatted PDF reports. This library is well-suited for this task and widely used in production environments.

```python
# Import necessary libraries
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, sections):
    """
    Generate a formatted PDF report.

    Args:
        filename (str): Name of the PDF file to be generated.
        title (str): Title of the report.
        sections (list of dict): Sections in the report, 
                                 each with 'header' and 'content' keys.

    """
    try:
        # Create the PDF document
        doc = SimpleDocTemplate(filename, pagesize=A4)

        # Get standard styles for text and formatting
        styles = getSampleStyleSheet()

        # List to hold elements for the document
        elements = []

        # Add the title to the document
        title_style = styles['Title']
        title_paragraph = Paragraph(title, title_style)
        elements.append(title_paragraph)

        # Add a blank space after the title
        elements.append(Paragraph("<br/><br/>", styles['Normal']))

        # Add each section to the report
        for section in sections:
            # Add the section header
            header_style = styles['Heading2']
            header_paragraph = Paragraph(section['header'], header_style)
            elements.append(header_paragraph)

            # Add the section content
            content_style = styles['BodyText']
            content_paragraph = Paragraph(section['content'], content_style)
            elements.append(content_paragraph)

            # Add a blank space after each section
            elements.append(Paragraph("<br/><br/>", styles['Normal']))

        # Build the document with all the elements
        doc.build(elements)

        print(f"Report '{filename}' generated successfully!")

    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

# Example usage:
if __name__ == "__main__":
    # Define sections for the report
    report_sections = [
        {
            "header": "Introduction",
            "content": "This is the introduction of the report."
        },
        {
            "header": "Objectives",
            "content": "The objectives of this internship include gaining practical experience."
        },
        {
            "header": "Conclusion",
            "content": "The internship was successful and provided valuable insights."
        }
    ]

    # Generate the report
    generate_report("internship_report.pdf", "汽修毕业实习报告", report_sections)
```

You'll need to install the `reportlab` library if you haven't already:

```bash
pip install reportlab
```
