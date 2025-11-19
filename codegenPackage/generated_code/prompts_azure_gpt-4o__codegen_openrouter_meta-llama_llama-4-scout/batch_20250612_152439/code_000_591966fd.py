"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Write Python code to calculate the cost of 3D printing a model using FDM technology, considering layer thickness between 50 to 300 microns and material types like PLA or ABS, as described on https://tabriz3dprint.ir.
Generated: DETERMINISTIC_591966fd887a16fb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# 3D Printing Cost Calculator using FDM Technology

class Material:
    """Material types and their properties."""

    def __init__(self, name, density, price_per_kg):
        """
        Initialize a material.

        Args:
            name (str): Material name.
            density (float): Material density in g/cm^3.
            price_per_kg (float): Material price per kilogram.
        """
        self.name = name
        self.density = density
        self.price_per_kg = price_per_kg

class PrintingSettings:
    """3D printing settings."""

    def __init__(self, layer_thickness, material, print_volume):
        """
        Initialize printing settings.

        Args:
            layer_thickness (float): Layer thickness in microns.
            material (Material): Printing material.
            print_volume (float): Print volume in cm^3.
        """
        if not 50 <= layer_thickness <= 300:
            raise ValueError("Layer thickness must be between 50 and 300 microns")

        self.layer_thickness = layer_thickness / 1000  # Convert microns to mm
        self.material = material
        self.print_volume = print_volume

    def calculate_material_weight(self):
        """
        Calculate the weight of material needed.

        Returns:
            float: Material weight in grams.
        """
        return self.print_volume * self.material.density

    def calculate_material_cost(self):
        """
        Calculate the cost of material.

        Returns:
            float: Material cost.
        """
        weight_in_kg = self.calculate_material_weight() / 1000
        return weight_in_kg * self.material.price_per_kg

    def calculate_printing_time(self):
        """
        Estimate printing time in hours.

        Note:
            This is a rough estimate and actual printing time may vary.

        Returns:
            float: Printing time in hours.
        """
        # Assume a constant printing speed of 50 mm/h
        # This is a very rough estimate and actual speed may vary
        printing_speed = 50  # mm/h
        layer_height_in_mm = self.layer_thickness
        build_volume_in_mm = (self.print_volume ** (1/3)) * 1000  # Convert cm to mm
        build_layers = build_volume_in_mm / layer_height_in_mm
        printing_time_in_hours = build_layers / printing_speed
        return printing_time_in_hours

def main():
    try:
        # Define materials
        pla = Material("PLA", 1.24, 20)
        abs_material = Material("ABS", 1.04, 30)

        # Get user input
        layer_thickness = float(input("Enter layer thickness in microns: "))
        material_name = input("Enter material type (PLA or ABS): ")
        material = pla if material_name.upper() == "PLA" else abs_material if material_name.upper() == "ABS" else None
        if material is None:
            raise ValueError("Invalid material type")

        print_volume = float(input("Enter print volume in cm^3: "))

        # Create printing settings
        settings = PrintingSettings(layer_thickness, material, print_volume)

        # Calculate costs
        material_cost = settings.calculate_material_cost()
        printing_time = settings.calculate_printing_time()
        labor_cost_per_hour = 10  # Assume $10 per hour labor cost
        labor_cost = printing_time * labor_cost_per_hour
        total_cost = material_cost + labor_cost

        # Print results
        print(f"Material: {settings.material.name}")
        print(f"Layer Thickness: {settings.layer_thickness * 1000} microns")
        print(f"Print Volume: {settings.print_volume} cm^3")
        print(f"Material Cost: ${material_cost:.2f}")
        print(f"Printing Time: {printing_time:.2f} hours")
        print(f"Labor Cost: ${labor_cost:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
