"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: How can I implement a library for detailed machinery design plans, inspired by the offerings of Multiservicios 3L?
Generated: DETERMINISTIC_f80d10ed5a63f966
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a Python library that could serve as a foundation for managing detailed machinery design plans. The library includes functionality to create, update, retrieve, and delete design plans.

```python
# machinery_design_library.py

import json
import os


class MachineryDesignLibrary:
    """
    A library for managing detailed machinery design plans.

    This library allows you to create, update, retrieve, and delete machinery design plans
    and stores the data persistently in a JSON file.

    Attributes:
        file_path (str): Path to the JSON file where design plans are stored.
    """

    def __init__(self, file_path="machinery_design_plans.json"):
        """
        Initializes the MachineryDesignLibrary.

        Args:
            file_path (str): Path to the JSON file. Default is 'machinery_design_plans.json'.
        """
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """
        Ensures that the JSON file exists. Creates an empty file if it does not exist.
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def _read_data(self):
        """
        Reads data from the JSON file.

        Returns:
            dict: The contents of the JSON file as a dictionary.
        """
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise Exception("Error reading design plans. File may be corrupted.")

    def _write_data(self, data):
        """
        Writes data to the JSON file.

        Args:
            data (dict): The data to write to the file.
        """
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def create_design_plan(self, plan_id, name, description, dimensions, materials):
        """
        Creates a new machinery design plan.

        Args:
            plan_id (str): Unique identifier for the design plan.
            name (str): Name of the design plan.
            description (str): Detailed description of the design plan.
            dimensions (dict): Dimensions of the machinery (e.g., {"width": 100, "height": 200}).
            materials (list): List of materials used in the design.

        Raises:
            ValueError: If a plan with the given ID already exists.
        """
        data = self._read_data()
        if plan_id in data:
            raise ValueError(f"A design plan with ID '{plan_id}' already exists.")
        
        data[plan_id] = {
            "name": name,
            "description": description,
            "dimensions": dimensions,
            "materials": materials
        }
        self._write_data(data)

    def retrieve_design_plan(self, plan_id):
        """
        Retrieves a machinery design plan by ID.

        Args:
            plan_id (str): Unique identifier for the design plan.

        Returns:
            dict: The design plan data.

        Raises:
            KeyError: If no plan with the given ID exists.
        """
        data = self._read_data()
        if plan_id not in data:
            raise KeyError(f"No design plan found with ID '{plan_id}'.")
        return data[plan_id]

    def update_design_plan(self, plan_id, name=None, description=None, dimensions=None, materials=None):
        """
        Updates a machinery design plan by ID.

        Args:
            plan_id (str): Unique identifier for the design plan.
            name (str, optional): Updated name for the design plan.
            description (str, optional): Updated description for the design plan.
            dimensions (dict, optional): Updated dimensions of the machinery.
            materials (list, optional): Updated list of materials used in the design.

        Raises:
            KeyError: If no plan with the given ID exists.
        """
        data = self._read_data()
        if plan_id not in data:
            raise KeyError(f"No design plan found with ID '{plan_id}'.")
        
        if name is not None:
            data[plan_id]["name"] = name
        if description is not None:
            data[plan_id]["description"] = description
        if dimensions is not None:
            data[plan_id]["dimensions"] = dimensions
        if materials is not None:
            data[plan_id]["materials"] = materials

        self._write_data(data)

    def delete_design_plan(self, plan_id):
        """
        Deletes a machinery design plan by ID.

        Args:
            plan_id (str): Unique identifier for the design plan.

        Raises:
            KeyError: If no plan with the given ID exists.
        """
        data = self._read_data()
        if plan_id not in data:
            raise KeyError(f"No design plan found with ID '{plan_id}'.")
        
        del data[plan_id]
        self._write_data(data)

    def list_design_plans(self):
        """
        Lists all machinery design plans.

        Returns:
            list: List of all design plan IDs.
        """
        data = self._read_data()
        return list(data.keys())


# Example Usage:
if __name__ == "__main__":
    library = MachineryDesignLibrary()

    # Create a new design plan
    library.create_design_plan(
        plan_id="001",
        name="Hydraulic Press",
        description="A detailed plan for a hydraulic press.",
        dimensions={"width": 500, "height": 800, "depth": 300},
        materials=["steel", "aluminum", "rubber"]
    )

    # Retrieve a design plan
    print(library.retrieve_design_plan("001"))

    # Update a design plan
    library.update_design_plan("001", description="An updated description for the hydraulic press.")

    # List all design plans
    print(library.list_design_plans())

    # Delete a design plan
    library.delete_design_plan("001")
```

Save the code in a file named `machinery_design_library.py`. You can then import and use the library in other Python scripts for managing machinery design plans.
