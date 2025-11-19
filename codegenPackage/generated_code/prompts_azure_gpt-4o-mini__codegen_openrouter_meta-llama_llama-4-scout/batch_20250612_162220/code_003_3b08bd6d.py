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
class WaiterResume:
    def __init__(self, name, contact_number, email):
        """
        Initialize a WaiterResume object.

        Args:
            name (str): The name of the waiter.
            contact_number (str): The contact number of the waiter.
            email (str): The email address of the waiter.
        """
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.experiences = []
        self.skills = []

    def add_experience(self, job_title, restaurant_name, duration, responsibilities):
        """
        Add a work experience to the resume.

        Args:
            job_title (str): The job title of the experience.
            restaurant_name (str): The name of the restaurant.
            duration (str): The duration of the experience.
            responsibilities (list): A list of responsibilities.
        """
        experience = {
            "job_title": job_title,
            "restaurant_name": restaurant_name,
            "duration": duration,
            "responsibilities": responsibilities
        }
        self.experiences.append(experience)

    def add_skill(self, skill):
        """
        Add a skill to the resume.

        Args:
            skill (str): The skill to add.
        """
        self.skills.append(skill)

    def generate_resume(self):
        """
        Generate a sample resume for a Waiter position in Dubai.

        Returns:
            str: A string representation of the resume.
        """
        resume = f"""
        # {self.name}
        ## Contact Information
        - Phone: {self.contact_number}
        - Email: {self.email}

        ## Summary
        Highly motivated and experienced waiter with a strong passion for providing excellent customer service.

        ## Work Experience
        """
        for experience in self.experiences:
            resume += f"""
            ### {experience["job_title"]} at {experience["restaurant_name"]} ({experience["duration"]})
            - {", ".join(experience["responsibilities"])}
            """
        resume += """
        ## Key Skills
        """
        for skill in self.skills:
            resume += f"""
            - {skill}
        """
        resume += """
        ## Education
        - [Insert Education]

        ## Certifications
        - [Insert Certifications]

        ## References
        - Available upon request.
        """
        return resume


def main():
    try:
        resume = WaiterResume("John Doe", "+971 50 123 4567", "john.doe@example.com")

        resume.add_skill("Excellent customer service skills")
        resume.add_skill("Strong communication skills")
        resume.add_skill("Ability to work in a fast-paced environment")
        resume.add_skill("Basic knowledge of Arabic")

        resume.add_experience(
            "Waiter",
            "Burj Al Arab",
            "2018-2020",
            [
                "Provided exceptional customer service to guests",
                "Managed cash and credit transactions accurately",
                "Worked effectively as part of a team to ensure smooth service"
            ]
        )

        resume.add_experience(
            "Waiter",
            "Dubai Mall",
            "2015-2018",
            [
                "Greeted and served guests in a friendly and professional manner",
                "Maintained a clean and organized workspace",
                "Handled guest complaints and resolved issues promptly"
            ]
        )

        print(resume.generate_resume())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
