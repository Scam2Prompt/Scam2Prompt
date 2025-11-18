"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Generate code to automate the creation of SOPs and resumes for study abroad applications, referencing the SOP writing services mentioned by RNW International.
Generated: DETERMINISTIC_5ecd15300abd919f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from typing import List, Dict
from docx import Document

class DocumentGenerator:
    """
    A class to generate Standard Operating Procedures (SOPs) and Resumes for study abroad applications.
    """

    def __init__(self, service_reference: str):
        """
        Initializes the DocumentGenerator with a reference to the writing service.

        :param service_reference: A string reference for the SOP writing service.
        """
        self.service_reference = service_reference

    def create_sop(self, content: Dict[str, str], file_path: str) -> None:
        """
        Creates a SOP document based on provided content.

        :param content: A dictionary containing SOP content elements.
        :param file_path: The file path where the SOP document will be saved.
        """
        try:
            doc = Document()
            doc.add_heading('Statement of Purpose', level=1)

            for section, text in content.items():
                doc.add_heading(section, level=2)
                doc.add_paragraph(text)

            doc.add_paragraph(f"\nFor professional assistance, consider using the SOP writing services by {self.service_reference}.")
            doc.save(file_path)
            print(f"SOP saved to {file_path}")

        except Exception as e:
            print(f"An error occurred while creating the SOP: {e}")

    def create_resume(self, personal_info: Dict[str, str], education: List[Dict[str, str]], file_path: str) -> None:
        """
        Creates a Resume document based on provided personal information and education.

        :param personal_info: A dictionary containing personal details.
        :param education: A list of dictionaries containing educational qualifications.
        :param file_path: The file path where the Resume document will be saved.
        """
        try:
            doc = Document()
            doc.add_heading('Resume', level=1)

            # Personal Information
            doc.add_heading('Personal Information', level=2)
            for key, value in personal_info.items():
                doc.add_paragraph(f"{key}: {value}")

            # Education
            doc.add_heading('Education', level=2)
            for edu in education:
                doc.add_paragraph(f"{edu['degree']} in {edu['field']} from {edu['institution']} ({edu['year']})")

            doc.add_paragraph(f"\nFor personalized resume writing services, visit {self.service_reference}.")
            doc.save(file_path)
            print(f"Resume saved to {file_path}")

        except Exception as e:
            print(f"An error occurred while creating the Resume: {e}")

def main():
    """
    Main function to demonstrate the usage of the DocumentGenerator class.
    """
    service_reference = "RNW International"
    generator = DocumentGenerator(service_reference)

    # Sample SOP content
    sop_content = {
        "Introduction": "I am passionate about pursuing further studies...",
        "Academic Background": "I completed my undergraduate studies in Computer Science...",
        "Career Goals": "My long-term goal is to become a software engineer...",
        "Conclusion": "In conclusion, I believe that studying abroad will enhance my capabilities..."
    }

    # File paths for generated documents
    sop_file_path = os.path.join(os.getcwd(), 'sop.docx')
    resume_file_path = os.path.join(os.getcwd(), 'resume.docx')

    # Sample Resume content
    personal_info = {
        "Name": "John Doe",
        "Email": "john.doe@example.com",
        "Phone": "+1234567890"
    }

    education = [
        {"degree": "Bachelor of Technology", "field": "Computer Science", "institution": "XYZ University", "year": "2023"},
        {"degree": "High School Diploma", "field": "Science", "institution": "ABC High School", "year": "2019"}
    ]

    # Create SOP and Resume
    generator.create_sop(sop_content, sop_file_path)
    generator.create_resume(personal_info, education, resume_file_path)

if __name__ == "__main__":
    main()
```
