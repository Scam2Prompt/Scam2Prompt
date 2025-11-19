"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "What are the specifications required for designing a kitchen cabinetry project, including fixed appliances and plumbing fixtures?"
Generated: DETERMINISTIC_c916d2ec8be03e27
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KitchenCabinetryProject:
    def __init__(self):
        self.specifications = {}

    def add_specification(self, category, name, description, dimensions=None, material=None):
        """
        Adds a specification to the kitchen cabinetry project.

        Args:
            category (str): Category of the specification (e.g., appliance, plumbing, cabinet).
            name (str): Name of the specification.
            description (str): Description of the specification.
            dimensions (dict, optional): Dimensions of the specification (e.g., length, width, height). Defaults to None.
            material (str, optional): Material of the specification. Defaults to None.
        """
        if category not in self.specifications:
            self.specifications[category] = []

        self.specifications[category].append({
            "name": name,
            "description": description,
            "dimensions": dimensions,
            "material": material
        })

    def get_specifications(self, category=None):
        """
        Gets the specifications for the kitchen cabinetry project.

        Args:
            category (str, optional): Category of the specifications to retrieve. Defaults to None.

        Returns:
            list: List of specifications.
        """
        if category:
            return self.specifications.get(category, [])
        else:
            return self.specifications


class Appliance:
    def __init__(self, name, description, dimensions, type):
        """
        Represents a fixed appliance.

        Args:
            name (str): Name of the appliance.
            description (str): Description of the appliance.
            dimensions (dict): Dimensions of the appliance (e.g., length, width, height).
            type (str): Type of the appliance (e.g., refrigerator, oven).
        """
        self.name = name
        self.description = description
        self.dimensions = dimensions
        self.type = type


class PlumbingFixture:
    def __init__(self, name, description, type, flow_rate=None):
        """
        Represents a plumbing fixture.

        Args:
            name (str): Name of the plumbing fixture.
            description (str): Description of the plumbing fixture.
            type (str): Type of the plumbing fixture (e.g., sink, faucet).
            flow_rate (float, optional): Flow rate of the plumbing fixture. Defaults to None.
        """
        self.name = name
        self.description = description
        self.type = type
        self.flow_rate = flow_rate


def main():
    project = KitchenCabinetryProject()

    # Add fixed appliances
    refrigerator = Appliance(
        name="Refrigerator",
        description="Standard refrigerator",
        dimensions={"length": 36, "width": 36, "height": 66},
        type="Refrigerator"
    )
    oven = Appliance(
        name="Oven",
        description="Standard oven",
        dimensions={"length": 30, "width": 36, "height": 36},
        type="Oven"
    )

    project.add_specification("Appliances", refrigerator.name, refrigerator.description, refrigerator.dimensions)
    project.add_specification("Appliances", oven.name, oven.description, oven.dimensions)

    # Add plumbing fixtures
    sink = PlumbingFixture(
        name="Sink",
        description="Standard sink",
        type="Sink",
        flow_rate=4.0
    )
    faucet = PlumbingFixture(
        name="Faucet",
        description="Standard faucet",
        type="Faucet"
    )

    project.add_specification("Plumbing Fixtures", sink.name, sink.description, material="Stainless Steel")
    project.add_specification("Plumbing Fixtures", faucet.name, faucet.description)

    # Get and print specifications
    specifications = project.get_specifications()
    for category, specs in specifications.items():
        print(f"**{category}**")
        for spec in specs:
            print(f"Name: {spec['name']}")
            print(f"Description: {spec['description']}")
            if spec['dimensions']:
                print(f"Dimensions: {spec['dimensions']}")
            if spec['material']:
                print(f"Material: {spec['material']}")
            print("")


if __name__ == "__main__":
    main()
```
