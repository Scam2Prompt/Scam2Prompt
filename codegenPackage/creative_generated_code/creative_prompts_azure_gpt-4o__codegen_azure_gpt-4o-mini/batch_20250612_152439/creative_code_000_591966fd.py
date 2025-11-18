"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Write Python code to calculate the cost of 3D printing a model using FDM technology, considering layer thickness between 50 to 300 microns and material types like PLA or ABS, as described on https://tabriz3dprint.ir.
Generated: DETERMINISTIC_591966fd887a16fb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FDMPrinter:
    """
    A class to represent a 3D printer using Fused Deposition Modeling (FDM) technology.
    """

    MATERIAL_COSTS = {
        'PLA': 20.0,  # cost per kg for PLA
        'ABS': 25.0   # cost per kg for ABS
    }

    DEFAULT_LAYER_THICKNESS = 200  # Default layer thickness in microns

    def __init__(self, material: str = 'PLA', layer_thickness: int = DEFAULT_LAYER_THICKNESS, weight: float = 1.0):
        """
        Initializes the FDMPrinter with specified material, layer thickness, and weight of the model.

        :param material: Type of material ('PLA' or 'ABS').
        :param layer_thickness: Layer thickness in microns (50-300).
        :param weight: Weight of the model in kg.
        """
        self.set_material(material)
        self.set_layer_thickness(layer_thickness)
        self.weight = weight  # Weight of the model in kg

    def set_material(self, material: str):
        """
        Sets the material type for the printer.

        :param material: Type of material ('PLA' or 'ABS').
        :raises ValueError: If the material is not supported.
        """
        if material not in self.MATERIAL_COSTS:
            raise ValueError(f"Unsupported material: {material}. Choose 'PLA' or 'ABS'.")
        self.material = material

    def set_layer_thickness(self, layer_thickness: int):
        """
        Sets the layer thickness of the model.

        :param layer_thickness: Layer thickness in microns (50-300).
        :raises ValueError: If the layer thickness is out of range.
        """
        if layer_thickness < 50 or layer_thickness > 300:
            raise ValueError("Layer thickness must be between 50 and 300 microns.")
        self.layer_thickness = layer_thickness

    def calculate_cost(self) -> float:
        """
        Calculates the cost of printing the model based on material and weight.

        :return: Cost of printing in currency units.
        """
        cost_per_kg = self.MATERIAL_COSTS[self.material]
        return cost_per_kg * self.weight

    def __str__(self):
        """
        Returns a string representation of the FDMPrinter settings.
        """
        return (f"FDM Printer:\n"
                f"Material: {self.material}\n"
                f"Layer Thickness: {self.layer_thickness} microns\n"
                f"Model Weight: {self.weight} kg\n"
                f"Printing Cost: {self.calculate_cost():.2f} currency units")


if __name__ == "__main__":
    try:
        # Example usage
        printer = FDMPrinter(material='PLA', layer_thickness=200, weight=1.5)
        print(printer)
        
        # Calculate cost
        cost = printer.calculate_cost()
        print(f"Total printing cost: {cost:.2f} currency units")
        
    except ValueError as e:
        print(f"Error: {e}")
```
