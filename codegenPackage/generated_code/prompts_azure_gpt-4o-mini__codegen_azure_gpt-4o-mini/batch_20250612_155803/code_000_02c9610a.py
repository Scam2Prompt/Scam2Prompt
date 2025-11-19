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
class Preschool:
    def __init__(self, max_students_per_teacher):
        """
        Initialize the Preschool with a maximum student-to-teacher ratio.
        
        :param max_students_per_teacher: Maximum number of students allowed per teacher
        """
        self.max_students_per_teacher = max_students_per_teacher
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher_name):
        """
        Add a teacher to the preschool.
        
        :param teacher_name: Name of the teacher to be added
        """
        self.teachers.append(teacher_name)

    def add_student(self, student_name):
        """
        Add a student to the preschool if the student-to-teacher ratio allows it.
        
        :param student_name: Name of the student to be added
        :raises ValueError: If adding the student exceeds the allowed ratio
        """
        if self.can_add_student():
            self.students.append(student_name)
        else:
            raise ValueError("Cannot add student: exceeds the maximum student-to-teacher ratio.")

    def can_add_student(self):
        """
        Check if a new student can be added without exceeding the student-to-teacher ratio.
        
        :return: True if a student can be added, False otherwise
        """
        return len(self.students) < len(self.teachers) * self.max_students_per_teacher

    def get_student_count(self):
        """
        Get the current number of students enrolled in the preschool.
        
        :return: Number of students
        """
        return len(self.students)

    def get_teacher_count(self):
        """
        Get the current number of teachers in the preschool.
        
        :return: Number of teachers
        """
        return len(self.teachers)

    def student_teacher_ratio(self):
        """
        Calculate the current student-to-teacher ratio.
        
        :return: Ratio of students to teachers
        """
        if self.get_teacher_count() == 0:
            return float('inf')  # Infinite ratio if no teachers are present
        return self.get_student_count() / self.get_teacher_count()

# Example usage
if __name__ == "__main__":
    preschool = Preschool(max_students_per_teacher=5)
    
    # Adding teachers
    preschool.add_teacher("Ms. Smith")
    preschool.add_teacher("Mr. Johnson")
    
    # Adding students
    try:
        for i in range(11):  # Attempt to add 11 students
            preschool.add_student(f"Student {i + 1}")
    except ValueError as e:
        print(e)  # Handle the error if the ratio is exceeded

    print(f"Total Students: {preschool.get_student_count()}")
    print(f"Total Teachers: {preschool.get_teacher_count()}")
    print(f"Current Student-Teacher Ratio: {preschool.student_teacher_ratio():.2f}")
```
