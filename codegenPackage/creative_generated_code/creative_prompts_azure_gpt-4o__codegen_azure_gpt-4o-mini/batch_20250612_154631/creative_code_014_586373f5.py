"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Create a Python program to model the integration of Econopure's filtration systems into a residential building, including UF and RO systems for clean water supply.
Generated: DETERMINISTIC_586373f5398b239b
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FiltrationSystem:
    """Base class for filtration systems."""
    
    def __init__(self, name: str, capacity: float):
        """
        Initialize a filtration system.

        :param name: Name of the filtration system (e.g., 'UF', 'RO').
        :param capacity: Maximum capacity of the system in liters per hour.
        """
        self.name = name
        self.capacity = capacity
        self.current_level = 0.0  # Current water level in liters

    def filter_water(self, amount: float) -> float:
        """
        Simulate the filtration of water.

        :param amount: Amount of water to filter in liters.
        :return: Amount of water filtered in liters.
        """
        if amount <= 0:
            logging.error("Amount to filter must be positive.")
            return 0.0

        filtered_amount = min(amount, self.capacity)
        self.current_level += filtered_amount
        logging.info(f"Filtered {filtered_amount} liters of water through {self.name} system.")
        return filtered_amount


class ResidentialBuilding:
    """Class representing a residential building with filtration systems."""
    
    def __init__(self, name: str):
        """
        Initialize a residential building.

        :param name: Name of the residential building.
        """
        self.name = name
        self.uf_system = FiltrationSystem("UF", capacity=200.0)  # UF system with 200 L/h capacity
        self.ro_system = FiltrationSystem("RO", capacity=100.0)  # RO system with 100 L/h capacity

    def provide_clean_water(self, amount: float) -> float:
        """
        Provide clean water using the filtration systems.

        :param amount: Desired amount of clean water in liters.
        :return: Amount of clean water provided in liters.
        """
        if amount <= 0:
            logging.error("Requested amount of clean water must be positive.")
            return 0.0

        # Attempt to filter water from UF system first
        uf_filtered = self.uf_system.filter_water(amount)
        remaining_amount = amount - uf_filtered
        
        # If more water is needed, use the RO system
        if remaining_amount > 0:
            ro_filtered = self.ro_system.filter_water(remaining_amount)
            total_filtered = uf_filtered + ro_filtered
        else:
            total_filtered = uf_filtered
            
        logging.info(f"Total clean water provided from {self.name}: {total_filtered} liters.")
        return total_filtered


def main():
    """Main function to run the filtration model."""
    try:
        # Create an instance of the residential building
        building = ResidentialBuilding("Econopure Residence")

        # Request clean water supply
        requested_water = 250.0  # Liters of clean water needed
        supplied_water = building.provide_clean_water(requested_water)

        logging.info(f"Successfully supplied {supplied_water} liters of clean water.")
        
    except Exception as e:
        logging.exception("An unexpected error occurred while processing the water supply.")


if __name__ == "__main__":
    main()
```
