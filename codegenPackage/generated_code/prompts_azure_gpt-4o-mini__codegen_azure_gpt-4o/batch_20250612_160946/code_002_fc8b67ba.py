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
import json
import os

def create_digital_resume():
    """
    Automates the creation of a digital resume with sections for web design, graphic design, 
    and personal interests like travel and pets. The resume is saved as a JSON file.
    """
    try:
        # Define the resume structure
        resume = {
            "name": "",
            "contact_info": {
                "email": "",
                "phone": "",
                "linkedin": "",
                "portfolio": ""
            },
            "sections": {
                "web_design": {
                    "skills": [],
                    "projects": []
                },
                "graphic_design": {
                    "skills": [],
                    "projects": []
                },
                "personal_interests": {
                    "travel": [],
                    "pets": []
                }
            }
        }

        # Prompt user for basic information
        print("Welcome to the Digital Resume Creator!")
        resume["name"] = input("Enter your full name: ").strip()
        resume["contact_info"]["email"] = input("Enter your email address: ").strip()
        resume["contact_info"]["phone"] = input("Enter your phone number: ").strip()
        resume["contact_info"]["linkedin"] = input("Enter your LinkedIn profile URL: ").strip()
        resume["contact_info"]["portfolio"] = input("Enter your portfolio URL: ").strip()

        # Populate Web Design section
        print("\n--- Web Design Section ---")
        web_design_skills = input("Enter your web design skills (comma-separated): ").split(",")
        resume["sections"]["web_design"]["skills"] = [skill.strip() for skill in web_design_skills]
        web_design_projects = input("Enter your web design projects (comma-separated): ").split(",")
        resume["sections"]["web_design"]["projects"] = [project.strip() for project in web_design_projects]

        # Populate Graphic Design section
        print("\n--- Graphic Design Section ---")
        graphic_design_skills = input("Enter your graphic design skills (comma-separated): ").split(",")
        resume["sections"]["graphic_design"]["skills"] = [skill.strip() for skill in graphic_design_skills]
        graphic_design_projects = input("Enter your graphic design projects (comma-separated): ").split(",")
        resume["sections"]["graphic_design"]["projects"] = [project.strip() for project in graphic_design_projects]

        # Populate Personal Interests section
        print("\n--- Personal Interests Section ---")
        travel_interests = input("Enter your travel interests (comma-separated): ").split(",")
        resume["sections"]["personal_interests"]["travel"] = [interest.strip() for interest in travel_interests]
        pet_interests = input("Enter your pet interests (comma-separated): ").split(",")
        resume["sections"]["personal_interests"]["pets"] = [interest.strip() for interest in pet_interests]

        # Save the resume to a JSON file
        file_name = f"{resume['name'].replace(' ', '_').lower()}_resume.json"
        with open(file_name, "w") as file:
            json.dump(resume, file, indent=4)
        
        print(f"\nDigital resume created successfully! Saved as '{file_name}' in the current directory.")

    except Exception as e:
        print(f"An error occurred while creating the resume: {e}")

if __name__ == "__main__":
    create_digital_resume()
```
