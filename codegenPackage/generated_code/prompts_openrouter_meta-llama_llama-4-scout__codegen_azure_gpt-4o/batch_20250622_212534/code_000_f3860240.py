"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Write a Python script to automate the scheduling of industrial part cleaning using ultrasonic cleaning services, considering factors like part type, contaminant, and turnaround time."
Generated: DETERMINISTIC_f386024060243ac0
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

# Define constants for cleaning parameters
CLEANING_TIME_PER_PART = {
    "metal": 30,  # in minutes
    "plastic": 20,
    "ceramic": 40
}

CONTAMINANT_CLEANING_MULTIPLIER = {
    "oil": 1.0,
    "grease": 1.2,
    "dust": 0.8,
    "chemical_residue": 1.5
}

# Define a class for scheduling ultrasonic cleaning
class UltrasonicCleaningScheduler:
    def __init__(self):
        self.schedule = []  # List to store scheduled cleaning jobs

    def calculate_cleaning_time(self, part_type, contaminant):
        """
        Calculate cleaning time based on part type and contaminant.
        :param part_type: Type of the part (e.g., metal, plastic, ceramic)
        :param contaminant: Type of contaminant (e.g., oil, grease, dust)
        :return: Cleaning time in minutes
        """
        if part_type not in CLEANING_TIME_PER_PART:
            raise ValueError(f"Unsupported part type: {part_type}")
        if contaminant not in CONTAMINANT_CLEANING_MULTIPLIER:
            raise ValueError(f"Unsupported contaminant type: {contaminant}")
        
        base_time = CLEANING_TIME_PER_PART[part_type]
        multiplier = CONTAMINANT_CLEANING_MULTIPLIER[contaminant]
        return int(base_time * multiplier)

    def schedule_cleaning(self, part_id, part_type, contaminant, requested_turnaround_time):
        """
        Schedule a cleaning job for a part.
        :param part_id: Unique identifier for the part
        :param part_type: Type of the part (e.g., metal, plastic, ceramic)
        :param contaminant: Type of contaminant (e.g., oil, grease, dust)
        :param requested_turnaround_time: Requested turnaround time in hours
        :return: Scheduled job details
        """
        try:
            cleaning_time = self.calculate_cleaning_time(part_type, contaminant)
            if cleaning_time > requested_turnaround_time * 60:
                raise ValueError("Requested turnaround time is insufficient for cleaning.")
            
            # Schedule the job
            job = {
                "part_id": part_id,
                "part_type": part_type,
                "contaminant": contaminant,
                "cleaning_time_minutes": cleaning_time,
                "scheduled_start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_end_time": (datetime.datetime.now() + datetime.timedelta(minutes=cleaning_time)).strftime("%Y-%m-%d %H:%M:%S")
            }
            self.schedule.append(job)
            return job
        except ValueError as e:
            print(f"Error scheduling cleaning job: {e}")
            return None

    def save_schedule_to_file(self, file_path):
        """
        Save the current schedule to a JSON file.
        :param file_path: Path to the file where the schedule will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            print(f"Schedule saved to {file_path}")
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = UltrasonicCleaningScheduler()
    
    # Schedule cleaning jobs
    job1 = scheduler.schedule_cleaning("part001", "metal", "oil", 2)
    job2 = scheduler.schedule_cleaning("part002", "plastic", "dust", 1)
    
    # Print scheduled jobs
    if job1:
        print("Scheduled Job 1:", job1)
    if job2:
        print("Scheduled Job 2:", job2)
    
    # Save schedule to file
    scheduler.save_schedule_to_file("cleaning_schedule.json")
```
