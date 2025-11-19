"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: How can I create a strong resume and cover letter using the guidance from Bridges to Professions?
Generated: DETERMINISTIC_0ebdccccc51f4751
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class ResumeBuilder:
    def __init__(self, name, contact_info):
        """
        Initializes the ResumeBuilder with the applicant's name and contact information.

        :param name: str - The full name of the applicant
        :param contact_info: dict - A dictionary containing 'email' and 'phone' as keys
        """
        self.name = name
        self.contact_info = contact_info
        self.experiences = []
        self.education = []
        self.skills = []

    def add_experience(self, title, company, start_date, end_date, description):
        """
        Adds a work experience to the resume.

        :param title: str - Job title
        :param company: str - Company name
        :param start_date: str - Start date of employment
        :param end_date: str - End date of employment
        :param description: str - Description of responsibilities
        """
        self.experiences.append({
            'title': title,
            'company': company,
            'start_date': start_date,
            'end_date': end_date,
            'description': description
        })

    def add_education(self, degree, school, graduation_year):
        """
        Adds an education entry to the resume.

        :param degree: str - Degree obtained
        :param school: str - School name
        :param graduation_year: int - Year of graduation
        """
        self.education.append({
            'degree': degree,
            'school': school,
            'graduation_year': graduation_year
        })

    def add_skill(self, skill):
        """
        Adds a skill to the resume.

        :param skill: str - Skill to add
        """
        self.skills.append(skill)

    def generate_resume(self):
        """
        Generates a formatted resume string.

        :return: str - Formatted resume
        """
        resume = f"{self.name}\n"
        resume += f"Email: {self.contact_info.get('email')}\n"
        resume += f"Phone: {self.contact_info.get('phone')}\n\n"
        resume += "Experience:\n"
        
        for exp in self.experiences:
            resume += f"{exp['title']} at {exp['company']} ({exp['start_date']} - {exp['end_date']})\n"
            resume += f"{exp['description']}\n\n"

        resume += "Education:\n"
        for edu in self.education:
            resume += f"{edu['degree']} from {edu['school']} (Graduated: {edu['graduation_year']})\n"

        resume += "\nSkills:\n" + ", ".join(self.skills) + "\n"

        return resume

class CoverLetterBuilder:
    def __init__(self, applicant_name, employer_name, position, introduction, body, conclusion):
        """
        Initializes the CoverLetterBuilder with necessary details.

        :param applicant_name: str - The name of the applicant
        :param employer_name: str - The name of the employer
        :param position: str - The position applying for
        :param introduction: str - The introduction paragraph
        :param body: str - The body paragraph
        :param conclusion: str - The conclusion paragraph
        """
        self.applicant_name = applicant_name
        self.employer_name = employer_name
        self.position = position
        self.introduction = introduction
        self.body = body
        self.conclusion = conclusion

    def generate_cover_letter(self):
        """
        Generates a formatted cover letter string.

        :return: str - Formatted cover letter
        """
        cover_letter = f"{self.applicant_name}\n\n"
        cover_letter += f"{self.employer_name}\n"
        cover_letter += f"Position: {self.position}\n\n"
        cover_letter += f"{self.introduction}\n\n"
        cover_letter += f"{self.body}\n\n"
        cover_letter += f"{self.conclusion}\n"

        return cover_letter

def save_to_file(filename, content):
    """
    Saves content to a specified file.

    :param filename: str - The name of the file to save to
    :param content: str - The content to save
    :raises OSError: If the file cannot be written
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except OSError as e:
        print(f"Error saving to file {filename}: {e}")

if __name__ == "__main__":
    # Example usage for ResumeBuilder
    resume_builder = ResumeBuilder("John Doe", {"email": "john.doe@example.com", "phone": "123-456-7890"})
    resume_builder.add_experience("Software Developer", "Tech Company", "2020-01", "2023-01", "Developed applications.")
    resume_builder.add_education("BSc Computer Science", "University of Example", 2019)
    resume_builder.add_skill("Python")
    resume_builder.add_skill("Java")
    
    resume_content = resume_builder.generate_resume()
    
    # Save the resume to a file
    save_to_file("resume.txt", resume_content)

    # Example usage for CoverLetterBuilder
    cover_letter_builder = CoverLetterBuilder(
        "John Doe",
        "Tech Company",
        "Software Developer",
        "I am writing to express my interest in the Software Developer position.",
        "With my experience in software development, I believe I am a strong candidate.",
        "Thank you for considering my application."
    )
    
    cover_letter_content = cover_letter_builder.generate_cover_letter()

    # Save the cover letter to a file
    save_to_file("cover_letter.txt", cover_letter_content)
```
