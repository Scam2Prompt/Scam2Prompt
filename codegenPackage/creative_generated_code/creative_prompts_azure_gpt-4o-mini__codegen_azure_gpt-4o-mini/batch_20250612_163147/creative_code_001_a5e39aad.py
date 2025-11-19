"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Write a Python script that automates the scheduling of occupational health exams, referencing the types of exams offered by Medicid IPS.
Generated: DETERMINISTIC_a5e39aad367c8aef
Batch ID: 20250612_163147
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
from typing import List, Dict, Any

class OccupationalHealthExamScheduler:
    """
    A class to automate the scheduling of occupational health exams offered by Medicid IPS.
    """

    def __init__(self, exam_data_file: str):
        """
        Initializes the scheduler with exam data from a JSON file.

        :param exam_data_file: Path to the JSON file containing exam types and availability.
        """
        self.exam_data_file = exam_data_file
        self.exams = self.load_exam_data()

    def load_exam_data(self) -> Dict[str, Any]:
        """
        Loads exam data from a JSON file.

        :return: A dictionary containing exam types and their scheduling information.
        :raises FileNotFoundError: If the specified exam data file does not exist.
        :raises json.JSONDecodeError: If the file contents cannot be parsed as JSON.
        """
        try:
            with open(self.exam_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.exam_data_file} does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the exam data file.")

    def schedule_exam(self, exam_type: str, date: datetime.date, time: str) -> str:
        """
        Schedules an occupational health exam.

        :param exam_type: The type of exam to schedule.
        :param date: The date for the exam.
        :param time: The time for the exam.
        :return: A confirmation message.
        :raises ValueError: If the exam type is not available or if the date/time is invalid.
        """
        if exam_type not in self.exams:
            raise ValueError(f"Exam type '{exam_type}' is not available.")
        
        exam_availability = self.exams[exam_type]
        if not self.is_date_time_valid(exam_availability['availability'], date, time):
            raise ValueError(f"The selected date and time for '{exam_type}' is not available.")

        # Here we would typically add the scheduling logic, such as saving to a database.
        return f"Successfully scheduled '{exam_type}' on {date} at {time}."

    def is_date_time_valid(self, availability: List[Dict[str, Any]], date: datetime.date, time: str) -> bool:
        """
        Validates if the requested date and time are within the available schedule.

        :param availability: List of available date and time slots for an exam type.
        :param date: The requested date for scheduling.
        :param time: The requested time for scheduling.
        :return: True if the requested date and time are valid, False otherwise.
        """
        for slot in availability:
            slot_date = datetime.datetime.strptime(slot['date'], '%Y-%m-%d').date()
            if slot_date == date and slot['time'] == time:
                return True
        return False

# Example usage
if __name__ == "__main__":
    scheduler = OccupationalHealthExamScheduler("exam_data.json")
    try:
        confirmation = scheduler.schedule_exam("Blood Test", datetime.date(2023, 10, 15), "10:00")
        print(confirmation)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
```

Make sure to have a properly formatted JSON file named `exam_data.json` that contains the schedule details for the exams. Here's an example of what the JSON file might look like:

```json
{
    "Blood Test": {
        "availability": [
            {"date": "2023-10-15", "time": "10:00"},
            {"date": "2023-10-15", "time": "11:00"}
        ]
    },
    "Vision Exam": {
        "availability": [
            {"date": "2023-10-16", "time": "09:00"},
            {"date": "2023-10-16", "time": "10:00"}
        ]
    }
}
```
