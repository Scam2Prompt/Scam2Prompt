"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: "Create a program for automating industrial processes using programmable logic controllers (PLCs), including data acquisition and logging."
Generated: DETERMINISTIC_71942c109e392cac
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
import random

# Configure logging for data acquisition
logging.basicConfig(filename='plc_data.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PLC:
    """A class to represent a Programmable Logic Controller (PLC) for industrial automation."""
    
    def __init__(self, id):
        """Initialize the PLC with a unique identifier."""
        self.id = id
        self.data = {}
    
    def read_sensor(self, sensor_id):
        """Simulate reading data from a sensor."""
        # Simulate sensor data acquisition
        value = random.uniform(0, 100)  # Random value between 0 and 100
        logging.info(f"Sensor {sensor_id} read value: {value}")
        return value
    
    def log_data(self, sensor_id, value):
        """Log the sensor data to a file."""
        self.data[sensor_id] = value
        logging.info(f"Logged data for sensor {sensor_id}: {value}")
    
    def run_process(self, sensor_ids, interval=5):
        """Run the data acquisition process for the specified sensors."""
        try:
            while True:
                for sensor_id in sensor_ids:
                    value = self.read_sensor(sensor_id)
                    self.log_data(sensor_id, value)
                time.sleep(interval)  # Wait for the specified interval before the next read
        except KeyboardInterrupt:
            logging.info("Data acquisition process stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

def main():
    """Main function to set up and run the PLC data acquisition."""
    try:
        # Create a PLC instance
        plc = PLC(id="PLC_001")
        
        # Define the sensors to monitor
        sensor_ids = ["Sensor_1", "Sensor_2", "Sensor_3"]
        
        # Start the data acquisition process
        plc.run_process(sensor_ids, interval=10)  # 10 seconds interval
    except Exception as e:
        logging.error(f"Failed to initialize PLC: {e}")

if __name__ == "__main__":
    main()
```
