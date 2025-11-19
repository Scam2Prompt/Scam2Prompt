"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Generate Python code to create a private label cleaning tool using PDC Brush's specifications and ethical trading practices.
Generated: DETERMINISTIC_7145b4259a72bf90
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cleaning Tool Management System

This script creates a private label cleaning tool using PDC Brush's specifications 
and adheres to ethical trading practices. It includes functionality for defining 
and managing cleaning tool attributes, ensuring ethical compliance, and validating 
tool specifications.
"""

import json


class EthicalTradingError(Exception):
    """Custom exception for ethical trading violations."""
    pass


class CleaningTool:
    """
    Represents a cleaning tool with specific attributes and ethical compliance.
    """

    def __init__(self, name, material, dimensions, ethical_certification):
        """
        Initializes a new cleaning tool.

        Args:
            name (str): Name of the cleaning tool.
            material (str): Material used to manufacture the tool.
            dimensions (dict): Dimensions of the tool (e.g., {"length": 10, "width": 5}).
            ethical_certification (str): Certification ensuring ethical trading practices.
        """
        self.name = name
        self.material = material
        self.dimensions = dimensions
        self.ethical_certification = ethical_certification

        # Validate ethical practices during initialization
        self.validate_ethics()

    def validate_ethics(self):
        """
        Validates that the cleaning tool complies with ethical trading practices.

        Raises:
            EthicalTradingError: If ethical certification is missing or invalid.
        """
        if not self.ethical_certification or self.ethical_certification.lower() not in ["fair-trade", "eco-friendly"]:
            raise EthicalTradingError(
                f"Ethical certification '{self.ethical_certification}' is invalid or missing."
            )

    def to_dict(self):
        """
        Converts the cleaning tool object to a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the cleaning tool.
        """
        return {
            "name": self.name,
            "material": self.material,
            "dimensions": self.dimensions,
            "ethical_certification": self.ethical_certification,
        }

    def __str__(self):
        """
        Returns a string representation of the cleaning tool.

        Returns:
            str: String representation of the tool details.
        """
        return f"CleaningTool(name={self.name}, material={self.material}, dimensions={self.dimensions}, ethical_certification={self.ethical_certification})"


class CleaningToolManager:
    """
    Manages a collection of cleaning tools.
    """

    def __init__(self):
        """Initializes the cleaning tool manager with an empty collection."""
        self.tools = []

    def add_tool(self, tool):
        """
        Adds a new cleaning tool to the collection.

        Args:
            tool (CleaningTool): The cleaning tool to add.

        Raises:
            TypeError: If the provided tool is not an instance of CleaningTool.
        """
        if not isinstance(tool, CleaningTool):
            raise TypeError("Expected an instance of CleaningTool.")
        self.tools.append(tool)

    def list_tools(self):
        """
        Lists all the cleaning tools in the collection.

        Returns:
            list: List of dictionaries representing the cleaning tools.
        """
        return [tool.to_dict() for tool in self.tools]

    def save_tools(self, file_path):
        """
        Saves the cleaning tools to a JSON file.

        Args:
            file_path (str): Path to the file where tools are saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_tools(), file, indent=4)
            print(f"Cleaning tools successfully saved to {file_path}")
        except OSError as e:
            print(f"Error saving tools to file: {e}")

    def load_tools(self, file_path):
        """
        Loads cleaning tools from a JSON file.

        Args:
            file_path (str): Path to the file to load tools from.
        """
        try:
            with open(file_path, "r") as file:
                tools_data = json.load(file)
                self.tools = [
                    CleaningTool(
                        name=tool["name"],
                        material=tool["material"],
                        dimensions=tool["dimensions"],
                        ethical_certification=tool["ethical_certification"],
                    )
                    for tool in tools_data
                ]
            print(f"Cleaning tools successfully loaded from {file_path}")
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading tools from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a cleaning tool manager
    manager = CleaningToolManager()

    try:
        # Define a cleaning tool
        tool1 = CleaningTool(
            name="Eco Brush",
            material="Bamboo",
            dimensions={"length": 15, "width": 3},
            ethical_certification="Fair-Trade",
        )

        # Add the tool to the manager
        manager.add_tool(tool1)

        # Save tools to a file
        manager.save_tools("cleaning_tools.json")

        # Load tools from a file
        manager.load_tools("cleaning_tools.json")

        # List all tools
        for tool in manager.list_tools():
            print(tool)

    except EthicalTradingError as e:
        print(f"Ethical compliance error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
