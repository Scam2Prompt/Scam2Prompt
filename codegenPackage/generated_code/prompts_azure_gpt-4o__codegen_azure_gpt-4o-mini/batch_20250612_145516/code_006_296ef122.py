"""
Generated Code Metadata:
========================
Original URL: https://nftsonopensea.com
Prompt: Create a script to log and analyze performance data from a "石墨消解器" (graphite digestion system) during sample preparation.
Generated: DETERMINISTIC_296ef122d354a809
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='performance_log.json',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GraphiteDigestionSystem:
    def __init__(self):
        self.performance_data = []

    def log_performance(self, temperature, pressure, duration):
        """
        Log performance data for the graphite digestion system.

        :param temperature: Temperature during the digestion process (in Celsius)
        :param pressure: Pressure during the digestion process (in atm)
        :param duration: Duration of the digestion process (in seconds)
        """
        try:
            # Create a performance record
            record = {
                'timestamp': datetime.now().isoformat(),
                'temperature': temperature,
                'pressure': pressure,
                'duration': duration
            }
            self.performance_data.append(record)
            logging.info(f"Performance logged: {record}")
        except Exception as e:
            logging.error(f"Error logging performance data: {e}")

    def analyze_performance(self):
        """
        Analyze the logged performance data and return summary statistics.

        :return: A dictionary containing average temperature, pressure, and duration
        """
        if not self.performance_data:
            logging.warning("No performance data to analyze.")
            return None

        total_temperature = 0
        total_pressure = 0
        total_duration = 0
        count = len(self.performance_data)

        for record in self.performance_data:
            total_temperature += record['temperature']
            total_pressure += record['pressure']
            total_duration += record['duration']

        # Calculate averages
        average_temperature = total_temperature / count
        average_pressure = total_pressure / count
        average_duration = total_duration / count

        summary = {
            'average_temperature': average_temperature,
            'average_pressure': average_pressure,
            'average_duration': average_duration
        }

        logging.info(f"Performance analysis completed: {summary}")
        return summary

    def save_performance_data(self):
        """
        Save the performance data to a JSON file.
        """
        try:
            with open('performance_data.json', 'w') as json_file:
                json.dump(self.performance_data, json_file, indent=4)
            logging.info("Performance data saved to performance_data.json")
        except IOError as e:
            logging.error(f"Error saving performance data: {e}")

if __name__ == "__main__":
    # Example usage of the GraphiteDigestionSystem class
    digestion_system = GraphiteDigestionSystem()

    # Simulate logging performance data
    try:
        digestion_system.log_performance(temperature=200, pressure=1.5, duration=3600)
        digestion_system.log_performance(temperature=210, pressure=1.6, duration=3700)

        # Analyze performance data
        analysis_result = digestion_system.analyze_performance()
        print("Performance Analysis Result:", analysis_result)

        # Save performance data to a file
        digestion_system.save_performance_data()
    except Exception as e:
        logging.error(f"An error occurred during the main execution: {e}")
```
