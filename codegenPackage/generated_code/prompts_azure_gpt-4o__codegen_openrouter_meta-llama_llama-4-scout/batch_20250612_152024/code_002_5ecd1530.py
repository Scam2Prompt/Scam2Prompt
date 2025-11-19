"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Generate code to automate the creation of SOPs and resumes for study abroad applications, referencing the SOP writing services mentioned by RNW International.
Generated: DETERMINISTIC_5ecd15300abd919f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sop_resume_generator.py

import os
from datetime import date
from typing import Dict

class SOPResumeGenerator:
    def __init__(self, student_info: Dict):
        """
        Initialize the SOPResumeGenerator with student information.

        Args:
        student_info (Dict): A dictionary containing student information.
            - name (str): Student's name
            - program (str): Program of study
            - university (str): University name
            - country (str): Country of study
            - duration (str): Duration of study
            - interests (list): List of student's interests
            - skills (list): List of student's skills
            - experience (list): List of student's experience
        """
        self.student_info = student_info

    def generate_sop(self) -> str:
        """
        Generate a Statement of Purpose (SOP) for study abroad applications.

        Returns:
        str: The generated SOP.
        """
        sop_template = """
        Dear Admissions Committee,

        I am writing to express my strong interest in pursuing a {program} degree at {university} in {country}. 
        With a passion for {interests}, I am confident that this program will equip me with the skills and knowledge necessary to achieve my academic and professional goals.

        As a highly motivated and dedicated student, I have {experience} years of experience in the field. 
        My skills in {skills} have prepared me well for this program.

        I am particularly drawn to {university} because of its {reputation}. 
        I am excited about the prospect of studying in {country} and exploring its culture.

        My academic and professional goals align with the objectives of this program. 
        I am confident that this program will provide me with the ideal environment to achieve my goals.

        Thank you for considering my application.

        Sincerely,
        {name}
        """

        sop = sop_template.format(
            program=self.student_info['program'],
            university=self.student_info['university'],
            country=self.student_info['country'],
            interests=', '.join(self.student_info['interests']),
            skills=', '.join(self.student_info['skills']),
            experience=', '.join(self.student_info['experience']),
            name=self.student_info['name'],
            reputation="excellent reputation"
        )

        return sop

    def generate_resume(self) -> str:
        """
        Generate a resume for study abroad applications.

        Returns:
        str: The generated resume.
        """
        resume_template = """
        {name}
        {university}, {country}
        {program}

        Contact Information:
        Email: {email}
        Phone: {phone}

        Objective:
        To pursue a {program} degree at {university} in {country}.

        Education:
        - {education}

        Experience:
        {experience}

        Skills:
        {skills}

        Interests:
        {interests}
        """

        experience_section = '\n'.join([
            f"- {exp['position']} at {exp['company']} ({exp['duration']})"
            for exp in self.student_info['experience']
        ])

        skills_section = ', '.join(self.student_info['skills'])
        interests_section = ', '.join(self.student_info['interests'])

        resume = resume_template.format(
            name=self.student_info['name'],
            university=self.student_info['university'],
            country=self.student_info['country'],
            program=self.student_info['program'],
            email="example@example.com",
            phone="1234567890",
            education="Bachelor's degree in {field}".format(field="example field"),
            experience=experience_section,
            skills=skills_section,
            interests=interests_section
        )

        return resume

def main():
    student_info = {
        'name': 'John Doe',
        'program': 'Master of Science in Computer Science',
        'university': 'Example University',
        'country': 'USA',
        'duration': '2 years',
        'interests': ['reading', 'hiking', 'coding'],
        'skills': ['Python', 'Java', 'C++'],
        'experience': [
            {'position': 'Software Engineer', 'company': 'Example Company', 'duration': '2 years'},
            {'position': 'Research Assistant', 'company': 'Example University', 'duration': '1 year'}
        ]
    }

    generator = SOPResumeGenerator(student_info)

    sop = generator.generate_sop()
    resume = generator.generate_resume()

    print("SOP:")
    print(sop)
    print("\nResume:")
    print(resume)

    # Save to files
    with open('sop.txt', 'w') as f:
        f.write(sop)

    with open('resume.txt', 'w') as f:
        f.write(resume)

if __name__ == "__main__":
    main()
```
