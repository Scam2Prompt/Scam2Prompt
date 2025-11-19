"""
Generated Code Metadata:
========================
Original URL: https://freejobsindubai.com
Prompt: Write a job description for a Civil Engineer position in UAE, including responsibilities such as putting, stacking, or conveying blocks, and utilizing heavy equipment like earth movers or tractors.
Generated: DETERMINISTIC_d6505b39e56f8ac3
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JobDescription:
    def __init__(self, job_title, location):
        """
        Initialize a JobDescription object.

        Args:
            job_title (str): The title of the job.
            location (str): The location of the job.
        """
        self.job_title = job_title
        self.location = location
        self.responsibilities = []
        self.requirements = []

    def add_responsibility(self, responsibility):
        """
        Add a responsibility to the job description.

        Args:
            responsibility (str): A responsibility of the job.
        """
        self.responsibilities.append(responsibility)

    def add_requirement(self, requirement):
        """
        Add a requirement to the job description.

        Args:
            requirement (str): A requirement of the job.
        """
        self.requirements.append(requirement)

    def generate_job_description(self):
        """
        Generate a job description.

        Returns:
            str: A job description.
        """
        job_description = f"**Job Title:** {self.job_title}\n"
        job_description += f"**Location:** {self.location}\n\n"
        job_description += "**Job Summary:**\n"
        job_description += f"We are seeking a highly skilled {self.job_title} to join our team in {self.location}. The successful candidate will be responsible for various aspects of civil engineering projects.\n\n"
        job_description += "**Responsibilities:**\n"
        for i, responsibility in enumerate(self.responsibilities, start=1):
            job_description += f"{i}. {responsibility}\n"
        job_description += "\n"
        job_description += "**Requirements:**\n"
        for i, requirement in enumerate(self.requirements, start=1):
            job_description += f"{i}. {requirement}\n"

        return job_description


def main():
    try:
        job_title = "Civil Engineer"
        location = "UAE"

        job_description = JobDescription(job_title, location)

        job_description.add_responsibility("Putting, stacking, or conveying blocks")
        job_description.add_responsibility("Utilizing heavy equipment like earth movers or tractors")
        job_description.add_responsibility("Overseeing construction sites and ensuring projects are completed on time")
        job_description.add_responsibility("Collaborating with architects, contractors, and other stakeholders")

        job_description.add_requirement("Bachelor's degree in Civil Engineering")
        job_description.add_requirement("Minimum 5 years of experience in civil engineering")
        job_description.add_requirement("Strong knowledge of construction methods and materials")
        job_description.add_requirement("Excellent communication and project management skills")

        print(job_description.generate_job_description())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
