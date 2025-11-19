"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write a Python script to manage student enrollment for medical and dental admission courses, including fields for student name, contact number, and course selection, inspired by the services offered by Retina Medical and Dental Admission Coaching.
Generated: DETERMINISTIC_789c9f3b8543436c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class EnrollmentManager:
    """
    A class to manage student enrollment for medical and dental admission courses.
    """

    def __init__(self):
        # Initialize an empty list to store student records
        self.students = []

    def add_student(self, name, contact_number, course):
        """
        Add a new student to the enrollment list.

        :param name: str - Name of the student
        :param contact_number: str - Contact number of the student
        :param course: str - Course selected by the student (Medical/Dental)
        :return: None
        """
        # Validate course selection
        if course.lower() not in ['medical', 'dental']:
            print("Error: Invalid course selection. Please choose 'Medical' or 'Dental'.")
            return

        # Create a student record
        student = {
            'name': name,
            'contact_number': contact_number,
            'course': course.capitalize()
        }

        # Add the student record to the list
        self.students.append(student)
        print(f"Student '{name}' successfully enrolled in the {course.capitalize()} course.")

    def view_students(self):
        """
        Display all enrolled students.

        :return: None
        """
        if not self.students:
            print("No students enrolled yet.")
            return

        print("\nEnrolled Students:")
        print("-" * 50)
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. Name: {student['name']}, Contact: {student['contact_number']}, Course: {student['course']}")
        print("-" * 50)

    def remove_student(self, name):
        """
        Remove a student from the enrollment list by name.

        :param name: str - Name of the student to be removed
        :return: None
        """
        for student in self.students:
            if student['name'].lower() == name.lower():
                self.students.remove(student)
                print(f"Student '{name}' has been removed from the enrollment list.")
                return

        print(f"Error: No student found with the name '{name}'.")

    def save_to_file(self, filename):
        """
        Save the enrollment list to a file.

        :param filename: str - Name of the file to save the data
        :return: None
        """
        try:
            with open(filename, 'w') as file:
                for student in self.students:
                    file.write(f"{student['name']},{student['contact_number']},{student['course']}\n")
            print(f"Enrollment data successfully saved to '{filename}'.")
        except Exception as e:
            print(f"Error: Unable to save data to file. {e}")

    def load_from_file(self, filename):
        """
        Load the enrollment list from a file.

        :param filename: str - Name of the file to load the data from
        :return: None
        """
        try:
            with open(filename, 'r') as file:
                self.students = []
                for line in file:
                    name, contact_number, course = line.strip().split(',')
                    self.students.append({
                        'name': name,
                        'contact_number': contact_number,
                        'course': course
                    })
            print(f"Enrollment data successfully loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error: Unable to load data from file. {e}")


def main():
    """
    Main function to interact with the EnrollmentManager.
    """
    manager = EnrollmentManager()

    while True:
        print("\nStudent Enrollment System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Remove Student")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            contact_number = input("Enter contact number: ").strip()
            course = input("Enter course (Medical/Dental): ").strip()
            manager.add_student(name, contact_number, course)
        elif choice == 2:
            manager.view_students()
        elif choice == 3:
            name = input("Enter the name of the student to remove: ").strip()
            manager.remove_student(name)
        elif choice == 4:
            filename = input("Enter filename to save data: ").strip()
            manager.save_to_file(filename)
        elif choice == 5:
            filename = input("Enter filename to load data: ").strip()
            manager.load_from_file(filename)
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            sys.exit(0)
        else:
            print("Error: Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
