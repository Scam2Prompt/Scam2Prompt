"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Write a job description for a Senior Expert Bauabrechnung (m/w/d) in Medizintechnik, including key responsibilities and qualifications, as per jobONE's recruitment standards.
Generated: DETERMINISTIC_d936ed83f2b0ecbe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JobDescription:
    """
    A class to represent a job description for a Senior Expert Bauabrechnung in Medizintechnik.
    """

    def __init__(self, title, location, responsibilities, qualifications):
        """
        Initializes the JobDescription with title, location, responsibilities, and qualifications.

        :param title: str - The title of the job position.
        :param location: str - The location of the job.
        :param responsibilities: list - A list of key responsibilities for the job.
        :param qualifications: list - A list of required qualifications for the job.
        """
        self.title = title
        self.location = location
        self.responsibilities = responsibilities
        self.qualifications = qualifications

    def display_job_description(self):
        """
        Displays the job description in a formatted manner.
        """
        try:
            print(f"Job Title: {self.title}")
            print(f"Location: {self.location}\n")
            print("Key Responsibilities:")
            for responsibility in self.responsibilities:
                print(f"- {responsibility}")
            print("\nQualifications:")
            for qualification in self.qualifications:
                print(f"- {qualification}")
        except Exception as e:
            print(f"An error occurred while displaying the job description: {e}")

# Define the job details
job_title = "Senior Expert Bauabrechnung (m/w/d)"
job_location = "Germany"
job_responsibilities = [
    "Lead the planning and execution of Bauabrechnung processes in Medizintechnik projects.",
    "Ensure compliance with relevant regulations and standards.",
    "Collaborate with cross-functional teams to optimize project delivery.",
    "Provide expert guidance on cost estimation and budgeting.",
    "Conduct risk assessments and implement mitigation strategies.",
    "Mentor junior staff and provide training on best practices."
]
job_qualifications = [
    "Master's degree in Engineering, Business Administration, or a related field.",
    "Minimum 5 years of experience in Bauabrechnung within the Medizintechnik sector.",
    "Strong knowledge of relevant regulations and compliance standards.",
    "Excellent analytical and problem-solving skills.",
    "Proficient in project management software and tools.",
    "Fluent in German and English, both written and spoken."
]

# Create a JobDescription instance
job_description = JobDescription(job_title, job_location, job_responsibilities, job_qualifications)

# Display the job description
job_description.display_job_description()
```
