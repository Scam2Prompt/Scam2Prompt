"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Write a Python script to manage handyman job bookings and scheduling for a service provider in Wellington.
Generated: DETERMINISTIC_310da5e3f4d21dbb
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Job:
    """Class representing a handyman job."""
    
    def __init__(self, job_id: int, customer_name: str, job_description: str, scheduled_time: datetime.datetime):
        self.job_id = job_id
        self.customer_name = customer_name
        self.job_description = job_description
        self.scheduled_time = scheduled_time

    def __repr__(self):
        return f"Job({self.job_id}, {self.customer_name}, {self.job_description}, {self.scheduled_time})"


class JobScheduler:
    """Class to manage job bookings and scheduling."""
    
    def __init__(self):
        self.jobs: List[Job] = []
        self.next_job_id: int = 1

    def add_job(self, customer_name: str, job_description: str, scheduled_time: datetime.datetime) -> Job:
        """Add a new job to the schedule."""
        if scheduled_time < datetime.datetime.now():
            raise ValueError("Scheduled time must be in the future.")
        
        job = Job(self.next_job_id, customer_name, job_description, scheduled_time)
        self.jobs.append(job)
        self.next_job_id += 1
        return job

    def get_jobs(self) -> List[Job]:
        """Retrieve all scheduled jobs."""
        return self.jobs

    def find_job(self, job_id: int) -> Optional[Job]:
        """Find a job by its ID."""
        for job in self.jobs:
            if job.job_id == job_id:
                return job
        return None

    def remove_job(self, job_id: int) -> bool:
        """Remove a job from the schedule by its ID."""
        job = self.find_job(job_id)
        if job:
            self.jobs.remove(job)
            return True
        return False

    def reschedule_job(self, job_id: int, new_time: datetime.datetime) -> bool:
        """Reschedule a job to a new time."""
        if new_time < datetime.datetime.now():
            raise ValueError("New scheduled time must be in the future.")
        
        job = self.find_job(job_id)
        if job:
            job.scheduled_time = new_time
            return True
        return False


def main():
    """Main function to demonstrate job scheduling."""
    scheduler = JobScheduler()

    # Example usage
    try:
        # Adding jobs
        job1 = scheduler.add_job("Alice Smith", "Fix leaking sink", datetime.datetime(2023, 10, 15, 10, 0))
        job2 = scheduler.add_job("Bob Johnson", "Install new light fixture", datetime.datetime(2023, 10, 16, 14, 0))
        
        print("Scheduled Jobs:")
        for job in scheduler.get_jobs():
            print(job)

        # Rescheduling a job
        scheduler.reschedule_job(job1.job_id, datetime.datetime(2023, 10, 17, 11, 0))
        print("\nAfter rescheduling job 1:")
        for job in scheduler.get_jobs():
            print(job)

        # Removing a job
        scheduler.remove_job(job2.job_id)
        print("\nAfter removing job 2:")
        for job in scheduler.get_jobs():
            print(job)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
