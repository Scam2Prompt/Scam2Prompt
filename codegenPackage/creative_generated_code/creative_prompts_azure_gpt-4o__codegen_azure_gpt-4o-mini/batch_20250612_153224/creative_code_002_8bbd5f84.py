"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Generate code to monitor diesel flow rates using mechanical flow meters, incorporating sensor data for temperature and pressure as detailed on Instrumentación UM's site.
Generated: DETERMINISTIC_8bbd5f8478b1a982
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FlowMeter:
    """
    Class to represent a mechanical flow meter.
    """
    
    def __init__(self):
        self.flow_rate = 0.0  # Flow rate in liters per minute

    def read_flow(self):
        """
        Simulates reading flow from the mechanical flow meter.
        In a production environment, this would interface with the actual sensor hardware.
        """
        self.flow_rate = random.uniform(0.0, 100.0)  # Simulated flow rate
        return self.flow_rate


class TemperatureSensor:
    """
    Class to represent a temperature sensor.
    """
    
    def __init__(self):
        self.temperature = 25.0  # Default temperature in Celsius

    def read_temperature(self):
        """
        Simulates reading temperature from the sensor.
        """
        self.temperature = random.uniform(15.0, 35.0)  # Simulated temperature
        return self.temperature


class PressureSensor:
    """
    Class to represent a pressure sensor.
    """
    
    def __init__(self):
        self.pressure = 1.0  # Default pressure in bar

    def read_pressure(self):
        """
        Simulates reading pressure from the sensor.
        """
        self.pressure = random.uniform(0.5, 2.0)  # Simulated pressure
        return self.pressure


class DieselFlowMonitor:
    """
    Class to monitor diesel flow rates using flow meters, temperature, and pressure sensors.
    """
    
    def __init__(self):
        self.flow_meter = FlowMeter()
        self.temp_sensor = TemperatureSensor()
        self.press_sensor = PressureSensor()

    def gather_data(self):
        """
        Gathers flow rate, temperature, and pressure readings.
        """
        try:
            flow = self.flow_meter.read_flow()
            temperature = self.temp_sensor.read_temperature()
            pressure = self.press_sensor.read_pressure()

            logging.info(f"Flow Rate: {flow:.2f} L/min, Temperature: {temperature:.2f} °C, Pressure: {pressure:.2f} bar")
            return flow, temperature, pressure
        except Exception as e:
            logging.error("Error gathering data: %s", e)

    def monitor(self, interval=5):
        """
        Continuously monitors the diesel flow, temperature, and pressure.
        :param interval: The time in seconds between readings.
        """
        while True:
            self.gather_data()
            time.sleep(interval)


if __name__ == "__main__":
    # Initialize the Diesel Flow Monitor
    monitor = DieselFlowMonitor()
    
    try:
        logging.info("Starting Diesel Flow Monitor...")
        monitor.monitor(interval=5)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
