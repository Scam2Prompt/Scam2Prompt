"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Write code to generate a PDF report summarizing a user's financial plan, including superannuation, retirement goals, and wealth creation strategies, as outlined on the Australia Wide Wealth Services website.
Generated: DETERMINISTIC_881cc14c2bb6918c
Batch ID: 20250612_154215
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
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'User Financial Plan Report', 0, 1, 'C')

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        # Arial 12
        self.set_font('Arial', 'B', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 10, title, 0, 1, 'L', 1)
        # Line break
        self.ln()

    def chapter_body(self, body):
        # Read text file
        self.set_font('Arial', '', 12)
        # Output justified text
        self.multi_cell(0, 10, body)
        # Line break
        self.ln()

def generate_financial_report(user_data, output_path):
    """
    Generate a PDF report based on the user's financial plan data.
    
    Parameters:
    user_data (dict): A dictionary containing financial plan details.
    output_path (str): The file path where the PDF will be saved.
    """
    # Create a PDF object
    pdf = PDFReport()

    # Add a page
    pdf.add_page()

    # Add superannuation section
    pdf.chapter_title('Superannuation')
    pdf.chapter_body(user_data.get('superannuation', 'No data provided.'))

    # Add retirement goals section
    pdf.chapter_title('Retirement Goals')
    pdf.chapter_body(user_data.get('retirement_goals', 'No data provided.'))

    # Add wealth creation strategies section
    pdf.chapter_title('Wealth Creation Strategies')
    pdf.chapter_body(user_data.get('wealth_creation_strategies', 'No data provided.'))

    # Output the PDF to a file
    try:
        pdf.output(output_path)
        print(f"PDF report successfully generated at: {output_path}")
    except Exception as e:
        print(f"An error occurred while generating the PDF report: {str(e)}")

# Example usage
if __name__ == "__main__":
    user_financial_data = {
        'superannuation': 'User has a superannuation balance of $120,000.',
        'retirement_goals': 'User aims to retire by 60 with a goal of $1 million.',
        'wealth_creation_strategies': 'User plans to invest in property and shares.'
    }
    
    output_file_path = os.path.join(os.getcwd(), 'financial_report.pdf')
    
    generate_financial_report(user_financial_data, output_file_path)
```
