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
from docx import Document
from datetime import datetime

# Define constants
OUTPUT_DIR = "Generated_Documents"
DATE_FORMAT = "%Y-%m-%d"

class DocumentGenerator:
    """
    A class to automate creation of SOPs and resumes for study abroad applications.
    """

    def __init__(self):
        """
        Initialize the DocumentGenerator instance and ensure the output directory exists.
        """
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def generate_sop(self, name, university, program, personal_statement):
        """
        Generate a Statement of Purpose (SOP) document.

        :param name: Name of the applicant
        :param university: Target university for application
        :param program: Target program for application
        :param personal_statement: Personal statement provided by the applicant
        :return: Path to the generated SOP document
        """
        try:
            document = Document()
            
            # Add title
            document.add_heading(f"Statement of Purpose - {name}", level=1)

            # Add content
            document.add_paragraph(f"To: The Admissions Committee at {university}")
            document.add_paragraph(f"Subject: Application to {program}")
            document.add_paragraph(personal_statement)

            # Add footer section
            date_str = datetime.now().strftime(DATE_FORMAT)
            document.add_paragraph(f"Generated on: {date_str}")

            # Save the SOP document
            sop_filename = f"SOP_{name.replace(' ', '_')}_{university.replace(' ', '_')}.docx"
            sop_filepath = os.path.join(OUTPUT_DIR, sop_filename)
            document.save(sop_filepath)

            return sop_filepath
        except Exception as e:
            raise Exception(f"Error generating SOP: {e}")

    def generate_resume(self, name, contact_info, education, work_experience, skills):
        """
        Generate a Resume document.

        :param name: Name of the applicant
        :param contact_info: Contact information of the applicant
        :param education: Education details of the applicant
        :param work_experience: Work experience details of the applicant
        :param skills: Skills possessed by the applicant
        :return: Path to the generated Resume document
        """
        try:
            document = Document()
            
            # Add title
            document.add_heading(f"Resume - {name}", level=1)

            # Add contact information
            document.add_heading("Contact Information", level=2)
            document.add_paragraph(contact_info)

            # Add education section
            document.add_heading("Education", level=2)
            for edu in education:
                document.add_paragraph(edu)

            # Add work experience section
            document.add_heading("Work Experience", level=2)
            for exp in work_experience:
                document.add_paragraph(exp)

            # Add skills section
            document.add_heading("Skills", level=2)
            for skill in skills:
                document.add_paragraph(skill)

            # Save the Resume document
            resume_filename = f"Resume_{name.replace(' ', '_')}.docx"
            resume_filepath = os.path.join(OUTPUT_DIR, resume_filename)
            document.save(resume_filepath)

            return resume_filepath
        except Exception as e:
            raise Exception(f"Error generating Resume: {e}")


# Example usage
if __name__ == "__main__":
    try:
        generator = DocumentGenerator()

        # Generate SOP
        sop_path = generator.generate_sop(
            name="John Doe",
            university="Example University",
            program="Master of Computer Science",
            personal_statement="I am passionate about leveraging technology to solve global challenges..."
        )
        print(f"SOP generated at: {sop_path}")

        # Generate Resume
        resume_path = generator.generate_resume(
            name="John Doe",
            contact_info="Email: john.doe@example.com | Phone: +123456789",
            education=[
                "B.Sc. Computer Science - Example University (2018-2022)",
                "High School Diploma - Example High School (2016-2018)"
            ],
            work_experience=[
                "Software Engineer at TechCorp (2022-Present)",
                "Intern at DevWorks (2021-2022)"
            ],
            skills=[
                "Python, Java, C++",
                "Machine Learning and AI",
                "Effective communication and teamwork"
            ]
        )
        print(f"Resume generated at: {resume_path}")

    except Exception as error:
        print(f"An error occurred: {error}")
```
