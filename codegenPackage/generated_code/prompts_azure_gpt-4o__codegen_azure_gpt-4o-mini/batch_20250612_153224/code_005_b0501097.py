"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Write a script to generate PDF documents for student constancy requests, incorporating the processing time requirements specified on the Escuela Preparatoria Oficial N.73 FAQ page.
Generated: DETERMINISTIC_b05010975890a2ae
Batch ID: 20250612_153224
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
from datetime import datetime, timedelta

class PDFGenerator:
    def __init__(self, student_name, request_date, processing_time_days):
        """
        Initialize the PDFGenerator with student details and processing time.

        :param student_name: Name of the student
        :param request_date: Date of the request
        :param processing_time_days: Number of days required for processing
        """
        self.student_name = student_name
        self.request_date = request_date
        self.processing_time_days = processing_time_days
        self.pdf = FPDF()

    def create_pdf(self):
        """
        Create a PDF document for the student constancy request.
        """
        try:
            self.pdf.add_page()
            self.pdf.set_font("Arial", size=12)

            # Add title
            self.pdf.cell(200, 10, txt="Constancy Request", ln=True, align='C')

            # Add student details
            self.pdf.cell(200, 10, txt=f"Student Name: {self.student_name}", ln=True)
            self.pdf.cell(200, 10, txt=f"Request Date: {self.request_date.strftime('%Y-%m-%d')}", ln=True)

            # Calculate and add processing time
            processing_end_date = self.request_date + timedelta(days=self.processing_time_days)
            self.pdf.cell(200, 10, txt=f"Processing Time: {self.processing_time_days} days", ln=True)
            self.pdf.cell(200, 10, txt=f"Expected Completion Date: {processing_end_date.strftime('%Y-%m-%d')}", ln=True)

            # Save the PDF to a file
            output_filename = f"{self.student_name.replace(' ', '_')}_constancy_request.pdf"
            self.pdf.output(output_filename)
            print(f"PDF generated successfully: {output_filename}")

        except Exception as e:
            print(f"An error occurred while generating the PDF: {e}")

def main():
    """
    Main function to execute the PDF generation process.
    """
    # Example student data
    student_name = "John Doe"
    request_date = datetime.now()  # Current date
    processing_time_days = 5  # Example processing time

    # Create PDF generator instance
    pdf_generator = PDFGenerator(student_name, request_date, processing_time_days)

    # Generate the PDF
    pdf_generator.create_pdf()

if __name__ == "__main__":
    main()
```

### Requirements:
- Ensure you have the `fpdf` library installed. You can install it using:
  ```bash
  pip install fpdf
  ```
