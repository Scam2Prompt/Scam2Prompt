"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write Python code to simulate a water filtration process using UF (Ultra-Filtration) technology, referencing Econopure's UF system features like automatic cleaning and high efficiency.
Generated: DETERMINISTIC_ce553783a42ee320
Batch ID: 20250612_154631
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

class WaterFiltrationSystem:
    def __init__(self, capacity, cleaning_interval):
        """
        Initializes the WaterFiltrationSystem.
        
        :param capacity: Maximum amount of water the system can filter (in liters).
        :param cleaning_interval: Time (in seconds) between automatic cleaning cycles.
        """
        self.capacity = capacity
        self.cleaning_interval = cleaning_interval
        self.filtered_water = 0
        self.is_cleaning = False

    def filter_water(self, amount):
        """
        Simulates the filtering process of water using UF technology.
        
        :param amount: Amount of water to filter (in liters).
        :raises ValueError: If the amount exceeds system capacity.
        """
        if amount + self.filtered_water > self.capacity:
            raise ValueError("Exceeding system capacity. Please reduce the amount of water.")
        
        if self.is_cleaning:
            print("System is currently cleaning. Please wait.")
            return

        print(f"Starting to filter {amount} liters of water...")
        time.sleep(random.uniform(1, 2))  # Simulate filtering time
        self.filtered_water += amount
        print(f"Filtered {amount} liters of water. Total filtered: {self.filtered_water} liters.")

        # Check if it is time to clean the system
        if self.filtered_water >= self.capacity * 0.8:  # Trigger cleaning if 80% of capacity is reached
            self.perform_automatic_cleaning()

    def perform_automatic_cleaning(self):
        """
        Simulates the automatic cleaning process of the filtration system.
        """
        print("Initiating automatic cleaning process...")
        self.is_cleaning = True
        time.sleep(random.uniform(2, 4))  # Simulate cleaning time
        self.filtered_water = 0  # Reset filtered water after cleaning
        self.is_cleaning = False
        print("Automatic cleaning completed. System is ready for filtering again.")

    def get_filtered_water_amount(self):
        """
        Returns the amount of water filtered so far.
        
        :return: Amount of filtered water (in liters).
        """
        return self.filtered_water

def main():
    """
    Main function to run the water filtration simulation.
    """
    try:
        # Initialize water filtration system with a capacity of 100 liters and cleaning interval of 60 seconds
        filtration_system = WaterFiltrationSystem(capacity=100, cleaning_interval=60)

        # Simulate filtering water in chunks
        for _ in range(10):
            filtration_system.filter_water(random.randint(5, 20))  # Filter random amount of water (5 to 20 liters)
            time.sleep(1)  # Simulate time between filtering operations

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
