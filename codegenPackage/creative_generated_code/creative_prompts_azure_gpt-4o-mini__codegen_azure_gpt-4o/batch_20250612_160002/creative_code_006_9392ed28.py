"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Design a curriculum for a digital marketing course that includes hands-on projects, similar to those offered by PDMA Technologies.
Generated: DETERMINISTIC_9392ed2812f2ba87
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# curriculum_generator.py

# Import necessary library
import json

class CurriculumGenerator:
    """
    A class to generate a digital marketing curriculum.
    """

    def __init__(self, course_name, duration_weeks):
        """
        Initializes the CurriculumGenerator with basic course information.

        Args:
            course_name (str): The name of the course.
            duration_weeks (int): The total duration of the course in weeks.
        """
        self.course_name = course_name
        self.duration_weeks = duration_weeks
        self.curriculum = {}

    def define_modules(self, modules):
        """
        Defines the main modules of the course.

        Args:
            modules (list): A list of module names.
        """
        self.curriculum['Modules'] = [
            {"Module Name": module, "Projects": []} for module in modules
        ]

    def add_project_to_module(self, module_name, project_name, description):
        """
        Adds a hands-on project to a module.

        Args:
            module_name (str): The name of the module where the project will be added.
            project_name (str): The name of the project.
            description (str): A brief description of the project.
        
        Raises:
            ValueError: If the module name does not exist in the curriculum.
        """
        for module in self.curriculum['Modules']:
            if module['Module Name'] == module_name:
                module['Projects'].append({
                    "Project Name": project_name,
                    "Description": description
                })
                return
        raise ValueError(f"Module '{module_name}' does not exist in the curriculum.")

    def generate_curriculum(self):
        """
        Generates the complete curriculum as a dictionary.

        Returns:
            dict: The complete curriculum.
        """
        self.curriculum['Course Name'] = self.course_name
        self.curriculum['Duration (weeks)'] = self.duration_weeks
        return self.curriculum

    def export_curriculum_to_json(self, file_name):
        """
        Exports the curriculum to a JSON file.

        Args:
            file_name (str): The name of the JSON file to create.
        """
        try:
            with open(file_name, 'w') as json_file:
                json.dump(self.curriculum, json_file, indent=4)
            print(f"Curriculum successfully exported to {file_name}")
        except Exception as e:
            print(f"An error occurred while exporting the curriculum: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the curriculum generator
    cg = CurriculumGenerator(course_name="Digital Marketing Masterclass", duration_weeks=12)

    # Define course modules
    cg.define_modules(["Introduction to Digital Marketing", "SEO Fundamentals", 
                       "Content Marketing Strategies", "Social Media Management", 
                       "Analytics and Reporting", "Paid Advertising Campaigns"])

    # Add hands-on projects to each module
    cg.add_project_to_module("Introduction to Digital Marketing", 
                              "Market Research Report", 
                              "Create a detailed market research report for a chosen industry.")

    cg.add_project_to_module("SEO Fundamentals", 
                              "Keyword Analysis", 
                              "Conduct a comprehensive keyword analysis using popular SEO tools.")

    cg.add_project_to_module("Content Marketing Strategies", 
                              "Blog Post Creation", 
                              "Write and optimize a blog post for search engines.")

    cg.add_project_to_module("Social Media Management", 
                              "Social Media Calendar", 
                              "Develop a content calendar for social media platforms.")

    cg.add_project_to_module("Analytics and Reporting", 
                              "Google Analytics Report", 
                              "Analyze website performance using Google Analytics and create a report.")

    cg.add_project_to_module("Paid Advertising Campaigns", 
                              "Ad Campaign Setup", 
                              "Set up and optimize a paid advertising campaign using Google Ads.")

    # Generate the curriculum
    curriculum = cg.generate_curriculum()

    # Export the curriculum to a JSON file
    cg.export_curriculum_to_json("digital_marketing_curriculum.json")
```
