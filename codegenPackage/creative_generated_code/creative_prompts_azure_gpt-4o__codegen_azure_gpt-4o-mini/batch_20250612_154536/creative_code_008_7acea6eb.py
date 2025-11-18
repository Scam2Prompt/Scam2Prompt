"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Write code to generate alerts for anomalies in Vertiv's cooling systems based on sensor data collected from edge computing environments.
Generated: DETERMINISTIC_7acea6eb9323c77b
Batch ID: 20250612_154536
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
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CoolingSystemMonitor:
    def __init__(self, threshold: float, alert_email: str):
        """
        Initialize the CoolingSystemMonitor with a specific anomaly threshold
        and an email for alert notifications.

        Args:
            threshold (float): The threshold value for determining anomalies.
            alert_email (str): The email address to send alerts to.
        """
        self.threshold = threshold
        self.alert_email = alert_email

    def parse_sensor_data(self, data: str) -> List[Dict[str, float]]:
        """
        Parse sensor data from a JSON string.

        Args:
            data (str): A JSON string containing sensor data.

        Returns:
            List[Dict[str, float]]: A list of sensor readings.
        """
        try:
            sensor_data = json.loads(data)
            logging.info("Sensor data parsed successfully.")
            return sensor_data
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing sensor data: {e}")
            raise ValueError("Invalid sensor data format.") from e

    def detect_anomalies(self, sensor_data: List[Dict[str, float]]) -> List[Dict[str, float]]:
        """
        Detect anomalies in the provided sensor data based on the threshold.

        Args:
            sensor_data (List[Dict[str, float]]): A list of sensor readings.

        Returns:
            List[Dict[str, float]]: A list of detected anomalies.
        """
        anomalies = []
        for reading in sensor_data:
            temperature = reading.get('temperature')
            humidity = reading.get('humidity')

            if temperature is None or humidity is None:
                logging.warning("Missing temperature or humidity data in reading.")
                continue

            if temperature > self.threshold or humidity > self.threshold:
                anomalies.append(reading)
                logging.info(f"Anomaly detected: {reading}")

        return anomalies

    def send_alert(self, anomaly: Dict[str, float]):
        """
        Send an alert for a detected anomaly.

        Args:
            anomaly (Dict[str, float]): The anomaly data to include in the alert.
        """
        # Here you can implement actual email sending logic
        logging.info(f"Alert sent to {self.alert_email}: Anomaly detected - {anomaly}")

    def process_sensor_data(self, data: str):
        """
        Process incoming sensor data to detect and alert anomalies.

        Args:
            data (str): A JSON string containing sensor data.
        """
        try:
            sensor_data = self.parse_sensor_data(data)
            anomalies = self.detect_anomalies(sensor_data)

            for anomaly in anomalies:
                self.send_alert(anomaly)

        except ValueError as e:
            logging.error(f"Error processing sensor data: {e}")

# Example usage
if __name__ == "__main__":
    threshold_value = 80.0  # Example threshold for temperature/humidity
    alert_email = "alerts@vertiv.com"
    monitor = CoolingSystemMonitor(threshold=threshold_value, alert_email=alert_email)

    # Simulated incoming sensor data
    incoming_data = '''
    [
        {"timestamp": "2023-10-01T12:00:00Z", "temperature": 85.0, "humidity": 75.0},
        {"timestamp": "2023-10-01T12:05:00Z", "temperature": 78.0, "humidity": 82.0},
        {"timestamp": "2023-10-01T12:10:00Z", "temperature": 82.0, "humidity": 70.0}
    ]
    '''

    monitor.process_sensor_data(incoming_data)
```
