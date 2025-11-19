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
"""
This script provides a template and guidance for creating a strong resume and cover letter 
based on the Bridges to Professions framework. It includes sections for resume content,
cover letter content, and validation to ensure completeness.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class ResumeBuilder:
    """
    A class to build a professional resume following Bridges to Professions guidelines.
    """
    
    def __init__(self):
        self.resume = {
            "contact_info": {},
            "summary": "",
            "education": [],
            "experience": [],
            "skills": [],
            "certifications": [],
            "projects": []
        }
    
    def add_contact_info(self, name: str, email: str, phone: str, 
                         linkedin: Optional[str] = None, portfolio: Optional[str] = None) -> None:
        """
        Add contact information to the resume.
        
        Args:
            name: Full name
            email: Professional email address
            phone: Contact phone number
            linkedin: LinkedIn profile URL (optional)
            portfolio: Personal website/portfolio URL (optional)
        """
        self.resume["contact_info"] = {
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "portfolio": portfolio
        }
    
    def add_summary(self, summary: str) -> None:
        """
        Add a professional summary/objective.
        
        Args:
            summary: 3-4 sentence professional summary
        """
        if len(summary.split()) > 50:
            raise ValueError("Summary should be concise (3-4 sentences max)")
        self.resume["summary"] = summary
    
    def add_education(self, institution: str, degree: str, field: str, 
                      graduation_date: str, gpa: Optional[float] = None) -> None:
        """
        Add education information.
        
        Args:
            institution: Name of school/university
            degree: Degree earned
            field: Field of study
            graduation_date: Graduation date (format: MM/YYYY)
            gpa: GPA (optional, include if 3.0+)
        """
        try:
            datetime.strptime(graduation_date, "%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use MM/YYYY")
            
        self.resume["education"].append({
            "institution": institution,
            "degree": degree,
            "field": field,
            "graduation_date": graduation_date,
            "gpa": gpa
        })
    
    def add_experience(self, title: str, company: str, location: str, 
                       start_date: str, end_date: str, 
                       responsibilities: List[str], current: bool = False) -> None:
        """
        Add work experience.
        
        Args:
            title: Job title
            company: Company name
            location: Job location
            start_date: Start date (format: MM/YYYY)
            end_date: End date (format: MM/YYYY) or "Present" if current
            responsibilities: List of bullet points describing responsibilities
            current: Whether this is a current position
        """
        try:
            datetime.strptime(start_date, "%m/%Y")
            if not current:
                datetime.strptime(end_date, "%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use MM/YYYY")
            
        self.resume["experience"].append({
            "title": title,
            "company": company,
            "location": location,
            "start_date": start_date,
            "end_date": "Present" if current else end_date,
            "responsibilities": responsibilities
        })
    
    def add_skill(self, skill: str, proficiency: Optional[str] = None) -> None:
        """
        Add a skill to the resume.
        
        Args:
            skill: Name of skill
            proficiency: Proficiency level (optional)
        """
        self.resume["skills"].append({
            "skill": skill,
            "proficiency": proficiency
        })
    
    def add_certification(self, name: str, issuing_org: str, 
                          date_earned: str, expiry_date: Optional[str] = None) -> None:
        """
        Add a certification.
        
        Args:
            name: Certification name
            issuing_org: Issuing organization
            date_earned: Date earned (format: MM/YYYY)
            expiry_date: Expiry date if applicable (format: MM/YYYY)
        """
        try:
            datetime.strptime(date_earned, "%m/%Y")
            if expiry_date:
                datetime.strptime(expiry_date, "%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use MM/YYYY")
            
        self.resume["certifications"].append({
            "name": name,
            "issuing_org": issuing_org,
            "date_earned": date_earned,
            "expiry_date": expiry_date
        })
    
    def add_project(self, name: str, description: str, 
                    technologies: List[str], url: Optional[str] = None) -> None:
        """
        Add a project.
        
        Args:
            name: Project name
            description: Brief description
            technologies: List of technologies used
            url: Project URL (optional)
        """
        self.resume["projects"].append({
            "name": name,
            "description": description,
            "technologies": technologies,
            "url": url
        })
    
    def validate_resume(self) -> bool:
        """
        Validate that the resume has all required sections.
        
        Returns:
            bool: True if resume is valid, False otherwise
        """
        required_sections = ["contact_info", "summary", "education", "experience"]
        for section in required_sections:
            if not self.resume[section]:
                return False
        return True
    
    def generate_resume_text(self) -> str:
        """
        Generate formatted resume text.
        
        Returns:
            str: Formatted resume text
        """
        if not self.validate_resume():
            raise ValueError("Resume is incomplete. Missing required sections.")
        
        text = f"{self.resume['contact_info']['name']}\n"
        text += f"{self.resume['contact_info']['email']} | {self.resume['contact_info']['phone']}\n"
        if self.resume['contact_info'].get('linkedin'):
            text += f"LinkedIn: {self.resume['contact_info']['linkedin']}\n"
        if self.resume['contact_info'].get('portfolio'):
            text += f"Portfolio: {self.resume['contact_info']['portfolio']}\n"
        
        text += "\nSUMMARY:\n"
        text += f"{self.resume['summary']}\n"
        
        text += "\nEDUCATION:\n"
        for edu in self.resume['education']:
            text += f"{edu['degree']} in {edu['field']}, {edu['institution']}\n"
            text += f"Graduated: {edu['graduation_date']}"
            if edu.get('gpa'):
                text += f" | GPA: {edu['gpa']}"
            text += "\n"
        
        text += "\nEXPERIENCE:\n"
        for exp in self.resume['experience']:
            text += f"{exp['title']} at {exp['company']}, {exp['location']}\n"
            text += f"{exp['start_date']} - {exp['end_date']}\n"
            for resp in exp['responsibilities']:
                text += f"- {resp}\n"
            text += "\n"
        
        if self.resume['skills']:
            text += "SKILLS:\n"
            text += ", ".join([skill['skill'] for skill in self.resume['skills']]) + "\n"
        
        if self.resume['certifications']:
            text += "\nCERTIFICATIONS:\n"
            for cert in self.resume['certifications']:
                text += f"{cert['name']} ({cert['issuing_org']}) - {cert['date_earned']}"
                if cert.get('expiry_date'):
                    text += f" (Expires: {cert['expiry_date']})"
                text += "\n"
        
        if self.resume['projects']:
            text += "\nPROJECTS:\n"
            for proj in self.resume['projects']:
                text += f"{proj['name']}\n"
                text += f"Technologies: {', '.join(proj['technologies'])}\n"
                text += f"{proj['description']}\n"
                if proj.get('url'):
                    text += f"URL: {proj['url']}\n"
                text += "\n"
        
        return text

class CoverLetterBuilder:
    """
    A class to build a professional cover letter following Bridges to Professions guidelines.
    """
    
    def __init__(self):
        self.letter = {
            "contact_info": {},
            "date": "",
            "employer_info": {},
            "salutation": "",
            "introduction": "",
            "body": [],
            "closing": "",
            "signature": ""
        }
