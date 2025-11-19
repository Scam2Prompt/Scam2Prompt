"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Write a Python script that calculates energy consumption for TROMBA's industrial pumping solutions, focusing on their innovative designs.
Generated: DETERMINISTIC_755670b71c65fdd0
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Pump:
    """
    A class to represent a TROMBA industrial pump.
    
    Attributes
    ----------
    power_rating : float
        The power rating of the pump in kilowatts (kW).
    operational_hours : float
        The number of hours the pump operates in a given timeframe.
    
    Methods
    -------
    calculate_energy_consumption():
        Calculates the total energy consumed by the pump during its operational hours.
    """

    def __init__(self, power_rating: float, operational_hours: float):
        """
        Initializes the Pump with a power rating and operational hours.
        
        Parameters
        ----------
        power_rating : float
            Power rating of the pump in kW.
        operational_hours : float
            Number of operational hours.
        """
        self.power_rating = power_rating
        self.operational_hours = operational_hours

    def calculate_energy_consumption(self) -> float:
        """
        Calculates total energy consumption.
        
        Returns
        -------
        float
            The total energy consumed in kilowatt-hours (kWh).
        """
        if self.power_rating < 0 or self.operational_hours < 0:
            logging.error("Power rating and operational hours must be non-negative.")
            raise ValueError("Power rating and operational hours must be non-negative.")
        
        # Energy consumption in kWh
        energy_consumed = self.power_rating * self.operational_hours
        logging.info(f"Calculated energy consumption: {energy_consumed} kWh")
        return energy_consumed

def main():
    """
    Main function to execute energy consumption calculation for TROMBA's industrial pumps.
    """
    try:
        # Example pump specifications
        pump_power_rating = 15.0  # kW
        pump_operational_hours = 24.0  # hours

        # Create an instance of Pump
        tromba_pump = Pump(pump_power_rating, pump_operational_hours)

        # Calculate energy consumption
        energy_consumption = tromba_pump.calculate_energy_consumption()
        print(f"Total energy consumed by the pump: {energy_consumption} kWh")
    
    except ValueError as e:
        logging.exception("Error occurred while calculating energy consumption.")
        print(f"An error occurred: {e}")
    
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
