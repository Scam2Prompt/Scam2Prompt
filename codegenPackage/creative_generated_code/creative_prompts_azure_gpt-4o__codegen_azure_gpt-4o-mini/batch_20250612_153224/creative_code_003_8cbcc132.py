"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Create a code snippet to monitor and log temperature and pressure data for a "Kızgın Yağ Kazanı ve Buhar Santrali" in a potato processing facility, referencing the equipment details on the CEMNAZ Makine webpage.
Generated: DETERMINISTIC_8cbcc132fb93df1e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import random

# Configure logging
logging.basicConfig(
    filename='temperature_pressure_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def read_sensor_data():
    """
    Simulates reading temperature and pressure data from sensors.
    In a real application, this function would interface with actual hardware.
    
    Returns:
        tuple: A tuple containing temperature (float) and pressure (float) readings.
    """
    try:
        # Simulated sensor readings; replace with actual sensor interface
        temperature = random.uniform(50.0, 150.0)  # Simulated temperature in Celsius
        pressure = random.uniform(1.0, 10.0)       # Simulated pressure in bar
        return temperature, pressure
    except Exception as e:
        logging.error("Error reading sensor data: %s", e)
        return None, None

def log_data(temperature, pressure):
    """
    Logs the temperature and pressure data to a file.
    
    Args:
        temperature (float): The temperature reading.
        pressure (float): The pressure reading.
    """
    try:
        if temperature is not None and pressure is not None:
            logging.info("Temperature: %.2f °C, Pressure: %.2f bar", temperature, pressure)
        else:
            logging.warning("Received invalid sensor data for logging.")
    except Exception as e:
        logging.error("Error logging data: %s", e)

def monitor_system(interval=60):
    """
    Monitors the temperature and pressure data at specified intervals.

    Args:
        interval (int): The time interval (in seconds) between measurements.
    """
    try:
        while True:
            temperature, pressure = read_sensor_data()
            log_data(temperature, pressure)
            time.sleep(interval)  # Wait for the specified interval before the next measurement
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error("An error occurred during monitoring: %s", e)

if __name__ == "__main__":
    monitor_system(interval=60)  # Start monitoring with a 60-second interval
```
