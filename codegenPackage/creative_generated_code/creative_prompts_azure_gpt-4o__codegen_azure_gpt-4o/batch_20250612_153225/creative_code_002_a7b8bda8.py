"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Create a script to simulate the reduction in CO₂ emissions achieved by using solar panels, based on the data and goals outlined by Soltec Solutions.
Generated: DETERMINISTIC_a7b8bda8a7341690
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SolarPanelCO2ReductionSimulator:
    """
    A class to simulate the CO₂ emissions reduction achieved by using solar panels.
    """
    def __init__(self, solar_panel_data_file):
        """
        Initializes the simulator with solar panel data.

        :param solar_panel_data_file: Path to the JSON file containing solar panel data.
        """
        self.solar_panel_data = self.load_solar_panel_data(solar_panel_data_file)

    def load_solar_panel_data(self, file_path):
        """
        Loads solar panel data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing solar panel data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {file_path}")

    def calculate_co2_reduction(self, electricity_usage_kwh):
        """
        Calculates the CO₂ reduction based on the electricity usage provided.

        :param electricity_usage_kwh: Annual electricity usage in kilowatt-hours (kWh).
        :return: Estimated annual CO₂ reduction in kilograms (kg).
        """
        # CO₂ emissions per kWh (in kg) based on traditional energy sources
        co2_emissions_per_kwh = self.solar_panel_data.get("co2_emissions_per_kwh", 0.7)

        # Solar panel efficiency in percentage
        solar_panel_efficiency = self.solar_panel_data.get("solar_panel_efficiency", 18)

        # Conversion of efficiency percentage to decimal
        efficiency_decimal = solar_panel_efficiency / 100

        # CO₂ reduction calculation
        co2_reduction = electricity_usage_kwh * co2_emissions_per_kwh * efficiency_decimal
        return co2_reduction

def main():
    """
    Main function to run the simulator.
    """
    # Define file path to solar panel data
    solar_panel_data_file = "solar_panel_data.json"

    # Initialize the simulator
    try:
        simulator = SolarPanelCO2ReductionSimulator(solar_panel_data_file)
    except Exception as e:
        print(f"Error initializing simulator: {e}")
        return

    # Ask user for annual electricity usage
    try:
        electricity_usage_kwh = float(input("Enter your annual electricity usage in kWh: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Calculate CO₂ reduction
    try:
        co2_reduction = simulator.calculate_co2_reduction(electricity_usage_kwh)
        print(f"Estimated annual CO₂ reduction: {co2_reduction:.2f} kg")
    except Exception as e:
        print(f"Error calculating CO₂ reduction: {e}")

if __name__ == "__main__":
    main()
```

### Required Example JSON File (`solar_panel_data.json`):
```json
{
  "co2_emissions_per_kwh": 0.7,
  "solar_panel_efficiency": 18
}
```
