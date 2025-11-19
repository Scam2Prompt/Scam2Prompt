"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: "Design an electrical safety compliance system using IoT sensors and provide a code example in C++ or Python."
Generated: DETERMINISTIC_8e3dedfb1fe487fe
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Safety Compliance System using IoT Sensors
This Python script monitors electrical parameters (e.g., voltage, current, temperature) using IoT sensors.
It checks for safety thresholds and triggers alerts if values exceed safe limits.
"""

import time
import random

# Define safety thresholds
SAFETY_THRESHOLDS = {
    "voltage": {"min": 210, "max": 240},  # Voltage in volts
    "current": {"min": 0, "max": 10},    # Current in amperes
    "temperature": {"min": 0, "max": 75} # Temperature in degrees Celsius
}

# Simulated IoT sensor data (replace with actual sensor integration in production)
def read_sensor_data():
    """
    Simulates reading data from IoT sensors.
    Replace this function with actual sensor integration code.
    """
    return {
        "voltage": random.uniform(200, 250),  # Simulated voltage
        "current": random.uniform(0, 15),    # Simulated current
        "temperature": random.uniform(20, 100) # Simulated temperature
    }

def check_compliance(sensor_data):
    """
    Checks if the sensor data is within safety thresholds.
    Returns a list of alerts if any parameter is out of range.
    """
    alerts = []
    for parameter, value in sensor_data.items():
        thresholds = SAFETY_THRESHOLDS.get(parameter)
        if thresholds:
            if value < thresholds["min"] or value > thresholds["max"]:
                alerts.append(f"{parameter.capitalize()} out of range: {value:.2f}")
    return alerts

def main():
    """
    Main function to monitor electrical safety compliance.
    Continuously reads sensor data, checks compliance, and triggers alerts.
    """
    try:
        print("Starting Electrical Safety Compliance System...")
        while True:
            # Read sensor data
            sensor_data = read_sensor_data()
            
            # Check compliance
            alerts = check_compliance(sensor_data)
            
            # Display sensor data
            print(f"Sensor Data: {sensor_data}")
            
            # Trigger alerts if necessary
            if alerts:
                print("ALERTS:")
                for alert in alerts:
                    print(f"  - {alert}")
            else:
                print("All parameters are within safe limits.")
            
            # Wait before next reading (simulate real-time monitoring)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nSystem stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
