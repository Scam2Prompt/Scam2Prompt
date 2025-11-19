"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Develop a code snippet to track staff competency in infection prevention and control measures, as required by Shareth Homecare Services' outbreak prevention program."
Generated: DETERMINISTIC_1a4cf8f2a8a089a7
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staff_competency_tracker.py

from datetime import datetime
from typing import Dict, List

class StaffMember:
    """Represents a staff member with their competency details."""

    def __init__(self, staff_id: int, name: str):
        """
        Initializes a StaffMember object.

        Args:
        staff_id (int): Unique identifier for the staff member.
        name (str): Name of the staff member.
        """
        self.staff_id = staff_id
        self.name = name
        self.competencies = {}  # type: Dict[str, bool]

    def add_competency(self, competency_name: str, is_proficient: bool):
        """
        Adds a competency to the staff member's record.

        Args:
        competency_name (str): Name of the competency.
        is_proficient (bool): Whether the staff member is proficient in the competency.
        """
        self.competencies[competency_name] = is_proficient

    def update_competency(self, competency_name: str, is_proficient: bool):
        """
        Updates a competency in the staff member's record.

        Args:
        competency_name (str): Name of the competency.
        is_proficient (bool): Whether the staff member is proficient in the competency.

        Raises:
        ValueError: If the competency does not exist in the staff member's record.
        """
        if competency_name not in self.competencies:
            raise ValueError(f"Competency '{competency_name}' does not exist.")
        self.competencies[competency_name] = is_proficient

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}"


class InfectionPreventionProgram:
    """Manages staff competency in infection prevention and control measures."""

    def __init__(self):
        self.staff_members = {}  # type: Dict[int, StaffMember]
        self.competency_names = []  # type: List[str]

    def add_staff_member(self, staff_id: int, name: str):
        """
        Adds a staff member to the program.

        Args:
        staff_id (int): Unique identifier for the staff member.
        name (str): Name of the staff member.
        """
        self.staff_members[staff_id] = StaffMember(staff_id, name)

    def add_competency_name(self, competency_name: str):
        """
        Adds a competency name to the program.

        Args:
        competency_name (str): Name of the competency.
        """
        self.competency_names.append(competency_name)

    def assign_competency(self, staff_id: int, competency_name: str, is_proficient: bool):
        """
        Assigns a competency to a staff member.

        Args:
        staff_id (int): Unique identifier for the staff member.
        competency_name (str): Name of the competency.
        is_proficient (bool): Whether the staff member is proficient in the competency.

        Raises:
        ValueError: If the staff member or competency does not exist.
        """
        if staff_id not in self.staff_members:
            raise ValueError(f"Staff member with ID {staff_id} does not exist.")
        if competency_name not in self.competency_names:
            raise ValueError(f"Competency '{competency_name}' does not exist.")

        self.staff_members[staff_id].add_competency(competency_name, is_proficient)

    def update_competency(self, staff_id: int, competency_name: str, is_proficient: bool):
        """
        Updates a competency for a staff member.

        Args:
        staff_id (int): Unique identifier for the staff member.
        competency_name (str): Name of the competency.
        is_proficient (bool): Whether the staff member is proficient in the competency.

        Raises:
        ValueError: If the staff member or competency does not exist.
        """
        if staff_id not in self.staff_members:
            raise ValueError(f"Staff member with ID {staff_id} does not exist.")
        if competency_name not in self.competency_names:
            raise ValueError(f"Competency '{competency_name}' does not exist.")

        self.staff_members[staff_id].update_competency(competency_name, is_proficient)

    def print_staff_competencies(self):
        """Prints the competency details for all staff members."""
        for staff_member in self.staff_members.values():
            print(staff_member)
            for competency_name, is_proficient in staff_member.competencies.items():
                print(f"  - {competency_name}: {'Proficient' if is_proficient else 'Not Proficient'}")
            print()


def main():
    program = InfectionPreventionProgram()

    # Add competency names
    program.add_competency_name("Hand Hygiene")
    program.add_competency_name("Personal Protective Equipment (PPE)")
    program.add_competency_name("Isolation Precautions")

    # Add staff members
    program.add_staff_member(1, "John Doe")
    program.add_staff_member(2, "Jane Smith")

    # Assign competencies
    program.assign_competency(1, "Hand Hygiene", True)
    program.assign_competency(1, "PPE", False)
    program.assign_competency(2, "Hand Hygiene", True)
    program.assign_competency(2, "Isolation Precautions", True)

    # Print staff competencies
    program.print_staff_competencies()

    # Update competency
    program.update_competency(1, "PPE", True)

    # Print updated staff competencies
    print("Updated Competencies:")
    program.print_staff_competencies()


if __name__ == "__main__":
    main()
```
