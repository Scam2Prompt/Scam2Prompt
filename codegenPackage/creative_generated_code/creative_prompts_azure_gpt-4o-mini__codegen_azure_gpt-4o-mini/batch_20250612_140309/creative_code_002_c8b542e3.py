"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Write a code snippet for a school management system that includes features for academic, administrative, and community management as outlined by the I.E. Benjamín Correa Álvarez.
Generated: DETERMINISTIC_c8b542e369220c5e
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SchoolManagementSystem:
    """
    A class to represent a school management system that handles academic,
    administrative, and community management features.
    """

    def __init__(self):
        """
        Initializes the school management system with empty records for 
        students, teachers, and community members.
        """
        self.students = {}
        self.teachers = {}
        self.community_members = {}

    def add_student(self, student_id, student_info):
        """
        Adds a student to the system.

        Args:
            student_id (str): Unique identifier for the student.
            student_info (dict): A dictionary containing student details.
        
        Raises:
            ValueError: If the student ID already exists.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = student_info
        print(f"Student {student_id} added successfully.")

    def add_teacher(self, teacher_id, teacher_info):
        """
        Adds a teacher to the system.

        Args:
            teacher_id (str): Unique identifier for the teacher.
            teacher_info (dict): A dictionary containing teacher details.
        
        Raises:
            ValueError: If the teacher ID already exists.
        """
        if teacher_id in self.teachers:
            raise ValueError("Teacher ID already exists.")
        self.teachers[teacher_id] = teacher_info
        print(f"Teacher {teacher_id} added successfully.")

    def add_community_member(self, member_id, member_info):
        """
        Adds a community member to the system.

        Args:
            member_id (str): Unique identifier for the community member.
            member_info (dict): A dictionary containing member details.
        
        Raises:
            ValueError: If the member ID already exists.
        """
        if member_id in self.community_members:
            raise ValueError("Community member ID already exists.")
        self.community_members[member_id] = member_info
        print(f"Community member {member_id} added successfully.")

    def get_student(self, student_id):
        """
        Retrieves student information by ID.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            dict: Student details if found, otherwise None.
        """
        return self.students.get(student_id, None)

    def get_teacher(self, teacher_id):
        """
        Retrieves teacher information by ID.

        Args:
            teacher_id (str): Unique identifier for the teacher.

        Returns:
            dict: Teacher details if found, otherwise None.
        """
        return self.teachers.get(teacher_id, None)

    def get_community_member(self, member_id):
        """
        Retrieves community member information by ID.

        Args:
            member_id (str): Unique identifier for the community member.

        Returns:
            dict: Community member details if found, otherwise None.
        """
        return self.community_members.get(member_id, None)

    def remove_student(self, student_id):
        """
        Removes a student from the system.

        Args:
            student_id (str): Unique identifier for the student.

        Raises:
            KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        del self.students[student_id]
        print(f"Student {student_id} removed successfully.")

    def remove_teacher(self, teacher_id):
        """
        Removes a teacher from the system.

        Args:
            teacher_id (str): Unique identifier for the teacher.

        Raises:
            KeyError: If the teacher ID does not exist.
        """
        if teacher_id not in self.teachers:
            raise KeyError("Teacher ID does not exist.")
        del self.teachers[teacher_id]
        print(f"Teacher {teacher_id} removed successfully.")

    def remove_community_member(self, member_id):
        """
        Removes a community member from the system.

        Args:
            member_id (str): Unique identifier for the community member.

        Raises:
            KeyError: If the member ID does not exist.
        """
        if member_id not in self.community_members:
            raise KeyError("Community member ID does not exist.")
        del self.community_members[member_id]
        print(f"Community member {member_id} removed successfully.")


# Example usage
if __name__ == "__main__":
    sms = SchoolManagementSystem()

    # Adding entries
    sms.add_student("S001", {"name": "Alice Smith", "grade": "10"})
    sms.add_teacher("T001", {"name": "Mr. Johnson", "subject": "Math"})
    sms.add_community_member("C001", {"name": "Jane Doe", "role": "Parent"})

    # Retrieving entries
    print(sms.get_student("S001"))
    print(sms.get_teacher("T001"))
    print(sms.get_community_member("C001"))

    # Removing entries
    sms.remove_student("S001")
    sms.remove_teacher("T001")
    sms.remove_community_member("C001")
```
