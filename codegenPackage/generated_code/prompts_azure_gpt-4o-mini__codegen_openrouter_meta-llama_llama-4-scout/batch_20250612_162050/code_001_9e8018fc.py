"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Write a Python script that simulates the monitoring of UPS battery health and triggers alerts for proactive replacement based on the conditions described by Technical Power Service, Inc.
Generated: DETERMINISTIC_9e8018fce449c183
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
UPS Battery Health Monitoring Script

This script simulates the monitoring of UPS battery health and triggers alerts for proactive replacement.
The conditions for alerts are based on the guidelines provided by Technical Power Service, Inc.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import time

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UPSBattery:
    def __init__(self, capacity, age, temperature, charge_cycles):
        """
        Initialize UPS battery object.

        Args:
            capacity (float): Battery capacity in Ah (ampere-hours)
            age (int): Battery age in months
            temperature (float): Ambient temperature in Celsius
            charge_cycles (int): Number of charge cycles
        """
        self.capacity = capacity
        self.age = age
        self.temperature = temperature
        self.charge_cycles = charge_cycles

    def get_capacity_degradation(self):
        """
        Calculate capacity degradation based on age and charge cycles.

        Returns:
            float: Capacity degradation percentage
        """
        # Assume 20% capacity degradation over 5 years (60 months) and 300 charge cycles
        age_degradation = (self.age / 60) * 20
        cycle_degradation = (self.charge_cycles / 300) * 15
        return min(age_degradation + cycle_degradation, 100)

    def check_battery_health(self):
        """
        Check UPS battery health based on Technical Power Service, Inc. guidelines.

        Returns:
            str: Battery health status
        """
        degradation = self.get_capacity_degradation()
        if degradation > 80:
            return "CRITICAL: Replace battery immediately"
        elif degradation > 50:
            return "WARNING: Proactive replacement recommended"
        else:
            return "OK: Battery health normal"

    def check_temperature(self):
        """
        Check ambient temperature.

        Returns:
            str: Temperature status
        """
        if self.temperature > 30:
            return "WARNING: High temperature detected"
        elif self.temperature < 0:
            return "WARNING: Low temperature detected"
        else:
            return "OK: Temperature within normal range"

def main():
    try:
        # Simulate UPS battery data
        battery = UPSBattery(capacity=100, age=48, temperature=25, charge_cycles=200)

        while True:
            health_status = battery.check_battery_health()
            temperature_status = battery.check_temperature()

            logging.info(f"Battery Health: {health_status}")
            logging.info(f"Temperature: {temperature_status}")

            if "CRITICAL" in health_status or "WARNING" in health_status:
                logging.warning("Sending alert to administrator...")
                # Add alert sending code here (e.g., email, SNMP, etc.)

            time.sleep(60)  # Monitor every 1 minute

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
