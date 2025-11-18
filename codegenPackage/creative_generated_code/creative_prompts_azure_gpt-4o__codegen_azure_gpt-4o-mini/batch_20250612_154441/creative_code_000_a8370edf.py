"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Write code to calculate the optimal thickness for rubber flooring in a gym setting, referencing the types of rubber flooring materials like EPDM and TPV mentioned on Rubber Flooring Indonesia's website.
Generated: DETERMINISTIC_a8370edfa2b3afbf
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RubberFlooringCalculator:
    def __init__(self):
        # Define standard thickness recommendations for various rubber flooring materials
        self.material_thickness_recommendations = {
            'EPDM': {
                'minimum': 8,  # Minimum thickness in mm for EPDM
                'recommended': 10,  # Recommended thickness in mm for most gym settings
                'maximum': 12  # Maximum thickness in mm for EPDM
            },
            'TPV': {
                'minimum': 6,  # Minimum thickness in mm for TPV
                'recommended': 8,  # Recommended thickness in mm for most gym settings
                'maximum': 10  # Maximum thickness in mm for TPV
            },
        }

    def calculate_optimal_thickness(self, material_type: str, use_case: str) -> int:
        """
        Calculate the optimal thickness for rubber flooring based on material type and use case.

        :param material_type: Type of rubber flooring material ('EPDM' or 'TPV')
        :param use_case: The intended use case (e.g., 'gym', 'playground')
        :return: Optimal thickness in mm
        :raises ValueError: If an unsupported material type is provided
        """
        # Normalize material type to uppercase for consistency
        material_type = material_type.upper()

        # Validate material type
        if material_type not in self.material_thickness_recommendations:
            raise ValueError(f"Unsupported material type: {material_type}. Choose 'EPDM' or 'TPV'.")

        # Extract thickness recommendations for the chosen material
        thickness_info = self.material_thickness_recommendations[material_type]

        # Determine optimal thickness based on use case
        optimal_thickness = thickness_info['recommended']

        # Adjust thickness based on the specific use case
        if use_case == 'gym':
            optimal_thickness = thickness_info['recommended']
        elif use_case == 'high-impact':
            optimal_thickness = thickness_info['maximum']
        elif use_case == 'light-use':
            optimal_thickness = thickness_info['minimum']
        else:
            raise ValueError(f"Unsupported use case: {use_case}. Choose 'gym', 'high-impact', or 'light-use'.")

        return optimal_thickness


def main():
    # Create an instance of the RubberFlooringCalculator class
    calculator = RubberFlooringCalculator()

    try:
        # Example usage: Calculate optimal thickness for EPDM flooring in a gym setting
        material = 'EPDM'
        use_case = 'gym'
        optimal_thickness = calculator.calculate_optimal_thickness(material, use_case)
        print(f"The optimal thickness for {material} flooring in a {use_case} setting is: {optimal_thickness} mm.")
        
        # Example usage: Calculate optimal thickness for TPV flooring in a high-impact setting
        material = 'TPV'
        use_case = 'high-impact'
        optimal_thickness = calculator.calculate_optimal_thickness(material, use_case)
        print(f"The optimal thickness for {material} flooring in a {use_case} setting is: {optimal_thickness} mm.")
        
    except ValueError as e:
        # Handle any value errors that occur during calculations
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
