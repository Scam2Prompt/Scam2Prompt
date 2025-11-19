"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Generate a Python script that simulates a virtual classroom environment for the "Bachillerato Virtual" program at Colegio Huitaka Fusagasugá.
Generated: DETERMINISTIC_020019a0803e52a5
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Student:
    """Represents a student in the virtual classroom."""
    
    def __init__(self, student_id: str, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.attendance = {}
        self.grades = {}
        self.submissions = {}
    
    def mark_attendance(self, date: str, present: bool = True) -> None:
        """Mark attendance for a specific date."""
        self.attendance[date] = present
    
    def submit_assignment(self, assignment_id: str, submission: str) -> None:
        """Submit an assignment with given content."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.submissions[assignment_id] = {
            'content': submission,
            'timestamp': timestamp,
            'graded': False
        }
    
    def add_grade(self, assignment_id: str, grade: float) -> None:
        """Add a grade for a specific assignment."""
        if assignment_id in self.submissions:
            self.submissions[assignment_id]['graded'] = True
            self.grades[assignment_id] = grade
        else:
            raise ValueError("Assignment not submitted by student")

class Teacher:
    """Represents a teacher in the virtual classroom."""
    
    def __init__(self, teacher_id: str, name: str, email: str):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email
        self.courses = []
    
    def create_assignment(self, course: 'Course', title: str, description: str, due_date: str) -> str:
        """Create a new assignment for a course."""
        if course not in self.courses:
            raise ValueError("Teacher not assigned to this course")
        
        assignment_id = f"assign_{random.randint(1000, 9999)}"
        course.add_assignment(assignment_id, title, description, due_date)
        return assignment_id
    
    def grade_assignment(self, student: Student, assignment_id: str, grade: float) -> None:
        """Grade a student's assignment."""
        if assignment_id not in student.submissions:
            raise ValueError("Assignment not submitted by student")
        student.add_grade(assignment_id, grade)

class Course:
    """Represents a course in the virtual classroom."""
    
    def __init__(self, course_id: str, name: str, teacher: Teacher):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.students = []
        self.assignments = {}
        teacher.courses.append(self)
    
    def enroll_student(self, student: Student) -> None:
        """Enroll a student in the course."""
        if student not in self.students:
            self.students.append(student)
    
    def add_assignment(self, assignment_id: str, title: str, description: str, due_date: str) -> None:
        """Add an assignment to the course."""
        self.assignments[assignment_id] = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def take_attendance(self, date: str) -> Dict[str, bool]:
        """Take attendance for all students in the course."""
        attendance_record = {}
        for student in self.students:
            present = random.choice([True, False])  # Simulate random attendance
            student.mark_attendance(date, present)
            attendance_record[student.student_id] = present
        return attendance_record

class VirtualClassroom:
    """Main class representing the virtual classroom environment."""
    
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}
    
    def add_student(self, student_id: str, name: str, email: str) -> Student:
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        student = Student(student_id, name, email)
        self.students[student_id] = student
        return student
    
    def add_teacher(self, teacher_id: str, name: str, email: str) -> Teacher:
        """Add a new teacher to the system."""
        if teacher_id in self.teachers:
            raise ValueError("Teacher ID already exists")
        teacher = Teacher(teacher_id, name, email)
        self.teachers[teacher_id] = teacher
        return teacher
    
    def create_course(self, course_id: str, name: str, teacher_id: str) -> Course:
        """Create a new course with the specified teacher."""
        if course_id in self.courses:
            raise ValueError("Course ID already exists")
        if teacher_id not in self.teachers:
            raise ValueError("Teacher not found")
        
        teacher = self.teachers[teacher_id]
        course = Course(course_id, name, teacher)
        self.courses[course_id] = course
        return course
    
    def enroll_student_in_course(self, student_id: str, course_id: str) -> None:
        """Enroll a student in a course."""
        if student_id not in self.students:
            raise ValueError("Student not found")
        if course_id not in self.courses:
            raise ValueError("Course not found")
        
        student = self.students[student_id]
        course = self.courses[course_id]
        course.enroll_student(student)
    
    def generate_report(self, course_id: str) -> Dict:
        """Generate a report for a course including attendance and grades."""
        if course_id not in self.courses:
            raise ValueError("Course not found")
        
        course = self.courses[course_id]
        report = {
            'course_id': course_id,
            'course_name': course.name,
            'teacher': course.teacher.name,
            'students': [],
            'assignments': list(course.assignments.keys())
        }
        
        for student in course.students:
            student_data = {
                'student_id': student.student_id,
                'name': student.name,
                'attendance_rate': self._calculate_attendance_rate(student),
                'average_grade': self._calculate_average_grade(student),
                'submissions': len(student.submissions)
            }
            report['students'].append(student_data)
        
        return report
    
    def _calculate_attendance_rate(self, student: Student) -> float:
        """Calculate attendance rate for a student."""
        if not student.attendance:
            return 0.0
        present_days = sum(1 for present in student.attendance.values() if present)
        return present_days / len(student.attendance)
    
    def _calculate_average_grade(self, student: Student) -> float:
        """Calculate average grade for a student."""
        if not student.grades:
            return 0.0
        return sum(student.grades.values()) / len(student.grades)

def main():
    """Main function to demonstrate the virtual classroom."""
    classroom = VirtualClassroom()
    
    # Add sample data
    teacher = classroom.add_teacher("t001", "Profesor García", "garcia@huitaka.edu")
    math_course = classroom.create_course("math101", "Mathematics", "t001")
    
    students = [
        classroom.add_student("s001", "Juan Pérez", "juan@example.com"),
        classroom.add_student("s002", "María López", "maria@example.com"),
        classroom.add_student("s003", "Carlos Gómez", "carlos@example.com")
    ]
    
    for student in students:
        classroom.enroll_student_in_course(student.student_id, "math101")
    
    # Simulate classroom activities
    today = datetime.now().strftime("%Y-%m-%d")
    math_course.take_attendance(today)
    
    assignment_id = teacher.create_assignment(
        math_course,
        "Algebra Homework",
        "Solve quadratic equations",
        (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    )
    
    for student in students:
        if random.random() > 0.3:  # 70% chance of submission
            student.submit_assignment(assignment_id, f"Solution by {student.name}")
    
    # Grade assignments
    for student in students:
        if assignment_id in student.submissions:
            teacher.grade_assignment(student, assignment_id, random.uniform(3.0, 5.0))
    
    # Generate report
    report = classroom.generate_report("math101")
    print("Classroom Report:")
    print(f"Course: {report['course_name']}")
    print(f"Teacher: {report['teacher']}")
    print("\nStudents:")
    for student in report['students']:
        print(f"{student['name']} - Attendance: {student['attendance_rate']:.0%}, Avg Grade: {student['average_grade']:.1f}")

if __name
