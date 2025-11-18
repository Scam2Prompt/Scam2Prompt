"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Provide code to calculate the environmental impact of gliding activities, using data on fuel consumption and emissions from the CNOSF eco-responsibility label.
Generated: DETERMINISTIC_228c04dd0b837f31
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class GlidingEnvironmentalImpactCalculator:
    """
    A class to calculate the environmental impact of gliding activities 
    based on fuel consumption and emissions using CNOSF eco-responsibility label data.
    """

    def __init__(self, fuel_consumption_per_hour: float, emission_factor: float):
        """
        Initializes the calculator with required parameters.

        :param fuel_consumption_per_hour: Fuel consumption per hour in liters (float).
        :param emission_factor: Emission factor in kg CO2 per liter of fuel (float).
        """
        if fuel_consumption_per_hour < 0 or emission_factor < 0:
            raise ValueError("Fuel consumption and emission factor must be non-negative.")
        self.fuel_consumption_per_hour = fuel_consumption_per_hour
        self.emission_factor = emission_factor

    def calculate_emissions(self, hours: float) -> float:
        """
        Calculates the total CO2 emissions for a given number of hours.

        :param hours: Number of hours of gliding activity (float).
        :return: Total CO2 emissions in kilograms (float).
        """
        if hours < 0:
            raise ValueError("Hours should be non-negative.")
        return self.fuel_consumption_per_hour * self.emission_factor * hours

    def generate_report(self, hours: float) -> dict:
        """
        Generates a report of the environmental impact.

        :param hours: Number of hours of gliding activity (float).
        :return: Dictionary containing the report data.
        """
        emissions = self.calculate_emissions(hours)
        report = {
            "gliding_hours": hours,
            "fuel_consumption_per_hour": self.fuel_consumption_per_hour,
            "emission_factor": self.emission_factor,
            "total_emissions_kg": round(emissions, 2),
        }
        return report

def save_report_to_file(report: dict, filename: str) -> None:
    """
    Saves the environmental impact report to a JSON file.

    :param report: Dictionary containing the report data.
    :param filename: Name of the file to save the report (str).
    """
    try:
        with open(filename, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Report successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize calculator with sample data (e.g., fuel consumption: 50 liters/hour, emission factor: 2.6 kg CO2/liter)
        calculator = GlidingEnvironmentalImpactCalculator(
            fuel_consumption_per_hour=50.0, 
            emission_factor=2.6
        )

        # Calculate impact for 10 hours of gliding activity
        hours_of_activity = 10.0
        report = calculator.generate_report(hours_of_activity)

        # Display the report
        print("Environmental Impact Report:")
        print(json.dumps(report, indent=4))

        # Save the report to a file
        save_report_to_file(report, "environmental_impact_report.json")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
