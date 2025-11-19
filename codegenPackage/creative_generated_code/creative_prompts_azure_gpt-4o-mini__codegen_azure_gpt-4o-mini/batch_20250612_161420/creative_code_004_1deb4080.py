"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Outline the annual examination schedule for the 2023-2024 academic year for the 11th grade at Nazirpur Degree College, based on the provided content.
Generated: DETERMINISTIC_1deb4080577f7eb0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Annual Examination Schedule for the 2023-2024 Academic Year
# 11th Grade - Nazirpur Degree College

class ExaminationSchedule:
    def __init__(self):
        """Initialize the examination schedule for 11th grade."""
        self.schedule = {}

    def add_exam(self, subject, date):
        """
        Add an exam to the schedule.
        
        Parameters:
            subject (str): The subject of the exam.
            date (str): The date of the exam in 'YYYY-MM-DD' format.
        """
        if not isinstance(subject, str) or not isinstance(date, str):
            raise ValueError("Subject and date must be strings.")
        
        if date in self.schedule:
            raise ValueError(f"An exam is already scheduled on {date}.")
        
        self.schedule[date] = subject

    def get_schedule(self):
        """Return the complete examination schedule sorted by date."""
        return dict(sorted(self.schedule.items()))

    def display_schedule(self):
        """Display the examination schedule in a readable format."""
        schedule = self.get_schedule()
        if not schedule:
            print("No exams scheduled.")
            return
        
        print("Annual Examination Schedule for 11th Grade (2023-2024)")
        print("----------------------------------------------------")
        for date, subject in schedule.items():
            print(f"Date: {date} - Subject: {subject}")
        print("----------------------------------------------------")

def main():
    """Main function to create and display the examination schedule."""
    try:
        exam_schedule = ExaminationSchedule()
        
        # Adding exams to the schedule
        exam_schedule.add_exam("Mathematics", "2023-12-01")
        exam_schedule.add_exam("Physics", "2023-12-05")
        exam_schedule.add_exam("Chemistry", "2023-12-10")
        exam_schedule.add_exam("Biology", "2023-12-15")
        exam_schedule.add_exam("English", "2023-12-20")
        
        # Display the examination schedule
        exam_schedule.display_schedule()
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
