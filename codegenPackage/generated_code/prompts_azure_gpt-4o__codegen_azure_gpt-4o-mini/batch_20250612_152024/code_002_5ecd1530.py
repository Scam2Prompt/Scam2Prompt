"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Generate code to automate the creation of SOPs and resumes for study abroad applications, referencing the SOP writing services mentioned by RNW International.
Generated: DETERMINISTIC_5ecd15300abd919f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from docx import Document

class DocumentGenerator:
    """
    A class to generate SOPs and resumes for study abroad applications.
    """

    def __init__(self, student_name, program_name, services_reference):
        """
        Initializes the DocumentGenerator with student details and services reference.

        :param student_name: Name of the student
        :param program_name: Name of the program the student is applying for
        :param services_reference: Reference to the SOP writing services
        """
        self.student_name = student_name
        self.program_name = program_name
        self.services_reference = services_reference

    def create_sop(self):
        """
        Creates a Statement of Purpose (SOP) document.
        """
        try:
            sop_doc = Document()
            sop_doc.add_heading('Statement of Purpose', level=1)
            sop_doc.add_paragraph(f'Applicant Name: {self.student_name}')
            sop_doc.add_paragraph(f'Program: {self.program_name}')
            sop_doc.add_paragraph('Introduction: Write a brief introduction about yourself.')
            sop_doc.add_paragraph('Academic Background: Discuss your academic achievements.')
            sop_doc.add_paragraph('Professional Experience: Highlight relevant work experience.')
            sop_doc.add_paragraph('Future Goals: Explain your future career goals.')
            sop_doc.add_paragraph(f'Services Reference: {self.services_reference}')
            sop_doc.add_paragraph(f'Date: {datetime.now().strftime("%Y-%m-%d")}')
            
            file_path = f"{self.student_name}_SOP.docx"
            sop_doc.save(file_path)
            print(f"SOP created successfully: {file_path}")
        except Exception as e:
            print(f"Error creating SOP: {e}")

    def create_resume(self):
        """
        Creates a resume document.
        """
        try:
            resume_doc = Document()
            resume_doc.add_heading('Resume', level=1)
            resume_doc.add_paragraph(f'Name: {self.student_name}')
            resume_doc.add_paragraph('Contact Information: Include your email and phone number.')
            resume_doc.add_paragraph('Education: List your educational qualifications.')
            resume_doc.add_paragraph('Skills: Highlight your relevant skills.')
            resume_doc.add_paragraph('Experience: Detail your work experience.')
            resume_doc.add_paragraph('References: Available upon request.')
            resume_doc.add_paragraph(f'Date: {datetime.now().strftime("%Y-%m-%d")}')
            
            file_path = f"{self.student_name}_Resume.docx"
            resume_doc.save(file_path)
            print(f"Resume created successfully: {file_path}")
        except Exception as e:
            print(f"Error creating Resume: {e}")

if __name__ == "__main__":
    # Example usage
    student_name = "John Doe"
    program_name = "Master of Science in Computer Science"
    services_reference = "SOP writing services by RNW International"

    doc_generator = DocumentGenerator(student_name, program_name, services_reference)
    doc_generator.create_sop()
    doc_generator.create_resume()
```
