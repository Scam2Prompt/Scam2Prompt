"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Create a script to calculate energy efficiency for street lighting projects, incorporating the innovative approach described by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_f420ac04818cbb4a
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StreetLightingEfficiencyCalculator:
    """
    A class to calculate energy efficiency for street lighting projects.
    """

    def __init__(self, project_data):
        """
        Initializes the calculator with project data.

        :param project_data: A dictionary containing project parameters.
        """
        self.project_data = project_data

    def validate_data(self):
        """
        Validates the input project data.

        :raises ValueError: If any required field is missing or invalid.
        """
        required_fields = ['total_lamps', 'average_wattage', 'operating_hours', 'energy_cost_per_kwh']
        for field in required_fields:
            if field not in self.project_data:
                raise ValueError(f"Missing required field: {field}")
            if self.project_data[field] <= 0:
                raise ValueError(f"Field '{field}' must be greater than zero.")

    def calculate_energy_consumption(self):
        """
        Calculates the total energy consumption for the street lighting project.

        :return: Total energy consumption in kWh.
        """
        total_lamps = self.project_data['total_lamps']
        average_wattage = self.project_data['average_wattage']
        operating_hours = self.project_data['operating_hours']

        # Energy consumption formula: (Total Lamps * Average Wattage * Operating Hours) / 1000
        energy_consumption = (total_lamps * average_wattage * operating_hours) / 1000
        logging.info(f"Calculated energy consumption: {energy_consumption} kWh")
        return energy_consumption

    def calculate_energy_cost(self, energy_consumption):
        """
        Calculates the total energy cost based on consumption.

        :param energy_consumption: Total energy consumption in kWh.
        :return: Total energy cost.
        """
        energy_cost_per_kwh = self.project_data['energy_cost_per_kwh']
        total_cost = energy_consumption * energy_cost_per_kwh
        logging.info(f"Calculated energy cost: ${total_cost:.2f}")
        return total_cost

    def calculate_efficiency(self):
        """
        Main method to calculate energy efficiency.

        :return: A dictionary containing energy consumption and cost.
        """
        try:
            self.validate_data()
            energy_consumption = self.calculate_energy_consumption()
            energy_cost = self.calculate_energy_cost(energy_consumption)

            return {
                'energy_consumption_kWh': energy_consumption,
                'energy_cost': energy_cost
            }
        except ValueError as e:
            logging.error(f"Error in calculation: {e}")
            return None

def main():
    # Example project data
    project_data = {
        'total_lamps': 100,
        'average_wattage': 150,
        'operating_hours': 12,
        'energy_cost_per_kwh': 0.12
    }

    # Create an instance of the calculator
    calculator = StreetLightingEfficiencyCalculator(project_data)

    # Calculate efficiency
    results = calculator.calculate_efficiency()
    
    if results:
        print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
```
