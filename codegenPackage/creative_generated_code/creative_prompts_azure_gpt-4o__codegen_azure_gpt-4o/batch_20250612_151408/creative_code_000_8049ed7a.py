"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write Python code to simulate the ice preservation performance of Engel UltraLite coolers, incorporating features like closed-cell foam insulation and tapered drainage channels.
Generated: DETERMINISTIC_8049ed7acb47bd12
Batch ID: 20250612_151408
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

# Configure logging for debugging and error handling
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EngelUltraLiteCooler:
    """
    Simulates the ice preservation performance of Engel UltraLite Coolers.
    Features:
    - Closed-cell foam insulation
    - Tapered drainage channels
    - Adjustable cooler size and ambient temperature
    """
    
    def __init__(self, cooler_size_liters: float, ambient_temperature_celsius: float):
        """
        Initialize the cooler with size and ambient temperature.

        :param cooler_size_liters: Size of the cooler in liters.
        :param ambient_temperature_celsius: Current ambient temperature in Celsius.
        """
        if cooler_size_liters <= 0:
            raise ValueError("Cooler size must be greater than 0 liters.")
        self.cooler_size_liters = cooler_size_liters
        self.ambient_temperature_celsius = ambient_temperature_celsius
        self.ice_amount_kilograms = 0
        self.closed_cell_insulation_factor = 0.85  # Efficiency factor of the insulation
        self.drainage_efficiency = 0.9  # Efficiency of tapered drainage channels

    def add_ice(self, ice_amount_kilograms: float):
        """
        Adds ice to the cooler.

        :param ice_amount_kilograms: Amount of ice in kilograms to be added.
        """
        if ice_amount_kilograms <= 0:
            raise ValueError("Ice amount must be greater than 0 kilograms.")
        self.ice_amount_kilograms += ice_amount_kilograms
        logging.info(f"Added {ice_amount_kilograms:.2f} kg of ice. Total ice: {self.ice_amount_kilograms:.2f} kg.")

    def simulate_ice_melting(self, hours: int):
        """
        Simulates the process of ice melting over time due to ambient temperature.

        :param hours: Number of hours to simulate ice melting.
        """
        if hours <= 0:
            raise ValueError("Hours must be greater than 0.")
        
        melting_rate_per_hour = self.calculate_melting_rate()  # Melting rate in kg/hour
        total_melted_ice = 0

        for hour in range(1, hours + 1):
            melted_ice = melting_rate_per_hour * self.closed_cell_insulation_factor * self.drainage_efficiency
            melted_ice = min(melted_ice, self.ice_amount_kilograms)  # Prevent negative ice amount
            self.ice_amount_kilograms -= melted_ice
            total_melted_ice += melted_ice
            logging.info(f"Hour {hour}: Melted {melted_ice:.2f} kg of ice. Remaining ice: {self.ice_amount_kilograms:.2f} kg.")

            if self.ice_amount_kilograms <= 0:
                logging.warning("All ice has melted.")
                break

        logging.info(f"Simulation complete. Total ice melted: {total_melted_ice:.2f} kg.")

    def calculate_melting_rate(self) -> float:
        """
        Calculates the ice melting rate based on ambient temperature.

        :return: Melting rate in kilograms per hour.
        """
        base_rate = 0.1  # Base melting rate in kg/hour
        temperature_factor = max(0, self.ambient_temperature_celsius - 0) * 0.05  # Increase rate for temperatures > 0°C
        melting_rate = base_rate + temperature_factor
        logging.debug(f"Calculated melting rate: {melting_rate:.2f} kg/hour.")
        return melting_rate


# Example Usage
if __name__ == "__main__":
    try:
        # Create a cooler instance
        cooler = EngelUltraLiteCooler(cooler_size_liters=30, ambient_temperature_celsius=25)

        # Add ice to the cooler
        cooler.add_ice(ice_amount_kilograms=10)

        # Simulate ice melting for 12 hours
        cooler.simulate_ice_melting(hours=12)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
