"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Create a script to log and analyze performance data from a "石墨消解器" (graphite digestion system) during sample preparation.
Generated: DETERMINISTIC_296ef122d354a809
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    filename='performance_log.json',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GraphiteDigestionSystem:
    def __init__(self, system_id):
        self.system_id = system_id
        self.performance_data = []

    def log_performance(self, temperature, pressure, duration):
        """
        Log the performance data of the graphite digestion system.

        :param temperature: Temperature of the system in degrees Celsius.
        :param pressure: Pressure in the system in Pascals.
        :param duration: Duration of the digestion process in seconds.
        """
        try:
            if not isinstance(temperature, (int, float)) or not isinstance(pressure, (int, float)) or not isinstance(duration, (int, float)):
                raise ValueError("Temperature, pressure, and duration must be numeric values.")

            performance_entry = {
                'system_id': self.system_id,
                'timestamp': datetime.now().isoformat(),
                'temperature': temperature,
                'pressure': pressure,
                'duration': duration
            }
            self.performance_data.append(performance_entry)
            logging.info('Performance data logged: %s', performance_entry)

        except Exception as e:
            logging.error('Error logging performance data: %s', e)

    def save_performance_data(self):
        """
        Save the logged performance data to a JSON file.
        """
        try:
            if not self.performance_data:
                raise ValueError("No performance data to save.")

            if not os.path.exists('logs'):
                os.makedirs('logs')

            with open('logs/performance_data.json', 'w') as json_file:
                json.dump(self.performance_data, json_file, indent=4)
            logging.info('Performance data saved to logs/performance_data.json')

        except Exception as e:
            logging.error('Error saving performance data: %s', e)

    def analyze_performance(self):
        """
        Analyze the logged performance data and provide basic statistics.
        """
        try:
            if not self.performance_data:
                raise ValueError("No performance data to analyze.")

            temperature_data = [entry['temperature'] for entry in self.performance_data]
            pressure_data = [entry['pressure'] for entry in self.performance_data]
            duration_data = [entry['duration'] for entry in self.performance_data]

            analysis_results = {
                'average_temperature': sum(temperature_data) / len(temperature_data),
                'average_pressure': sum(pressure_data) / len(pressure_data),
                'average_duration': sum(duration_data) / len(duration_data),
                'total_entries': len(self.performance_data)
            }
            logging.info('Performance analysis results: %s', analysis_results)
            return analysis_results

        except Exception as e:
            logging.error('Error analyzing performance data: %s', e)
            return None

# Example usage
if __name__ == "__main__":
    system = GraphiteDigestionSystem(system_id='GD-001')
    
    # Log some sample data
    system.log_performance(temperature=350.5, pressure=150000, duration=120)
    system.log_performance(temperature=360.0, pressure=155000, duration=130)
    
    # Save the performance data to a file
    system.save_performance_data()
    
    # Analyze the performance data
    analysis_results = system.analyze_performance()
    if analysis_results:
        print("Analysis Results:", analysis_results)
```
