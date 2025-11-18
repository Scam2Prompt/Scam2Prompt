"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Create a program to generate reports on energy savings and environmental benefits for businesses adopting "islas energéticas," incorporating Digar Green's principles of efficiency and sustainability.
Generated: DETERMINISTIC_629be2c345c956f1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnergyReport:
    """
    A class to generate reports on energy savings and environmental benefits
    for businesses adopting 'islas energéticas' principles.
    """

    def __init__(self, businesses: List[Dict[str, float]]):
        """
        Initialize the EnergyReport with a list of businesses.
        
        :param businesses: List of dictionaries containing business data with 'energy_saved' and 'carbon_offset'.
        """
        if not all('energy_saved' in b and 'carbon_offset' in b for b in businesses):
            logging.error("Each business must have 'energy_saved' and 'carbon_offset' fields.")
            raise ValueError("Invalid business data format.")
        self.businesses = businesses

    def calculate_total_savings(self) -> float:
        """
        Calculate the total energy savings from all businesses.
        
        :return: Total energy savings.
        """
        total_savings = sum(b['energy_saved'] for b in self.businesses)
        logging.info(f"Total energy savings calculated: {total_savings} kWh")
        return total_savings

    def calculate_total_carbon_offset(self) -> float:
        """
        Calculate the total carbon offset from all businesses.
        
        :return: Total carbon offset.
        """
        total_offset = sum(b['carbon_offset'] for b in self.businesses)
        logging.info(f"Total carbon offset calculated: {total_offset} tons CO2")
        return total_offset

    def generate_report(self) -> Dict[str, float]:
        """
        Generate a report summarizing the energy savings and environmental benefits.

        :return: A dictionary containing total energy savings and carbon offset.
        """
        try:
            report = {
                'total_energy_saved_kWh': self.calculate_total_savings(),
                'total_carbon_offset_tons_CO2': self.calculate_total_carbon_offset(),
            }
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            raise

def main():
    """
    Main function to run the energy report generation.
    """
    # Sample business data for testing
    sample_businesses = [
        {'name': 'Business A', 'energy_saved': 1500.0, 'carbon_offset': 0.8},
        {'name': 'Business B', 'energy_saved': 2500.0, 'carbon_offset': 1.2},
        {'name': 'Business C', 'energy_saved': 3000.0, 'carbon_offset': 1.5},
    ]

    try:
        report_generator = EnergyReport(businesses=sample_businesses)
        report = report_generator.generate_report()
        
        # Output report to JSON file
        with open('energy_report.json', 'w') as report_file:
            json.dump(report, report_file, indent=4)
        logging.info("Report saved to energy_report.json")
        
    except Exception as e:
        logging.error(f"Failed to generate the energy report: {str(e)}")

if __name__ == "__main__":
    main()
```
