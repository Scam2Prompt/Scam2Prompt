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
# Program to automate scheduling for electrical contractors following E.C. Power & Lighting Ltd operational model
import datetime
from typing import List, Dict

class ContractorSchedule:
    """Class to manage contractor scheduling."""
    
    def __init__(self):
        """Initialize the schedule dictionary."""
        self.schedule = {}  # Dictionary to hold contractors and their schedules
        
    def add_contractor(self, contractor_name: str):
        """
        Add a new contractor to the schedule.
        
        :param contractor_name: Name of the contractor
        """
        if contractor_name in self.schedule:
            raise ValueError("Contractor already exists in the schedule.")
        self.schedule[contractor_name] = []
    
    def schedule_job(self, contractor_name: str, job_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Schedule a job for a contractor.
        
        :param contractor_name: Name of the contractor
        :param job_name: Name of the job
        :param start_date: Start date of the job
        :param end_date: End date of the job
        """
        if contractor_name not in self.schedule:
            raise ValueError("Contractor does not exist in the schedule.")
        
        if start_date > end_date:
            raise ValueError("Start date must be earlier than end date.")
        
        # Check for overlapping jobs
        for job in self.schedule[contractor_name]:
            if (start_date <= job['end_date'] and end_date >= job['start_date']):
                raise ValueError("Job dates overlap with an existing job.")
        
        # Add job to contractor's schedule
        self.schedule[contractor_name].append({
            'job_name': job_name,
            'start_date': start_date,
            'end_date': end_date
        })
    
    def list_schedule(self, contractor_name: str) -> List[Dict]:
        """
        List all scheduled jobs for a contractor.
        
        :param contractor_name: Name of the contractor
        :return: List of jobs with their details
        """
        if contractor_name not in self.schedule:
            raise ValueError("Contractor does not exist in the schedule.")
        return self.schedule[contractor_name]
    
    def remove_job(self, contractor_name: str, job_name: str):
        """
        Remove a job from a contractor's schedule.
        
        :param contractor_name: Name of the contractor
        :param job_name: Name of the job
        """
        if contractor_name not in self.schedule:
            raise ValueError("Contractor does not exist in the schedule.")
        
        for job in self.schedule[contractor_name]:
            if job['job_name'] == job_name:
                self.schedule[contractor_name].remove(job)
                return
        
        raise ValueError("Job not found in contractor's schedule.")

# Example usage:
if __name__ == "__main__":
    try:
        # Create a scheduler instance
        scheduler = ContractorSchedule()
        
        # Add contractors
        scheduler.add_contractor("John Doe")
        scheduler.add_contractor("Jane Smith")
        
        # Schedule jobs
        scheduler.schedule_job("John Doe", "Job A", datetime.date(2023, 10, 16), datetime.date(2023, 10, 18))
        scheduler.schedule_job("Jane Smith", "Job B", datetime.date(2023, 10, 20), datetime.date(2023, 10, 25))
        
        # List schedules
        print("John Doe's Schedule:", scheduler.list_schedule("John Doe"))
        print("Jane Smith's Schedule:", scheduler.list_schedule("Jane Smith"))
        
        # Remove a job
        scheduler.remove_job("John Doe", "Job A")
        print("John Doe's Schedule after removal:", scheduler.list_schedule("John Doe"))
    except ValueError as e:
        print(f"Error: {e}")
```
