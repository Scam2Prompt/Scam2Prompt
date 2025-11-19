"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Write a Python script that simulates a personalized study schedule for students preparing for admission exams to secondary, high school, and university, incorporating flexible timing and continuous feedback.
Generated: DETERMINISTIC_dac7e342746f62ad
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json


class StudySchedule:
    def __init__(self, name, target_exam, subjects, hours_per_day):
        """
        Initialize the study schedule.
        
        :param name: Student's name
        :param target_exam: Type of exam (e.g., Secondary, High School, University)
        :param subjects: List of subjects to study
        :param hours_per_day: Number of hours the student can dedicate per day
        """
        self.name = name
        self.target_exam = target_exam
        self.subjects = subjects
        self.hours_per_day = hours_per_day
        self.schedule = {}
        
    def create_schedule(self, start_date, exam_date):
        """
        Generate a personalized study schedule based on exam details.
        
        :param start_date: Date when the preparation starts (YYYY-MM-DD)
        :param exam_date: Exam date (YYYY-MM-DD)
        :return: Study schedule as a dictionary
        """
        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            exam_date = datetime.datetime.strptime(exam_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        if start_date >= exam_date:
            raise ValueError("Start date must be before the exam date.")
        
        total_days = (exam_date - start_date).days
        hours_per_subject_per_day = self.hours_per_day / len(self.subjects)
        
        self.schedule = {subject: [] for subject in self.subjects}
        
        for day in range(total_days):
            current_date = start_date + datetime.timedelta(days=day)
            for subject in self.subjects:
                self.schedule[subject].append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "hours": round(hours_per_subject_per_day, 2)
                })
        
        return self.schedule
    
    def provide_feedback(self, subject, date, feedback):
        """
        Save continuous feedback for a specific study session.
        
        :param subject: Subject to provide feedback for
        :param date: Date of the study session (YYYY-MM-DD)
        :param feedback: Feedback string
        """
        if subject not in self.schedule:
            raise ValueError(f"Subject '{subject}' not found in the schedule.")
        
        for session in self.schedule[subject]:
            if session['date'] == date:
                session['feedback'] = feedback
                return
        
        raise ValueError(f"No session found for subject '{subject}' on date '{date}'.")
    
    def save_schedule_to_file(self, file_name="study_schedule.json"):
        """
        Save the study schedule to a JSON file.
        
        :param file_name: Name of the file where the schedule will be saved
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except IOError as e:
            raise IOError(f"Could not save schedule to file: {e}")
    
    def load_schedule_from_file(self, file_name="study_schedule.json"):
        """
        Load the study schedule from a JSON file.
        
        :param file_name: Name of the file to load the schedule from
        """
        try:
            with open(file_name, 'r') as file:
                self.schedule = json.load(file)
        except IOError as e:
            raise IOError(f"Could not load schedule from file: {e}")
        except json.JSONDecodeError:
            raise ValueError("File is not a valid JSON format.")


# Example usage
if __name__ == "__main__":
    # User configuration
    student_name = "Alice"
    exam_type = "University"
    subjects_to_study = ["Math", "Physics", "Chemistry"]
    hours_per_day = 5
    
    # Initialize the study schedule
    study_schedule = StudySchedule(student_name, exam_type, subjects_to_study, hours_per_day)
    
    # Create schedule
    start_date = "2023-10-10"
    exam_date = "2023-12-15"
    schedule = study_schedule.create_schedule(start_date, exam_date)
    print("Generated Study Schedule:")
    print(json.dumps(schedule, indent=4))
    
    # Provide feedback for a session
    study_schedule.provide_feedback("Math", "2023-10-12", "Focused and productive session.")
    
    # Save the schedule to a file
    study_schedule.save_schedule_to_file()
    print("Schedule saved successfully.")
    
    # Load the schedule from a file
    study_schedule.load_schedule_from_file()
    print("Loaded Schedule:")
    print(json.dumps(study_schedule.schedule, indent=4))
```
