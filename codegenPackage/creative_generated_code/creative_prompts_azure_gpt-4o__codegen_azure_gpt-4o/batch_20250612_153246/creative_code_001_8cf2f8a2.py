"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citygardenmexico.com.mx
Prompt: Generate code to simulate an irrigation system design for a rooftop garden, incorporating features mentioned in City Garden México's services.
Generated: DETERMINISTIC_8cf2f8a24d33bd82
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IrrigationSystem:
    """
    Class to simulate an irrigation system for a rooftop garden.
    Features:
    - Automated watering based on time intervals
    - Soil moisture monitoring
    - Rain detection to conserve water
    """
    def __init__(self, garden_area, water_capacity, moisture_threshold, rain_sensor_enabled=True):
        """
        Initialize the irrigation system.
        :param garden_area: Total area of the rooftop garden (in square meters)
        :param water_capacity: Total water capacity of the system (in liters)
        :param moisture_threshold: Minimum soil moisture level (%) to start watering
        :param rain_sensor_enabled: Whether the rain detection sensor is enabled
        """
        self.garden_area = garden_area
        self.water_capacity = water_capacity
        self.moisture_threshold = moisture_threshold
        self.rain_sensor_enabled = rain_sensor_enabled
        self.current_moisture = 50  # Placeholder for soil moisture level (%)
        self.is_raining = False  # Placeholder for rain detection

    def check_rain(self):
        """
        Simulate rain detection.
        In a real-world scenario, this would use a hardware rain sensor.
        """
        # Placeholder logic: Randomize rain detection
        self.is_raining = time.time() % 10 < 3  # Simulating rain (30% chance)
        logging.info(f"Rain detected: {'Yes' if self.is_raining else 'No'}")

    def check_soil_moisture(self):
        """
        Simulate soil moisture level measurement.
        In a real-world scenario, this would use a soil moisture sensor.
        """
        # Update current moisture randomly between 30% and 70% for simulation
        import random
        self.current_moisture = random.randint(30, 70)
        logging.info(f"Current soil moisture level: {self.current_moisture}%")

    def water_garden(self):
        """
        Activate the irrigation system to water the garden.
        """
        if self.water_capacity <= 0:
            logging.error("Water tank is empty! Refill required.")
            return

        logging.info("Activating irrigation system...")
        # Simulate water consumption during irrigation
        water_used = min(self.water_capacity, self.garden_area * 0.5)  # 0.5 liters per square meter
        self.water_capacity -= water_used
        logging.info(f"Water used: {water_used} liters. Remaining capacity: {self.water_capacity} liters.")
        time.sleep(1)  # Simulating irrigation time
        logging.info("Irrigation completed.")

    def run(self):
        """
        Run the irrigation system logic.
        """
        logging.info("Starting irrigation system...")
        self.check_rain()
        self.check_soil_moisture()

        # Decide whether to water the garden
        if self.is_raining and self.rain_sensor_enabled:
            logging.info("Rain detected. Irrigation canceled to conserve water.")
        elif self.current_moisture < self.moisture_threshold:
            self.water_garden()
        else:
            logging.info("Soil moisture is sufficient. Irrigation not required.")

if __name__ == "__main__":
    # Example configuration for the rooftop garden irrigation system
    irrigation_system = IrrigationSystem(
        garden_area=100,  # 100 square meters
        water_capacity=200,  # 200 liters
        moisture_threshold=40,  # Minimum 40% soil moisture
        rain_sensor_enabled=True
    )

    # Run the irrigation system periodically
    for _ in range(3):  # Simulate 3 cycles
        irrigation_system.run()
        time.sleep(5)  # Wait 5 seconds between cycles
```
