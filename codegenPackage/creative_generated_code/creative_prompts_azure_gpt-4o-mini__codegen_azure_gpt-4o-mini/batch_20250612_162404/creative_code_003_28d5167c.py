"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Generate a detailed report template that mimics the 10-page evaluation report provided to participants in the Proof of Pitch competition.
Generated: DETERMINISTIC_28d5167cfabc30a0
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF

class PDFReport(FPDF):
    """PDFReport class to generate a structured PDF report."""

    def header(self):
        """Add a header to each page."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Proof of Pitch Competition Evaluation Report', 0, 1, 'C')

    def footer(self):
        """Add a footer to each page."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        """Add a chapter title."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        """Add a chapter body text."""
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_evaluation_report(filename):
    """Create a detailed evaluation report in PDF format."""
    pdf = PDFReport()
    
    # Add a page
    pdf.add_page()
    
    # Title Section
    pdf.chapter_title('Participant Information')
    pdf.chapter_body('Name: [Participant Name]\nContact: [Participant Contact]\nOrganization: [Organization Name]\nDate: [Evaluation Date]')
    
    # Evaluation Criteria
    pdf.chapter_title('Evaluation Criteria')
    criteria = [
        "1. Idea Originality: [Score]\nComments: [Comments]",
        "2. Market Viability: [Score]\nComments: [Comments]",
        "3. Presentation Clarity: [Score]\nComments: [Comments]",
        "4. Team Capability: [Score]\nComments: [Comments]",
        "5. Financial Projection: [Score]\nComments: [Comments]"
    ]
    pdf.chapter_body('\n'.join(criteria))
    
    # Overall Assessment
    pdf.chapter_title('Overall Assessment')
    pdf.chapter_body('Overall Score: [Total Score]\nOverall Comments: [Comments]')

    # Next Page for Detailed Feedback
    pdf.add_page()
    
    pdf.chapter_title('Detailed Feedback')
    detailed_feedback = (
        "1. Strengths:\n   - [Strength 1]\n   - [Strength 2]\n\n"
        "2. Areas for Improvement:\n   - [Improvement 1]\n   - [Improvement 2]\n\n"
        "3. Additional Comments:\n   - [Comments]"
    )
    pdf.chapter_body(detailed_feedback)

    # Save the PDF
    try:
        pdf.output(filename)
        print(f"Report successfully created: {filename}")
    except Exception as e:
        print(f"Failed to create report: {e}")

if __name__ == "__main__":
    # Ensure the output directory exists
    output_dir = "reports"
    os.makedirs(output_dir, exist_ok=True)

    report_filename = os.path.join(output_dir, "evaluation_report.pdf")
    create_evaluation_report(report_filename)
```
