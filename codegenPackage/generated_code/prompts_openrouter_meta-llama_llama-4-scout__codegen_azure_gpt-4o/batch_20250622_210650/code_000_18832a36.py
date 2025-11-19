"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Design a bilingual education program for elementary students that incorporates the Singapore methodology and focuses on project-based learning, similar to Heart of Jesus College."
Generated: DETERMINISTIC_18832a36cfe496d5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bilingual Education Program for Elementary Students
This program incorporates the Singapore methodology and focuses on project-based learning.
The system allows teachers to create bilingual projects, assign them to students, and track progress.
"""

import json

class BilingualEducationProgram:
    def __init__(self):
        """
        Initialize the program with empty lists for students, projects, and teachers.
        """
        self.students = []
        self.projects = []
        self.teachers = []

    def add_student(self, name, age, language_preference):
        """
        Add a new student to the program.
        :param name: str - Name of the student
        :param age: int - Age of the student
        :param language_preference: str - Preferred language (e.g., "English", "Mandarin")
        """
        try:
            student = {
                "id": len(self.students) + 1,
                "name": name,
                "age": age,
                "language_preference": language_preference,
                "assigned_projects": []
            }
            self.students.append(student)
            print(f"Student {name} added successfully.")
        except Exception as e:
            print(f"Error adding student: {e}")

    def add_teacher(self, name, specialization):
        """
        Add a new teacher to the program.
        :param name: str - Name of the teacher
        :param specialization: str - Specialization (e.g., "Math", "Science", "Language")
        """
        try:
            teacher = {
                "id": len(self.teachers) + 1,
                "name": name,
                "specialization": specialization
            }
            self.teachers.append(teacher)
            print(f"Teacher {name} added successfully.")
        except Exception as e:
            print(f"Error adding teacher: {e}")

    def create_project(self, title, description, language_focus, teacher_id):
        """
        Create a new project for students.
        :param title: str - Title of the project
        :param description: str - Description of the project
        :param language_focus: str - Language focus (e.g., "English", "Mandarin")
        :param teacher_id: int - ID of the teacher responsible for the project
        """
        try:
            # Validate teacher ID
            teacher = next((t for t in self.teachers if t["id"] == teacher_id), None)
            if not teacher:
                raise ValueError("Invalid teacher ID.")

            project = {
                "id": len(self.projects) + 1,
                "title": title,
                "description": description,
                "language_focus": language_focus,
                "teacher_id": teacher_id,
                "assigned_students": []
            }
            self.projects.append(project)
            print(f"Project '{title}' created successfully.")
        except Exception as e:
            print(f"Error creating project: {e}")

    def assign_project_to_student(self, project_id, student_id):
        """
        Assign a project to a student.
        :param project_id: int - ID of the project
        :param student_id: int - ID of the student
        """
        try:
            # Validate project ID
            project = next((p for p in self.projects if p["id"] == project_id), None)
            if not project:
                raise ValueError("Invalid project ID.")

            # Validate student ID
            student = next((s for s in self.students if s["id"] == student_id), None)
            if not student:
                raise ValueError("Invalid student ID.")

            # Assign project to student
            project["assigned_students"].append(student_id)
            student["assigned_projects"].append(project_id)
            print(f"Project '{project['title']}' assigned to student '{student['name']}'.")
        except Exception as e:
            print(f"Error assigning project: {e}")

    def view_students(self):
        """
        View all students in the program.
        """
        print("Students:")
        for student in self.students:
            print(json.dumps(student, indent=4))

    def view_projects(self):
        """
        View all projects in the program.
        """
        print("Projects:")
        for project in self.projects:
            print(json.dumps(project, indent=4))

    def view_teachers(self):
        """
        View all teachers in the program.
        """
        print("Teachers:")
        for teacher in self.teachers:
            print(json.dumps(teacher, indent=4))


# Example usage
if __name__ == "__main__":
    program = BilingualEducationProgram()

    # Add teachers
    program.add_teacher("Ms. Tan", "Language")
    program.add_teacher("Mr. Lee", "Math")

    # Add students
    program.add_student("Alice", 10, "English")
    program.add_student("Bob", 9, "Mandarin")

    # Create projects
    program.create_project("Math in Nature", "Explore math concepts in natural settings.", "English", 2)
    program.create_project("Storytelling", "Create bilingual stories.", "Mandarin", 1)

    # Assign projects to students
    program.assign_project_to_student(1, 1)
    program.assign_project_to_student(2, 2)

    # View data
    program.view_students()
    program.view_projects()
    program.view_teachers()
```
