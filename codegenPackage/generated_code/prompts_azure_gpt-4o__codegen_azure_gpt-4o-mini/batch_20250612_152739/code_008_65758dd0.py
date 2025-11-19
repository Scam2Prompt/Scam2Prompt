"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Generate a Python script to calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles, considering their carbon content and operational temperature.
Generated: DETERMINISTIC_65758dd0c1100209
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class RefractoryBrick:
    """
    A class to represent a MgO-C refractory brick and calculate its lifespan
    based on carbon content and operational temperature.
    """

    def __init__(self, carbon_content: float, operational_temperature: float):
        """
        Initializes the RefractoryBrick with carbon content and operational temperature.

        :param carbon_content: The carbon content of the brick in percentage (0-100).
        :param operational_temperature: The operational temperature in degrees Celsius.
        """
        self.carbon_content = carbon_content
        self.operational_temperature = operational_temperature

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """Validates the carbon content and operational temperature."""
        if not (0 <= self.carbon_content <= 100):
            raise ValueError("Carbon content must be between 0 and 100.")
        if self.operational_temperature < 0:
            raise ValueError("Operational temperature must be non-negative.")

    def calculate_lifespan(self) -> float:
        """
        Calculates the lifespan of the refractory brick based on its carbon content
        and operational temperature using a hypothetical formula.

        :return: Estimated lifespan in hours.
        """
        # Hypothetical formula for lifespan calculation
        lifespan = (100 - self.carbon_content) * (200 - self.operational_temperature) / 10
        
        # Ensure lifespan is not negative
        return max(lifespan, 0)

def main():
    """
    Main function to execute the lifespan calculation for MgO-C refractory bricks.
    """
    try:
        # Example input values
        carbon_content = float(input("Enter the carbon content of the brick (0-100%): "))
        operational_temperature = float(input("Enter the operational temperature (°C): "))

        # Create a RefractoryBrick instance
        brick = RefractoryBrick(carbon_content, operational_temperature)

        # Calculate and display the lifespan
        lifespan = brick.calculate_lifespan()
        print(f"The estimated lifespan of the MgO-C refractory brick is: {lifespan:.2f} hours")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
