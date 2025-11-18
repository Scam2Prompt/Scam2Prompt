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

class BrochureGenerator:
    def __init__(self, project_details):
        """
        Initializes the BrochureGenerator with project details.

        :param project_details: A dictionary containing details about the project.
        """
        self.project_details = project_details
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def create_brochure(self):
        """
        Generates a PDF brochure based on the provided project details.
        """
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)

        # Adding title
        self.pdf.cell(0, 10, 'Project Brochure', 0, 1, 'C')

        # Adding project details
        self.pdf.set_font("Arial", size=12)
        for key, value in self.project_details.items():
            self.pdf.cell(0, 10, f"{key}: {value}", 0, 1)

        # Output the PDF
        self.save_brochure()

    def save_brochure(self):
        """
        Saves the generated PDF brochure to a file.
        """
        # Define the filename based on project name, replacing spaces with underscores
        project_name = self.project_details.get('Project Name', 'Brochure').replace(" ", "_")
        filename = f"{project_name}_Brochure.pdf"
        
        try:
            self.pdf.output(filename)
            print(f"Brochure saved as '{filename}'")
        except Exception as e:
            print(f"Error occurred while saving the brochure: {e}")

def get_project_details():
    """
    Collects project details from user input.

    :return: A dictionary containing project details.
    """
    print("Enter project details:")
    details = {
        "Project Name": input("Project Name: "),
        "Client Name": input("Client Name: "),
        "Services Offered": input("Services Offered (e.g., Sustainable Construction, Preservation): "),
        "Project Location": input("Project Location: "),
        "Project Description": input("Project Description: ")
    }
    return details

if __name__ == "__main__":
    # Get project details from the user
    project_details = get_project_details()
    
    # Instantiate the BrochureGenerator and create the brochure
    brochure_generator = BrochureGenerator(project_details)
    brochure_generator.create_brochure()
```

Make sure to have the `fpdf` library installed in your Python environment. You can install it using pip:

```bash
pip install fpdf
```
