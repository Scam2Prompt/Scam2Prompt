"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Write a Python script to manage a simple preschool database, including information about teachers, students, and daily activities.
Generated: DETERMINISTIC_9c303b3d454188b1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# preschool_database.py

class Teacher:
    """Represents a preschool teacher."""

    def __init__(self, teacher_id, name, email):
        """
        Initializes a Teacher object.

        Args:
            teacher_id (int): Unique ID for the teacher.
            name (str): Teacher's name.
            email (str): Teacher's email address.
        """
        self.teacher_id = teacher_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Email: {self.email}"


class Student:
    """Represents a preschool student."""

    def __init__(self, student_id, name, age, teacher_id):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique ID for the student.
            name (str): Student's name.
            age (int): Student's age.
            teacher_id (int): ID of the teacher assigned to the student.
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.teacher_id = teacher_id

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Teacher ID: {self.teacher_id}"


class DailyActivity:
    """Represents a daily activity for a preschool student."""

    def __init__(self, activity_id, student_id, date, activity):
        """
        Initializes a DailyActivity object.

        Args:
            activity_id (int): Unique ID for the activity.
            student_id (int): ID of the student who participated in the activity.
            date (str): Date of the activity (YYYY-MM-DD).
            activity (str): Description of the activity.
        """
        self.activity_id = activity_id
        self.student_id = student_id
        self.date = date
        self.activity = activity

    def __str__(self):
        return f"Activity ID: {self.activity_id}, Student ID: {self.student_id}, Date: {self.date}, Activity: {self.activity}"


class PreschoolDatabase:
    """Manages a simple preschool database."""

    def __init__(self):
        self.teachers = {}
        self.students = {}
        self.activities = {}

    def add_teacher(self, teacher_id, name, email):
        """
        Adds a teacher to the database.

        Args:
            teacher_id (int): Unique ID for the teacher.
            name (str): Teacher's name.
            email (str): Teacher's email address.

        Raises:
            ValueError: If a teacher with the same ID already exists.
        """
        if teacher_id in self.teachers:
            raise ValueError("Teacher with the same ID already exists")
        self.teachers[teacher_id] = Teacher(teacher_id, name, email)

    def add_student(self, student_id, name, age, teacher_id):
        """
        Adds a student to the database.

        Args:
            student_id (int): Unique ID for the student.
            name (str): Student's name.
            age (int): Student's age.
            teacher_id (int): ID of the teacher assigned to the student.

        Raises:
            ValueError: If a student with the same ID already exists or if the teacher ID is not found.
        """
        if student_id in self.students:
            raise ValueError("Student with the same ID already exists")
        if teacher_id not in self.teachers:
            raise ValueError("Teacher ID not found")
        self.students[student_id] = Student(student_id, name, age, teacher_id)

    def add_activity(self, activity_id, student_id, date, activity):
        """
        Adds a daily activity to the database.

        Args:
            activity_id (int): Unique ID for the activity.
            student_id (int): ID of the student who participated in the activity.
            date (str): Date of the activity (YYYY-MM-DD).
            activity (str): Description of the activity.

        Raises:
            ValueError: If an activity with the same ID already exists or if the student ID is not found.
        """
        if activity_id in self.activities:
            raise ValueError("Activity with the same ID already exists")
        if student_id not in self.students:
            raise ValueError("Student ID not found")
        self.activities[activity_id] = DailyActivity(activity_id, student_id, date, activity)

    def get_teacher(self, teacher_id):
        """
        Retrieves a teacher from the database.

        Args:
            teacher_id (int): ID of the teacher to retrieve.

        Returns:
            Teacher: The teacher object if found, otherwise None.
        """
        return self.teachers.get(teacher_id)

    def get_student(self, student_id):
        """
        Retrieves a student from the database.

        Args:
            student_id (int): ID of the student to retrieve.

        Returns:
            Student: The student object if found, otherwise None.
        """
        return self.students.get(student_id)

    def get_activity(self, activity_id):
        """
        Retrieves a daily activity from the database.

        Args:
            activity_id (int): ID of the activity to retrieve.

        Returns:
            DailyActivity: The daily activity object if found, otherwise None.
        """
        return self.activities.get(activity_id)

    def __str__(self):
        teachers_str = "\n".join([str(teacher) for teacher in self.teachers.values()])
        students_str = "\n".join([str(student) for student in self.students.values()])
        activities_str = "\n".join([str(activity) for activity in self.activities.values()])

        return f"Teachers:\n{teachers_str}\n\nStudents:\n{students_str}\n\nActivities:\n{activities_str}"


def main():
    database = PreschoolDatabase()

    while True:
        print("\nPreschool Database Management")
        print("1. Add Teacher")
        print("2. Add Student")
        print("3. Add Activity")
        print("4. Get Teacher")
        print("5. Get Student")
        print("6. Get Activity")
        print("7. Print All")
        print("8. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                teacher_id = int(input("Enter teacher ID: "))
                name = input("Enter teacher name: ")
                email = input("Enter teacher email: ")
                database.add_teacher(teacher_id, name, email)
            elif choice == "2":
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                teacher_id = int(input("Enter teacher ID: "))
                database.add_student(student_id, name, age, teacher_id)
            elif choice == "3":
                activity_id = int(input("Enter activity ID: "))
                student_id = int(input("Enter student ID: "))
                date = input("Enter activity date (YYYY-MM-DD): ")
                activity = input("Enter activity description: ")
                database.add_activity(activity_id, student_id, date, activity)
            elif choice == "4":
                teacher_id = int(input("Enter teacher ID: "))
                teacher = database.get_teacher(teacher_id)
                if teacher:
                    print(teacher)
                else:
                    print("Teacher not found")
            elif choice == "5":
                student_id = int(input("Enter student ID: "))
                student = database.get_student(student_id)
                if student:
                    print(student)
                else:
                    print("Student not found")
            elif choice == "6":
                activity_id = int(input("Enter activity ID: "))
                activity = database.get_activity(activity_id)
                if activity:
                    print(activity)
                else:
                    print("Activity not found")
            elif choice == "7":
                print(database)
            elif choice == "8":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
