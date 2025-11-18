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
from typing import Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDU:
    """
    Class to simulate a Power Distribution Unit (PDU) with sensors.
    """

    def __init__(self, id: str) -> None:
        """
        Initialize a PDU instance with a unique identifier.
        
        :param id: Unique identifier for the PDU
        """
        self.id = id
        self.sensors = {
            'temperature': 25.0,  # in degrees Celsius
            'humidity': 50.0,     # in percentage
            'voltage': 230.0,     # in volts
            'current': 10.0       # in amps
        }

    def update_sensor_data(self) -> None:
        """
        Simulate the updating of sensor data with random values.
        """
        try:
            self.sensors['temperature'] = round(random.uniform(20, 30), 2)
            self.sensors['humidity'] = round(random.uniform(30, 70), 2)
            self.sensors['voltage'] = round(random.uniform(220, 240), 2)
            self.sensors['current'] = round(random.uniform(5, 15), 2)

            logging.info(f"Sensors updated: {self.sensors}")

        except Exception as e:
            logging.error(f"Error updating sensor data: {e}")

    def get_sensor_data(self) -> Dict[str, Any]:
        """
        Retrieve the current sensor data.
        
        :return: Dictionary containing sensor data
        """
        return self.sensors


def monitor_pdu(pdu: PDU, interval: int = 5) -> None:
    """
    Monitor the PDU by periodically updating and logging sensor data.
    
    :param pdu: PDU instance to monitor
    :param interval: Time interval (in seconds) between updates
    """
    try:
        while True:
            pdu.update_sensor_data()
            time.sleep(interval)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

    except Exception as e:
        logging.error(f"Error during monitoring: {e}")


if __name__ == "__main__":
    # Create a PDU instance
    pdu_id = "PDU_01"
    pdu = PDU(pdu_id)

    # Start monitoring the PDU
    monitor_pdu(pdu)
```
