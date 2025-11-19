"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Generate a CV for a PhD candidate in Civil Engineering, including research experience, education, and skills, similar to Akash Yadav's profile.
Generated: DETERMINISTIC_28f5f6fc6e8485c5
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class CV:
    def __init__(self, name, contact_info, education, research_experience, skills):
        """
        Initialize the CV with personal details, education, research experience, and skills.

        :param name: str - Full name of the candidate
        :param contact_info: dict - Contact information including email and phone
        :param education: list - List of education details
        :param research_experience: list - List of research experiences
        :param skills: list - List of skills
        """
        self.name = name
        self.contact_info = contact_info
        self.education = education
        self.research_experience = research_experience
        self.skills = skills

    def generate_cv(self):
        """
        Generate a formatted CV as a string.

        :return: str - Formatted CV
        """
        cv_content = f"Curriculum Vitae\n\nName: {self.name}\n"
        cv_content += f"Contact Information: {self.contact_info['email']}, {self.contact_info['phone']}\n\n"
        cv_content += "Education:\n"
        for edu in self.education:
            cv_content += f"- {edu['degree']} in {edu['field']} from {edu['institution']} ({edu['year']})\n"
        
        cv_content += "\nResearch Experience:\n"
        for research in self.research_experience:
            cv_content += f"- {research['title']} at {research['institution']} ({research['year']})\n"
        
        cv_content += "\nSkills:\n"
        cv_content += ", ".join(self.skills) + "\n"
        
        return cv_content

    def save_to_file(self, filename):
        """
        Save the CV to a text file.

        :param filename: str - The name of the file to save the CV
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_cv())
            print(f"CV saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving CV to file: {e}")

# Example usage
if __name__ == "__main__":
    # Candidate details
    candidate_name = "Akash Yadav"
    candidate_contact_info = {
        "email": "akash.yadav@example.com",
        "phone": "+1234567890"
    }
    candidate_education = [
        {"degree": "PhD", "field": "Civil Engineering", "institution": "XYZ University", "year": 2023},
        {"degree": "MSc", "field": "Structural Engineering", "institution": "ABC University", "year": 2019},
        {"degree": "BEng", "field": "Civil Engineering", "institution": "DEF University", "year": 2017}
    ]
    candidate_research_experience = [
        {"title": "Research Assistant", "institution": "XYZ University", "year": "2020-2023"},
        {"title": "Intern", "institution": "GHI Engineering Firm", "year": "2018"}
    ]
    candidate_skills = ["Structural Analysis", "Project Management", "AutoCAD", "MATLAB", "Geotechnical Engineering"]

    # Create CV instance
    akash_cv = CV(candidate_name, candidate_contact_info, candidate_education, candidate_research_experience, candidate_skills)

    # Generate and save CV
    akash_cv.save_to_file("Akash_Yadav_CV.txt")
```
