"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Write code to calculate the load-bearing capacity of pretensioned concrete beams that imitate wood, referencing Fortic's technical specifications for rustic, minimalist, and garden designs.
Generated: DETERMINISTIC_a51185aa258afa5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PretensionedConcreteBeam:
    """
    A class to represent a pretensioned concrete beam and calculate its load-bearing capacity.

    Attributes:
    ----------
    width : float
        The width of the beam (in meters).
    height : float
        The height of the beam (in meters).
    length : float
        The length of the beam (in meters).
    fck : float
        The characteristic compressive strength of concrete (in MPa).
    fyt : float
        The yield strength of the prestressing steel (in MPa).
    safety_factor : float
        The safety factor for structural design.

    Methods:
    -------
    calculate_load_bearing_capacity():
        Computes the load-bearing capacity of the beam based on its properties.
    """

    def __init__(self, width, height, length, fck, fyt, safety_factor=1.5):
        """
        Initializes the PretensionedConcreteBeam with dimensions and material properties.

        Parameters:
        ----------
        width : float
            Width of the beam.
        height : float
            Height of the beam.
        length : float
            Length of the beam.
        fck : float
            Characteristic compressive strength of concrete.
        fyt : float
            Yield strength of prestressing steel.
        safety_factor : float, optional
            Safety factor (default is 1.5).
        """
        self.width = width
        self.height = height
        self.length = length
        self.fck = fck
        self.fyt = fyt
        self.safety_factor = safety_factor

    def calculate_load_bearing_capacity(self):
        """
        Calculates the load-bearing capacity of the beam.

        Returns:
        -------
        float
            The load-bearing capacity of the beam (in kN).
        """
        try:
            # Calculate the effective depth of the beam
            effective_depth = self.height * 0.85  # Assuming 85% of height is effective for bending
            # Calculate the area of the beam's cross-section
            cross_sectional_area = self.width * self.height

            # Calculate the moment of inertia for the beam (rectangular section)
            moment_of_inertia = (self.width * (self.height ** 3)) / 12

            # Calculate the compressive strength in kN
            compressive_strength = (self.fck * cross_sectional_area) / 1000  # Convert to kN

            # Calculate the tensile strength of prestressing steel
            tensile_strength = (self.fyt * cross_sectional_area) / 1000  # Convert to kN

            # Calculate the design load-bearing capacity
            load_bearing_capacity = (compressive_strength + tensile_strength) / self.safety_factor

            return load_bearing_capacity

        except ZeroDivisionError as e:
            print("Error: Division by zero. Please check the beam dimensions and safety factor.")
            raise e
        except Exception as e:
            print(f"An error occurred while calculating the load-bearing capacity: {e}")
            raise e


# Example usage
if __name__ == "__main__":
    # Define beam properties based on Fortic's technical specifications
    beam = PretensionedConcreteBeam(width=0.3, height=0.5, length=6.0, fck=40, fyt=500)

    try:
        capacity = beam.calculate_load_bearing_capacity()
        print(f"The load-bearing capacity of the pretensioned concrete beam is: {capacity:.2f} kN")
    except Exception as e:
        print("Unable to calculate load-bearing capacity:", e)
```
