"""
Generated Code Metadata:
========================
Original URL: https://daddys-universitys.com
Prompt: Write a Python script to automate the generation of digital brochures for a company offering services like sustainable construction and historical building preservation, based on user input about project details.
Generated: DETERMINISTIC_81056e7a232e2983
Batch ID: 20250612_151003
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

class BrochureGenerator:
    def __init__(self, company_name, services):
        """
        Initialize the BrochureGenerator with company name and services offered.

        :param company_name: Name of the company
        :param services: List of services offered by the company
        """
        self.company_name = company_name
        self.services = services

    def create_brochure(self, project_details):
        """
        Create a digital brochure based on project details.

        :param project_details: Dictionary containing project information
        :return: Path to the generated brochure PDF
        """
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()

            # Set title
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, f"{self.company_name} - Project Brochure", ln=True, align='C')

            # Add project details
            pdf.set_font("Arial", size=12)
            for key, value in project_details.items():
                pdf.cell(0, 10, f"{key}: {value}", ln=True)

            # Add services offered
            pdf.cell(0, 10, "Services Offered:", ln=True)
            for service in self.services:
                pdf.cell(0, 10, f"- {service}", ln=True)

            # Save the PDF to a file
            brochure_path = f"{project_details.get('Project Name', 'Brochure')}.pdf"
            pdf.output(brochure_path)

            return brochure_path

        except Exception as e:
            print(f"An error occurred while creating the brochure: {e}")
            return None

def main():
    # Company information
    company_name = "EcoBuild Solutions"
    services = [
        "Sustainable Construction",
        "Historical Building Preservation",
        "Energy Efficiency Consulting",
        "Green Roof Installation"
    ]

    # Initialize the brochure generator
    brochure_generator = BrochureGenerator(company_name, services)

    # User input for project details
    project_details = {
        "Project Name": input("Enter the project name: "),
        "Client Name": input("Enter the client's name: "),
        "Project Location": input("Enter the project location: "),
        "Project Description": input("Enter a brief project description: "),
        "Start Date": input("Enter the project start date: "),
        "End Date": input("Enter the project end date: ")
    }

    # Generate the brochure
    brochure_path = brochure_generator.create_brochure(project_details)

    if brochure_path:
        print(f"Brochure created successfully: {brochure_path}")
    else:
        print("Failed to create the brochure.")

if __name__ == "__main__":
    main()
```

### Requirements
To run this script, ensure you have the `fpdf` library installed. You can install it using pip:

```bash
pip install fpdf
```
