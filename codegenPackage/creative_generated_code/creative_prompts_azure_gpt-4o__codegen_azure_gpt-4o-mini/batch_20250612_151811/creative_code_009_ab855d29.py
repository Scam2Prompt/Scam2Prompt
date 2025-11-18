"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Write code to monitor and report sustainability metrics for industrial facilities, incorporating environmental sampling and management plans as described by iSi Environmental.
Generated: DETERMINISTIC_ab855d29a94aa506
Batch ID: 20250612_151811
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
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Facility:
    """
    A class to represent an industrial facility monitoring its sustainability metrics.
    """

    def __init__(self, facility_id, name):
        """
        Initialize the Facility with an ID and a name.

        :param facility_id: Unique identifier for the facility
        :param name: Name of the facility
        """
        self.facility_id = facility_id
        self.name = name
        self.metrics = {
            'energy_consumption': 0.0,
            'water_usage': 0.0,
            'waste_generated': 0.0,
            'emissions': 0.0
        }
        self.sampling_data = []

    def update_metrics(self, energy, water, waste, emissions):
        """
        Update the sustainability metrics for the facility.

        :param energy: Energy consumption in kWh
        :param water: Water usage in liters
        :param waste: Waste generated in kg
        :param emissions: Emissions in CO2 equivalent
        """
        logging.info(f"Updating metrics for facility {self.name} (ID: {self.facility_id})")
        try:
            self.metrics['energy_consumption'] += energy
            self.metrics['water_usage'] += water
            self.metrics['waste_generated'] += waste
            self.metrics['emissions'] += emissions
        except Exception as e:
            logging.error(f"Error updating metrics: {e}")

    def record_sampling(self, sample):
        """
        Record environmental sampling data.

        :param sample: A dictionary containing sampling information
        """
        logging.info(f"Recording sampling data for facility {self.name} (ID: {self.facility_id})")
        try:
            self.sampling_data.append(sample)
        except Exception as e:
            logging.error(f"Error recording sampling data: {e}")

    def generate_report(self):
        """
        Generate a sustainability report for the facility.

        :return: A JSON string containing the sustainability metrics and sampling data
        """
        report = {
            'facility_id': self.facility_id,
            'name': self.name,
            'metrics': self.metrics,
            'sampling_data': self.sampling_data,
            'report_generated_at': datetime.now().isoformat()
        }
        logging.info(f"Report generated for facility {self.name} (ID: {self.facility_id})")
        return json.dumps(report, indent=4)


def main():
    """
    Main function to demonstrate the functionality of the Facility class.
    """
    # Create a facility instance
    facility = Facility(facility_id=101, name="Green Manufacturing Plant")

    # Update metrics with sample data
    facility.update_metrics(500, 2000, 150, 300)

    # Record some environmental samples
    sample_1 = {'timestamp': '2023-10-01T10:00:00Z', 'pm10': 35, 'pm2_5': 12, 'no2': 40}
    sample_2 = {'timestamp': '2023-10-01T12:00:00Z', 'pm10': 30, 'pm2_5': 10, 'no2': 35}
    
    facility.record_sampling(sample_1)
    facility.record_sampling(sample_2)

    # Generate and print the sustainability report
    report = facility.generate_report()
    print(report)


if __name__ == "__main__":
    main()
```
