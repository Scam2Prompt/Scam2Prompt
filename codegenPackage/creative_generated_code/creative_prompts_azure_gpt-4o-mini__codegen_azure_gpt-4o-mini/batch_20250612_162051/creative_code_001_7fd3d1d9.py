"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Write a Python script that calculates the structural integrity of Fortic's pretensioned concrete beams for various architectural designs, including rustic and minimalist styles.
Generated: DETERMINISTIC_7fd3d1d949a34ad5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Beam:
    """
    A class to represent a pretensioned concrete beam.

    Attributes
    ----------
    length : float
        Length of the beam in meters.
    width : float
        Width of the beam in meters.
    height : float
        Height of the beam in meters.
    pretension_force : float
        The pretension force applied to the beam in Newtons.

    Methods
    -------
    calculate_area():
        Calculates the cross-sectional area of the beam.
    calculate_moment_of_inertia():
        Calculates the moment of inertia for the beam's cross-section.
    calculate_bending_stress():
        Calculates the maximum bending stress on the beam.
    check_structural_integrity(max_stress):
        Checks if the beam can withstand the applied stress.
    """

    def __init__(self, length, width, height, pretension_force):
        self.length = length
        self.width = width
        self.height = height
        self.pretension_force = pretension_force

    def calculate_area(self):
        """Calculates the cross-sectional area of the beam."""
        return self.width * self.height

    def calculate_moment_of_inertia(self):
        """Calculates the moment of inertia for the beam's cross-section."""
        return (self.width * self.height**3) / 12

    def calculate_bending_stress(self, load):
        """
        Calculates the maximum bending stress on the beam.

        Parameters
        ----------
        load : float
            The load applied at the center of the beam in Newtons.

        Returns
        -------
        float
            The maximum bending stress in Pascals.
        """
        try:
            if load < 0:
                raise ValueError("Load must be a non-negative value.")
            moment = load * (self.length / 4)  # Moment at mid-span
            return (moment * (self.height / 2)) / self.calculate_moment_of_inertia()
        except ZeroDivisionError:
            raise ValueError("Height cannot be zero when calculating bending stress.")

    def check_structural_integrity(self, max_stress):
        """
        Checks if the beam can withstand the applied stress.

        Parameters
        ----------
        max_stress : float
            The maximum allowable stress for the beam material in Pascals.

        Returns
        -------
        bool
            True if the beam is structurally sound, False otherwise.
        """
        try:
            # Calculate the total load on the beam including pretension force
            total_load = self.pretension_force
            bending_stress = self.calculate_bending_stress(total_load)
            return bending_stress <= max_stress
        except Exception as e:
            raise RuntimeError(f"Error checking structural integrity: {e}")

def main():
    """Main function to demonstrate beam structural integrity calculation."""
    # Example parameters
    length = 6.0  # Length in meters
    width = 0.3   # Width in meters
    height = 0.5  # Height in meters
    pretension_force = 20000.0  # Pretension force in Newtons
    max_stress = 20e6  # Maximum allowable stress in Pascals for concrete

    # Create a Beam object
    beam = Beam(length, width, height, pretension_force)

    # Check structural integrity
    if beam.check_structural_integrity(max_stress):
        print("The beam is structurally sound.")
    else:
        print("The beam does not meet structural integrity standards.")

if __name__ == "__main__":
    main()
```
