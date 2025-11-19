"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write a script to schedule and track laboratory tests such as hematology, immunology, and toxicology, ensuring compliance with the workflow described on Medicid IPS's website.
Generated: DETERMINISTIC_da73ffa7a5721bfd
Batch ID: 20250612_150902
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
from typing import List, Dict, Optional

class LabTest:
    """Class representing a laboratory test."""
    
    def __init__(self, test_type: str, patient_id: str, scheduled_date: datetime.date):
        self.test_type = test_type
        self.patient_id = patient_id
        self.scheduled_date = scheduled_date
        self.status = 'Scheduled'  # Initial status of the test

    def __repr__(self):
        return f"LabTest(test_type={self.test_type}, patient_id={self.patient_id}, scheduled_date={self.scheduled_date}, status={self.status})"


class LabTestScheduler:
    """Class to schedule and track laboratory tests."""
    
    def __init__(self):
        self.tests: List[LabTest] = []  # List to store scheduled tests

    def schedule_test(self, test_type: str, patient_id: str, scheduled_date: datetime.date) -> None:
        """Schedules a new laboratory test."""
        if scheduled_date < datetime.date.today():
            raise ValueError("Scheduled date cannot be in the past.")
        
        new_test = LabTest(test_type, patient_id, scheduled_date)
        self.tests.append(new_test)
        print(f"Test scheduled: {new_test}")

    def get_tests_by_patient(self, patient_id: str) -> List[LabTest]:
        """Retrieves all tests scheduled for a specific patient."""
        return [test for test in self.tests if test.patient_id == patient_id]

    def update_test_status(self, patient_id: str, test_type: str, new_status: str) -> None:
        """Updates the status of a scheduled test."""
        for test in self.tests:
            if test.patient_id == patient_id and test.test_type == test_type:
                test.status = new_status
                print(f"Updated test status: {test}")
                return
        raise ValueError("Test not found for the given patient ID and test type.")

    def save_tests_to_file(self, filename: str) -> None:
        """Saves the scheduled tests to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([test.__dict__ for test in self.tests], file, default=str)
            print(f"Tests saved to {filename}")
        except IOError as e:
            print(f"Error saving tests to file: {e}")

    def load_tests_from_file(self, filename: str) -> None:
        """Loads scheduled tests from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tests_data = json.load(file)
                self.tests = [LabTest(**data) for data in tests_data]
            print(f"Tests loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading tests from file: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = LabTestScheduler()
    
    # Schedule some tests
    try:
        scheduler.schedule_test("Hematology", "patient_001", datetime.date(2023, 12, 1))
        scheduler.schedule_test("Immunology", "patient_001", datetime.date(2023, 12, 5))
        scheduler.schedule_test("Toxicology", "patient_002", datetime.date(2023, 11, 20))
    except ValueError as e:
        print(e)

    # Update a test status
    try:
        scheduler.update_test_status("patient_001", "Hematology", "Completed")
    except ValueError as e:
        print(e)

    # Save tests to a file
    scheduler.save_tests_to_file("scheduled_tests.json")

    # Load tests from a file
    scheduler.load_tests_from_file("scheduled_tests.json")
```
