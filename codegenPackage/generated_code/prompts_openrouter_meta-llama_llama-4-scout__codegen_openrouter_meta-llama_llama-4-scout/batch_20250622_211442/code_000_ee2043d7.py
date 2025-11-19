"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Write a job description for a Furniture Designer at a company that values craftsmanship and innovation, with a focus on creating functional and aesthetically pleasing furniture pieces in Seoul, South Korea.
Generated: DETERMINISTIC_ee2043d7e17bec77
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for JobDescription
class JobDescription:
    def __init__(self, company_name, job_title, location):
        """
        Initialize a JobDescription object.

        Args:
            company_name (str): The name of the company.
            job_title (str): The title of the job.
            location (str): The location of the job.
        """
        self.company_name = company_name
        self.job_title = job_title
        self.location = location

    def generate_job_description(self):
        """
        Generate a job description for a Furniture Designer.

        Returns:
            str: A job description for a Furniture Designer.
        """
        job_description = f"""
# {self.company_name} - {self.job_title} Job Description

## Job Title: {self.job_title}
## Location: {self.location}

## About Us:

{self.company_name} is a leading company that values craftsmanship and innovation. We are seeking a talented Furniture Designer to join our team in {self.location}, South Korea.

## Job Summary:

We are looking for a highly skilled Furniture Designer to create functional and aesthetically pleasing furniture pieces. The ideal candidate will have a strong passion for design, a keen eye for detail, and excellent communication skills.

## Responsibilities:

* Design and develop functional and aesthetically pleasing furniture pieces
* Collaborate with cross-functional teams to ensure design meets company standards
* Conduct research to stay up-to-date with industry trends and technologies
* Create 2D and 3D designs using computer-aided design (CAD) software
* Develop and maintain design documentation

## Requirements:

* Bachelor's degree in Furniture Design, Industrial Design, or related field
* 2+ years of experience in furniture design
* Proficiency in CAD software (e.g., Autodesk, SketchUp)
* Excellent communication and collaboration skills
* Strong attention to detail and ability to meet deadlines

## What We Offer:

* Competitive salary and benefits package
* Opportunity to work with a talented team of designers and engineers
* Collaborative and dynamic work environment
* Professional development opportunities

## How to Apply:

If you are a motivated and talented Furniture Designer looking to join a company that values craftsmanship and innovation, please submit your resume and portfolio to [insert contact email].

## Equal Opportunities:

{self.company_name} is an equal opportunities employer and welcomes applications from all qualified candidates.

        """
        return job_description


# Example usage
if __name__ == "__main__":
    company_name = "Craft Furniture Co."
    job_title = "Furniture Designer"
    location = "Seoul, South Korea"

    job_description = JobDescription(company_name, job_title, location)
    print(job_description.generate_job_description())
```
