"""
Generated Code Metadata:
========================
Original URL: https://freejobsindubai.com
Prompt: Develop a sample resume tailored for a Waiter position in Dubai, incorporating key skills and experiences highlighted on FreeJobsInDubai.com.
Generated: DETERMINISTIC_3b08bd6dfdb566dc
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Resume:
    def __init__(self, name, contact_info, objective, skills, experience, education):
        """
        Initializes a new Resume instance.

        :param name: str - The name of the applicant
        :param contact_info: dict - A dictionary containing contact information
        :param objective: str - A brief career objective
        :param skills: list - A list of key skills relevant to the position
        :param experience: list - A list of work experiences
        :param education: list - A list of educational qualifications
        """
        self.name = name
        self.contact_info = contact_info
        self.objective = objective
        self.skills = skills
        self.experience = experience
        self.education = education

    def display_resume(self):
        """
        Displays the resume in a formatted manner.
        """
        print(f"Name: {self.name}")
        print("Contact Information:")
        for key, value in self.contact_info.items():
            print(f"{key}: {value}")
        print("\nObjective:")
        print(self.objective)
        print("\nSkills:")
        for skill in self.skills:
            print(f"- {skill}")
        print("\nExperience:")
        for job in self.experience:
            print(f"- {job}")
        print("\nEducation:")
        for edu in self.education:
            print(f"- {edu}")

def main():
    """
    Main function to create and display a sample resume for a Waiter position in Dubai.
    """
    try:
        # Applicant's name
        name = "John Doe"

        # Contact information
        contact_info = {
            "Phone": "+971 50 123 4567",
            "Email": "johndoe@example.com",
            "LinkedIn": "linkedin.com/in/johndoe"
        }

        # Career objective
        objective = ("Dedicated and customer-oriented waiter with over 3 years of experience "
                     "in high-end restaurants. Seeking to leverage my skills in a dynamic team "
                     "environment in Dubai.")

        # Key skills
        skills = [
            "Excellent communication skills",
            "Strong customer service orientation",
            "Ability to work in a fast-paced environment",
            "Knowledge of food and beverage pairings",
            "Team player with a positive attitude"
        ]

        # Work experience
        experience = [
            "Waiter at The Ritz-Carlton, Dubai (2020 - Present)",
            "Waiter at Burj Al Arab, Dubai (2018 - 2020)",
            "Server at The Address Downtown, Dubai (2017 - 2018)"
        ]

        # Educational qualifications
        education = [
            "Diploma in Hospitality Management, Dubai College of Tourism (2016)",
            "High School Diploma, Dubai International School (2014)"
        ]

        # Create a Resume instance
        resume = Resume(name, contact_info, objective, skills, experience, education)

        # Display the resume
        resume.display_resume()

    except Exception as e:
        print(f"An error occurred while creating the resume: {e}")

if __name__ == "__main__":
    main()
```
