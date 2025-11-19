"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-link.io
Prompt: Generate a Python script that utilizes MIT's new fuel cell technology for energy-efficient applications in electric vehicles.
Generated: DETERMINISTIC_afd28c38655d1bbd
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class FuelCell:
    """
    A class representing MIT's new fuel cell technology.
    This class simulates energy-efficient fuel cell operations for electric vehicles.
    """

    def __init__(self, max_capacity: float):
        """
        Initialize the FuelCell object.

        Args:
            max_capacity (float): Maximum capacity of the fuel cell in kWh.
        """
        if max_capacity <= 0:
            raise ValueError("Max capacity must be greater than zero.")
        self.max_capacity = max_capacity  # Maximum energy storage in kWh
        self.current_charge = 0  # Current energy storage in kWh

    def charge(self, energy: float):
        """
        Charge the fuel cell with a specified amount of energy.

        Args:
            energy (float): Amount of energy to charge in kWh.

        Raises:
            ValueError: If the energy value is negative or exceeds max capacity.
        """
        if energy < 0:
            raise ValueError("Energy to charge must be non-negative.")
        if self.current_charge + energy > self.max_capacity:
            raise ValueError("Charging exceeds maximum capacity.")
        self.current_charge += energy
        logging.info(f"Fuel cell charged with {energy} kWh. Current charge: {self.current_charge} kWh.")

    def discharge(self, energy: float) -> float:
        """
        Discharge the fuel cell by a specified amount of energy.

        Args:
            energy (float): Amount of energy to discharge in kWh.

        Returns:
            float: Actual energy discharged.

        Raises:
            ValueError: If the energy value is negative.
        """
        if energy < 0:
            raise ValueError("Energy to discharge must be non-negative.")

        discharged_energy = min(energy, self.current_charge)
        self.current_charge -= discharged_energy
        logging.info(f"Fuel cell discharged {discharged_energy} kWh. Current charge: {self.current_charge} kWh.")
        return discharged_energy

    def get_status(self) -> str:
        """
        Get the current status of the fuel cell.

        Returns:
            str: Status of the fuel cell including current charge and max capacity.
        """
        return f"Fuel Cell Status: {self.current_charge}/{self.max_capacity} kWh"

def simulate_electric_vehicle():
    """
    Simulate the operation of an electric vehicle using MIT's new fuel cell technology.
    """
    try:
        # Initialize the fuel cell with a maximum capacity of 100 kWh
        fuel_cell = FuelCell(max_capacity=100.0)
        
        # Charge the fuel cell with energy
        fuel_cell.charge(50.0)  # Charging 50 kWh
        print(fuel_cell.get_status())
        
        # Discharge energy to simulate vehicle operation
        discharged = fuel_cell.discharge(30.0)  # Consuming 30 kWh
        print(f"Energy used by vehicle: {discharged} kWh")
        print(fuel_cell.get_status())
        
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Run the simulation
if __name__ == "__main__":
    simulate_electric_vehicle()
```
