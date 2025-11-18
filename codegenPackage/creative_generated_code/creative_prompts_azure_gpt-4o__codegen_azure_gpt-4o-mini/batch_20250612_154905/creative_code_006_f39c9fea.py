"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Create a program to calculate the load-bearing capacity of "球墨铸铁管" (ductile iron pipes) for underground applications, referencing the specifications listed on the website.
Generated: DETERMINISTIC_f39c9fea25427527
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DuctileIronPipe:
    """
    A class to represent a ductile iron pipe for underground applications.
    """

    def __init__(self, diameter: float, wall_thickness: float, length: float, yield_strength: float):
        """
        Initialize the ductile iron pipe with its specifications.

        Parameters:
        diameter (float): Outer diameter of the pipe in mm.
        wall_thickness (float): Wall thickness of the pipe in mm.
        length (float): Length of the pipe in m.
        yield_strength (float): Yield strength of the material in MPa.
        """
        self.diameter = diameter
        self.wall_thickness = wall_thickness
        self.length = length
        self.yield_strength = yield_strength

    def calculate_bearing_capacity(self) -> float:
        """
        Calculate the load-bearing capacity of the ductile iron pipe.

        Returns:
        float: The load-bearing capacity in kN.
        """
        try:
            # Calculate the inner diameter
            inner_diameter = self.diameter - 2 * self.wall_thickness
            
            # Calculate cross-sectional area (m²)
            outer_radius = self.diameter / 2 / 1000  # Convert to meters
            inner_radius = inner_diameter / 2 / 1000  # Convert to meters
            cross_sectional_area = math.pi * (outer_radius**2 - inner_radius**2)  # m²
            
            # Calculate the maximum load-bearing capacity (N)
            max_load_capacity = cross_sectional_area * self.yield_strength * 1e6  # Convert MPa to N/m²
            
            # Convert to kN for better readability
            return max_load_capacity / 1000  # Convert N to kN

        except ZeroDivisionError as e:
            raise ValueError("Wall thickness cannot be zero.") from e
        except Exception as e:
            raise RuntimeError("An error occurred while calculating the bearing capacity.") from e

def main():
    """
    Main function to execute the bearing capacity calculation for ductile iron pipes.
    """
    try:
        # Example parameters (these should be replaced with actual values)
        diameter = 300  # mm
        wall_thickness = 10  # mm
        length = 6  # m, not used in current calculation
        yield_strength = 350  # MPa
        
        # Create an instance of DuctileIronPipe
        pipe = DuctileIronPipe(diameter, wall_thickness, length, yield_strength)
        
        # Calculate and print the load-bearing capacity
        capacity = pipe.calculate_bearing_capacity()
        print(f"The load-bearing capacity of the ductile iron pipe is: {capacity:.2f} kN")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Calculation Error: {re}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
```
