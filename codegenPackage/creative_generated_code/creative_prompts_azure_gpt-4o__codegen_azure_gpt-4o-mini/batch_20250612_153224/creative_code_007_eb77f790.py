"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Generate code to calculate the optimal drilling angle and depth for a geotechnical survey, referencing the types of drilling work described by URANPRES.
Generated: DETERMINISTIC_eb77f7904744fa40
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DrillingCalculator:
    def __init__(self, soil_type, rock_hardness, survey_depth):
        """
        Initializes the DrillingCalculator with parameters.

        :param soil_type: Type of soil (string)
        :param rock_hardness: Hardness of the rock (int, scale 1-10)
        :param survey_depth: Depth of the survey in meters (float)
        """
        self.soil_type = soil_type
        self.rock_hardness = rock_hardness
        self.survey_depth = survey_depth

    def calculate_optimal_angle(self):
        """
        Calculates the optimal drilling angle based on soil type and rock hardness.
        
        :return: Optimal angle in degrees (float)
        :raises ValueError: If soil_type is not recognized
        """
        # Define base angles for different soil types
        angle_mapping = {
            'clay': 30,
            'sand': 45,
            'silt': 35,
            'rock': 60
        }

        if self.soil_type.lower() not in angle_mapping:
            raise ValueError(f"Unrecognized soil type: {self.soil_type}")

        base_angle = angle_mapping[self.soil_type.lower()]

        # Adjust angle based on rock hardness
        optimal_angle = base_angle + (self.rock_hardness - 5) * 2

        # Ensure angle is within reasonable limits
        optimal_angle = max(0, min(optimal_angle, 90))
        return optimal_angle

    def calculate_drilling_depth(self):
        """
        Calculates the optimal drilling depth based on the survey depth.

        :return: Optimal drilling depth in meters (float)
        """
        # For this example, we consider a simple factor based on survey depth
        drilling_depth = self.survey_depth * 1.2  # Increase depth by 20%
        return drilling_depth

    def optimal_drilling_parameters(self):
        """
        Computes and returns the optimal drilling parameters.

        :return: Dictionary containing optimal angle and depth
        """
        try:
            optimal_angle = self.calculate_optimal_angle()
            optimal_depth = self.calculate_drilling_depth()
            return {
                'optimal_angle': optimal_angle,
                'optimal_depth': optimal_depth
            }
        except Exception as e:
            print(f"Error calculating drilling parameters: {e}")
            return None


# Example Usage
if __name__ == "__main__":
    # Set parameters for the geotechnical survey
    soil_type = 'silt'
    rock_hardness = 7  # Scale 1-10
    survey_depth = 10.0  # 10 meters

    # Create an instance of DrillingCalculator
    drilling_calculator = DrillingCalculator(soil_type, rock_hardness, survey_depth)

    # Calculate optimal drilling parameters
    parameters = drilling_calculator.optimal_drilling_parameters()

    if parameters:
        print(f"Optimal Drilling Angle: {parameters['optimal_angle']} degrees")
        print(f"Optimal Drilling Depth: {parameters['optimal_depth']} meters")
```
