"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write Python code to generate a catalog of "Karma Çalışma Tezgahları" with specifications like dimensions, material type (DKP sac), and coating (electrostatic powder paint) in JSON format.
Generated: DETERMINISTIC_a14804ba5df2ea32
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Workbench:
    def __init__(self, name, dimensions, material_type, coating):
        """
        Initialize a Workbench object.

        Args:
            name (str): Name of the workbench.
            dimensions (dict): Dimensions of the workbench (length, width, height).
            material_type (str): Type of material used (e.g., DKP sac).
            coating (str): Type of coating used (e.g., electrostatic powder paint).
        """
        self.name = name
        self.dimensions = dimensions
        self.material_type = material_type
        self.coating = coating

    def to_dict(self):
        """
        Convert the Workbench object to a dictionary.

        Returns:
            dict: Dictionary representation of the Workbench object.
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "material_type": self.material_type,
            "coating": self.coating
        }

class WorkbenchCatalog:
    def __init__(self):
        """
        Initialize an empty workbench catalog.
        """
        self.workbenches = []

    def add_workbench(self, workbench):
        """
        Add a workbench to the catalog.

        Args:
            workbench (Workbench): Workbench object to add.
        """
        self.workbenches.append(workbench)

    def to_json(self):
        """
        Convert the workbench catalog to JSON.

        Returns:
            str: JSON representation of the workbench catalog.
        """
        catalog = [workbench.to_dict() for workbench in self.workbenches]
        return json.dumps(catalog, indent=4)

def main():
    try:
        catalog = WorkbenchCatalog()

        workbench1 = Workbench(
            "Karma Çalışma Tezgahı 1",
            {"length": 2000, "width": 800, "height": 900},
            "DKP sac",
            "electrostatic powder paint"
        )
        catalog.add_workbench(workbench1)

        workbench2 = Workbench(
            "Karma Çalışma Tezgahı 2",
            {"length": 2500, "width": 1000, "height": 950},
            "DKP sac",
            "electrostatic powder paint"
        )
        catalog.add_workbench(workbench2)

        workbench3 = Workbench(
            "Karma Çalışma Tezgahı 3",
            {"length": 3000, "width": 1200, "height": 1000},
            "DKP sac",
            "electrostatic powder paint"
        )
        catalog.add_workbench(workbench3)

        json_catalog = catalog.to_json()
        print(json_catalog)

        with open("workbench_catalog.json", "w") as f:
            json.dump(json.loads(json_catalog), f, indent=4)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
