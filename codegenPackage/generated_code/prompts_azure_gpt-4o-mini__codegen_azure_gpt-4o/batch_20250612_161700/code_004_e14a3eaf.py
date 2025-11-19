"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: What are the key features of a recruitment system that aligns with the strategic business management services provided by Management en Red?
Generated: DETERMINISTIC_e14a3eafd3aec593
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recruitment System: Key Features
This Python script outlines a recruitment system that aligns with strategic business management services.
The system includes features such as job posting, candidate application, candidate evaluation, and reporting.
"""

import json
from datetime import datetime


class RecruitmentSystem:
    """
    Recruitment System Class
    Handles job postings, candidate applications, and reporting.
    """

    def __init__(self):
        # Initialize the system with empty job postings and candidate applications
        self.job_postings = []
        self.candidate_applications = []

    def create_job_posting(self, title, description, requirements, salary_range):
        """
        Create a new job posting.
        :param title: Job title
        :param description: Job description
        :param requirements: List of job requirements
        :param salary_range: Salary range for the position
        """
        job_posting = {
            "id": len(self.job_postings) + 1,
            "title": title,
            "description": description,
            "requirements": requirements,
            "salary_range": salary_range,
            "created_at": datetime.now().isoformat()
        }
        self.job_postings.append(job_posting)
        print(f"Job posting '{title}' created successfully.")

    def list_job_postings(self):
        """
        List all job postings.
        :return: List of job postings
        """
        if not self.job_postings:
            print("No job postings available.")
            return []
        return self.job_postings

    def apply_for_job(self, job_id, candidate_name, candidate_email, resume):
        """
        Apply for a job.
        :param job_id: ID of the job to apply for
        :param candidate_name: Name of the candidate
        :param candidate_email: Email of the candidate
        :param resume: Resume of the candidate (as a string or file path)
        """
        # Validate job ID
        job = next((job for job in self.job_postings if job["id"] == job_id), None)
        if not job:
            print(f"Job ID {job_id} not found.")
            return

        application = {
            "job_id": job_id,
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "resume": resume,
            "applied_at": datetime.now().isoformat()
        }
        self.candidate_applications.append(application)
        print(f"Application submitted successfully for job ID {job_id}.")

    def list_applications(self, job_id=None):
        """
        List all applications or applications for a specific job.
        :param job_id: (Optional) ID of the job to filter applications
        :return: List of applications
        """
        if job_id:
            applications = [app for app in self.candidate_applications if app["job_id"] == job_id]
            if not applications:
                print(f"No applications found for job ID {job_id}.")
                return []
            return applications
        return self.candidate_applications

    def generate_report(self):
        """
        Generate a summary report of job postings and applications.
        :return: Report as a dictionary
        """
        report = {
            "total_jobs": len(self.job_postings),
            "total_applications": len(self.candidate_applications),
            "applications_per_job": {
                job["title"]: len([app for app in self.candidate_applications if app["job_id"] == job["id"]])
                for job in self.job_postings
            }
        }
        return report

    def save_data(self, file_path):
        """
        Save job postings and applications to a JSON file.
        :param file_path: Path to the file where data will be saved
        """
        data = {
            "job_postings": self.job_postings,
            "candidate_applications": self.candidate_applications
        }
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved successfully to {file_path}.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, file_path):
        """
        Load job postings and applications from a JSON file.
        :param file_path: Path to the file to load data from
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.job_postings = data.get("job_postings", [])
                self.candidate_applications = data.get("candidate_applications", [])
            print(f"Data loaded successfully from {file_path}.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    system = RecruitmentSystem()

    # Create job postings
    system.create_job_posting(
        title="Software Engineer",
        description="Develop and maintain software applications.",
        requirements=["Python", "Django", "REST APIs"],
        salary_range="50,000 - 70,000 USD"
    )
    system.create_job_posting(
        title="Data Analyst",
        description="Analyze and interpret complex data sets.",
        requirements=["SQL", "Excel", "Data Visualization"],
        salary_range="40,000 - 60,000 USD"
    )

    # List job postings
    print("Job Postings:", system.list_job_postings())

    # Apply for a job
    system.apply_for_job(
        job_id=1,
        candidate_name="John Doe",
        candidate_email="john.doe@example.com",
        resume="John_Doe_Resume.pdf"
    )

    # List applications
    print("Applications for Job ID 1:", system.list_applications(job_id=1))

    # Generate report
    print("Report:", system.generate_report())

    # Save data to file
    system.save_data("recruitment_data.json")

    # Load data from file
    system.load_data("recruitment_data.json")
```
