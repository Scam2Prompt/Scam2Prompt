"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Generate a code snippet that demonstrates how to implement a multi-disciplinary approach in a university setting, as discussed in the UEH special issue.
Generated: DETERMINISTIC_d345ea96527c0746
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UniversityDepartment:
    """
    A class to represent a university department.
    """

    def __init__(self, name):
        """
        Initializes the department with a name and an empty list of faculty members.
        
        :param name: str - The name of the department
        """
        self.name = name
        self.faculty_members = []

    def add_faculty_member(self, faculty_member):
        """
        Adds a faculty member to the department.
        
        :param faculty_member: FacultyMember - The faculty member to add
        """
        if isinstance(faculty_member, FacultyMember):
            self.faculty_members.append(faculty_member)
        else:
            raise ValueError("Invalid faculty member. Must be an instance of FacultyMember.")

    def get_faculty_members(self):
        """
        Returns a list of faculty members in the department.
        
        :return: list - List of faculty members
        """
        return self.faculty_members


class FacultyMember:
    """
    A class to represent a faculty member.
    """

    def __init__(self, name, expertise):
        """
        Initializes the faculty member with a name and area of expertise.
        
        :param name: str - The name of the faculty member
        :param expertise: str - The area of expertise
        """
        self.name = name
        self.expertise = expertise

    def __repr__(self):
        """
        Returns a string representation of the faculty member.
        
        :return: str - String representation
        """
        return f"{self.name} (Expertise: {self.expertise})"


class MultiDisciplinaryProject:
    """
    A class to represent a multi-disciplinary project.
    """

    def __init__(self, title):
        """
        Initializes the project with a title and an empty list of contributors.
        
        :param title: str - The title of the project
        """
        self.title = title
        self.contributors = []

    def add_contributor(self, faculty_member):
        """
        Adds a contributor to the project.
        
        :param faculty_member: FacultyMember - The faculty member contributing to the project
        """
        if isinstance(faculty_member, FacultyMember):
            self.contributors.append(faculty_member)
        else:
            raise ValueError("Invalid contributor. Must be an instance of FacultyMember.")

    def get_contributors(self):
        """
        Returns a list of contributors to the project.
        
        :return: list - List of contributors
        """
        return self.contributors


# Example usage
if __name__ == "__main__":
    try:
        # Create departments
        cs_department = UniversityDepartment("Computer Science")
        bio_department = UniversityDepartment("Biology")

        # Create faculty members
        prof_smith = FacultyMember("Dr. Smith", "Artificial Intelligence")
        prof_jones = FacultyMember("Dr. Jones", "Genetics")

        # Add faculty members to departments
        cs_department.add_faculty_member(prof_smith)
        bio_department.add_faculty_member(prof_jones)

        # Create a multi-disciplinary project
        project = MultiDisciplinaryProject("AI in Genomics")

        # Add contributors to the project
        project.add_contributor(prof_smith)
        project.add_contributor(prof_jones)

        # Display project contributors
        print(f"Project: {project.title}")
        print("Contributors:")
        for contributor in project.get_contributors():
            print(contributor)

    except Exception as e:
        print(f"An error occurred: {e}")
```
