"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Generate code in Python to calculate tunnel stability using geotechnical parameters such as rock density, stress distribution, and excavation depth, which align with the underground construction services offered by URANPRES.
Generated: DETERMINISTIC_f5f5bb70f657fbb2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math

class TunnelStabilityCalculator:
    """
    A class to calculate tunnel stability using geotechnical parameters.
    Parameters include rock density, stress distribution, and excavation depth.
    """

    def __init__(self, rock_density, stress_distribution, excavation_depth):
        """
        Initialize the calculator with provided geotechnical parameters.
        
        :param rock_density: Density of the rock in kg/m³
        :param stress_distribution: Stress distribution in the rock in MPa
        :param excavation_depth: Depth of excavation in meters
        """
        self.rock_density = rock_density
        self.stress_distribution = stress_distribution
        self.excavation_depth = excavation_depth

    def calculate_stability_index(self):
        """
        Calculate the stability index for the tunnel based on geotechnical parameters.
        
        :return: Stability index as a float value
        """
        try:
            # Gravitational acceleration constant (m/s²)
            GRAVITY = 9.81
            
            # Convert stress distribution from MPa to Pascals (1 MPa = 1e6 Pa)
            stress_distribution_pa = self.stress_distribution * 1e6
            
            # Calculate overburden pressure (rock density * gravity * excavation depth)
            overburden_pressure = self.rock_density * GRAVITY * self.excavation_depth
            
            # Calculate stability index (stress distribution / overburden pressure)
            stability_index = stress_distribution_pa / overburden_pressure
            
            return stability_index
        except ZeroDivisionError:
            # Handle division by zero if overburden pressure is zero
            raise ValueError("Overburden pressure cannot be zero. Check the input parameters.")
        except Exception as e:
            # Handle unexpected errors gracefully
            raise RuntimeError(f"An error occurred while calculating stability index: {str(e)}")

    def determine_stability_category(self, stability_index):
        """
        Determine the stability category based on the calculated stability index.
        
        :param stability_index: Calculated stability index
        :return: Stability category as a string
        """
        try:
            if stability_index > 2.0:
                return "Stable"
            elif 1.0 <= stability_index <= 2.0:
                return "Moderately Stable"
            else:
                return "Unstable"
        except Exception as e:
            # Handle unexpected errors gracefully
            raise RuntimeError(f"An error occurred while determining stability category: {str(e)}")
        

def main():
    """
    Main function to demonstrate tunnel stability calculation.
    """
    try:
        # Example input parameters (customize as needed)
        rock_density = 2500  # kg/m³
        stress_distribution = 15  # MPa
        excavation_depth = 500  # meters

        # Instantiate the TunnelStabilityCalculator with input parameters
        calculator = TunnelStabilityCalculator(rock_density, stress_distribution, excavation_depth)

        # Calculate the stability index
        stability_index = calculator.calculate_stability_index()

        # Determine stability category
        stability_category = calculator.determine_stability_category(stability_index)

        # Display results
        print(f"Stability Index: {stability_index:.2f}")
        print(f"Stability Category: {stability_category}")

    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except RuntimeError as re:
        print(f"Runtime Error: {str(re)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
