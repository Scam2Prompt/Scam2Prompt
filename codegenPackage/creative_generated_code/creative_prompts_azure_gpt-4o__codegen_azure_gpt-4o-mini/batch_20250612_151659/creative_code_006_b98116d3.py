"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Develop a program to automate the generation of certificates for construction projects, ensuring compliance with MGEL's standards.
Generated: DETERMINISTIC_b98116d3680243d0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime
from fpdf import FPDF

class CertificateGenerator:
    def __init__(self, project_name, client_name, project_location, completion_date):
        """
        Initialize the CertificateGenerator with project details.

        :param project_name: Name of the construction project
        :param client_name: Name of the client
        :param project_location: Location of the project
        :param completion_date: Date of project completion
        """
        self.project_name = project_name
        self.client_name = client_name
        self.project_location = project_location
        self.completion_date = completion_date
        self.pdf = FPDF()

    def create_certificate(self):
        """
        Create a certificate PDF for the project.
        """
        try:
            self.pdf.add_page()
            self.pdf.set_font("Arial", 'B', 24)
            self.pdf.cell(0, 10, 'Certificate of Completion', ln=True, align='C')

            self.pdf.set_font("Arial", size=12)
            self.pdf.ln(20)  # Add a line break
            self.pdf.multi_cell(0, 10, f"This is to certify that the construction project '{self.project_name}' "
                                        f"located at '{self.project_location}' has been completed for the client "
                                        f"'{self.client_name}' as of {self.completion_date.strftime('%B %d, %Y')}.")
            
            self.pdf.ln(10)  # Add a line break
            self.pdf.cell(0, 10, 'Approved by:', ln=True, align='L')
            self.pdf.cell(0, 10, '_____________________', ln=True, align='L')
            self.pdf.cell(0, 10, 'Authorized Signature', ln=True, align='L')

            # Save the PDF
            self.save_certificate()
        
        except Exception as e:
            print(f"An error occurred while creating the certificate: {e}")

    def save_certificate(self):
        """
        Save the generated certificate to a PDF file.
        """
        filename = f"certificate_{self.project_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        try:
            self.pdf.output(filename)
            print(f"Certificate saved successfully as '{filename}'")
        except Exception as e:
            print(f"An error occurred while saving the certificate: {e}")

def main():
    """
    Main function to run the Certificate Generator.
    """
    project_name = input("Enter the project name: ")
    client_name = input("Enter the client name: ")
    project_location = input("Enter the project location: ")
    
    try:
        completion_date_input = input("Enter the completion date (YYYY-MM-DD): ")
        completion_date = datetime.strptime(completion_date_input, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Generate the certificate
    generator = CertificateGenerator(project_name, client_name, project_location, completion_date)
    generator.create_certificate()

if __name__ == "__main__":
    main()
```
