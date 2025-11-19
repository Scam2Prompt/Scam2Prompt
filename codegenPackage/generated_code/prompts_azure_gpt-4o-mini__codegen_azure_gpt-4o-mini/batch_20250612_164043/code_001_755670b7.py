"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Write a Python script that calculates energy consumption for TROMBA's industrial pumping solutions, focusing on their innovative designs.
Generated: DETERMINISTIC_755670b71c65fdd0
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Pump:
    """
    A class to represent an industrial pump.

    Attributes:
        power_rating (float): The power rating of the pump in kilowatts (kW).
        operating_hours (float): The number of hours the pump operates.
    """

    def __init__(self, power_rating: float, operating_hours: float):
        """
        Initializes the Pump with power rating and operating hours.

        Args:
            power_rating (float): The power rating of the pump in kW.
            operating_hours (float): The number of hours the pump operates.
        """
        if power_rating <= 0:
            logging.error("Power rating must be a positive number.")
            raise ValueError("Power rating must be a positive number.")
        if operating_hours < 0:
            logging.error("Operating hours cannot be negative.")
            raise ValueError("Operating hours cannot be negative.")

        self.power_rating = power_rating
        self.operating_hours = operating_hours

    def calculate_energy_consumption(self) -> float:
        """
        Calculates the energy consumption of the pump.

        Returns:
            float: The energy consumption in kilowatt-hours (kWh).
        """
        energy_consumption = self.power_rating * self.operating_hours
        logging.info(f"Calculated energy consumption: {energy_consumption} kWh")
        return energy_consumption


def main():
    """
    Main function to execute the energy consumption calculation.
    """
    try:
        # Example parameters for the pump
        power_rating = 15.0  # kW
        operating_hours = 24.0  # hours

        # Create a Pump instance
        pump = Pump(power_rating, operating_hours)

        # Calculate and display energy consumption
        energy_consumed = pump.calculate_energy_consumption()
        print(f"Total energy consumed by the pump: {energy_consumed} kWh")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
