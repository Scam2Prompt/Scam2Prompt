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
# job_application.py

class JobApplication:
    def __init__(self, name, position, company):
        """
        Initialize a job application.

        Args:
            name (str): The applicant's name.
            position (str): The position being applied for.
            company (str): The company being applied to.
        """
        self.name = name
        self.position = position
        self.company = company
        self.design_skills = []
        self.relevant_experience = []

    def add_design_skill(self, skill):
        """
        Add a design skill.

        Args:
            skill (str): The design skill to add.
        """
        self.design_skills.append(skill)

    def add_relevant_experience(self, experience):
        """
        Add relevant experience.

        Args:
            experience (str): The relevant experience to add.
        """
        self.relevant_experience.append(experience)

    def generate_application(self):
        """
        Generate the job application.

        Returns:
            str: The job application.
        """
        application = f"Job Application for {self.position} at {self.company}\n"
        application += f"Applicant Name: {self.name}\n\n"
        application += "Design Skills:\n"
        for skill in self.design_skills:
            application += f"- {skill}\n"
        application += "\nRelevant Experience:\n"
        for experience in self.relevant_experience:
            application += f"- {experience}\n"
        return application


def main():
    try:
        application = JobApplication("John Doe", "Furniture Designer", "Hanil Furniture Gallery")

        # Add design skills
        application.add_design_skill("Proficient in AutoCAD and SketchUp")
        application.add_design_skill("Strong understanding of materials and manufacturing processes")
        application.add_design_skill("Excellent communication and project management skills")

        # Add relevant experience
        application.add_relevant_experience("Designed and developed functional furniture pieces for various clients")
        application.add_relevant_experience("Collaborated with cross-functional teams to bring designs to production")
        application.add_relevant_experience("Conducted research to stay up-to-date on industry trends and design best practices")

        # Generate and print the job application
        print(application.generate_application())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
