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
class BilingualEducationProgram:
    """
    A class to represent a bilingual education program for elementary students.
    This program incorporates the Singapore methodology and focuses on project-based learning.
    """

    def __init__(self, language1: str, language2: str):
        """
        Initializes the bilingual education program with two languages.

        Args:
            language1 (str): The first language of instruction.
            language2 (str): The second language of instruction.
        """
        self.language1 = language1
        self.language2 = language2
        self.projects = []

    def add_project(self, project_name: str, description: str):
        """
        Adds a project to the program.

        Args:
            project_name (str): The name of the project.
            description (str): A brief description of the project.

        Raises:
            ValueError: If the project name or description is empty.
        """
        if not project_name or not description:
            raise ValueError("Project name and description cannot be empty.")
        
        project = {
            'name': project_name,
            'description': description,
            'language1_materials': [],
            'language2_materials': []
        }
        self.projects.append(project)

    def add_material(self, project_name: str, language: str, material: str):
        """
        Adds educational materials to a specific project in the specified language.

        Args:
            project_name (str): The name of the project to which the material will be added.
            language (str): The language of the material ('language1' or 'language2').
            material (str): The educational material to be added.

        Raises:
            ValueError: If the project does not exist or if the language is invalid.
        """
        project = self._find_project(project_name)
        if language not in [self.language1, self.language2]:
            raise ValueError("Invalid language specified. Use 'language1' or 'language2'.")

        if language == self.language1:
            project['language1_materials'].append(material)
        else:
            project['language2_materials'].append(material)

    def _find_project(self, project_name: str):
        """
        Finds a project by its name.

        Args:
            project_name (str): The name of the project to find.

        Returns:
            dict: The project if found.

        Raises:
            ValueError: If the project is not found.
        """
        for project in self.projects:
            if project['name'] == project_name:
                return project
        raise ValueError(f"Project '{project_name}' not found.")

    def display_projects(self):
        """
        Displays all projects in the program along with their materials.
        """
        for project in self.projects:
            print(f"Project Name: {project['name']}")
            print(f"Description: {project['description']}")
            print(f"Materials in {self.language1}: {project['language1_materials']}")
            print(f"Materials in {self.language2}: {project['language2_materials']}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        program = BilingualEducationProgram("English", "Mandarin")
        program.add_project("Environmental Awareness", "A project to learn about recycling and conservation.")
        program.add_material("Environmental Awareness", "English", "Recycling Guide")
        program.add_material("Environmental Awareness", "Mandarin", "环保指南")
        program.display_projects()
    except ValueError as e:
        print(f"Error: {e}")
```
