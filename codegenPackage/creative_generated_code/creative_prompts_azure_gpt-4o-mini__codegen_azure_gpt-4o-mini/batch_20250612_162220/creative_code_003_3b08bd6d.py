"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freejobsindubai.com
Prompt: Develop a sample resume tailored for a Waiter position in Dubai, incorporating key skills and experiences highlighted on FreeJobsInDubai.com.
Generated: DETERMINISTIC_3b08bd6dfdb566dc
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Resume:
    """
    A class to represent a candidate's resume for a Waiter position.

    Attributes:
        name (str): Candidate's name.
        contact_info (dict): Candidate's contact information including phone and email.
        summary (str): A brief summary of qualifications.
        skills (list): A list of key skills relevant to the waiter position.
        experience (list): A list of previous job experiences.
        education (list): A list of educational qualifications.
    """

    def __init__(self, name, contact_info, summary, skills, experience, education):
        """
        Initializes the Resume object with name, contact information, summary, skills, experience, and education.

        Args:
            name (str): Candidate's name.
            contact_info (dict): Candidate's contact information.
            summary (str): Candidate's summary.
            skills (list): Candidate's skills.
            experience (list): Candidate's work experience.
            education (list): Candidate's educational qualifications.
        """
        self.name = name
        self.contact_info = contact_info
        self.summary = summary
        self.skills = skills
        self.experience = experience
        self.education = education

    def display_resume(self):
        """Displays the candidate's resume in a formatted manner."""
        try:
            print(f"Name: {self.name}\n")
            print("Contact Information:")
            for key, value in self.contact_info.items():
                print(f"{key.capitalize()}: {value}")
            print("\nSummary:")
            print(self.summary)
            print("\nSkills:")
            for skill in self.skills:
                print(f"- {skill}")
            print("\nWork Experience:")
            for job in self.experience:
                print(f"- {job}")
            print("\nEducation:")
            for edu in self.education:
                print(f"- {edu}")
        except Exception as e:
            print(f"An error occurred while displaying the resume: {e}")

# Sample resume data for a Waiter position
name = "John Doe"
contact_info = {
    "phone": "+971 50 123 4567",
    "email": "johndoe@example.com"
}
summary = ("Dedicated and customer-oriented waiter with over 5 years of experience in busy restaurants. "
           "Proficient in providing exceptional service, managing multiple tables, and ensuring customer satisfaction.")
skills = [
    "Excellent communication skills",
    "Strong attention to detail",
    "Ability to work in a fast-paced environment",
    "Knowledge of food and beverage offerings",
    "Cash handling and POS system experience",
    "Team player with a positive attitude"
]
experience = [
    "Waiter at The Dubai Mall Restaurant (2021 - Present)",
    "Server at Emirates Palace Hotel (2019 - 2021)",
    "Waitstaff at Dubai Marina Beach Resort (2017 - 2019)"
]
education = [
    "Diploma in Hospitality Management, Dubai College of Tourism (2017)",
    "High School Diploma, Dubai International School (2015)"
]

# Create a Resume object and display it
if __name__ == "__main__":
    waiter_resume = Resume(name, contact_info, summary, skills, experience, education)
    waiter_resume.display_resume()
```
