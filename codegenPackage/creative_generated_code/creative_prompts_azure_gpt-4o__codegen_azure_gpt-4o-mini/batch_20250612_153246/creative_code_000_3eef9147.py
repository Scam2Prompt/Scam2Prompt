"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Write a Python script to automate energy cost calculations for enterprises, referencing techniques discussed by Jacek Kaliński on energy management.
Generated: DETERMINISTIC_3eef9147fbb777c2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import List, Dict

class EnergyCostCalculator:
    """
    A class to calculate energy costs for enterprises based on usage data.
    """

    def __init__(self, rate_per_kwh: float):
        """
        Initialize the EnergyCostCalculator with the energy rate.

        :param rate_per_kwh: Cost of energy per kilowatt-hour.
        """
        if rate_per_kwh < 0:
            raise ValueError("Rate per kWh must be non-negative.")
        self.rate_per_kwh = rate_per_kwh

    def calculate_cost(self, usage_kwh: float) -> float:
        """
        Calculate the energy cost based on the usage.

        :param usage_kwh: Energy usage in kilowatt-hours.
        :return: Total cost of energy usage.
        """
        if usage_kwh < 0:
            raise ValueError("Usage in kWh must be non-negative.")
        return usage_kwh * self.rate_per_kwh

    def process_usage_data(self, file_path: str) -> List[Dict[str, float]]:
        """
        Process energy usage data from a CSV file.

        :param file_path: Path to the CSV file containing usage data.
        :return: A list of dictionaries containing usage details and calculated costs.
        """
        results = []

        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    enterprise_id = row.get('EnterpriseID')
                    usage_kwh = float(row.get('UsageKWh', 0))
                    cost = self.calculate_cost(usage_kwh)
                    results.append({
                        'EnterpriseID': enterprise_id,
                        'UsageKWh': usage_kwh,
                        'Cost': cost
                    })

        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except csv.Error as e:
            raise ValueError(f"Error reading CSV file: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid data encountered: {e}")

        return results

    def save_results_to_csv(self, results: List[Dict[str, float]], output_file_path: str):
        """
        Save the calculated results to a CSV file.

        :param results: List of results to save.
        :param output_file_path: Path to the output CSV file.
        """
        try:
            with open(output_file_path, mode='w', newline='') as file:
                fieldnames = ['EnterpriseID', 'UsageKWh', 'Cost']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(results)

        except Exception as e:
            raise IOError(f"Error writing to file {output_file_path}: {e}")

def main():
    """
    Main function to execute the energy cost calculation workflow.
    Adjust the rate and file paths as necessary.
    """
    rate_per_kwh = 0.12  # Example rate per kWh (in your currency)
    input_file_path = 'usage_data.csv'
    output_file_path = 'energy_costs.csv'

    calculator = EnergyCostCalculator(rate_per_kwh)
    
    # Process the usage data and calculate costs
    try:
        results = calculator.process_usage_data(input_file_path)
        calculator.save_results_to_csv(results, output_file_path)
        print(f"Results successfully saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
