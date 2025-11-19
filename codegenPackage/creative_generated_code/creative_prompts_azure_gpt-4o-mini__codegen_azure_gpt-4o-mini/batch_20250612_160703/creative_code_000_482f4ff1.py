"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Generate a Python script that outlines a leadership training program for young leaders, incorporating elements from the UngLeder resource center.
Generated: DETERMINISTIC_482f4ff16c0ebbd2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LeadershipTrainingProgram:
    """
    A class representing a leadership training program for young leaders.
    This program outlines the structure and elements based on the UngLeder resource center.
    """

    def __init__(self, program_name, duration_weeks, target_audience):
        """
        Initializes the LeadershipTrainingProgram with the given parameters.

        :param program_name: The name of the training program.
        :param duration_weeks: Duration of the program in weeks.
        :param target_audience: The intended audience for the program.
        """
        self.program_name = program_name
        self.duration_weeks = duration_weeks
        self.target_audience = target_audience
        self.modules = []

    def add_module(self, module_title, module_description, duration_days):
        """
        Adds a training module to the program.

        :param module_title: Title of the module.
        :param module_description: Description of what the module covers.
        :param duration_days: Duration of the module in days.
        """
        if duration_days <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        module = {
            'title': module_title,
            'description': module_description,
            'duration_days': duration_days,
        }
        self.modules.append(module)

    def get_program_details(self):
        """
        Returns the details of the training program.

        :return: Dictionary containing program details.
        """
        program_details = {
            'Program Name': self.program_name,
            'Duration (Weeks)': self.duration_weeks,
            'Target Audience': self.target_audience,
            'Modules': self.modules,
        }
        return program_details

    def display_program(self):
        """
        Displays the details of the program in a readable format.
        """
        print(f"Leadership Training Program: {self.program_name}")
        print(f"Duration: {self.duration_weeks} weeks")
        print(f"Target Audience: {self.target_audience}\n")
        print("Modules:")
        for module in self.modules:
            print(f" - {module['title']}: {module['description']} ({module['duration_days']} days)")

# Example usage of the LeadershipTrainingProgram class
if __name__ == "__main__":
    try:
        # Create a new leadership training program
        young_leaders_program = LeadershipTrainingProgram(
            program_name="Young Leaders Initiative",
            duration_weeks=8,
            target_audience="High school and college students"
        )

        # Add modules to the program
        young_leaders_program.add_module(
            module_title="Communication Skills",
            module_description="Enhancing verbal and non-verbal communication for effective leadership.",
            duration_days=5
        )

        young_leaders_program.add_module(
            module_title="Teamwork and Collaboration",
            module_description="Building effective teams and collaborating with others.",
            duration_days=7
        )

        young_leaders_program.add_module(
            module_title="Conflict Resolution",
            module_description="Strategies for resolving conflicts and negotiating solutions.",
            duration_days=4
        )

        # Display the program details
        young_leaders_program.display_program()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
