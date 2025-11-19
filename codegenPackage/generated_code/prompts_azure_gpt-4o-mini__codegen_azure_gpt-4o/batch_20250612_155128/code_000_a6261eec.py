"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Generate a code snippet for a mobile power washing service that includes features for scheduling and tracking jobs, similar to Klean-Pro Utah's offerings.
Generated: DETERMINISTIC_a6261eecc4e02f44
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
import uuid

class Job:
    """
    Represents a power washing job.
    """
    def __init__(self, customer_name, address, scheduled_date, service_type):
        self.job_id = str(uuid.uuid4())  # Unique identifier for the job
        self.customer_name = customer_name
        self.address = address
        self.scheduled_date = scheduled_date
        self.service_type = service_type
        self.status = "Scheduled"  # Initial status
        self.created_at = datetime.now()

    def update_status(self, new_status):
        """
        Updates the status of the job.
        :param new_status: New status for the job (e.g., 'In Progress', 'Completed').
        """
        valid_statuses = ["Scheduled", "In Progress", "Completed", "Cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        Returns a string representation of the job.
        """
        return (f"Job ID: {self.job_id}\n"
                f"Customer: {self.customer_name}\n"
                f"Address: {self.address}\n"
                f"Scheduled Date: {self.scheduled_date}\n"
                f"Service Type: {self.service_type}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n")


class PowerWashingService:
    """
    Manages scheduling and tracking of power washing jobs.
    """
    def __init__(self):
        self.jobs = {}  # Dictionary to store jobs by their ID

    def schedule_job(self, customer_name, address, scheduled_date, service_type):
        """
        Schedules a new power washing job.
        :param customer_name: Name of the customer.
        :param address: Address where the service will be performed.
        :param scheduled_date: Date and time for the service.
        :param service_type: Type of service (e.g., 'Residential', 'Commercial').
        :return: The newly created job.
        """
        try:
            job = Job(customer_name, address, scheduled_date, service_type)
            self.jobs[job.job_id] = job
            return job
        except Exception as e:
            print(f"Error scheduling job: {e}")
            return None

    def get_job(self, job_id):
        """
        Retrieves a job by its ID.
        :param job_id: The ID of the job to retrieve.
        :return: The job object if found, None otherwise.
        """
        return self.jobs.get(job_id, None)

    def update_job_status(self, job_id, new_status):
        """
        Updates the status of a job.
        :param job_id: The ID of the job to update.
        :param new_status: The new status for the job.
        """
        job = self.get_job(job_id)
        if not job:
            print(f"Job with ID {job_id} not found.")
            return
        try:
            job.update_status(new_status)
            print(f"Job {job_id} status updated to {new_status}.")
        except ValueError as e:
            print(f"Error updating job status: {e}")

    def list_jobs(self):
        """
        Lists all jobs.
        :return: A list of all jobs.
        """
        return list(self.jobs.values())


# Example usage
if __name__ == "__main__":
    service = PowerWashingService()

    # Schedule a new job
    job1 = service.schedule_job("John Doe", "123 Main St", "2023-10-15 10:00", "Residential")
    if job1:
        print("Scheduled Job:")
        print(job1)

    # Update job status
    if job1:
        service.update_job_status(job1.job_id, "In Progress")

    # List all jobs
    print("\nAll Jobs:")
    for job in service.list_jobs():
        print(job)
```
