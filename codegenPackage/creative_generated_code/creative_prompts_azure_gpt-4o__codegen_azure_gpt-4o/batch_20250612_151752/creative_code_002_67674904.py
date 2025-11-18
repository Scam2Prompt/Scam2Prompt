"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Generate a program in Python for geotechnical monitoring, including data acquisition and analysis, based on the methodologies mentioned by the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_6767490405638c49
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import statistics
import os
from datetime import datetime

class GeotechnicalMonitoring:
    """
    A class for geotechnical monitoring that includes data acquisition and analysis.
    """
    
    def __init__(self, data_file):
        """
        Initialize the monitoring system with the given CSV file for data storage.
        
        :param data_file: Path to the CSV file for storing sensor data
        """
        self.data_file = data_file
        self._initialize_data_file()
    
    def _initialize_data_file(self):
        """
        Initialize the CSV file if it does not exist.
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(["Timestamp", "Sensor_ID", "Measurement_Value"])
    
    def acquire_data(self, sensor_id, measurement_value):
        """
        Simulate data acquisition from a sensor and store it in the CSV file.
        
        :param sensor_id: Identifier of the sensor
        :param measurement_value: Measurement taken by the sensor
        """
        try:
            timestamp = datetime.now().isoformat()
            # Write data to the CSV file
            with open(self.data_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, sensor_id, measurement_value])
            print(f"Data recorded: Sensor {sensor_id}, Value {measurement_value}, Timestamp {timestamp}")
        except Exception as e:
            print(f"Error while recording data: {e}")
    
    def analyze_data(self):
        """
        Analyze the data stored in the CSV file and print summary statistics.
        """
        try:
            sensor_data = {}
            
            # Read data from the CSV file
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    sensor_id = row["Sensor_ID"]
                    measurement_value = float(row["Measurement_Value"])
                    
                    # Group data by sensor
                    if sensor_id not in sensor_data:
                        sensor_data[sensor_id] = []
                    sensor_data[sensor_id].append(measurement_value)
            
            # Calculate and display statistics for each sensor
            for sensor_id, measurements in sensor_data.items():
                mean = statistics.mean(measurements)
                median = statistics.median(measurements)
                min_val = min(measurements)
                max_val = max(measurements)
                print(f"Sensor {sensor_id}:")
                print(f"  Mean: {mean:.2f}, Median: {median:.2f}, Min: {min_val:.2f}, Max: {max_val:.2f}")
        
        except FileNotFoundError:
            print("Data file not found. Please ensure data acquisition is performed before analysis.")
        except Exception as e:
            print(f"Error during data analysis: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize the monitoring system with the file "geotechnical_data.csv"
    monitoring_system = GeotechnicalMonitoring("geotechnical_data.csv")
    
    # Simulate acquiring data from sensors
    monitoring_system.acquire_data("Sensor_1", 25.6)
    monitoring_system.acquire_data("Sensor_1", 26.3)
    monitoring_system.acquire_data("Sensor_2", 19.8)
    monitoring_system.acquire_data("Sensor_2", 21.4)
    monitoring_system.acquire_data("Sensor_3", 33.5)
    
    # Analyze the acquired data
    monitoring_system.analyze_data()
```
