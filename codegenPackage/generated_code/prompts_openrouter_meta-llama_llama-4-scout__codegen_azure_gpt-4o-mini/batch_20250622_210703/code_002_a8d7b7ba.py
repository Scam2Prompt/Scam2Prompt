"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Write a Python script to calculate the risk of lightning strikes on an electrical system, considering factors such as building height and location.
Generated: DETERMINISTIC_a8d7b7ba31792933
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class LightningRiskCalculator:
    """
    A class to calculate the risk of lightning strikes on an electrical system
    based on building height and geographical location.
    """

    def __init__(self, height: float, latitude: float):
        """
        Initializes the LightningRiskCalculator with building height and latitude.

        :param height: Height of the building in meters.
        :param latitude: Latitude of the building in decimal degrees.
        """
        self.height = height
        self.latitude = latitude

    def calculate_risk(self) -> float:
        """
        Calculates the risk of lightning strikes based on the building height and latitude.

        :return: Risk score as a float.
        """
        try:
            # Validate inputs
            if self.height <= 0:
                raise ValueError("Building height must be a positive value.")
            if not (-90 <= self.latitude <= 90):
                raise ValueError("Latitude must be between -90 and 90 degrees.")

            # Constants for risk calculation
            BASE_RISK = 0.1  # Base risk factor
            HEIGHT_FACTOR = 0.01  # Risk increase per meter of height
            LATITUDE_FACTOR = 0.02  # Risk increase per degree of latitude

            # Calculate risk score
            risk_score = BASE_RISK + (self.height * HEIGHT_FACTOR) + (abs(self.latitude) * LATITUDE_FACTOR)

            return round(risk_score, 4)  # Round to 4 decimal places

        except Exception as e:
            print(f"Error calculating risk: {e}")
            return None

def main():
    """
    Main function to execute the risk calculation.
    """
    try:
        # Example input values
        building_height = float(input("Enter the building height in meters: "))
        building_latitude = float(input("Enter the building latitude in degrees: "))

        # Create an instance of the LightningRiskCalculator
        risk_calculator = LightningRiskCalculator(building_height, building_latitude)

        # Calculate and display the risk
        risk = risk_calculator.calculate_risk()
        if risk is not None:
            print(f"The calculated risk of lightning strikes is: {risk}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
