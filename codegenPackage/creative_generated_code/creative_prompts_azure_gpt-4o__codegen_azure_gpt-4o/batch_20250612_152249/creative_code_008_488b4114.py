"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opsense.com
Prompt: Create a Python function that simulates automated alerts for temperature deviations in healthcare facilities, leveraging OpSense's monitoring capabilities.
Generated: DETERMINISTIC_488b4114f865de22
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Define constants
TEMPERATURE_THRESHOLD = {
    "low": 15.0,  # Minimum acceptable temperature in Celsius
    "high": 25.0  # Maximum acceptable temperature in Celsius
}

ALERT_RECIPIENTS = ["admin@healthcarefacility.com", "maintenanceteam@healthcarefacility.com"]

def send_alert(temperature: float, location: str) -> None:
    """
    Sends an alert to the appropriate recipients when temperature deviates from the threshold.

    Args:
        temperature (float): The reported temperature.
        location (str): The location where the temperature was reported.
    """
    try:
        # Simulate sending an alert (replace with actual email/sms API call in production)
        alert_message = f"ALERT: Temperature deviation detected! "\
                        f"Location: {location}, Reported Temp: {temperature:.2f}°C."
        for recipient in ALERT_RECIPIENTS:
            logging.info(f"Sending alert to {recipient}: {alert_message}")
        logging.info("Alert successfully sent.")
    except Exception as e:
        logging.error(f"Failed to send alert due to error: {e}")

def monitor_temperature(data: List[Dict[str, float]]) -> None:
    """
    Monitors temperature readings and triggers alerts for deviations.

    Args:
        data (List[Dict[str, float]]): A list of dictionaries containing temperature data.
                                       Expected format: [{"location": str, "temperature": float}, ...]
    """
    for entry in data:
        try:
            location = entry.get("location")
            temperature = entry.get("temperature")

            if location is None or temperature is None:
                logging.warning("Invalid data entry detected. Skipping.")
                continue

            # Check for temperature deviations
            if temperature < TEMPERATURE_THRESHOLD["low"] or temperature > TEMPERATURE_THRESHOLD["high"]:
                logging.info(f"Temperature deviation detected at {location}. Temp: {temperature:.2f}°C")
                send_alert(temperature, location)
            else:
                logging.info(f"Temperature at {location} is within acceptable range: {temperature:.2f}°C")
        except Exception as e:
            logging.error(f"Error processing temperature data for {entry}. Error: {e}")

# Example usage
if __name__ == "__main__":
    # Simulated temperature data from OpSense's monitoring capabilities
    temperature_data = [
        {"location": "Room A", "temperature": 14.5},
        {"location": "Room B", "temperature": 22.0},
        {"location": "Room C", "temperature": 26.3},
        {"location": "Room D", "temperature": None},  # Invalid entry
    ]

    monitor_temperature(temperature_data)
```
