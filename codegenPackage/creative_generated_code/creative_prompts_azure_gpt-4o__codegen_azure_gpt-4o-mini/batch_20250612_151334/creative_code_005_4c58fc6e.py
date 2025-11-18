"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Write a program to automate scheduling for electrical contractors, referencing the operational model of E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_4c58fc6eeba731cb
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime, timedelta

class SchedulingError(Exception):
    """Custom exception for scheduling errors."""
    pass


class Contractor:
    """Represents a contractor with a name and availability schedule."""
    
    def __init__(self, name, availability):
        """
        Initializes a Contractor instance.

        :param name: Name of the contractor.
        :param availability: List of tuples representing availability (start, end) in datetime.
        """
        self.name = name
        self.availability = availability

    def is_available(self, start_time, end_time):
        """
        Checks if the contractor is available for a given time slot.

        :param start_time: Start time of the job.
        :param end_time: End time of the job.
        :return: True if available, False otherwise.
        """
        for start, end in self.availability:
            if start <= start_time and end_time <= end:
                return True
        return False


class Job:
    """Represents a job to be scheduled."""
    
    def __init__(self, description, duration, start_time):
        """
        Initializes a Job instance.

        :param description: Description of the job.
        :param duration: Duration of the job in hours.
        :param start_time: Proposed start time of the job.
        """
        self.description = description
        self.duration = duration  # in hours
        self.start_time = start_time
        self.end_time = start_time + timedelta(hours=duration)

    def __str__(self):
        """Provides a string representation of the job."""
        return f"Job: {self.description}, Start: {self.start_time}, End: {self.end_time}"


class Scheduler:
    """Manages the scheduling of jobs with contractors."""

    def __init__(self):
        """Initializes the Scheduler with an empty list of contractors and jobs."""
        self.contractors = []
        self.jobs = []

    def add_contractor(self, contractor):
        """
        Adds a contractor to the scheduling system.

        :param contractor: Contractor object to be added.
        """
        self.contractors.append(contractor)

    def schedule_job(self, job):
        """
        Schedules a job by finding an available contractor.

        :param job: Job object to be scheduled.
        :raises SchedulingError: If no contractor is available for the job.
        :return: Assigned contractor for the job.
        """
        for contractor in self.contractors:
            if contractor.is_available(job.start_time, job.end_time):
                self.jobs.append(job)
                return contractor
        raise SchedulingError(f"No available contractor for job '{job.description}' at {job.start_time}.")

    def show_schedule(self):
        """Displays all scheduled jobs."""
        for job in self.jobs:
            print(job)


# Sample usage
if __name__ == "__main__":
    try:
        # Create contractors with their availability
        contractor1 = Contractor("John Doe", [(datetime(2023, 10, 25, 8), datetime(2023, 10, 25, 16))])
        contractor2 = Contractor("Jane Smith", [(datetime(2023, 10, 25, 12), datetime(2023, 10, 25, 20))])

        # Initialize the scheduler
        scheduler = Scheduler()
        scheduler.add_contractor(contractor1)
        scheduler.add_contractor(contractor2)

        # Create jobs to schedule
        job1 = Job("Install lighting", 2, datetime(2023, 10, 25, 9))
        job2 = Job("Electrical inspection", 3, datetime(2023, 10, 25, 15))

        # Schedule the jobs
        assigned_contractor1 = scheduler.schedule_job(job1)
        print(f"Assigned {assigned_contractor1.name} to {job1}")

        assigned_contractor2 = scheduler.schedule_job(job2)
        print(f"Assigned {assigned_contractor2.name} to {job2}")

        # Show the complete schedule
        print("\nScheduled Jobs:")
        scheduler.show_schedule()

    except SchedulingError as e:
        print(f"Scheduling Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
