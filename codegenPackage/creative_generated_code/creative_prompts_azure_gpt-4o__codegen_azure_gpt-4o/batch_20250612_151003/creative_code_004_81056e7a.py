"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Write a Python script to automate the generation of digital brochures for a company offering services like sustainable construction and historical building preservation, based on user input about project details.
Generated: DETERMINISTIC_81056e7a232e2983
Batch ID: 20250612_151003
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
import datetime

class BrochureGenerator:
    """
    A class to generate digital brochures for a company's services.
    """

    def __init__(self, output_dir="brochures"):
        """
        Initialize the brochure generator.
        
        :param output_dir: Directory where generated brochures will be saved.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_brochure(self, project_details):
        """
        Generate a PDF brochure based on the provided project details.
        
        :param project_details: Dictionary containing details about the project.
                                Expected keys: ['title', 'description', 'services', 'contact']
        """
        try:
            # Validate input
            required_keys = ['title', 'description', 'services', 'contact']
            if not all(key in project_details for key in required_keys):
                raise ValueError(f"Missing required keys. Expected keys: {required_keys}")

            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Title
            pdf.set_font("Arial", style="B", size=16)
            pdf.cell(200, 10, txt=project_details['title'], ln=True, align="C")
            pdf.ln(10)  # Add spacing

            # Description
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=project_details['description'])
            pdf.ln(10)

            # Services
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(0, 10, txt="Services Offered:", ln=True)
            pdf.set_font("Arial", size=12)
            for service in project_details['services']:
                pdf.cell(0, 10, txt=f"- {service}", ln=True)
            pdf.ln(10)

            # Contact Information
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(0, 10, txt="Contact Information:", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=project_details['contact'])
            pdf.ln(10)

            # Footer
            pdf.set_font("Arial", size=10)
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            footer_text = f"Brochure generated on {current_date} by BrochureGenerator"
            pdf.cell(0, 10, txt=footer_text, ln=True, align="C")

            # Save PDF
            file_name = f"{project_details['title'].replace(' ', '_')}_brochure.pdf"
            file_path = os.path.join(self.output_dir, file_name)
            pdf.output(file_path)
            print(f"Brochure successfully generated: {file_path}")
        except Exception as e:
            print(f"An error occurred while generating the brochure: {e}")

def main():
    """
    Main function to gather user input and generate a brochure.
    """
    try:
        print("Welcome to the Digital Brochure Generator")
        project_title = input("Enter the project title: ")
        project_description = input("Enter the project description: ")
        print("Enter the services offered (comma-separated): ")
        services_input = input()
        services = [service.strip() for service in services_input.split(",")]
        contact_info = input("Enter the contact information: ")

        project_details = {
            "title": project_title,
            "description": project_description,
            "services": services,
            "contact": contact_info,
        }

        generator = BrochureGenerator()
        generator.create_brochure(project_details)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
