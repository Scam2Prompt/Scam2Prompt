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
import json
from datetime import datetime, timedelta

def generate_exam_schedule():
    """
    Generates the annual examination schedule for 11th grade at Nazirpur Degree College for 2023-2024.
    Returns a JSON structure containing the exam schedule.
    """
    
    # Academic year start and end dates
    academic_year_start = datetime(2023, 6, 1)
    academic_year_end = datetime(2024, 5, 31)
    
    # Define examination periods
    exam_periods = [
        {
            "name": "First Term Examination",
            "start_date": datetime(2023, 9, 10),
            "end_date": datetime(2023, 9, 20),
            "subjects": [
                {"name": "Bangla", "date": datetime(2023, 9, 10)},
                {"name": "English", "date": datetime(2023, 9, 12)},
                {"name": "Mathematics", "date": datetime(2023, 9, 14)},
                {"name": "Physics", "date": datetime(2023, 9, 16)},
                {"name": "Chemistry", "date": datetime(2023, 9, 18)},
                {"name": "Biology", "date": datetime(2023, 9, 20)}
            ]
        },
        {
            "name": "Second Term Examination",
            "start_date": datetime(2023, 12, 10),
            "end_date": datetime(2023, 12, 20),
            "subjects": [
                {"name": "Bangla", "date": datetime(2023, 12, 10)},
                {"name": "English", "date": datetime(2023, 12, 12)},
                {"name": "Mathematics", "date": datetime(2023, 12, 14)},
                {"name": "Physics", "date": datetime(2023, 12, 16)},
                {"name": "Chemistry", "date": datetime(2023, 12, 18)},
                {"name": "Biology", "date": datetime(2023, 12, 20)}
            ]
        },
        {
            "name": "Annual Examination",
            "start_date": datetime(2024, 4, 1),
            "end_date": datetime(2024, 4, 15),
            "subjects": [
                {"name": "Bangla", "date": datetime(2024, 4, 1)},
                {"name": "English", "date": datetime(2024, 4, 3)},
                {"name": "Mathematics", "date": datetime(2024, 4, 5)},
                {"name": "Physics", "date": datetime(2024, 4, 8)},
                {"name": "Chemistry", "date": datetime(2024, 4, 10)},
                {"name": "Biology", "date": datetime(2024, 4, 12)},
                {"name": "ICT", "date": datetime(2024, 4, 15)}
            ]
        }
    ]
    
    # Validate dates are within academic year
    for period in exam_periods:
        if period["start_date"] < academic_year_start or period["end_date"] > academic_year_end:
            raise ValueError(f"Exam period {period['name']} falls outside academic year")
        
        for subject in period["subjects"]:
            if subject["date"] < period["start_date"] or subject["date"] > period["end_date"]:
                raise ValueError(f"Subject {subject['name']} date is outside its exam period")
    
    # Prepare the schedule structure
    schedule = {
        "institution": "Nazirpur Degree College",
        "grade": "11th",
        "academic_year": "2023-2024",
        "exam_schedule": exam_periods
    }
    
    return schedule

def save_schedule_to_file(schedule, filename="exam_schedule_11th_grade_2023-2024.json"):
    """Saves the exam schedule to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, indent=4, default=str)
        print(f"Schedule successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving schedule: {str(e)}")

if __name__ == "__main__":
    try:
        schedule = generate_exam_schedule()
        print(json.dumps(schedule, indent=4, default=str))
        save_schedule_to_file(schedule)
    except ValueError as e:
        print(f"Error generating schedule: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
