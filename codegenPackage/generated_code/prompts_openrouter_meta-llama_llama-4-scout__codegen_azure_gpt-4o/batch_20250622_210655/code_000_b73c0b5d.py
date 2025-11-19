"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Generate a Python script to manage certification programs for a training institute like Geta Consulenze, including tracking course completion and certification expiry dates."
Generated: DETERMINISTIC_b73c0b5d97ad2b26
Batch ID: 20250622_210655
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

class CertificationManager:
    """
    A class to manage certification programs for a training institute.
    Tracks course completion and certification expiry dates.
    """

    def __init__(self, data_file: str = "certifications.json"):
        """
        Initializes the CertificationManager with a data file to store certifications.

        :param data_file: Path to the JSON file for storing certification data.
        """
        self.data_file = data_file
        self.certifications = self._load_data()

    def _load_data(self) -> Dict[str, Dict]:
        """
        Loads certification data from the JSON file.

        :return: A dictionary containing certification data.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty dictionary if the file does not exist
            return {}
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Corrupted data file. Starting with empty data.")
            return {}

    def _save_data(self) -> None:
        """
        Saves certification data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.certifications, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_certification(self, student_name: str, course_name: str, completion_date: str, validity_years: int) -> None:
        """
        Adds a new certification for a student.

        :param student_name: Name of the student.
        :param course_name: Name of the course.
        :param completion_date: Date of course completion (YYYY-MM-DD).
        :param validity_years: Number of years the certification is valid.
        """
        try:
            completion_date_obj = datetime.datetime.strptime(completion_date, "%Y-%m-%d")
            expiry_date = completion_date_obj + datetime.timedelta(days=validity_years * 365)

            self.certifications[student_name] = {
                "course_name": course_name,
                "completion_date": completion_date,
                "expiry_date": expiry_date.strftime("%Y-%m-%d")
            }
            self._save_data()
            print(f"Certification added for {student_name}.")
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")

    def get_certification(self, student_name: str) -> Optional[Dict]:
        """
        Retrieves certification details for a student.

        :param student_name: Name of the student.
        :return: A dictionary containing certification details, or None if not found.
        """
        return self.certifications.get(student_name, None)

    def check_expiry(self, student_name: str) -> Optional[bool]:
        """
        Checks if a student's certification has expired.

        :param student_name: Name of the student.
        :return: True if expired, False if valid, or None if not found.
        """
        certification = self.get_certification(student_name)
        if not certification:
            print(f"No certification found for {student_name}.")
            return None

        expiry_date = datetime.datetime.strptime(certification["expiry_date"], "%Y-%m-%d")
        return datetime.datetime.now() > expiry_date

    def list_certifications(self) -> List[Dict]:
        """
        Lists all certifications.

        :return: A list of dictionaries containing certification details.
        """
        return list(self.certifications.values())


# Example usage
if __name__ == "__main__":
    manager = CertificationManager()

    # Add certifications
    manager.add_certification("Alice", "Python Programming", "2023-01-15", 2)
    manager.add_certification("Bob", "Data Science", "2022-06-10", 1)

    # Retrieve certification
    print(manager.get_certification("Alice"))

    # Check expiry
    is_expired = manager.check_expiry("Bob")
    if is_expired is not None:
        print(f"Bob's certification expired: {is_expired}")

    # List all certifications
    print(manager.list_certifications())
```
