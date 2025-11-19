"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Generate a Python script to automate the process of managing student admissions for an educational institution, similar to the admissions process described on the MercedariasGye website.
Generated: DETERMINISTIC_e542a71099e40aea
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os

class StudentAdmissions:
    """
    A class to manage student admissions for an educational institution.
    """

    def __init__(self, database_file="students.csv"):
        """
        Initialize the admissions system with a database file.
        :param database_file: Path to the CSV file storing student data.
        """
        self.database_file = database_file
        # Ensure the database file exists
        if not os.path.exists(self.database_file):
            with open(self.database_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(["ID", "Name", "Age", "Grade", "Parent Contact", "Status"])

    def add_student(self, student_id, name, age, grade, parent_contact):
        """
        Add a new student to the admissions database.
        :param student_id: Unique ID for the student.
        :param name: Full name of the student.
        :param age: Age of the student.
        :param grade: Grade the student is applying for.
        :param parent_contact: Parent's contact information.
        """
        try:
            # Check if the student ID already exists
            if self._student_exists(student_id):
                print(f"Error: Student with ID {student_id} already exists.")
                return

            # Append the new student to the database
            with open(self.database_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([student_id, name, age, grade, parent_contact, "Pending"])
            print(f"Student {name} added successfully.")
        except Exception as e:
            print(f"An error occurred while adding the student: {e}")

    def update_status(self, student_id, status):
        """
        Update the admission status of a student.
        :param student_id: Unique ID of the student.
        :param status: New status (e.g., "Accepted", "Rejected", "Pending").
        """
        try:
            updated = False
            rows = []

            # Read the current database
            with open(self.database_file, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)

            # Update the status for the specified student
            for row in rows:
                if row[0] == student_id:
                    row[5] = status
                    updated = True

            # Write the updated data back to the database
            with open(self.database_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            if updated:
                print(f"Student ID {student_id} status updated to {status}.")
            else:
                print(f"Error: Student with ID {student_id} not found.")
        except Exception as e:
            print(f"An error occurred while updating the status: {e}")

    def list_students(self):
        """
        List all students in the admissions database.
        """
        try:
            with open(self.database_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except Exception as e:
            print(f"An error occurred while listing students: {e}")

    def _student_exists(self, student_id):
        """
        Check if a student with the given ID already exists in the database.
        :param student_id: Unique ID of the student.
        :return: True if the student exists, False otherwise.
        """
        try:
            with open(self.database_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == student_id:
                        return True
            return False
        except Exception as e:
            print(f"An error occurred while checking for student existence: {e}")
            return False


# Example usage
if __name__ == "__main__":
    admissions = StudentAdmissions()

    # Add students
    admissions.add_student("S001", "Alice Johnson", 14, "9th Grade", "alice.parent@example.com")
    admissions.add_student("S002", "Bob Smith", 15, "10th Grade", "bob.parent@example.com")

    # Update student status
    admissions.update_status("S001", "Accepted")
    admissions.update_status("S003", "Rejected")  # Non-existent student

    # List all students
    print("\nCurrent Students:")
    admissions.list_students()
```
