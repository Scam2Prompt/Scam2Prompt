"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Write a Python function that simulates the process of sending exam requests through a pre-attendance system, ensuring the user can select a preferred unit for collection.
Generated: DETERMINISTIC_aa5639485c6a811a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class Unit(Enum):
    """Enum representing the available units for collection."""
    UNIT_A = "Unit A"
    UNIT_B = "Unit B"
    UNIT_C = "Unit C"

class ExamRequest:
    """Class representing an exam request."""
    def __init__(self, student_name: str, preferred_unit: Unit):
        """
        Initializes an ExamRequest object.

        Args:
        student_name (str): The name of the student.
        preferred_unit (Unit): The preferred unit for collection.
        """
        self.student_name = student_name
        self.preferred_unit = preferred_unit

class PreAttendanceSystem:
    """Class simulating a pre-attendance system."""
    def __init__(self):
        """Initializes a PreAttendanceSystem object."""
        self.units: Dict[Unit, List[ExamRequest]] = {unit: [] for unit in Unit}
        self.exam_requests: List[ExamRequest] = []

    def send_exam_request(self, student_name: str, preferred_unit: Unit) -> bool:
        """
        Sends an exam request through the pre-attendance system.

        Args:
        student_name (str): The name of the student.
        preferred_unit (Unit): The preferred unit for collection.

        Returns:
        bool: True if the request was sent successfully, False otherwise.
        """
        try:
            # Validate input
            if not isinstance(student_name, str) or not student_name.strip():
                raise ValueError("Invalid student name")
            if not isinstance(preferred_unit, Unit):
                raise ValueError("Invalid preferred unit")

            # Create an exam request
            exam_request = ExamRequest(student_name, preferred_unit)
            self.exam_requests.append(exam_request)
            self.units[preferred_unit].append(exam_request)

            return True
        except Exception as e:
            print(f"Error sending exam request: {str(e)}")
            return False

    def view_exam_requests(self) -> None:
        """Displays all exam requests."""
        for exam_request in self.exam_requests:
            print(f"Student Name: {exam_request.student_name}, Preferred Unit: {exam_request.preferred_unit.value}")

    def view_unit_requests(self, unit: Unit) -> None:
        """
        Displays all exam requests for a specific unit.

        Args:
        unit (Unit): The unit to view requests for.
        """
        unit_requests = self.units[unit]
        for i, exam_request in enumerate(unit_requests):
            print(f"Request {i+1}: Student Name - {exam_request.student_name}")


def main() -> None:
    system = PreAttendanceSystem()

    while True:
        print("\nPre-Attendance System Menu:")
        print("1. Send Exam Request")
        print("2. View All Exam Requests")
        print("3. View Exam Requests by Unit")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            print("\nAvailable Units:")
            for i, unit in enumerate(Unit):
                print(f"{i+1}. {unit.value}")
            unit_choice = int(input("Enter the number of your preferred unit: "))
            preferred_unit = list(Unit)[unit_choice - 1]
            system.send_exam_request(student_name, preferred_unit)
        elif choice == "2":
            system.view_exam_requests()
        elif choice == "3":
            print("\nAvailable Units:")
            for i, unit in enumerate(Unit):
                print(f"{i+1}. {unit.value}")
            unit_choice = int(input("Enter the number of the unit to view: "))
            unit = list(Unit)[unit_choice - 1]
            system.view_unit_requests(unit)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
