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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Digital Resume Generator
Automates the creation of a digital resume with customizable sections.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class DigitalResumeGenerator:
    """A class to generate a digital resume with customizable sections."""

    def __init__(self, output_dir: str = "resume_output"):
        """Initialize the resume generator with default settings."""
        self.output_dir = output_dir
        self.resume_data = {
            "personal_info": {},
            "sections": {
                "web_design": [],
                "graphic_design": [],
                "interests": {
                    "travel": [],
                    "pets": []
                }
            }
        }
        self._ensure_output_dir()

    def _ensure_output_dir(self) -> None:
        """Ensure the output directory exists."""
        os.makedirs(self.output_dir, exist_ok=True)

    def add_personal_info(self, name: str, email: str, phone: str, address: str) -> None:
        """Add personal information to the resume."""
        self.resume_data["personal_info"] = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        }

    def add_web_design_experience(self, title: str, description: str, skills: List[str]) -> None:
        """Add web design experience to the resume."""
        self.resume_data["sections"]["web_design"].append({
            "title": title,
            "description": description,
            "skills": skills
        })

    def add_graphic_design_experience(self, title: str, description: str, skills: List[str]) -> None:
        """Add graphic design experience to the resume."""
        self.resume_data["sections"]["graphic_design"].append({
            "title": title,
            "description": description,
            "skills": skills
        })

    def add_travel_experience(self, location: str, description: str, year: int) -> None:
        """Add travel experience to the resume."""
        self.resume_data["sections"]["interests"]["travel"].append({
            "location": location,
            "description": description,
            "year": year
        })

    def add_pet_info(self, name: str, species: str, description: str) -> None:
        """Add pet information to the resume."""
        self.resume_data["sections"]["interests"]["pets"].append({
            "name": name,
            "species": species,
            "description": description
        })

    def generate_html(self) -> str:
        """Generate an HTML version of the resume."""
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.resume_data["personal_info"].get("name", "Digital Resume")}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; }}
                h2 {{ color: #2980b9; }}
                .section {{ margin-bottom: 30px; }}
                .item {{ margin-bottom: 15px; }}
                .skills {{ font-style: italic; color: #7f8c8d; }}
            </style>
        </head>
        <body>
            <h1>{self.resume_data["personal_info"].get("name", "Digital Resume")}</h1>
            <div class="personal-info">
                <p>Email: {self.resume_data["personal_info"].get("email", "")}</p>
                <p>Phone: {self.resume_data["personal_info"].get("phone", "")}</p>
                <p>Address: {self.resume_data["personal_info"].get("address", "")}</p>
            </div>
        """

        # Web Design Section
        if self.resume_data["sections"]["web_design"]:
            html += '<div class="section"><h2>Web Design Experience</h2>'
            for item in self.resume_data["sections"]["web_design"]:
                html += f"""
                <div class="item">
                    <h3>{item["title"]}</h3>
                    <p>{item["description"]}</p>
                    <p class="skills">Skills: {", ".join(item["skills"])}</p>
                </div>
                """
            html += "</div>"

        # Graphic Design Section
        if self.resume_data["sections"]["graphic_design"]:
            html += '<div class="section"><h2>Graphic Design Experience</h2>'
            for item in self.resume_data["sections"]["graphic_design"]:
                html += f"""
                <div class="item">
                    <h3>{item["title"]}</h3>
                    <p>{item["description"]}</p>
                    <p class="skills">Skills: {", ".join(item["skills"])}</p>
                </div>
                """
            html += "</div>"

        # Interests Section
        html += '<div class="section"><h2>Personal Interests</h2>'

        # Travel Subsection
        if self.resume_data["sections"]["interests"]["travel"]:
            html += '<div class="subsection"><h3>Travel</h3>'
            for item in self.resume_data["sections"]["interests"]["travel"]:
                html += f"""
                <div class="item">
                    <h4>{item["location"]} ({item["year"]})</h4>
                    <p>{item["description"]}</p>
                </div>
                """
            html += "</div>"

        # Pets Subsection
        if self.resume_data["sections"]["interests"]["pets"]:
            html += '<div class="subsection"><h3>Pets</h3>'
            for item in self.resume_data["sections"]["interests"]["pets"]:
                html += f"""
                <div class="item">
                    <h4>{item["name"]} ({item["species"]})</h4>
                    <p>{item["description"]}</p>
                </div>
                """
            html += "</div>"

        html += """
            </div>
        </body>
        </html>
        """
        return html

    def generate_json(self) -> str:
        """Generate a JSON version of the resume."""
        return json.dumps(self.resume_data, indent=2)

    def save_resume(self, format_type: str = "html") -> str:
        """Save the resume in the specified format."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"resume_{timestamp}.{format_type}"
        filepath = os.path.join(self.output_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                if format_type == "html":
                    content = self.generate_html()
                elif format_type == "json":
                    content = self.generate_json()
                else:
                    raise ValueError("Unsupported format type. Use 'html' or 'json'.")
                
                f.write(content)
            return f"Resume successfully saved to {filepath}"
        except Exception as e:
            return f"Error saving resume: {str(e)}"


def main():
    """Example usage of the DigitalResumeGenerator."""
    resume = DigitalResumeGenerator()

    # Add personal information
    resume.add_personal_info(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="(123) 456-7890",
        address="123 Main St, Anytown, USA"
    )

    # Add web design experience
    resume.add_web_design_experience(
        title="Frontend Developer",
        description="Developed responsive websites using modern frameworks.",
        skills=["HTML", "CSS", "JavaScript", "React"]
    )

    # Add graphic design experience
    resume.add_graphic_design_experience(
        title="Graphic Designer",
        description="Created visual content for marketing campaigns.",
        skills=["Photoshop", "Illustrator", "InDesign"]
    )

    # Add travel experiences
    resume.add_travel_experience(
        location="Paris, France",
        description="Explored historic landmarks and local cuisine.",
        year=2022
    )

    # Add pet information
    resume.add_pet_info(
        name="Max",
        species="Dog",
        description="Friendly golden retriever who loves to play fetch."
    )

    # Save the resume
    print(resume.save_resume("html"))
    print(resume.save_resume("json"))


if __name__ == "__main__":
    main()
```
