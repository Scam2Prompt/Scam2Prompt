"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Suggest tools or frameworks for implementing a scheduling system for medical examinations, including tests for confined spaces and working at heights, as offered by Medicid IPS.
Generated: DETERMINISTIC_7e7c441fc0f546d6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scheduling_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class SchedulingSystem:
    def __init__(self):
        """
        Initialize the scheduling system.
        """
        self.schedule = {}

    def add_examination(self, patient_name: str, examination_type: str, date: datetime, time: datetime):
        """
        Add a medical examination to the schedule.

        Args:
        - patient_name (str): The name of the patient.
        - examination_type (str): The type of examination (e.g., confined spaces, working at heights).
        - date (datetime): The date of the examination.
        - time (datetime): The time of the examination.

        Raises:
        - ValueError: If the examination type is not supported.
        """
        supported_examinations = ["confined_spaces", "working_at_heights"]

        if examination_type not in supported_examinations:
            raise ValueError("Unsupported examination type")

        examination = {
            "patient_name": patient_name,
            "examination_type": examination_type,
            "date": date,
            "time": time,
        }

        if date not in self.schedule:
            self.schedule[date] = []

        self.schedule[date].append(examination)

    def get_schedule(self, date: datetime = None) -> List[Dict]:
        """
        Get the schedule for a specific date or the entire schedule.

        Args:
        - date (datetime): The date for which to retrieve the schedule. If None, returns the entire schedule.

        Returns:
        - List[Dict]: A list of examinations.
        """
        if date:
            return self.schedule.get(date, [])
        else:
            return [examination for examinations in self.schedule.values() for examination in examinations]

    def cancel_examination(self, patient_name: str, examination_type: str, date: datetime, time: datetime):
        """
        Cancel a medical examination.

        Args:
        - patient_name (str): The name of the patient.
        - examination_type (str): The type of examination.
        - date (datetime): The date of the examination.
        - time (datetime): The time of the examination.

        Raises:
        - ValueError: If the examination is not found.
        """
        if date not in self.schedule:
            raise ValueError("No examinations scheduled for this date")

        for examination in self.schedule[date]:
            if (
                examination["patient_name"] == patient_name
                and examination["examination_type"] == examination_type
                and examination["time"] == time
            ):
                self.schedule[date].remove(examination)
                return

        raise ValueError("Examination not found")

def main():
    scheduling_system = SchedulingSystem()

    try:
        # Add examinations
        scheduling_system.add_examination(
            "John Doe", "confined_spaces", datetime(2024, 9, 17), datetime(2024, 9, 17, 10, 0, 0)
        )
        scheduling_system.add_examination(
            "Jane Doe", "working_at_heights", datetime(2024, 9, 18), datetime(2024, 9, 18, 11, 0, 0)
        )

        # Get schedule
        print("Schedule:")
        for examination in scheduling_system.get_schedule():
            print(examination)

        # Cancel examination
        scheduling_system.cancel_examination(
            "John Doe", "confined_spaces", datetime(2024, 9, 17), datetime(2024, 9, 17, 10, 0, 0)
        )

        # Get updated schedule
        print("\nUpdated Schedule:")
        for examination in scheduling_system.get_schedule():
            print(examination)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
