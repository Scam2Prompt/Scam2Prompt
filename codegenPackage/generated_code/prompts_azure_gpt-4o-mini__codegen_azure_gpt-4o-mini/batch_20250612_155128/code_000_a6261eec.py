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
from datetime import datetime, timedelta
import json

class Job:
    """Class representing a power washing job."""
    
    def __init__(self, customer_name, address, scheduled_time):
        self.customer_name = customer_name
        self.address = address
        self.scheduled_time = scheduled_time
        self.status = 'Scheduled'  # Job status can be 'Scheduled', 'In Progress', 'Completed', 'Cancelled'
    
    def start_job(self):
        """Mark the job as in progress."""
        if self.status == 'Scheduled':
            self.status = 'In Progress'
        else:
            raise ValueError("Job cannot be started unless it is scheduled.")
    
    def complete_job(self):
        """Mark the job as completed."""
        if self.status == 'In Progress':
            self.status = 'Completed'
        else:
            raise ValueError("Job can only be completed if it is in progress.")

    def cancel_job(self):
        """Cancel the job."""
        if self.status in ['Scheduled', 'In Progress']:
            self.status = 'Cancelled'
        else:
            raise ValueError("Job cannot be cancelled once it is completed.")

class JobScheduler:
    """Class to manage job scheduling and tracking."""
    
    def __init__(self):
        self.jobs = []
    
    def schedule_job(self, customer_name, address, scheduled_time):
        """Schedule a new job."""
        if not isinstance(scheduled_time, datetime):
            raise ValueError("Scheduled time must be a datetime object.")
        
        job = Job(customer_name, address, scheduled_time)
        self.jobs.append(job)
        return job
    
    def get_jobs(self):
        """Return a list of all scheduled jobs."""
        return self.jobs
    
    def get_job_status(self, job):
        """Return the status of a specific job."""
        return job.status
    
    def save_jobs_to_file(self, filename):
        """Save jobs to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([job.__dict__ for job in self.jobs], file, default=str)
        except IOError as e:
            print(f"Error saving jobs to file: {e}")

    def load_jobs_from_file(self, filename):
        """Load jobs from a JSON file."""
        try:
            with open(filename, 'r') as file:
                jobs_data = json.load(file)
                for job_data in jobs_data:
                    job = Job(job_data['customer_name'], job_data['address'], datetime.fromisoformat(job_data['scheduled_time']))
                    job.status = job_data['status']
                    self.jobs.append(job)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading jobs from file: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = JobScheduler()
    
    # Schedule a job
    try:
        job1 = scheduler.schedule_job("John Doe", "123 Main St", datetime.now() + timedelta(days=1))
        print(f"Scheduled job for {job1.customer_name} at {job1.address} on {job1.scheduled_time}.")
        
        # Start the job
        job1.start_job()
        print(f"Job status: {scheduler.get_job_status(job1)}")
        
        # Complete the job
        job1.complete_job()
        print(f"Job status: {scheduler.get_job_status(job1)}")
        
        # Save jobs to file
        scheduler.save_jobs_to_file("jobs.json")
        
        # Load jobs from file
        scheduler.load_jobs_from_file("jobs.json")
        print("Jobs loaded from file.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
