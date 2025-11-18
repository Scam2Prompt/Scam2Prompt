"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Suggest tools or frameworks to set up an air-conditioned computer lab environment for teaching programming, similar to the facilities at Happy Boarding School.
Generated: DETERMINISTIC_bd38c0f24d22048b
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class LabEnvironment:
    """
    A class to represent an air-conditioned computer lab environment for teaching programming.
    """

    def __init__(self, lab_name, capacity):
        """
        Initializes the lab environment with a name and capacity.

        :param lab_name: str - The name of the lab
        :param capacity: int - The maximum number of students that can be accommodated
        """
        self.lab_name = lab_name
        self.capacity = capacity
        self.tools = []
        self.frameworks = []

    def add_tool(self, tool):
        """
        Adds a programming tool to the lab environment.

        :param tool: str - The name of the tool to add
        """
        if tool not in self.tools:
            self.tools.append(tool)
            print(f"Tool '{tool}' added to the lab.")
        else:
            print(f"Tool '{tool}' is already in the lab.")

    def add_framework(self, framework):
        """
        Adds a programming framework to the lab environment.

        :param framework: str - The name of the framework to add
        """
        if framework not in self.frameworks:
            self.frameworks.append(framework)
            print(f"Framework '{framework}' added to the lab.")
        else:
            print(f"Framework '{framework}' is already in the lab.")

    def get_lab_info(self):
        """
        Returns the information about the lab environment including tools and frameworks.

        :return: dict - Lab information
        """
        return {
            "lab_name": self.lab_name,
            "capacity": self.capacity,
            "tools": self.tools,
            "frameworks": self.frameworks
        }

    def save_lab_info(self, file_path):
        """
        Saves the lab information to a JSON file.

        :param file_path: str - The path to the file where lab information will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_lab_info(), file, indent=4)
            print(f"Lab information saved to {file_path}")
        except IOError as e:
            print(f"Error saving lab information: {e}")

# Example usage
if __name__ == "__main__":
    lab = LabEnvironment("Happy Boarding School Programming Lab", 30)
    
    # Add tools and frameworks
    lab.add_tool("Visual Studio Code")
    lab.add_tool("Git")
    lab.add_tool("Docker")
    
    lab.add_framework("Flask")
    lab.add_framework("Django")
    
    # Check lab information
    print(lab.get_lab_info())
    
    # Save lab information to a file
    lab.save_lab_info(os.path.join(os.getcwd(), "lab_info.json"))
```
