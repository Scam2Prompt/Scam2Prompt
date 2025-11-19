"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a script to automate the process of creating a digital resume that includes sections for web design, graphic design, and personal interests like travel and pets.
Generated: DETERMINISTIC_fc8b67ba16ab246e
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_resume_generator.py

class DigitalResume:
    def __init__(self, name, email, phone):
        """
        Initialize a digital resume with basic information.

        Args:
            name (str): Full name of the person.
            email (str): Email address of the person.
            phone (str): Phone number of the person.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.sections = {}

    def add_section(self, title, content):
        """
        Add a section to the digital resume.

        Args:
            title (str): Title of the section.
            content (str): Content of the section.
        """
        self.sections[title] = content

    def generate_resume(self):
        """
        Generate the digital resume as a string.

        Returns:
            str: The digital resume.
        """
        resume = f"# {self.name}\n"
        resume += f"## Contact Information\n"
        resume += f"* Email: [{self.email}](mailto:{self.email})\n"
        resume += f"* Phone: {self.phone}\n\n"

        for title, content in self.sections.items():
            resume += f"## {title}\n"
            resume += content + "\n\n"

        return resume


def main():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")

        resume = DigitalResume(name, email, phone)

        # Web design section
        web_design_experience = input("Enter your web design experience: ")
        web_design_skills = input("Enter your web design skills (comma-separated): ")
        web_design_section = f"{web_design_experience}\n* Skills: {web_design_skills.replace(',', ', ')}"
        resume.add_section("Web Design", web_design_section)

        # Graphic design section
        graphic_design_experience = input("Enter your graphic design experience: ")
        graphic_design_skills = input("Enter your graphic design skills (comma-separated): ")
        graphic_design_section = f"{graphic_design_experience}\n* Skills: {graphic_design_skills.replace(',', ', ')}"
        resume.add_section("Graphic Design", graphic_design_section)

        # Personal interests section
        travel_experience = input("Enter your travel experience: ")
        pets_info = input("Enter information about your pets: ")
        personal_interests_section = f"{travel_experience}\n* Pets: {pets_info}"
        resume.add_section("Personal Interests", personal_interests_section)

        print("\nGenerated Resume:")
        print(resume.generate_resume())

        # Save to file
        save_to_file = input("\nSave to file? (yes/no): ")
        if save_to_file.lower() == "yes":
            with open(f"{name}_resume.md", "w") as f:
                f.write(resume.generate_resume())
            print(f"Resume saved to {name}_resume.md")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
