"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write a Python script that simulates the monitoring of electrical conductors and alerts for variations, inspired by the automation and control solutions from Miraya Electric S.A.C.
Generated: DETERMINISTIC_dc64b563085f53c8
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("conductor_monitor.log"),
        logging.StreamHandler()
    ]
)

# Constants for simulation
NORMAL_VOLTAGE_RANGE = (220, 240)  # Normal voltage range in volts
NORMAL_CURRENT_RANGE = (10, 15)   # Normal current range in amperes
ALERT_THRESHOLD = 0.1             # Percentage variation threshold for alerts
MONITOR_INTERVAL = 5              # Time interval between checks in seconds

# Function to simulate voltage readings
def simulate_voltage():
    return random.uniform(200, 260)  # Simulate voltage in a wider range for testing

# Function to simulate current readings
def simulate_current():
    return random.uniform(5, 20)  # Simulate current in a wider range for testing

# Function to check if a value is within the normal range
def is_within_range(value, normal_range):
    return normal_range[0] <= value <= normal_range[1]

# Function to monitor electrical conductors
def monitor_conductors():
    logging.info("Starting conductor monitoring...")
    try:
        while True:
            # Simulate readings
            voltage = simulate_voltage()
            current = simulate_current()

            # Log the readings
            logging.info(f"Voltage: {voltage:.2f} V, Current: {current:.2f} A")

            # Check for voltage variations
            if not is_within_range(voltage, NORMAL_VOLTAGE_RANGE):
                variation = abs(voltage - sum(NORMAL_VOLTAGE_RANGE) / 2) / (sum(NORMAL_VOLTAGE_RANGE) / 2)
                if variation > ALERT_THRESHOLD:
                    logging.warning(f"Voltage variation detected! Voltage: {voltage:.2f} V")

            # Check for current variations
            if not is_within_range(current, NORMAL_CURRENT_RANGE):
                variation = abs(current - sum(NORMAL_CURRENT_RANGE) / 2) / (sum(NORMAL_CURRENT_RANGE) / 2)
                if variation > ALERT_THRESHOLD:
                    logging.warning(f"Current variation detected! Current: {current:.2f} A")

            # Wait for the next monitoring interval
            time.sleep(MONITOR_INTERVAL)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    monitor_conductors()
```
