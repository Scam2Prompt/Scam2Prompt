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
    """
    A class to calculate the optimal drilling angle and depth for a geotechnical survey.
    """

    def __init__(self, soil_type, target_depth, drilling_type):
        """
        Initializes the DrillingCalculator with relevant parameters.

        :param soil_type: Type of soil at the site (e.g., "rock", "sand", "clay")
        :param target_depth: Desired depth to reach during drilling (meters)
        :param drilling_type: Type of drilling work (e.g., "rotary", "percussion", "core")
        """
        self.soil_type = soil_type
        self.target_depth = target_depth
        self.drilling_type = drilling_type

    def calculate_optimal_angle(self):
        """
        Calculates the optimal angle for drilling based on soil type and drilling type.

        :return: Optimal angle in degrees
        """
        # Define default drilling angles (in degrees) for different soil and drilling types
        angle_map = {
            "rotary": {"rock": 90, "sand": 75, "clay": 70},
            "percussion": {"rock": 80, "sand": 70, "clay": 65},
            "core": {"rock": 85, "sand": 80, "clay": 75},
        }

        # Handle unknown soil or drilling types gracefully
        try:
            return angle_map[self.drilling_type][self.soil_type]
        except KeyError:
            raise ValueError("Invalid soil or drilling type. Please check your inputs.")

    def calculate_required_depth(self):
        """
        Calculates the required depth for drilling, ensuring safety margins.

        :return: Adjusted optimal depth (meters)
        """
        # Apply safety margin based on soil type
        safety_margin = {
            "rock": 1.05,  # +5%
            "sand": 1.10,  # +10%
            "clay": 1.15,  # +15%
        }

        # Handle unknown soil types gracefully
        try:
            margin = safety_margin[self.soil_type]
        except KeyError:
            raise ValueError("Invalid soil type. Please check your input.")

        # Adjust depth with safety margin
        return self.target_depth * margin

    def calculate_optimal_parameters(self):
        """
        Calculates both optimal angle and adjusted depth for drilling.

        :return: A dictionary containing optimal angle and depth
        """
        return {
            "optimal_angle": self.calculate_optimal_angle(),
            "optimal_depth": self.calculate_required_depth(),
        }


def main():
    """
    Main function to calculate drilling parameters for a geotechnical survey.
    """
    # Example inputs (these would typically come from user input or a configuration file)
    soil_type = "rock"
    target_depth = 100  # meters
    drilling_type = "rotary"

    try:
        # Initialize the calculator
        calculator = DrillingCalculator(soil_type, target_depth, drilling_type)

        # Calculate optimal parameters
        parameters = calculator.calculate_optimal_parameters()

        # Display results
        print("Optimal Drilling Parameters:")
        print(f" - Angle: {parameters['optimal_angle']} degrees")
        print(f" - Depth: {parameters['optimal_depth']} meters")

    except ValueError as e:
        # Handle input errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle all other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
