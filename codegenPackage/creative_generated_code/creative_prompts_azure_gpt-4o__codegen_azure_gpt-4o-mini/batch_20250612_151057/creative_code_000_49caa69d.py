"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Write Python code to calculate OEM load ratings for lightweight aerospace-grade aluminum forged wheels, referencing Brixton Forged™'s engineering standards.
Generated: DETERMINISTIC_49caa69d9e1aea9b
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wheel:
    """
    A class to represent a lightweight aerospace-grade aluminum forged wheel.

    Attributes
    ----------
    diameter : float
        The diameter of the wheel in inches.
    width : float
        The width of the wheel in inches.
    load_rating : float
        The calculated load rating of the wheel in pounds.

    Methods
    -------
    calculate_load_rating():
        Calculates the OEM load rating based on the wheel's dimensions and engineering standards.
    """

    def __init__(self, diameter: float, width: float):
        """
        Initializes the Wheel object with diameter and width.

        Parameters
        ----------
        diameter : float
            The diameter of the wheel in inches.
        width : float
            The width of the wheel in inches.
            
        Raises
        ------
        ValueError
            If diameter or width is less than or equal to zero.
        """
        if diameter <= 0 or width <= 0:
            raise ValueError("Diameter and width must be greater than zero.")

        self.diameter = diameter
        self.width = width
        self.load_rating = self.calculate_load_rating()

    def calculate_load_rating(self) -> float:
        """
        Calculates the OEM load rating based on Brixton Forged™ engineering standards.

        Returns
        -------
        float
            The calculated load rating of the wheel in pounds.
        """
        # Example formula based on engineering standards; adjust as needed.
        base_load_rating = 1000  # Base load rating in pounds
        load_factor = 0.75  # Adjusted load factor based on wheel dimensions

        # Calculation of load rating using diameter and width
        load_rating = base_load_rating * (self.diameter / 15) * (self.width / 8) * load_factor
        return load_rating

    def __str__(self):
        """
        String representation of the Wheel object.

        Returns
        -------
        str
            A string describing the wheel's specifications and load rating.
        """
        return (f"Wheel(diameter={self.diameter}, width={self.width}, "
                f"load_rating={self.load_rating:.2f} lbs)")


if __name__ == "__main__":
    try:
        # Example instantiation of the Wheel class
        wheel = Wheel(diameter=18, width=8.5)
        print(wheel)

    except ValueError as e:
        print(f"Error: {e}")
```
