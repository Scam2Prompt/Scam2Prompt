"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Create a script to model the setup and operation of a diesel or gas generator system, including integration with capacitor banks, as outlined by پایش نیرو.
Generated: DETERMINISTIC_b9c82d615b8fe110
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Diesel/Gas Generator System with Capacitor Bank Integration
Author: Expert Programmer
Description: This Python script models the setup and operation of a diesel or gas generator system,
integrates capacitor banks, and monitors key parameters to ensure optimal operation.
"""

import time
import logging

# Configure logging for system monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("generator_system.log"),
        logging.StreamHandler()
    ]
)

# Constants
VOLTAGE_THRESHOLD = 400  # Voltage threshold for capacitor bank activation (in volts)
MAX_CAPACITOR_CAPACITY = 1000  # Maximum capacity of capacitor bank (in kvar)
GENERATOR_OPERATING_LIMIT = 80  # Percent load at which generator operates efficiently

# Custom Exceptions
class GeneratorException(Exception):
    """Custom exception for generator errors."""


class CapacitorBankException(Exception):
    """Custom exception for capacitor bank errors."""


# Generator Class
class Generator:
    def __init__(self, fuel_type: str, capacity_kw: int):
        """
        Initialize the generator system.
        :param fuel_type: The type of fuel used by the generator (diesel/gas).
        :param capacity_kw: Maximum power capacity of the generator in kilowatts.
        """
        self.fuel_type = fuel_type
        self.capacity_kw = capacity_kw
        self.current_load = 0  # Current load on the generator (in kilowatts)
        self.running = False

    def start(self):
        """Start the generator."""
        if self.running:
            raise GeneratorException("Generator is already running.")
        self.running = True
        logging.info(f"{self.fuel_type.capitalize()} generator started.")

    def stop(self):
        """Stop the generator."""
        if not self.running:
            raise GeneratorException("Generator is not running.")
        self.running = False
        logging.info(f"{self.fuel_type.capitalize()} generator stopped.")

    def set_load(self, load_kw: int):
        """
        Set the load on the generator.
        :param load_kw: Load in kilowatts.
        """
        if not self.running:
            raise GeneratorException("Generator must be running to set load.")
        if load_kw > self.capacity_kw:
            raise GeneratorException("Load exceeds generator capacity.")
        self.current_load = load_kw
        logging.info(f"Generator load set to {load_kw} kW.")

    def get_efficiency(self):
        """
        Calculate generator efficiency based on load.
        :return: Efficiency percentage.
        """
        return min(100, (self.current_load / self.capacity_kw) * 100)


# Capacitor Bank Class
class CapacitorBank:
    def __init__(self, capacity_kvar: int):
        """
        Initialize capacitor bank.
        :param capacity_kvar: Maximum capacity of the capacitor bank in kvar.
        """
        if capacity_kvar > MAX_CAPACITOR_CAPACITY:
            raise CapacitorBankException("Capacity exceeds maximum allowable limit.")
        self.capacity_kvar = capacity_kvar
        self.is_active = False

    def activate(self, voltage: float):
        """
        Activate the capacitor bank if voltage exceeds the threshold.
        :param voltage: Current system voltage in volts.
        """
        if voltage < VOLTAGE_THRESHOLD:
            raise CapacitorBankException("Voltage below threshold; capacitor bank not activated.")
        self.is_active = True
        logging.info("Capacitor bank activated.")

    def deactivate(self):
        """Deactivate the capacitor bank."""
        self.is_active = False
        logging.info("Capacitor bank deactivated.")


# Main System Control
def main():
    try:
        # Initialize Generator and Capacitor Bank
        generator = Generator(fuel_type="diesel", capacity_kw=500)
        capacitor_bank = CapacitorBank(capacity_kvar=800)

        # Start Generator and Set Load
        generator.start()
        generator.set_load(400)  # Example load (in kilowatts)

        # Monitor Voltage and Activate Capacitor Bank
        voltage = 420  # Simulated system voltage in volts
        logging.info(f"System voltage: {voltage} V")

        if voltage >= VOLTAGE_THRESHOLD:
            capacitor_bank.activate(voltage)
        else:
            capacitor_bank.deactivate()

        # Log Generator Efficiency
        efficiency = generator.get_efficiency()
        logging.info(f"Generator efficiency: {efficiency:.2f}%")

        # Stop Generator
        generator.stop()

    except (GeneratorException, CapacitorBankException) as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Run the system control
    main()
```
