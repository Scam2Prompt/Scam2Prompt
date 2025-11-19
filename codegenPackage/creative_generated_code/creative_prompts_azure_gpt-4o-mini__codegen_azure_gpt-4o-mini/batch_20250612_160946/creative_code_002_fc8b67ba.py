"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a script to automate the process of creating a digital resume that includes sections for web design, graphic design, and personal interests like travel and pets.
Generated: DETERMINISTIC_fc8b67ba16ab246e
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class Resume:
    """Class to create a digital resume with sections for web design, graphic design, and personal interests."""
    
    def __init__(self, name, email, phone):
        """Initialize the resume with basic personal information."""
        self.name = name
        self.email = email
        self.phone = phone
        self.sections = {
            "Web Design": [],
            "Graphic Design": [],
            "Personal Interests": []
        }

    def add_web_design_project(self, project_name, description):
        """Add a web design project to the resume."""
        self.sections["Web Design"].append({"Project Name": project_name, "Description": description})

    def add_graphic_design_project(self, project_name, description):
        """Add a graphic design project to the resume."""
        self.sections["Graphic Design"].append({"Project Name": project_name, "Description": description})

    def add_personal_interest(self, interest):
        """Add a personal interest to the resume."""
        self.sections["Personal Interests"].append(interest)

    def generate_resume(self):
        """Generate the resume in JSON format."""
        resume_data = {
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Sections": self.sections
        }
        return json.dumps(resume_data, indent=4)

    def save_to_file(self, filename):
        """Save the resume to a JSON file."""
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_resume())
            print(f"Resume saved as {filename}")
        except IOError as e:
            print(f"Error saving resume to file: {e}")

def main():
    """Main function to create and save a resume."""
    # Collect user information
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    # Create a Resume instance
    my_resume = Resume(name, email, phone)

    # Add web design projects
    while True:
        project_name = input("Enter a web design project name (or 'done' to finish): ")
        if project_name.lower() == 'done':
            break
        description = input("Enter the project description: ")
        my_resume.add_web_design_project(project_name, description)

    # Add graphic design projects
    while True:
        project_name = input("Enter a graphic design project name (or 'done' to finish): ")
        if project_name.lower() == 'done':
            break
        description = input("Enter the project description: ")
        my_resume.add_graphic_design_project(project_name, description)

    # Add personal interests
    while True:
        interest = input("Enter a personal interest (or 'done' to finish): ")
        if interest.lower() == 'done':
            break
        my_resume.add_personal_interest(interest)

    # Save the resume to a file
    filename = input("Enter the filename to save your resume (e.g., resume.json): ")
    my_resume.save_to_file(filename)

if __name__ == "__main__":
    main()
```
