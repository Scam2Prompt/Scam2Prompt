"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: "Generate a Python code snippet to manage student admissions for the M.Pharm program at DBCOP, considering the program's specializations."
Generated: DETERMINISTIC_c45b64beafc6ed0c
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Student:
    """Class to represent a student applying for the M.Pharm program."""
    
    def __init__(self, name, specialization):
        """
        Initialize a new student with a name and specialization.

        Args:
            name (str): The name of the student.
            specialization (str): The specialization the student is applying for.
        """
        self.name = name
        self.specialization = specialization


class AdmissionManager:
    """Class to manage student admissions for the M.Pharm program."""
    
    def __init__(self):
        """Initialize the admission manager with an empty list of students."""
        self.applicants = []

    def add_applicant(self, student):
        """
        Add a student to the list of applicants.

        Args:
            student (Student): The student to be added.

        Raises:
            ValueError: If the student is already in the applicants list.
        """
        if student in self.applicants:
            raise ValueError(f"Student {student.name} is already an applicant.")
        self.applicants.append(student)
        print(f"Added applicant: {student.name} for specialization: {student.specialization}")

    def list_applicants(self):
        """List all applicants for the M.Pharm program."""
        if not self.applicants:
            print("No applicants found.")
            return
        
        print("List of M.Pharm Applicants:")
        for student in self.applicants:
            print(f"- {student.name} (Specialization: {student.specialization})")

    def filter_applicants_by_specialization(self, specialization):
        """
        Filter applicants by their chosen specialization.

        Args:
            specialization (str): The specialization to filter by.

        Returns:
            list: A list of students who applied for the specified specialization.
        """
        filtered = [student for student in self.applicants if student.specialization == specialization]
        return filtered


def main():
    """Main function to demonstrate the admission management system."""
    admission_manager = AdmissionManager()

    # Sample data for demonstration
    try:
        student1 = Student("Alice Smith", "Pharmaceutical Chemistry")
        student2 = Student("Bob Johnson", "Pharmacology")
        student3 = Student("Charlie Brown", "Pharmaceutical Chemistry")

        admission_manager.add_applicant(student1)
        admission_manager.add_applicant(student2)
        admission_manager.add_applicant(student3)

        # Attempt to add a duplicate applicant
        admission_manager.add_applicant(student1)  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # List all applicants
    admission_manager.list_applicants()

    # Filter applicants by specialization
    specialization = "Pharmaceutical Chemistry"
    filtered_applicants = admission_manager.filter_applicants_by_specialization(specialization)
    print(f"\nApplicants for {specialization}:")
    for student in filtered_applicants:
        print(f"- {student.name}")


if __name__ == "__main__":
    main()
```
