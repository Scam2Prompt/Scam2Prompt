"""
Generated Code Metadata:
========================
Original URL: https://siprosa.org
Prompt: How can I implement a low student-to-teacher ratio in a preschool setting to enhance early childhood education, similar to the Siprosa School model?
Generated: DETERMINISTIC_02c9610a0a0c6b81
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_teacher_ratio.py

class Preschool:
    def __init__(self, name, max_students_per_class, max_teachers_per_class):
        """
        Initialize a Preschool object.

        Args:
            name (str): The name of the preschool.
            max_students_per_class (int): The maximum number of students per class.
            max_teachers_per_class (int): The maximum number of teachers per class.
        """
        self.name = name
        self.max_students_per_class = max_students_per_class
        self.max_teachers_per_class = max_teachers_per_class
        self.classes = []

    def add_class(self, students, teachers):
        """
        Add a class to the preschool.

        Args:
            students (list): A list of student objects.
            teachers (list): A list of teacher objects.

        Raises:
            ValueError: If the number of students or teachers exceeds the maximum allowed.
        """
        if len(students) > self.max_students_per_class:
            raise ValueError("Too many students in class")
        if len(teachers) > self.max_teachers_per_class:
            raise ValueError("Too many teachers in class")

        self.classes.append({"students": students, "teachers": teachers})

    def get_student_to_teacher_ratio(self):
        """
        Calculate the average student-to-teacher ratio across all classes.

        Returns:
            float: The average student-to-teacher ratio.
        """
        total_students = 0
        total_teachers = 0

        for class_info in self.classes:
            total_students += len(class_info["students"])
            total_teachers += len(class_info["teachers"])

        if total_teachers == 0:
            return 0

        return total_students / total_teachers


class Student:
    def __init__(self, name, age):
        """
        Initialize a Student object.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
        """
        self.name = name
        self.age = age


class Teacher:
    def __init__(self, name, experience):
        """
        Initialize a Teacher object.

        Args:
            name (str): The name of the teacher.
            experience (int): The years of experience of the teacher.
        """
        self.name = name
        self.experience = experience


def main():
    preschool = Preschool("Siprosa Preschool", 10, 2)

    students = [Student(f"Student {i}", 3) for i in range(1, 11)]
    teachers = [Teacher("Teacher 1", 5), Teacher("Teacher 2", 3)]

    preschool.add_class(students, teachers)

    ratio = preschool.get_student_to_teacher_ratio()
    print(f"Student-to-teacher ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()
```
