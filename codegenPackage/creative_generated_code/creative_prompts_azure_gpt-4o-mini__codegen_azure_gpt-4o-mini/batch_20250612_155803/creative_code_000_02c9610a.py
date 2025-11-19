"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siprosa.org
Prompt: How can I implement a low student-to-teacher ratio in a preschool setting to enhance early childhood education, similar to the Siprosa School model?
Generated: DETERMINISTIC_02c9610a0a0c6b81
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Preschool:
    def __init__(self, max_students_per_teacher):
        """
        Initializes the Preschool with a maximum number of students per teacher.
        
        :param max_students_per_teacher: Maximum number of students that a single teacher can handle.
        """
        self.max_students_per_teacher = max_students_per_teacher
        self.teachers = []
        self.students = []
    
    def add_teacher(self, teacher_name):
        """
        Adds a teacher to the preschool.
        
        :param teacher_name: Name of the teacher to add.
        """
        self.teachers.append(teacher_name)
        print(f"Teacher {teacher_name} added.")
    
    def add_student(self, student_name):
        """
        Adds a student to the preschool, ensuring the student-to-teacher ratio is maintained.
        
        :param student_name: Name of the student to add.
        :raises ValueError: If the student-to-teacher ratio exceeds the allowed limit.
        """
        if self.get_current_student_count() >= self.max_students_per_teacher * self.get_current_teacher_count():
            raise ValueError("Cannot add student. Exceeds the allowed student-to-teacher ratio.")
        
        self.students.append(student_name)
        print(f"Student {student_name} added.")
    
    def get_current_teacher_count(self):
        """
        Returns the current number of teachers.
        
        :return: Number of teachers
        """
        return len(self.teachers)
    
    def get_current_student_count(self):
        """
        Returns the current number of students.
        
        :return: Number of students
        """
        return len(self.students)

    def get_student_teacher_ratio(self):
        """
        Calculates the current student-to-teacher ratio.
        
        :return: Ratio of students to teachers. Returns 0 if no teachers are present.
        """
        teacher_count = self.get_current_teacher_count()
        return self.get_current_student_count() / teacher_count if teacher_count > 0 else 0.0

    def display_info(self):
        """
        Displays the current number of teachers, students, and the student-to-teacher ratio.
        """
        ratio = self.get_student_teacher_ratio()
        print(f"Teachers: {self.get_current_teacher_count()}, Students: {self.get_current_student_count()}, Student-Teacher Ratio: {ratio:.2f}")

# Example usage
if __name__ == "__main__":
    preschool = Preschool(max_students_per_teacher=5)

    try:
        preschool.add_teacher("Ms. Smith")
        preschool.add_teacher("Mr. Johnson")

        preschool.add_student("Alice")
        preschool.add_student("Bob")
        preschool.add_student("Charlie")
        preschool.add_student("David")
        preschool.add_student("Eve")
        
        # Attempting to add a student exceeding the ratio
        preschool.add_student("Frank")  # This will raise an exception
    except ValueError as e:
        print(e)

    preschool.display_info()
```
