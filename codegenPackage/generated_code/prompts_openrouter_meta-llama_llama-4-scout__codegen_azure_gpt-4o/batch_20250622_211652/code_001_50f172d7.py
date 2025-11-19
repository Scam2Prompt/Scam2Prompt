"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Write a Python script to automate the process of generating quotes for CNC cutting services, considering factors like material type, thickness, and design specifications.
Generated: DETERMINISTIC_50f172d74db3bb4a
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CNCQuoteGenerator:
    """
    A class to generate quotes for CNC cutting services based on material type, thickness, and design specifications.
    """

    def __init__(self):
        # Base rates for different materials (per square inch)
        self.material_rates = {
            "steel": 0.50,
            "aluminum": 0.40,
            "plastic": 0.30,
            "wood": 0.20
        }
        # Additional cost per unit thickness (per square inch)
        self.thickness_rate = 0.10
        # Complexity multiplier for design specifications
        self.design_complexity_multiplier = {
            "simple": 1.0,
            "moderate": 1.5,
            "complex": 2.0
        }

    def calculate_quote(self, material, thickness, area, design_complexity):
        """
        Calculate the quote for CNC cutting services.

        :param material: str - Type of material (e.g., 'steel', 'aluminum', 'plastic', 'wood')
        :param thickness: float - Thickness of the material in inches
        :param area: float - Area of the design in square inches
        :param design_complexity: str - Complexity of the design ('simple', 'moderate', 'complex')
        :return: float - Total cost of the CNC cutting service
        """
        try:
            # Validate inputs
            if material not in self.material_rates:
                raise ValueError(f"Invalid material type: {material}. Supported materials: {list(self.material_rates.keys())}")
            if design_complexity not in self.design_complexity_multiplier:
                raise ValueError(f"Invalid design complexity: {design_complexity}. Supported complexities: {list(self.design_complexity_multiplier.keys())}")
            if thickness <= 0 or area <= 0:
                raise ValueError("Thickness and area must be positive values.")

            # Calculate base cost based on material and area
            base_cost = self.material_rates[material] * area

            # Calculate additional cost based on thickness
            thickness_cost = self.thickness_rate * thickness * area

            # Apply design complexity multiplier
            complexity_multiplier = self.design_complexity_multiplier[design_complexity]
            total_cost = (base_cost + thickness_cost) * complexity_multiplier

            return round(total_cost, 2)
        except Exception as e:
            print(f"Error calculating quote: {e}")
            return None

    def generate_quote(self, input_data):
        """
        Generate a quote based on input data.

        :param input_data: dict - Dictionary containing material, thickness, area, and design complexity
        :return: dict - Quote details including input data and total cost
        """
        try:
            material = input_data.get("material")
            thickness = input_data.get("thickness")
            area = input_data.get("area")
            design_complexity = input_data.get("design_complexity")

            # Calculate the total cost
            total_cost = self.calculate_quote(material, thickness, area, design_complexity)
            if total_cost is None:
                raise ValueError("Failed to calculate quote due to invalid input.")

            # Return quote details
            return {
                "material": material,
                "thickness": thickness,
                "area": area,
                "design_complexity": design_complexity,
                "total_cost": total_cost
            }
        except Exception as e:
            print(f"Error generating quote: {e}")
            return None


def main():
    """
    Main function to demonstrate the CNCQuoteGenerator functionality.
    """
    # Example input data
    input_data = {
        "material": "steel",
        "thickness": 0.25,
        "area": 100.0,
        "design_complexity": "moderate"
    }

    # Create an instance of CNCQuoteGenerator
    quote_generator = CNCQuoteGenerator()

    # Generate a quote
    quote = quote_generator.generate_quote(input_data)

    # Print the quote details
    if quote:
        print("Quote Details:")
        print(json.dumps(quote, indent=4))
    else:
        print("Failed to generate quote.")


if __name__ == "__main__":
    main()
```
