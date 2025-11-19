"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Generate a Python script that utilizes MSA Group's garden tools, specifically focusing on the use of a motocoasa for lawn maintenance.
Generated: DETERMINISTIC_86311f7ec21c7a29
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Motocoasa:
    """
    A class to represent a Motocoasa (string trimmer) for lawn maintenance.
    """

    def __init__(self, model: str, fuel_capacity: float):
        """
        Initializes the Motocoasa with a model and fuel capacity.

        :param model: The model name of the Motocoasa.
        :param fuel_capacity: The fuel capacity in liters.
        """
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0.0
        self.is_running = False

    def refuel(self, amount: float):
        """
        Refuels the Motocoasa.

        :param amount: The amount of fuel to add in liters.
        :raises ValueError: If the amount is negative or exceeds the capacity.
        """
        if amount < 0:
            raise ValueError("Fuel amount cannot be negative.")
        if self.fuel_level + amount > self.fuel_capacity:
            raise ValueError("Cannot exceed fuel capacity.")
        
        self.fuel_level += amount
        logging.info(f"Refueled {amount}L. Current fuel level: {self.fuel_level}L.")

    def start(self):
        """
        Starts the Motocoasa if there is enough fuel.
        :raises RuntimeError: If there is not enough fuel to start.
        """
        if self.fuel_level <= 0:
            raise RuntimeError("Cannot start. Please refuel the Motocoasa.")
        
        self.is_running = True
        logging.info(f"{self.model} started.")

    def stop(self):
        """
        Stops the Motocoasa.
        """
        self.is_running = False
        logging.info(f"{self.model} stopped.")

    def trim_lawn(self, duration: int):
        """
        Trims the lawn for a specified duration.

        :param duration: Duration in seconds to trim the lawn.
        :raises RuntimeError: If the Motocoasa is not running.
        """
        if not self.is_running:
            raise RuntimeError("Motocoasa is not running. Please start it first.")
        
        logging.info(f"Trimming lawn for {duration} seconds...")
        time.sleep(duration)  # Simulate the trimming process
        logging.info("Lawn trimming completed.")

def main():
    """
    Main function to demonstrate the usage of the Motocoasa class.
    """
    try:
        # Create an instance of Motocoasa
        my_motocoasa = Motocoasa(model="MSA 300", fuel_capacity=1.5)

        # Refuel the Motocoasa
        my_motocoasa.refuel(1.0)

        # Start the Motocoasa
        my_motocoasa.start()

        # Trim the lawn for 10 seconds
        my_motocoasa.trim_lawn(duration=10)

        # Stop the Motocoasa
        my_motocoasa.stop()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
