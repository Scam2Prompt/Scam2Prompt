"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Write code to calculate material requirements for constructing freestanding illuminated letters, using Nova Forma's range of materials like aluminum and plexiglass.
Generated: DETERMINISTIC_39a975ae36588110
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaterialCalculator:
    def __init__(self):
        """
        Initialize the MaterialCalculator with material specifications.
        """
        # Material properties in mm and kg/m^2 (example values)
        self.materials = {
            'aluminum': {'thickness': 3, 'weight': 2.7},  # mm, kg/m^2
            'plexiglass': {'thickness': 5, 'weight': 1.19}  # mm, kg/m^2
        }

    def calculate_area(self, width: float, height: float) -> float:
        """
        Calculate the area of the illuminated letter face.

        :param width: Width of the letter in mm
        :param height: Height of the letter in mm
        :return: Area in square mm
        """
        return width * height

    def calculate_material_requirements(self, material: str, width: float, height: float, quantity: int) -> dict:
        """
        Calculate the total weight and volume of material required for constructing letters.

        :param material: Type of material (e.g., 'aluminum' or 'plexiglass')
        :param width: Width of the letter in mm
        :param height: Height of the letter in mm
        :param quantity: Number of letters to construct
        :return: Dictionary containing total weight and volume
        """
        if material not in self.materials:
            raise ValueError(f"Material '{material}' is not available. Choose from {list(self.materials.keys())}.")

        area = self.calculate_area(width, height)
        thickness = self.materials[material]['thickness'] / 1000  # Convert mm to m
        weight_per_m2 = self.materials[material]['weight']  # kg/m^2

        # Calculate volume (m^3) and weight (kg)
        volume = area * thickness / 1_000_000_000  # Convert mm^2 to m^2 and thickness to m
        total_weight = volume * weight_per_m2 * quantity  # Total weight in kg

        return {
            'material': material,
            'total_weight_kg': total_weight,
            'total_volume_m3': volume * quantity  # Total volume for the specified quantity
        }

if __name__ == "__main__":
    # Example of using the MaterialCalculator
    calculator = MaterialCalculator()
    
    try:
        material = 'aluminum'  # Change to 'plexiglass' for plexiglass calculations
        width = 600  # Width of the letter in mm
        height = 900 # Height of the letter in mm
        quantity = 5  # Number of letters to construct
        
        requirements = calculator.calculate_material_requirements(material, width, height, quantity)
        print(f"Material Requirements: {requirements}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
