"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write code to calculate the optimal thickness for rubber flooring in a gym setting, referencing the types of rubber flooring materials like EPDM and TPV mentioned on Rubber Flooring Indonesia's website.
Generated: DETERMINISTIC_a8370edfa2b3afbf
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RubberFlooringCalculator:
    """
    A class to calculate the optimal thickness for rubber flooring in a gym setting.
    This class considers different types of rubber flooring materials such as EPDM and TPV.
    """

    def __init__(self, material_type: str, usage_intensity: str):
        """
        Initializes the calculator with the type of rubber flooring material and usage intensity.

        :param material_type: Type of rubber flooring material (e.g., 'EPDM', 'TPV').
        :param usage_intensity: Intensity of usage (e.g., 'low', 'medium', 'high').
        """
        self.material_type = material_type.upper()
        self.usage_intensity = usage_intensity.lower()
        self.thickness_recommendations = {
            'EPDM': {
                'low': 6,    # mm
                'medium': 8, # mm
                'high': 10   # mm
            },
            'TPV': {
                'low': 5,    # mm
                'medium': 7, # mm
                'high': 9    # mm
            }
        }

    def calculate_optimal_thickness(self) -> int:
        """
        Calculates the optimal thickness for the specified rubber flooring material and usage intensity.

        :return: Recommended thickness in mm.
        :raises ValueError: If the material type or usage intensity is invalid.
        """
        try:
            if self.material_type not in self.thickness_recommendations:
                raise ValueError(f"Invalid material type: {self.material_type}. "
                                 "Choose 'EPDM' or 'TPV'.")

            if self.usage_intensity not in self.thickness_recommendations[self.material_type]:
                raise ValueError(f"Invalid usage intensity: {self.usage_intensity}. "
                                 "Choose 'low', 'medium', or 'high'.")

            # Return the recommended thickness based on material type and usage intensity
            return self.thickness_recommendations[self.material_type][self.usage_intensity]

        except ValueError as e:
            print(f"Error: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create an instance of the calculator for EPDM flooring with high usage intensity
    flooring_calculator = RubberFlooringCalculator(material_type='EPDM', usage_intensity='high')
    
    # Calculate and print the optimal thickness
    optimal_thickness = flooring_calculator.calculate_optimal_thickness()
    if optimal_thickness is not None:
        print(f"The optimal thickness for {flooring_calculator.material_type} flooring with {flooring_calculator.usage_intensity} usage is {optimal_thickness} mm.")
```
