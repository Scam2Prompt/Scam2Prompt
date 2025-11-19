"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Provide recommendations for designing sprinkler systems compliant with modern safety codes for one- and two-family homes, as highlighted by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_1e382ed805ef07d5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class SprinklerSystem:
    """
    A class to design sprinkler systems for one- and two-family homes.

    Attributes:
    ----------
    home_type : str
        Type of home (one-family or two-family)
    home_size : float
        Size of the home in square feet
    hazard_class : str
        Hazard class of the home (ordinary, high, or special)
    sprinkler_type : str
        Type of sprinkler (pendent, upright, or sidewall)

    Methods:
    -------
    calculate_sprinkler_density()
        Calculates the required sprinkler density
    determine_sprinkler_spacing()
        Determines the maximum sprinkler spacing
    design_sprinkler_system()
        Designs the sprinkler system
    """

    def __init__(self, home_type, home_size, hazard_class, sprinkler_type):
        """
        Initializes the SprinklerSystem class.

        Parameters:
        ----------
        home_type : str
            Type of home (one-family or two-family)
        home_size : float
            Size of the home in square feet
        hazard_class : str
            Hazard class of the home (ordinary, high, or special)
        sprinkler_type : str
            Type of sprinkler (pendent, upright, or sidewall)
        """
        self.home_type = home_type
        self.home_size = home_size
        self.hazard_class = hazard_class
        self.sprinkler_type = sprinkler_type

    def calculate_sprinkler_density(self):
        """
        Calculates the required sprinkler density based on the hazard class.

        Returns:
        -------
        float
            Required sprinkler density in gpm/ft^2
        """
        # Define hazard class densities (gpm/ft^2)
        hazard_densities = {
            'ordinary': 0.05,
            'high': 0.10,
            'special': 0.15
        }

        # Check if hazard class is valid
        if self.hazard_class not in hazard_densities:
            raise ValueError("Invalid hazard class")

        return hazard_densities[self.hazard_class]

    def determine_sprinkler_spacing(self):
        """
        Determines the maximum sprinkler spacing based on the sprinkler type.

        Returns:
        -------
        float
            Maximum sprinkler spacing in feet
        """
        # Define sprinkler spacing (ft)
        sprinkler_spacings = {
            'pendent': 15,
            'upright': 12,
            'sidewall': 10
        }

        # Check if sprinkler type is valid
        if self.sprinkler_type not in sprinkler_spacings:
            raise ValueError("Invalid sprinkler type")

        return sprinkler_spacings[self.sprinkler_type]

    def design_sprinkler_system(self):
        """
        Designs the sprinkler system.

        Returns:
        -------
        dict
            Sprinkler system design parameters
        """
        try:
            # Calculate required sprinkler density
            density = self.calculate_sprinkler_density()

            # Determine maximum sprinkler spacing
            spacing = self.determine_sprinkler_spacing()

            # Calculate total number of sprinklers
            num_sprinklers = math.ceil(self.home_size / (spacing ** 2))

            # Calculate total water flow required
            total_flow = density * self.home_size

            # Return sprinkler system design parameters
            return {
                'density': density,
                'spacing': spacing,
                'num_sprinklers': num_sprinklers,
                'total_flow': total_flow
            }

        except Exception as e:
            # Handle any exceptions
            print(f"An error occurred: {e}")
            return None


def main():
    # Example usage
    home_type = "one-family"
    home_size = 2000  # sqft
    hazard_class = "ordinary"
    sprinkler_type = "pendent"

    sprinkler_system = SprinklerSystem(home_type, home_size, hazard_class, sprinkler_type)
    design_params = sprinkler_system.design_sprinkler_system()

    if design_params:
        print("Sprinkler System Design Parameters:")
        print(f"Density: {design_params['density']} gpm/ft^2")
        print(f"Sprinkler Spacing: {design_params['spacing']} ft")
        print(f"Number of Sprinklers: {design_params['num_sprinklers']}")
        print(f"Total Water Flow: {design_params['total_flow']} gpm")


if __name__ == "__main__":
    main()
```
