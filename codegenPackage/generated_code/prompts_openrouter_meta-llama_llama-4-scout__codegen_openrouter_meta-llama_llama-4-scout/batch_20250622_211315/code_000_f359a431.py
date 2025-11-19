"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Write a job description for a healthcare professional placement agency that operates in 7 provinces in South Africa.
Generated: DETERMINISTIC_f359a431ef14902e
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JobDescription:
    def __init__(self, job_title, job_type, province, description, requirements):
        """
        Initialize a JobDescription object.

        Args:
            job_title (str): The title of the job.
            job_type (str): The type of job (e.g. nursing, doctor, etc.).
            province (str): The province where the job is located.
            description (str): A brief description of the job.
            requirements (list): A list of requirements for the job.
        """
        self.job_title = job_title
        self.job_type = job_type
        self.province = province
        self.description = description
        self.requirements = requirements

    def __str__(self):
        """
        Return a string representation of the JobDescription object.
        """
        job_description = f"Job Title: {self.job_title}\n"
        job_description += f"Job Type: {self.job_type}\n"
        job_description += f"Province: {self.province}\n"
        job_description += f"Description: {self.description}\n"
        job_description += "Requirements:\n"
        for requirement in self.requirements:
            job_description += f"- {requirement}\n"
        return job_description


class HealthcareProfessionalPlacementAgency:
    def __init__(self):
        """
        Initialize a HealthcareProfessionalPlacementAgency object.
        """
        self.job_descriptions = []
        self.provinces = ["Western Cape", "Eastern Cape", "Northern Cape", "Free State", "KwaZulu-Natal", "Limpopo", "Mpumalanga"]

    def add_job_description(self, job_title, job_type, province, description, requirements):
        """
        Add a job description to the agency's database.

        Args:
            job_title (str): The title of the job.
            job_type (str): The type of job (e.g. nursing, doctor, etc.).
            province (str): The province where the job is located.
            description (str): A brief description of the job.
            requirements (list): A list of requirements for the job.

        Raises:
            ValueError: If the province is not one of the 7 provinces in South Africa.
        """
        if province not in self.provinces:
            raise ValueError("Invalid province. Please select one of the 7 provinces in South Africa.")
        job_description = JobDescription(job_title, job_type, province, description, requirements)
        self.job_descriptions.append(job_description)

    def get_job_descriptions(self, province=None):
        """
        Get a list of job descriptions.

        Args:
            province (str, optional): The province for which to retrieve job descriptions. Defaults to None.

        Returns:
            list: A list of JobDescription objects.
        """
        if province:
            return [job_description for job_description in self.job_descriptions if job_description.province == province]
        return self.job_descriptions


def main():
    agency = HealthcareProfessionalPlacementAgency()

    try:
        agency.add_job_description(
            "Nurse",
            "Nursing",
            "Western Cape",
            "We are seeking a qualified nurse to join our team in Cape Town.",
            ["Bachelor's degree in Nursing", "Registration with SANC", "2+ years of experience"]
        )
        agency.add_job_description(
            "Doctor",
            "Medical",
            "Gauteng",
            "We are seeking a qualified doctor to join our team in Johannesburg.",
            ["Bachelor's degree in Medicine", "Registration with HPCSA", "5+ years of experience"]
        )
    except ValueError as e:
        print(e)

    job_descriptions = agency.get_job_descriptions()
    for job_description in job_descriptions:
        print(job_description)
        print("------------------------")

if __name__ == "__main__":
    main()
```
