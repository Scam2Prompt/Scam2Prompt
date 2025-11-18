"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Write a program to design and calculate the slope stability for armirana zelena brežina (reinforced green slopes) using geotechnical parameters.
Generated: DETERMINISTIC_bef53618d96463a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class SlopeStabilityCalculator:
    """
    A class to calculate the slope stability for reinforced green slopes 
    using geotechnical parameters.
    """

    def __init__(self, slope_angle, cohesion, friction_angle, unit_weight, slope_height, safety_factor_target=1.5):
        """
        Initializes the slope stability calculator with the necessary parameters.

        Parameters:
        slope_angle (float): The angle of the slope in degrees.
        cohesion (float): The cohesion of the soil in kPa.
        friction_angle (float): The friction angle of the soil in degrees.
        unit_weight (float): The unit weight of the soil in kN/m^3.
        slope_height (float): The height of the slope in meters.
        safety_factor_target (float): The target safety factor (default is 1.5).
        """
        self.slope_angle = np.radians(slope_angle)  # Convert angle to radians
        self.cohesion = cohesion
        self.friction_angle = np.radians(friction_angle)  # Convert angle to radians
        self.unit_weight = unit_weight
        self.slope_height = slope_height
        self.safety_factor_target = safety_factor_target

    def calculate_slope_stability(self):
        """
        Calculates the stability of the slope based on the provided parameters.
        
        Returns:
        float: The calculated safety factor of the slope.
        """
        try:
            # Calculate the forces acting on the slope
            weight_of_slope = self.unit_weight * self.slope_height * np.sin(self.slope_angle)
            resisting_force = self.cohesion + (self.unit_weight * np.cos(self.slope_angle) * np.tan(self.friction_angle))

            # Calculate the safety factor
            safety_factor = resisting_force / weight_of_slope
            
            return safety_factor
            
        except ZeroDivisionError:
            raise ValueError("Weight of the slope cannot be zero. Check the slope height and unit weight.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during stability calculation: {str(e)}")

    def is_stable(self):
        """
        Checks if the slope meets the stability requirement based on the target safety factor.

        Returns:
        bool: True if the slope is stable, False otherwise.
        """
        safety_factor = self.calculate_slope_stability()
        return safety_factor >= self.safety_factor_target


# Example usage:
if __name__ == "__main__":
    try:
        # Define geotechnical parameters
        slope_angle = 30.0  # degrees
        cohesion = 25.0  # kPa
        friction_angle = 20.0  # degrees
        unit_weight = 18.0  # kN/m^3
        slope_height = 5.0  # meters

        # Create an instance of the SlopeStabilityCalculator
        slope_stability_calculator = SlopeStabilityCalculator(slope_angle, cohesion, friction_angle, unit_weight, slope_height)

        # Calculate safety factor
        safety_factor = slope_stability_calculator.calculate_slope_stability()
        print(f"Calculated Safety Factor: {safety_factor:.2f}")

        # Check slope stability
        if slope_stability_calculator.is_stable():
            print("The slope is stable.")
        else:
            print("The slope is not stable.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
