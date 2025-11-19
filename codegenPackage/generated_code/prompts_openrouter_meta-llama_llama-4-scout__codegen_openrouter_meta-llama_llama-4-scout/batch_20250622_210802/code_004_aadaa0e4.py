"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Create a certification program for commercial personnel (credit managers/ officers) using SIF's capacitación services.
Generated: DETERMINISTIC_aadaa0e47cabb475
Batch ID: 20250622_210802
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://sif-api.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# certification_program.py

from datetime import datetime
from typing import List, Dict

class CertificationProgram:
    """
    Certification program for commercial personnel using SIF's capacitación services.
    """

    def __init__(self, program_name: str, sif_api_url: str, sif_api_key: str):
        """
        Initialize the certification program.

        Args:
        - program_name (str): Name of the certification program.
        - sif_api_url (str): URL of SIF's API.
        - sif_api_key (str): API key for SIF's API.
        """
        self.program_name = program_name
        self.sif_api_url = sif_api_url
        self.sif_api_key = sif_api_key
        self.participants = {}
        self.courses = {}

    def add_participant(self, participant_id: str, name: str, email: str):
        """
        Add a participant to the certification program.

        Args:
        - participant_id (str): Unique ID of the participant.
        - name (str): Name of the participant.
        - email (str): Email address of the participant.
        """
        self.participants[participant_id] = {
            "name": name,
            "email": email,
            "courses": []
        }

    def add_course(self, course_id: str, course_name: str, duration: int):
        """
        Add a course to the certification program.

        Args:
        - course_id (str): Unique ID of the course.
        - course_name (str): Name of the course.
        - duration (int): Duration of the course in hours.
        """
        self.courses[course_id] = {
            "course_name": course_name,
            "duration": duration
        }

    def enroll_participant_in_course(self, participant_id: str, course_id: str):
        """
        Enroll a participant in a course.

        Args:
        - participant_id (str): Unique ID of the participant.
        - course_id (str): Unique ID of the course.

        Raises:
        - ValueError: If the participant or course does not exist.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant does not exist")
        if course_id not in self.courses:
            raise ValueError("Course does not exist")

        self.participants[participant_id]["courses"].append(course_id)

    def get_participant_courses(self, participant_id: str) -> List[str]:
        """
        Get the courses a participant is enrolled in.

        Args:
        - participant_id (str): Unique ID of the participant.

        Returns:
        - List[str]: List of course IDs the participant is enrolled in.

        Raises:
        - ValueError: If the participant does not exist.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant does not exist")

        return self.participants[participant_id]["courses"]

    def send_notification(self, participant_id: str, course_id: str):
        """
        Send a notification to the participant about the course.

        Args:
        - participant_id (str): Unique ID of the participant.
        - course_id (str): Unique ID of the course.

        Raises:
        - ValueError: If the participant or course does not exist.
        """
        import requests

        if participant_id not in self.participants:
            raise ValueError("Participant does not exist")
        if course_id not in self.courses:
            raise ValueError("Course does not exist")

        participant_email = self.participants[participant_id]["email"]
        course_name = self.courses[course_id]["course_name"]

        # Simulate sending a notification using SIF's API
        try:
            response = requests.post(
                f"{self.sif_api_url}/notifications",
                headers={"Authorization": f"Bearer {self.sif_api_key}"},
                json={"email": participant_email, "message": f"Course {course_name} assigned"}
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending notification: {e}")

def main():
    # Create a certification program
    program = CertificationProgram(
        "Commercial Personnel Certification",
        "https://sif-api.example.com",
        "your_api_key_here"
    )

    # Add participants
    program.add_participant("P001", "John Doe", "john.doe@example.com")
    program.add_participant("P002", "Jane Smith", "jane.smith@example.com")

    # Add courses
    program.add_course("C001", "Credit Management", 4)
    program.add_course("C002", "Risk Assessment", 3)

    # Enroll participants in courses
    program.enroll_participant_in_course("P001", "C001")
    program.enroll_participant_in_course("P002", "C002")

    # Get participant courses
    print(program.get_participant_courses("P001"))  # Output: ['C001']
    print(program.get_participant_courses("P002"))  # Output: ['C002']

    # Send notifications
    program.send_notification("P001", "C001")
    program.send_notification("P002", "C002")

if __name__ == "__main__":
    main()
```
