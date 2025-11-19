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
class FDMPrinter:
    """
    A class to represent a 3D printer using Fused Deposition Modeling (FDM) technology.
    """

    MATERIAL_COSTS = {
        'PLA': 0.02,  # Cost per gram for PLA
        'ABS': 0.03   # Cost per gram for ABS
    }

    def __init__(self, material: str, layer_thickness: int, model_weight: float):
        """
        Initializes the FDMPrinter with the specified material, layer thickness, and model weight.

        :param material: The type of material used for printing (PLA or ABS).
        :param layer_thickness: The thickness of each layer in microns (must be between 50 and 300).
        :param model_weight: The weight of the model in grams.
        :raises ValueError: If the material is not supported or if the layer thickness is out of range.
        """
        self.material = material
        self.layer_thickness = layer_thickness
        self.model_weight = model_weight

        if self.material not in self.MATERIAL_COSTS:
            raise ValueError(f"Unsupported material: {self.material}. Choose 'PLA' or 'ABS'.")
        
        if not (50 <= self.layer_thickness <= 300):
            raise ValueError("Layer thickness must be between 50 and 300 microns.")

    def calculate_cost(self) -> float:
        """
        Calculates the total cost of 3D printing the model.

        :return: The total cost of printing the model.
        """
        cost_per_gram = self.MATERIAL_COSTS[self.material]
        total_cost = self.model_weight * cost_per_gram
        return total_cost

    def print_summary(self) -> None:
        """
        Prints a summary of the printing parameters and the calculated cost.
        """
        try:
            cost = self.calculate_cost()
            print(f"Material: {self.material}")
            print(f"Layer Thickness: {self.layer_thickness} microns")
            print(f"Model Weight: {self.model_weight} grams")
            print(f"Total Printing Cost: ${cost:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating the cost: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the printer with PLA material, 200 microns layer thickness, and a model weight of 500 grams
        printer = FDMPrinter(material='PLA', layer_thickness=200, model_weight=500)
        printer.print_summary()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
