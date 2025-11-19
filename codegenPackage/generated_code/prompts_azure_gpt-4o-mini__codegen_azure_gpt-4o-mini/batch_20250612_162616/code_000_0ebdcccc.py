"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: How can I create a strong resume and cover letter using the guidance from Bridges to Professions?
Generated: DETERMINISTIC_0ebdccccc51f4751
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

class ResumeBuilder:
    """
    A class to create a strong resume and cover letter using guidance from Bridges to Professions.
    """

    def __init__(self, name, contact_info, education, experience, skills):
        """
        Initializes the ResumeBuilder with personal information.

        :param name: str - The name of the individual
        :param contact_info: dict - A dictionary containing contact information
        :param education: list - A list of educational qualifications
        :param experience: list - A list of work experiences
        :param skills: list - A list of skills
        """
        self.name = name
        self.contact_info = contact_info
        self.education = education
        self.experience = experience
        self.skills = skills

    def generate_resume(self):
        """
        Generates a formatted resume as a string.

        :return: str - The formatted resume
        """
        resume = f"Resume for {self.name}\n"
        resume += f"Contact Information: {self.contact_info['email']}, {self.contact_info['phone']}\n\n"
        resume += "Education:\n"
        for edu in self.education:
            resume += f"- {edu}\n"
        resume += "\nExperience:\n"
        for exp in self.experience:
            resume += f"- {exp}\n"
        resume += "\nSkills:\n"
        for skill in self.skills:
            resume += f"- {skill}\n"
        return resume

    def generate_cover_letter(self, job_title, company_name):
        """
        Generates a cover letter for a specific job application.

        :param job_title: str - The title of the job being applied for
        :param company_name: str - The name of the company
        :return: str - The formatted cover letter
        """
        cover_letter = f"Dear Hiring Manager,\n\n"
        cover_letter += f"I am writing to express my interest in the {job_title} position at {company_name}.\n"
        cover_letter += f"My background in {', '.join(self.skills)} makes me a suitable candidate for this role.\n"
        cover_letter += "I look forward to the opportunity to discuss my qualifications further.\n\n"
        cover_letter += "Sincerely,\n"
        cover_letter += self.name
        return cover_letter

    def save_to_file(self, filename, content):
        """
        Saves the generated content to a specified file.

        :param filename: str - The name of the file to save the content
        :param content: str - The content to save
        """
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"Content successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")

# Example usage
if __name__ == "__main__":
    # User's personal information
    user_name = "John Doe"
    user_contact_info = {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    user_education = [
        "B.S. in Computer Science, University of Example, 2020",
        "M.S. in Software Engineering, University of Example, 2022"
    ]
    user_experience = [
        "Software Developer at Example Corp (2020-2022)",
        "Senior Developer at Example Solutions (2022-Present)"
    ]
    user_skills = [
        "Python", "Java", "C++", "Project Management"
    ]

    # Create a ResumeBuilder instance
    resume_builder = ResumeBuilder(user_name, user_contact_info, user_education, user_experience, user_skills)

    # Generate resume and cover letter
    resume = resume_builder.generate_resume()
    cover_letter = resume_builder.generate_cover_letter("Software Engineer", "Tech Innovations Inc.")

    # Save to files
    resume_builder.save_to_file("resume.txt", resume)
    resume_builder.save_to_file("cover_letter.txt", cover_letter)
```
