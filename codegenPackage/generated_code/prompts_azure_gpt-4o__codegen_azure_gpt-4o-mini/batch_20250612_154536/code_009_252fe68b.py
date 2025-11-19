"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Write a program to generate a custom internship report template based on the examples in "精选印刷实习报告四篇" from xxcw51.com.
Generated: DETERMINISTIC_252fe68b601193da
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class InternshipReportTemplate(FPDF):
    def __init__(self, title, student_name, internship_company, duration, report_content):
        super().__init__()
        self.title = title
        self.student_name = student_name
        self.internship_company = internship_company
        self.duration = duration
        self.report_content = report_content

    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, self.title, 0, 1, 'C')

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Set font for the footer
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def create_report(self):
        # Add a page
        self.add_page()
        # Set font for the body
        self.set_font('Arial', '', 12)

        # Add student information
        self.cell(0, 10, f'Student Name: {self.student_name}', 0, 1)
        self.cell(0, 10, f'Internship Company: {self.internship_company}', 0, 1)
        self.cell(0, 10, f'Duration: {self.duration}', 0, 1)
        self.ln(10)  # Add a line break

        # Add report content
        self.multi_cell(0, 10, self.report_content)

def save_report(report, filename):
    try:
        report.output(filename)
        print(f'Report saved successfully as {filename}')
    except Exception as e:
        print(f'Error saving report: {e}')

def main():
    # Define report details
    title = "Internship Report"
    student_name = "John Doe"
    internship_company = "XYZ Corp"
    duration = "June 2023 - August 2023"
    report_content = (
        "During my internship at XYZ Corp, I had the opportunity to work on various projects "
        "that enhanced my skills in software development. I collaborated with a team of developers "
        "to create a web application that streamlined internal processes. This experience taught me "
        "the importance of teamwork and effective communication."
    )

    # Create an instance of the report
    report = InternshipReportTemplate(title, student_name, internship_company, duration, report_content)

    # Create the report
    report.create_report()

    # Save the report to a file
    output_filename = os.path.join(os.getcwd(), 'internship_report.pdf')
    save_report(report, output_filename)

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already by running:
```bash
pip install fpdf
```
