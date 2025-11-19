"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Design a curriculum for a digital marketing course that includes hands-on projects, similar to those offered by PDMA Technologies.
Generated: DETERMINISTIC_9392ed2812f2ba87
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DigitalMarketingCourse:
    """
    A class to represent a digital marketing course curriculum.
    """

    def __init__(self):
        """
        Initializes the course with a list of modules and projects.
        """
        self.modules = []
        self.projects = []

    def add_module(self, module_name, description):
        """
        Adds a module to the course curriculum.

        Parameters:
        module_name (str): The name of the module.
        description (str): A brief description of the module.
        """
        if not isinstance(module_name, str) or not isinstance(description, str):
            raise ValueError("Module name and description must be strings.")
        
        self.modules.append({'name': module_name, 'description': description})

    def add_project(self, project_name, details):
        """
        Adds a hands-on project to the course curriculum.

        Parameters:
        project_name (str): The name of the project.
        details (str): A brief description of the project.
        """
        if not isinstance(project_name, str) or not isinstance(details, str):
            raise ValueError("Project name and details must be strings.")
        
        self.projects.append({'name': project_name, 'details': details})

    def get_curriculum(self):
        """
        Returns the complete curriculum including modules and projects.

        Returns:
        dict: A dictionary containing modules and projects.
        """
        return {
            'modules': self.modules,
            'projects': self.projects
        }

    def display_curriculum(self):
        """
        Displays the curriculum in a readable format.
        """
        curriculum = self.get_curriculum()
        print("Digital Marketing Course Curriculum:\n")
        
        print("Modules:")
        for module in curriculum['modules']:
            print(f"- {module['name']}: {module['description']}")
        
        print("\nProjects:")
        for project in curriculum['projects']:
            print(f"- {project['name']}: {project['details']}")


# Example usage
if __name__ == "__main__":
    try:
        course = DigitalMarketingCourse()
        
        # Adding modules
        course.add_module("Introduction to Digital Marketing", "Overview of digital marketing concepts and strategies.")
        course.add_module("SEO Basics", "Understanding search engine optimization and its importance.")
        course.add_module("Social Media Marketing", "Strategies for marketing on various social media platforms.")
        
        # Adding projects
        course.add_project("Create a Blog", "Develop a blog using SEO best practices.")
        course.add_project("Social Media Campaign", "Design and execute a social media marketing campaign.")
        
        # Display the curriculum
        course.display_curriculum()
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
