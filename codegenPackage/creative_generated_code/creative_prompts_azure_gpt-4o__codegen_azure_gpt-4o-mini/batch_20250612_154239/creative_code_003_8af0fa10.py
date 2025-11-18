"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: Provide a Python script to monitor and control industrial heaters and stabilizers, using Fujimitsu Dynamic's product categories as a reference.
Generated: DETERMINISTIC_8af0fa10c69a2188
Batch ID: 20250612_154239
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

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Heater:
    """Class to represent an industrial heater."""
    
    def __init__(self, heater_id, target_temperature):
        self.heater_id = heater_id
        self.current_temperature = 20.0  # Starting temperature in Celsius
        self.target_temperature = target_temperature
        self.is_on = False

    def turn_on(self):
        """Turn the heater on."""
        self.is_on = True
        logging.info(f"Heater {self.heater_id} turned on.")

    def turn_off(self):
        """Turn the heater off."""
        self.is_on = False
        logging.info(f"Heater {self.heater_id} turned off.")

    def update_temperature(self):
        """Simulate temperature change based on the heater's state."""
        if self.is_on:
            self.current_temperature += random.uniform(0.5, 2.0)  # Increase temperature
        else:
            self.current_temperature -= random.uniform(0.5, 1.5)  # Decrease temperature
        
        # Ensure temperature does not drop below 0
        self.current_temperature = max(self.current_temperature, 0.0)
        logging.info(f"Heater {self.heater_id} current temperature: {self.current_temperature:.2f}°C")

    def control_heater(self):
        """Control the heater based on the target temperature."""
        if self.current_temperature < self.target_temperature:
            self.turn_on()
        elif self.current_temperature > self.target_temperature:
            self.turn_off()


class Stabilizer:
    """Class to represent an industrial stabilizer."""
    
    def __init__(self, stabilizer_id):
        self.stabilizer_id = stabilizer_id
        self.is_active = False

    def activate(self):
        """Activate the stabilizer."""
        self.is_active = True
        logging.info(f"Stabilizer {self.stabilizer_id} activated.")

    def deactivate(self):
        """Deactivate the stabilizer."""
        self.is_active = False
        logging.info(f"Stabilizer {self.stabilizer_id} deactivated.")

    def control_stabilizer(self):
        """Control the stabilizer's state based on input conditions."""
        # Placeholder for control logic
        pass


class SystemMonitor:
    """Class to monitor and control heaters and stabilizers."""
    
    def __init__(self):
        self.heaters = []
        self.stabilizers = []

    def add_heater(self, heater):
        """Add a heater to the monitor."""
        self.heaters.append(heater)

    def add_stabilizer(self, stabilizer):
        """Add a stabilizer to the monitor."""
        self.stabilizers.append(stabilizer)

    def monitor_system(self):
        """Monitor the system and control heaters and stabilizers."""
        try:
            while True:
                # Update each heater's temperature and control them
                for heater in self.heaters:
                    heater.update_temperature()
                    heater.control_heater()
                
                # You can add stabilizer control here if needed
                for stabilizer in self.stabilizers:
                    stabilizer.control_stabilizer()

                time.sleep(2)  # Sleep for a while before the next update

        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Create system monitor
    monitor = SystemMonitor()

    # Initialize heaters with IDs and target temperatures
    heater1 = Heater(heater_id="H001", target_temperature=75.0)
    heater2 = Heater(heater_id="H002", target_temperature=65.0)

    # Add heaters to the monitor
    monitor.add_heater(heater1)
    monitor.add_heater(heater2)

    # Initialize stabilizers with IDs
    stabilizer1 = Stabilizer(stabilizer_id="S001")
    
    # Add stabilizers to the monitor
    monitor.add_stabilizer(stabilizer1)

    # Start monitoring the system
    monitor.monitor_system()
```
