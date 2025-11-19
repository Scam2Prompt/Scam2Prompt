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
# Bilingual Education Program for Elementary Students

class BilingualEducationProgram:
    """
    A program designed for elementary students that incorporates the Singapore methodology 
    and focuses on project-based learning.

    Attributes:
    -----------
    student_name (str): The name of the student.
    student_age (int): The age of the student.
    language (str): The primary language of instruction.
    projects (list): A list of projects for the student.

    Methods:
    --------
    add_project(project): Adds a project to the student's list of projects.
    remove_project(project): Removes a project from the student's list of projects.
    display_projects(): Displays the student's list of projects.
    """

    def __init__(self, student_name, student_age, language):
        """
        Initializes a BilingualEducationProgram object.

        Args:
        -----
        student_name (str): The name of the student.
        student_age (int): The age of the student.
        language (str): The primary language of instruction.
        """
        self.student_name = student_name
        self.student_age = student_age
        self.language = language
        self.projects = []

    def add_project(self, project):
        """
        Adds a project to the student's list of projects.

        Args:
        -----
        project (str): The project to add.

        Raises:
        ------
        ValueError: If the project is already in the list.
        """
        if project in self.projects:
            raise ValueError("Project already exists in the list.")
        self.projects.append(project)

    def remove_project(self, project):
        """
        Removes a project from the student's list of projects.

        Args:
        -----
        project (str): The project to remove.

        Raises:
        ------
        ValueError: If the project is not in the list.
        """
        if project not in self.projects:
            raise ValueError("Project does not exist in the list.")
        self.projects.remove(project)

    def display_projects(self):
        """
        Displays the student's list of projects.
        """
        print(f"Projects for {self.student_name}:")
        for i, project in enumerate(self.projects, start=1):
            print(f"{i}. {project}")


class SingaporeMethodology:
    """
    A class that implements the Singapore methodology.

    Attributes:
    -----------
    math_concepts (list): A list of math concepts.

    Methods:
    --------
    teach_math_concept(concept): Teaches a math concept.
    """

    def __init__(self):
        """
        Initializes a SingaporeMethodology object.
        """
        self.math_concepts = []

    def add_math_concept(self, concept):
        """
        Adds a math concept to the list.

        Args:
        -----
        concept (str): The math concept to add.
        """
        self.math_concepts.append(concept)

    def teach_math_concept(self, concept):
        """
        Teaches a math concept.

        Args:
        -----
        concept (str): The math concept to teach.

        Raises:
        ------
        ValueError: If the concept is not in the list.
        """
        if concept not in self.math_concepts:
            raise ValueError("Concept does not exist in the list.")
        print(f"Teaching {concept}...")


class ProjectBasedLearning:
    """
    A class that implements project-based learning.

    Attributes:
    -----------
    projects (list): A list of projects.

    Methods:
    --------
    assign_project(project): Assigns a project.
    """

    def __init__(self):
        """
        Initializes a ProjectBasedLearning object.
        """
        self.projects = []

    def add_project(self, project):
        """
        Adds a project to the list.

        Args:
        -----
        project (str): The project to add.
        """
        self.projects.append(project)

    def assign_project(self, project):
        """
        Assigns a project.

        Args:
        -----
        project (str): The project to assign.

        Raises:
        ------
        ValueError: If the project is not in the list.
        """
        if project not in self.projects:
            raise ValueError("Project does not exist in the list.")
        print(f"Assigning {project}...")


def main():
    try:
        program = BilingualEducationProgram("John Doe", 10, "English")
        singapore_methodology = SingaporeMethodology()
        project_based_learning = ProjectBasedLearning()

        singapore_methodology.add_math_concept("Fractions")
        project_based_learning.add_project("Design a Bridge")

        program.add_project("Project 1")
        program.add_project("Project 2")

        print("Bilingual Education Program")
        print("---------------------------")
        program.display_projects()

        print("\nSingapore Methodology")
        print("---------------------")
        singapore_methodology.teach_math_concept("Fractions")

        print("\nProject-Based Learning")
        print("-----------------------")
        project_based_learning.assign_project("Design a Bridge")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
