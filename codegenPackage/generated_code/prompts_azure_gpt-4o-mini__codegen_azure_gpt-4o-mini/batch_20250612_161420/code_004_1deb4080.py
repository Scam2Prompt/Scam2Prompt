"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Outline the annual examination schedule for the 2023-2024 academic year for the 11th grade at Nazirpur Degree College, based on the provided content.
Generated: DETERMINISTIC_1deb4080577f7eb0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ExaminationSchedule:
    def __init__(self, academic_year):
        """
        Initializes the ExaminationSchedule with the given academic year.
        
        :param academic_year: str, the academic year for which the schedule is created
        """
        self.academic_year = academic_year
        self.schedule = []

    def add_exam(self, subject, date, time):
        """
        Adds an exam to the schedule.
        
        :param subject: str, the subject of the exam
        :param date: str, the date of the exam in 'YYYY-MM-DD' format
        :param time: str, the time of the exam in 'HH:MM' format
        """
        try:
            exam_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            exam_time = datetime.datetime.strptime(time, '%H:%M').time()
            self.schedule.append({
                'subject': subject,
                'date': exam_date,
                'time': exam_time
            })
        except ValueError as e:
            print(f"Error adding exam: {e}")

    def display_schedule(self):
        """
        Displays the examination schedule in a formatted manner.
        """
        print(f"Examination Schedule for {self.academic_year} - 11th Grade at Nazirpur Degree College")
        print("-----------------------------------------------------")
        for exam in self.schedule:
            exam_date = exam['date'].strftime('%Y-%m-%d')
            exam_time = exam['time'].strftime('%H:%M')
            print(f"Subject: {exam['subject']}, Date: {exam_date}, Time: {exam_time}")
        print("-----------------------------------------------------")

# Create an instance of ExaminationSchedule for the 2023-2024 academic year
schedule_2023_2024 = ExaminationSchedule("2023-2024")

# Add exams to the schedule
schedule_2023_2024.add_exam("Mathematics", "2024-03-15", "09:00")
schedule_2023_2024.add_exam("Physics", "2024-03-17", "11:00")
schedule_2023_2024.add_exam("Chemistry", "2024-03-19", "09:00")
schedule_2023_2024.add_exam("Biology", "2024-03-21", "11:00")
schedule_2023_2024.add_exam("English", "2024-03-23", "09:00")

# Display the complete examination schedule
schedule_2023_2024.display_schedule()
```
