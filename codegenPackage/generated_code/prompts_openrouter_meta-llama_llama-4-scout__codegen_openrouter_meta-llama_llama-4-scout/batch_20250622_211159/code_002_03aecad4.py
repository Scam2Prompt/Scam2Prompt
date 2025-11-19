"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Write a Python script to calculate the cost of stainless steel materials for a custom machinery project, considering factors like material type, quantity, and fabrication process."
Generated: DETERMINISTIC_03aecad4e292159b
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stainless_steel_calculator.py

class StainlessSteelMaterial:
    """Represents a stainless steel material with its properties."""

    def __init__(self, name, price_per_unit, unit='kg'):
        """
        Initializes a StainlessSteelMaterial instance.

        Args:
            name (str): Material name.
            price_per_unit (float): Price per unit of the material.
            unit (str, optional): Unit of the material. Defaults to 'kg'.
        """
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit = unit

class FabricationProcess:
    """Represents a fabrication process with its cost multiplier."""

    def __init__(self, name, cost_multiplier):
        """
        Initializes a FabricationProcess instance.

        Args:
            name (str): Process name.
            cost_multiplier (float): Cost multiplier for the process.
        """
        self.name = name
        self.cost_multiplier = cost_multiplier

class StainlessSteelCalculator:
    """Calculates the cost of stainless steel materials for a custom machinery project."""

    def __init__(self):
        self.materials = {}
        self.processes = {}

    def add_material(self, material):
        """
        Adds a stainless steel material to the calculator.

        Args:
            material (StainlessSteelMaterial): Material to add.
        """
        self.materials[material.name] = material

    def add_process(self, process):
        """
        Adds a fabrication process to the calculator.

        Args:
            process (FabricationProcess): Process to add.
        """
        self.processes[process.name] = process

    def calculate_cost(self, material_name, quantity, process_name):
        """
        Calculates the cost of a stainless steel material for a custom machinery project.

        Args:
            material_name (str): Name of the material.
            quantity (float): Quantity of the material.
            process_name (str): Name of the fabrication process.

        Returns:
            float: Total cost of the material.

        Raises:
            ValueError: If the material or process is not found.
        """
        if material_name not in self.materials:
            raise ValueError(f"Material '{material_name}' not found")

        if process_name not in self.processes:
            raise ValueError(f"Process '{process_name}' not found")

        material = self.materials[material_name]
        process = self.processes[process_name]

        # Calculate the base cost of the material
        base_cost = material.price_per_unit * quantity

        # Apply the fabrication process cost multiplier
        total_cost = base_cost * process.cost_multiplier

        return total_cost

def main():
    calculator = StainlessSteelCalculator()

    # Define materials
    material1 = StainlessSteelMaterial('304L', 10.0)
    material2 = StainlessSteelMaterial('316L', 15.0)

    # Define fabrication processes
    process1 = FabricationProcess('Cutting', 1.2)
    process2 = FabricationProcess('Welding', 1.5)

    # Add materials and processes to the calculator
    calculator.add_material(material1)
    calculator.add_material(material2)
    calculator.add_process(process1)
    calculator.add_process(process2)

    try:
        # Calculate the cost of 100 kg of 304L material with cutting process
        cost = calculator.calculate_cost('304L', 100.0, 'Cutting')
        print(f"Cost: ${cost:.2f}")

        # Calculate the cost of 50 kg of 316L material with welding process
        cost = calculator.calculate_cost('316L', 50.0, 'Welding')
        print(f"Cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```
