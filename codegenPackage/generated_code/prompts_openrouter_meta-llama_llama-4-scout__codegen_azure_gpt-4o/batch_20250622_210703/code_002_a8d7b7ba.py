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
    based on building height and location.
    """

    def __init__(self, building_height: float, location_factor: float):
        """
        Initialize the calculator with building height and location factor.

        :param building_height: Height of the building in meters.
        :param location_factor: A multiplier representing the risk based on location.
                                (e.g., 1.0 for low risk, 2.0 for moderate risk, 3.0 for high risk)
        """
        if building_height <= 0:
            raise ValueError("Building height must be greater than zero.")
        if location_factor <= 0:
            raise ValueError("Location factor must be greater than zero.")
        
        self.building_height = building_height
        self.location_factor = location_factor

    def calculate_risk(self) -> float:
        """
        Calculate the lightning strike risk score.

        :return: A risk score (higher values indicate higher risk).
        """
        # Risk formula: Risk = (Height Factor * Location Factor)
        # Height Factor is derived as log(building_height + 1) to account for diminishing returns at higher heights.
        height_factor = math.log(self.building_height + 1)
        risk_score = height_factor * self.location_factor
        return risk_score


def main():
    """
    Main function to interact with the user and calculate lightning strike risk.
    """
    print("Lightning Strike Risk Calculator")
    print("--------------------------------")

    try:
        # Get user input for building height and location factor
        building_height = float(input("Enter the building height in meters: "))
        location_factor = float(input("Enter the location factor (e.g., 1.0 for low risk, 2.0 for moderate risk, 3.0 for high risk): "))

        # Create an instance of the calculator
        calculator = LightningRiskCalculator(building_height, location_factor)

        # Calculate and display the risk score
        risk_score = calculator.calculate_risk()
        print(f"The calculated lightning strike risk score is: {risk_score:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
