"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Create a program to generate reports on energy savings and environmental benefits for businesses adopting "islas energéticas," incorporating Digar Green's principles of efficiency and sustainability.
Generated: DETERMINISTIC_629be2c345c956f1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class EnergyIslandReportGenerator:
    """
    A class to generate reports on energy savings and environmental benefits
    for businesses adopting "islas energéticas" based on Digar Green's principles.
    """

    def __init__(self, config_file: str = "config.json"):
        """
        Initialize the report generator with configuration.

        Args:
            config_file: Path to the configuration file (default: config.json)
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file {config_file}.")

        # Validate required configuration
        required_keys = ['energy_conversion_factors', 'default_parameters']
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")

    def calculate_savings(self, input_data: Dict) -> Dict:
        """
        Calculate energy savings and environmental benefits based on input data.

        Args:
            input_data: Dictionary containing input parameters including:
                - current_energy_consumption (float): Current energy consumption in kWh
                - energy_island_capacity (float): Energy island capacity in kW
                - operational_hours (float): Annual operational hours
                - region (str): Region for emission factors

        Returns:
            Dictionary containing calculated savings and benefits
        """
        try:
            # Validate input data
            required_fields = [
                'current_energy_consumption',
                'energy_island_capacity',
                'operational_hours',
                'region'
            ]
            for field in required_fields:
                if field not in input_data:
                    raise ValueError(f"Missing required field in input data: {field}")

            # Get conversion factors
            conversion_factors = self.config['energy_conversion_factors']
            if input_data['region'] not in conversion_factors['emission_factors']:
                raise ValueError(f"Region {input_data['region']} not found in emission factors")

            # Calculate energy production from island
            energy_produced = (
                input_data['energy_island_capacity'] * 
                input_data['operational_hours']
            )

            # Calculate energy savings
            energy_savings = min(
                input_data['current_energy_consumption'],
                energy_produced
            )

            # Calculate cost savings
            electricity_price = self.config['default_parameters'].get(
                'electricity_price', 0.12  # default $0.12/kWh
            )
            cost_savings = energy_savings * electricity_price

            # Calculate environmental benefits
            emission_factor = conversion_factors['emission_factors'][input_data['region']]
            co2_reduction = energy_savings * emission_factor

            # Calculate equivalent environmental benefits
            trees_planted_equivalent = co2_reduction / conversion_factors['co2_per_tree']
            cars_off_road_equivalent = co2_reduction / conversion_factors['co2_per_car']

            return {
                'energy_produced_kwh': round(energy_produced, 2),
                'energy_savings_kwh': round(energy_savings, 2),
                'cost_savings_usd': round(cost_savings, 2),
                'co2_reduction_kg': round(co2_reduction, 2),
                'trees_planted_equivalent': round(trees_planted_equivalent, 2),
                'cars_off_road_equivalent': round(cars_off_road_equivalent, 2),
                'calculation_date': datetime.now().isoformat()
            }

        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid input data: {str(e)}")

    def generate_report(self, input_data: Dict, output_format: str = "json") -> str:
        """
        Generate a report in the specified format.

        Args:
            input_data: Dictionary containing input parameters
            output_format: Output format ('json', 'csv', or 'text')

        Returns:
            Report in the requested format
        """
        try:
            results = self.calculate_savings(input_data)

            if output_format == "json":
                return json.dumps(results, indent=2)
            elif output_format == "csv":
                output = []
                headers = list(results.keys())
                values = list(results.values())
                output.append(",".join(headers))
                output.append(",".join(map(str, values)))
                return "\n".join(output)
            elif output_format == "text":
                report = [
                    "Energy Island Savings Report",
                    "--------------------------------",
                    f"Energy Produced: {results['energy_produced_kwh']} kWh",
                    f"Energy Savings: {results['energy_savings_kwh']} kWh",
                    f"Cost Savings: ${results['cost_savings_usd']} USD",
                    f"CO2 Reduction: {results['co2_reduction_kg']} kg",
                    f"Equivalent to planting {results['trees_planted_equivalent']} trees",
                    f"Equivalent to taking {results['cars_off_road_equivalent']} cars off the road",
                    f"Report generated on: {results['calculation_date']}",
                    "Based on Digar Green's principles of efficiency and sustainability"
                ]
                return "\n".join(report)
            else:
                raise ValueError(f"Unsupported output format: {output_format}")

        except Exception as e:
            raise RuntimeError(f"Failed to generate report: {str(e)}")

    def generate_report_to_file(self, input_data: Dict, output_file: str) -> None:
        """
        Generate a report and save it to a file.

        Args:
            input_data: Dictionary containing input parameters
            output_file: Path to the output file (extension determines format)
        """
        try:
            format_map = {
                '.json': 'json',
                '.csv': 'csv',
                '.txt': 'text'
            }

            file_extension = output_file[output_file.rfind('.'):].lower()
            if file_extension not in format_map:
                raise ValueError(f"Unsupported file extension: {file_extension}")

            report = self.generate_report(input_data, format_map[file_extension])

            with open(output_file, 'w') as f:
                f.write(report)

        except Exception as e:
            raise RuntimeError(f"Failed to save report to file: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize report generator
        generator = EnergyIslandReportGenerator()

        # Example input data
        input_data = {
            "current_energy_consumption": 50000,  # kWh
            "energy_island_capacity": 10,         # kW
            "operational_hours": 3000,           # hours/year
            "region": "north_america"
        }

        # Generate and print JSON report
        print("JSON Report:")
        print(generator.generate_report(input_data, "json"))

        # Generate and print text report
        print("\nText Report:")
        print(generator.generate_report(input_data, "text"))

        # Save report to file
        generator.generate_report_to_file(input_data, "energy_savings_report.json")

    except Exception as e:
        print(f"Error: {str(e)}")
```
