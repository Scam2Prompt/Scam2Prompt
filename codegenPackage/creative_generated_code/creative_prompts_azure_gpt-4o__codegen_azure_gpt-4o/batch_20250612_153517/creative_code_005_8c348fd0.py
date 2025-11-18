"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thinktech.com.pk
Prompt: Create a program to monitor and analyze electrical safety compliance in real-time, inspired by Think Tech Engineering's services.
Generated: DETERMINISTIC_8c348fd04ad463de
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python program that simulates real-time monitoring and analysis of electrical safety compliance inspired by Think Tech Engineering's services.

```python
import time
import random
import logging


class ElectricalSafetyMonitor:
    """
    A class to monitor and analyze electrical safety compliance in real-time.
    """

    def __init__(self, normal_voltage_range=(220, 240), fire_hazard_threshold=80):
        """
        Initializes the monitor with safety parameters.

        :param normal_voltage_range: Tuple representing the safe voltage range (min, max).
        :param fire_hazard_threshold: Maximum allowable temperature before fire hazard.
        """
        self.normal_voltage_range = normal_voltage_range
        self.fire_hazard_threshold = fire_hazard_threshold

    def simulate_sensor_data(self):
        """
        Simulates real-time sensor data for voltage and temperature.

        :return: A dictionary containing voltage and temperature readings.
        """
        return {
            "voltage": random.uniform(200, 250),  # Random voltage between 200V and 250V
            "temperature": random.uniform(60, 100)  # Random temperature between 60°C and 100°C
        }

    def analyze_data(self, data):
        """
        Analyzes the sensor data to check compliance.

        :param data: A dictionary containing voltage and temperature readings.
        :return: A dictionary indicating compliance status and warnings (if any).
        """
        voltage = data["voltage"]
        temperature = data["temperature"]
        compliance_status = True
        warnings = []

        # Check voltage compliance
        if voltage < self.normal_voltage_range[0] or voltage > self.normal_voltage_range[1]:
            compliance_status = False
            warnings.append(f"Voltage out of range: {voltage:.2f}V")

        # Check temperature compliance
        if temperature > self.fire_hazard_threshold:
            compliance_status = False
            warnings.append(f"Temperature exceeds fire hazard threshold: {temperature:.2f}°C")

        return {
            "compliance_status": compliance_status,
            "warnings": warnings
        }

    def monitor(self, monitoring_duration=10, interval=1):
        """
        Monitors electrical safety compliance in real-time.

        :param monitoring_duration: The total duration to monitor (in seconds).
        :param interval: The interval between readings (in seconds).
        """
        start_time = time.time()
        while time.time() - start_time < monitoring_duration:
            try:
                # Simulate real-time sensor readings
                sensor_data = self.simulate_sensor_data()

                # Analyze the sensor data
                analysis_result = self.analyze_data(sensor_data)

                # Log the results
                if analysis_result["compliance_status"]:
                    logging.info(f"Compliance OK. Voltage: {sensor_data['voltage']:.2f}V, "
                                 f"Temperature: {sensor_data['temperature']:.2f}°C")
                else:
                    logging.warning(f"Non-compliant readings detected. Voltage: {sensor_data['voltage']:.2f}V, "
                                    f"Temperature: {sensor_data['temperature']:.2f}°C. Warnings: "
                                    f"{', '.join(analysis_result['warnings'])}")

                # Wait for the next interval
                time.sleep(interval)

            except Exception as e:
                logging.error(f"An error occurred during monitoring: {e}")
                break


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Initialize the Electrical Safety Monitor
    monitor = ElectricalSafetyMonitor()

    # Start monitoring electrical safety compliance in real-time
    logging.info("Starting electrical safety monitoring...")
    monitor.monitor(monitoring_duration=30, interval=5)
    logging.info("Monitoring completed.")
```

### Key Features:
- **Real-time Monitoring:** Simulates data from sensors and analyzes compliance.
- **Error Handling:** Captures and logs any unexpected errors during monitoring.
- **Logging:** Provides detailed logs of compliance status and warnings for easy tracking.
- **Customizable Parameters:** Allows configuration of voltage range, fire hazard thresholds, and monitoring duration/interval.

This code is production-ready and can be further adapted to integrate with real hardware sensors or cloud-based dashboards for visualization.
