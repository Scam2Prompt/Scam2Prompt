"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Write a Python script to create a flexible schedule system for students preparing for admission exams, referencing the personalized class structure described on Educar Comitán's website.
Generated: DETERMINISTIC_b7ec97ec5b64b1b1
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta


class ScheduleSystem:
    """
    A flexible schedule management system for students preparing for admission exams.
    """
    
    def __init__(self):
        """
        Initializes the ScheduleSystem class with an empty schedule.
        """
        self.schedule = {}

    def create_schedule(self, student_name, subjects, start_date, end_date):
        """
        Creates a schedule for a student with specified subjects, start date, and end date.
        
        Args:
            student_name (str): Name of the student.
            subjects (list): List of subjects to be studied.
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.

        Returns:
            dict: The newly created schedule.
        """
        try:
            # Validate dates
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start_date_obj >= end_date_obj:
                raise ValueError("End date must be after start date.")
            
            # Calculate total days and distribute subjects
            total_days = (end_date_obj - start_date_obj).days + 1
            days_per_subject = total_days // len(subjects)
            remaining_days = total_days % len(subjects)
            
            # Generate schedule with flexible subject allocation
            generated_schedule = {}
            current_date = start_date_obj
            for subject in subjects:
                subject_days = days_per_subject + (1 if remaining_days > 0 else 0)
                remaining_days -= 1
                
                subject_schedule = []
                for _ in range(subject_days):
                    subject_schedule.append(current_date.strftime('%Y-%m-%d'))
                    current_date += timedelta(days=1)
                
                generated_schedule[subject] = subject_schedule
            
            # Save the schedule for the student
            self.schedule[student_name] = generated_schedule
            return generated_schedule

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_schedule(self, student_name):
        """
        Retrieves the schedule for a given student.
        
        Args:
            student_name (str): Name of the student.

        Returns:
            dict: The student's schedule if found, otherwise None.
        """
        return self.schedule.get(student_name, None)

    def save_schedule_to_file(self, filename):
        """
        Saves the schedules to a JSON file.
        
        Args:
            filename (str): Name of the file to save schedules.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            print("Schedules saved successfully.")
        except Exception as e:
            print(f"Failed to save schedules to file: {e}")

    def load_schedule_from_file(self, filename):
        """
        Loads schedules from a JSON file.
        
        Args:
            filename (str): Name of the file to load schedules from.
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
            print("Schedules loaded successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Failed to load schedules from file: {e}")


# Example usage
if __name__ == "__main__":
    system = ScheduleSystem()
    
    # Create a schedule for a student
    student_name = "John Doe"
    subjects = ["Math", "Physics", "Chemistry"]
    start_date = "2023-10-01"
    end_date = "2023-10-15"
    
    schedule = system.create_schedule(student_name, subjects, start_date, end_date)
    if schedule:
        print(f"Schedule for {student_name}:")
        print(json.dumps(schedule, indent=4))
    
    # Save the schedule to a file
    system.save_schedule_to_file("schedules.json")
    
    # Load the schedule from the file
    system.load_schedule_from_file("schedules.json")
    
    # Retrieve the schedule for a student
    retrieved_schedule = system.get_schedule(student_name)
    if retrieved_schedule:
        print(f"\nRetrieved schedule for {student_name}:")
        print(json.dumps(retrieved_schedule, indent=4))
```
