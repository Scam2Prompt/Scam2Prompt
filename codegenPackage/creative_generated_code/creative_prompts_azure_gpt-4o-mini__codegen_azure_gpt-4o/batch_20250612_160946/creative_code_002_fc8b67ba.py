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
from datetime import datetime

def create_digital_resume():
    """
    Automates the creation of a digital resume with sections for web design, graphic design, 
    and personal interests (travel and pets). The resume is saved as a JSON file.
    """
    try:
        # Define the resume structure
        resume = {
            "name": "",
            "contact": {
                "email": "",
                "phone": "",
                "linkedin": ""
            },
            "skills": {
                "web_design": [],
                "graphic_design": []
            },
            "personal_interests": ["travel", "pets"]
        }

        # Prompt user for essential details
        print("Welcome! Let's create your digital resume.")
        resume["name"] = input("Enter your full name: ").strip()
        resume["contact"]["email"] = input("Enter your email address: ").strip()
        resume["contact"]["phone"] = input("Enter your phone number: ").strip()
        resume["contact"]["linkedin"] = input("Enter your LinkedIn profile URL: ").strip()

        # Gather web design skills
        print("\nEnter your web design skills (type 'done' when finished):")
        while True:
            skill = input("Web Design Skill: ").strip()
            if skill.lower() == "done":
                break
            resume["skills"]["web_design"].append(skill)

        # Gather graphic design skills
        print("\nEnter your graphic design skills (type 'done' when finished):")
        while True:
            skill = input("Graphic Design Skill: ").strip()
            if skill.lower() == "done":
                break
            resume["skills"]["graphic_design"].append(skill)

        # Create a timestamped filename for the resume
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"resume_{resume['name'].replace(' ', '_')}_{timestamp}.json"

        # Save the resume to a JSON file
        with open(filename, "w") as file:
            json.dump(resume, file, indent=4)

        print(f"\nDigital resume successfully created and saved as '{filename}'.")

    except Exception as e:
        print(f"An error occurred while creating the digital resume: {e}")
        raise

if __name__ == "__main__":
    create_digital_resume()
```
