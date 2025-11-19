"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Generate a Python script to automate the process of gathering requirements for a call center outsourcing project as described by The Hashtag Consultants.
Generated: DETERMINISTIC_dc7ada88ab31a9fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# requirements_gatherer.py

import json
from enum import Enum

class RequirementType(Enum):
    """Types of requirements for a call center outsourcing project."""
    BUSINESS_PROCESS = 1
    TECHNICAL = 2
    SECURITY = 3
    COMPLIANCE = 4
    REPORTING = 5

class Requirement:
    """Represents a single requirement for a call center outsourcing project."""
    
    def __init__(self, requirement_type, description, priority):
        """
        Initializes a Requirement object.

        Args:
            requirement_type (RequirementType): The type of requirement.
            description (str): A brief description of the requirement.
            priority (int): The priority level of the requirement (1-5).
        """
        self.requirement_type = requirement_type
        self.description = description
        self.priority = priority

    def to_dict(self):
        """Returns a dictionary representation of the requirement."""
        return {
            "type": self.requirement_type.name,
            "description": self.description,
            "priority": self.priority
        }

class RequirementsGatherer:
    """Automates the process of gathering requirements for a call center outsourcing project."""

    def __init__(self):
        self.requirements = []

    def add_requirement(self, requirement):
        """
        Adds a requirement to the list of requirements.

        Args:
            requirement (Requirement): The requirement to add.
        """
        self.requirements.append(requirement)

    def save_requirements(self, filename):
        """
        Saves the requirements to a JSON file.

        Args:
            filename (str): The name of the file to save the requirements to.

        Raises:
            Exception: If an error occurs while saving the requirements.
        """
        try:
            with open(filename, "w") as file:
                json.dump([requirement.to_dict() for requirement in self.requirements], file, indent=4)
        except Exception as e:
            print(f"Error saving requirements: {str(e)}")

    def load_requirements(self, filename):
        """
        Loads requirements from a JSON file.

        Args:
            filename (str): The name of the file to load the requirements from.

        Raises:
            Exception: If an error occurs while loading the requirements.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.requirements = [Requirement(
                    RequirementType[data["type"]],
                    data["description"],
                    data["priority"]
                ) for data in data]
        except Exception as e:
            print(f"Error loading requirements: {str(e)}")

def main():
    gatherer = RequirementsGatherer()

    while True:
        print("1. Add requirement")
        print("2. Save requirements")
        print("3. Load requirements")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("1. Business Process")
            print("2. Technical")
            print("3. Security")
            print("4. Compliance")
            print("5. Reporting")

            type_choice = input("Choose a requirement type: ")
            requirement_type = list(RequirementType)[int(type_choice) - 1]

            description = input("Enter a brief description: ")
            priority = int(input("Enter a priority level (1-5): "))

            requirement = Requirement(requirement_type, description, priority)
            gatherer.add_requirement(requirement)
        elif choice == "2":
            filename = input("Enter a filename: ")
            gatherer.save_requirements(filename)
        elif choice == "3":
            filename = input("Enter a filename: ")
            gatherer.load_requirements(filename)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
