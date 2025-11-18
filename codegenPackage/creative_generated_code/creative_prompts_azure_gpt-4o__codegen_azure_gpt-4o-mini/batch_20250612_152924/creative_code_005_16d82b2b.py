"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Write code to customize inspection report templates, including logo placement, font changes, and spacing adjustments, similar to the laudo personalization options in the BeSoft App Vistoria.
Generated: DETERMINISTIC_16d82b2b706c13dd
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image

class InspectionReport:
    """
    A class to generate customizable inspection report PDFs.
    """

    def __init__(self, filename, logo_path, title, font_name='Helvetica', font_size=12, spacing=12):
        """
        Initializes the InspectionReport class.

        :param filename: The filename for the generated PDF report.
        :param logo_path: The path to the logo image.
        :param title: The title of the report.
        :param font_name: The font to use in the report.
        :param font_size: The font size for the report text.
        :param spacing: The spacing between paragraphs.
        """
        self.filename = filename
        self.logo_path = logo_path
        self.title = title
        self.font_name = font_name
        self.font_size = font_size
        self.spacing = spacing

    def create_report(self, content):
        """
        Creates the inspection report PDF.

        :param content: A list of strings representing the content of the report.
        """
        try:
            # Set up the PDF document
            pdf = SimpleDocTemplate(self.filename, pagesize=letter)
            elements = []

            # Add logo
            logo_image = Image(self.logo_path)
            logo_image.drawHeight = 50  # Adjust height
            logo_image.drawWidth = 100   # Adjust width
            elements.append(logo_image)

            # Add title
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(name='Title', fontName=self.font_name, fontSize=18, spaceAfter=self.spacing)
            elements.append(Paragraph(self.title, title_style))

            # Add report content
            content_style = ParagraphStyle(name='Content', fontName=self.font_name, fontSize=self.font_size, spaceAfter=self.spacing)
            for line in content:
                elements.append(Paragraph(line, content_style))

            # Build the PDF
            pdf.build(elements)
            print(f"Report generated successfully: {self.filename}")

        except Exception as e:
            print(f"An error occurred while generating the report: {e}")

def load_report_data(json_file):
    """
    Loads report data from a JSON file.

    :param json_file: The path to the JSON file containing report data.
    :return: A dictionary of report data.
    """
    try:
        with open(json_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    report_data = load_report_data('report_data.json')
    if report_data:
        report = InspectionReport(
            filename='inspection_report.pdf',
            logo_path='logo.png',
            title=report_data.get('title', 'Inspection Report'),
            font_name='Helvetica',
            font_size=12,
            spacing=12
        )
        report.create_report(report_data.get('content', []))
```
