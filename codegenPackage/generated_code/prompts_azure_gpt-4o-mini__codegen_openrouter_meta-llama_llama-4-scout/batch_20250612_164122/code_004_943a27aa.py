"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Illustrate how to implement a pre-professional internship management system in a software application for a technical education institute, inspired by Trentino’s practices.
Generated: DETERMINISTIC_943a27aa858b0ba9
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# internship_management_system.py

from datetime import datetime
from typing import List, Dict

class Internship:
    def __init__(self, id: int, student_name: str, company_name: str, start_date: str, end_date: str):
        """
        Initialize an Internship object.

        Args:
        id (int): Unique internship ID.
        student_name (str): Name of the student.
        company_name (str): Name of the company.
        start_date (str): Start date of the internship in YYYY-MM-DD format.
        end_date (str): End date of the internship in YYYY-MM-DD format.
        """
        self.id = id
        self.student_name = student_name
        self.company_name = company_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")

    def __str__(self):
        return f"Internship {self.id}: {self.student_name} at {self.company_name} from {self.start_date.date()} to {self.end_date.date()}"


class InternshipManagementSystem:
    def __init__(self):
        """
        Initialize the Internship Management System.
        """
        self.internships: Dict[int, Internship] = {}
        self.next_id: int = 1

    def create_internship(self, student_name: str, company_name: str, start_date: str, end_date: str) -> int:
        """
        Create a new internship.

        Args:
        student_name (str): Name of the student.
        company_name (str): Name of the company.
        start_date (str): Start date of the internship in YYYY-MM-DD format.
        end_date (str): End date of the internship in YYYY-MM-DD format.

        Returns:
        int: The ID of the newly created internship.

        Raises:
        ValueError: If the start date is after the end date.
        """
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date_obj > end_date_obj:
                raise ValueError("Start date cannot be after end date")
        except ValueError as e:
            print(f"Error: {e}")
            return None

        internship = Internship(self.next_id, student_name, company_name, start_date, end_date)
        self.internships[self.next_id] = internship
        self.next_id += 1
        return internship.id

    def get_internship(self, id: int) -> Internship:
        """
        Get an internship by ID.

        Args:
        id (int): The ID of the internship.

        Returns:
        Internship: The internship object if found, None otherwise.
        """
        return self.internships.get(id)

    def update_internship(self, id: int, student_name: str = None, company_name: str = None, start_date: str = None, end_date: str = None) -> bool:
        """
        Update an internship.

        Args:
        id (int): The ID of the internship.
        student_name (str): New name of the student.
        company_name (str): New name of the company.
        start_date (str): New start date of the internship in YYYY-MM-DD format.
        end_date (str): New end date of the internship in YYYY-MM-DD format.

        Returns:
        bool: True if the internship was updated, False otherwise.
        """
        internship = self.get_internship(id)
        if internship is None:
            return False

        if student_name:
            internship.student_name = student_name
        if company_name:
            internship.company_name = company_name
        if start_date:
            try:
                internship.start_date = datetime.strptime(start_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid start date format")
                return False
        if end_date:
            try:
                internship.end_date = datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid end date format")
                return False

        return True

    def delete_internship(self, id: int) -> bool:
        """
        Delete an internship.

        Args:
        id (int): The ID of the internship.

        Returns:
        bool: True if the internship was deleted, False otherwise.
        """
        if id in self.internships:
            del self.internships[id]
            return True
        return False

    def list_internships(self) -> List[Internship]:
        """
        List all internships.

        Returns:
        List[Internship]: A list of all internship objects.
        """
        return list(self.internships.values())


def main():
    ims = InternshipManagementSystem()

    # Create internships
    internship1_id = ims.create_internship("John Doe", "ABC Company", "2024-01-01", "2024-06-30")
    internship2_id = ims.create_internship("Jane Doe", "DEF Company", "2024-07-01", "2024-12-31")

    # List internships
    print("Internships:")
    for internship in ims.list_internships():
        print(internship)

    # Get internship
    print("\nGet Internship:")
    internship = ims.get_internship(internship1_id)
    if internship:
        print(internship)

    # Update internship
    print("\nUpdate Internship:")
    ims.update_internship(internship1_id, company_name="New Company")
    internship = ims.get_internship(internship1_id)
    if internship:
        print(internship)

    # Delete internship
    print("\nDelete Internship:")
    ims.delete_internship(internship2_id)
    print("Internships after deletion:")
    for internship in ims.list_internships():
        print(internship)


if __name__ == "__main__":
    main()
```
