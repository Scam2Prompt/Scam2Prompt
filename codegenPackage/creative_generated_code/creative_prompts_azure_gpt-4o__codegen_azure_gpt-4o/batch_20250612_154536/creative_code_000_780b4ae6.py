"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Write a Python script to simulate the monitoring of Vertiv's PDU (Power Distribution Unit) sensors for data center management, referencing Vertiv's IT infrastructure solutions.
Generated: DETERMINISTIC_780b4ae61c402e44
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import logging

# --- Configuration Section ---
# Set up logging for monitoring events
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pdu_monitor.log"),
        logging.StreamHandler()
    ]
)

# Simulated sensor names for the PDU
SENSOR_NAMES = ["Voltage", "Current", "Power", "Temperature"]

# Thresholds for alerts (can be customized based on Vertiv PDU specifications)
THRESHOLDS = {
    "Voltage": {"min": 210, "max": 240},  # Voltage in Volts
    "Current": {"min": 0, "max": 100},   # Current in Amps
    "Power": {"min": 0, "max": 24000},   # Power in Watts
    "Temperature": {"min": 10, "max": 40}  # Temperature in Celsius
}

MONITOR_INTERVAL_SECONDS = 5  # Interval between sensor readings
SIMULATION_DURATION_SECONDS = 60  # Total duration for the simulation


# --- Function Definitions ---

def simulate_sensor_data(sensor_name):
    """
    Simulates random sensor data for the given sensor name.

    Args:
        sensor_name (str): Name of the sensor to simulate.

    Returns:
        float: Simulated sensor value.
    """
    if sensor_name == "Voltage":
        return random.uniform(200, 250)  # Simulate Voltage in Volts
    elif sensor_name == "Current":
        return random.uniform(0, 120)    # Simulate Current in Amps
    elif sensor_name == "Power":
        return random.uniform(0, 30000)  # Simulate Power in Watts
    elif sensor_name == "Temperature":
        return random.uniform(5, 50)     # Simulate Temperature in Celsius
    else:
        raise ValueError(f"Unknown sensor name: {sensor_name}")


def check_sensor_threshold(sensor_name, sensor_value):
    """
    Checks if the sensor value is within the defined thresholds.

    Args:
        sensor_name (str): Name of the sensor to check.
        sensor_value (float): Value of the sensor.

    Returns:
        bool: True if the value is within the thresholds, False otherwise.
    """
    thresholds = THRESHOLDS.get(sensor_name)
    if not thresholds:
        raise ValueError(f"No thresholds defined for sensor: {sensor_name}")

    return thresholds["min"] <= sensor_value <= thresholds["max"]


def monitor_pdu_sensors():
    """
    Monitors the simulated PDU sensors and logs alerts for threshold violations.
    """
    logging.info("Starting PDU monitoring simulation...")
    start_time = time.time()

    while (time.time() - start_time) < SIMULATION_DURATION_SECONDS:
        for sensor in SENSOR_NAMES:
            try:
                sensor_value = simulate_sensor_data(sensor)
                within_threshold = check_sensor_threshold(sensor, sensor_value)

                if within_threshold:
                    logging.info(f"{sensor}: {sensor_value:.2f} (Within threshold)")
                else:
                    logging.warning(f"{sensor}: {sensor_value:.2f} (Out of threshold!)")
            except Exception as e:
                logging.error(f"Error monitoring {sensor}: {e}")

        time.sleep(MONITOR_INTERVAL_SECONDS)

    logging.info("PDU monitoring simulation ended.")


# --- Main Script Execution ---
if __name__ == "__main__":
    try:
        monitor_pdu_sensors()
    except KeyboardInterrupt:
        logging.info("PDU monitoring interrupted by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```
