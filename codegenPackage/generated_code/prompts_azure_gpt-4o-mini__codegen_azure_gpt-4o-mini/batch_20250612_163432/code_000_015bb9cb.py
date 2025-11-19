"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Generate a job application for a Furniture Designer position at Hanil Furniture Gallery, highlighting relevant design skills and experience in creating functional furniture pieces.
Generated: DETERMINISTIC_015bb9cb2d7f051e
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JobApplication:
    def __init__(self, applicant_name, position, company):
        """
        Initializes the JobApplication with applicant details.

        :param applicant_name: str - Name of the applicant
        :param position: str - Position applied for
        :param company: str - Company name
        """
        self.applicant_name = applicant_name
        self.position = position
        self.company = company
        self.skills = []
        self.experience = []

    def add_skill(self, skill):
        """
        Adds a skill to the applicant's profile.

        :param skill: str - A skill relevant to the job
        """
        if isinstance(skill, str) and skill:
            self.skills.append(skill)
        else:
            raise ValueError("Skill must be a non-empty string.")

    def add_experience(self, experience):
        """
        Adds work experience to the applicant's profile.

        :param experience: str - A description of relevant work experience
        """
        if isinstance(experience, str) and experience:
            self.experience.append(experience)
        else:
            raise ValueError("Experience must be a non-empty string.")

    def generate_cover_letter(self):
        """
        Generates a cover letter for the job application.

        :return: str - The formatted cover letter
        """
        try:
            letter = f"Dear Hiring Manager,\n\n"
            letter += f"I am writing to express my interest in the {self.position} position at {self.company}.\n\n"
            letter += "I believe my skills and experience make me a strong candidate for this role.\n\n"
            letter += "Relevant Skills:\n"
            for skill in self.skills:
                letter += f"- {skill}\n"
            letter += "\nRelevant Experience:\n"
            for exp in self.experience:
                letter += f"- {exp}\n"
            letter += "\nThank you for considering my application. I look forward to the opportunity to discuss my candidacy further.\n\n"
            letter += "Sincerely,\n"
            letter += self.applicant_name
            
            return letter
        except Exception as e:
            raise RuntimeError("An error occurred while generating the cover letter.") from e


# Example usage
if __name__ == "__main__":
    try:
        application = JobApplication("John Doe", "Furniture Designer", "Hanil Furniture Gallery")
        application.add_skill("3D Modeling")
        application.add_skill("Sustainable Design Practices")
        application.add_skill("Prototyping and Testing")
        application.add_experience("Designed a line of modular furniture for small spaces.")
        application.add_experience("Collaborated with a team to create ergonomic office furniture.")

        cover_letter = application.generate_cover_letter()
        print(cover_letter)
    except Exception as e:
        print(f"Error: {e}")
```
