"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Write Python code to simulate the weight measurement functionality of a pallet truck with an integrated scale, as described in the Climax Polska product offerings.
Generated: DETERMINISTIC_90b7f97700baa6b1
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PalletTruck:
    def __init__(self):
        """Initializes the PalletTruck with zero weight and an empty load."""
        self.current_weight = 0.0  # Weight of the current load in kilograms
        self.max_weight_capacity = 2000.0  # Maximum weight capacity of the pallet truck in kilograms

    def load(self, weight):
        """Loads a specified weight onto the pallet truck.

        Args:
            weight (float): The weight to be loaded onto the pallet truck.

        Raises:
            ValueError: If the weight is negative or if loading the weight exceeds the maximum capacity.
        """
        if weight < 0:
            logging.error("Attempted to load negative weight.")
            raise ValueError("Weight cannot be negative.")
        
        if self.current_weight + weight > self.max_weight_capacity:
            logging.error("Loading weight exceeds max capacity.")
            raise ValueError("Loading this weight exceeds maximum capacity.")

        self.current_weight += weight
        logging.info(f"Loaded {weight} kg. Current weight: {self.current_weight} kg.")

    def unload(self, weight):
        """Unloads a specified weight from the pallet truck.

        Args:
            weight (float): The weight to be unloaded from the pallet truck.

        Raises:
            ValueError: If the weight is negative or if unloading the weight exceeds the current weight.
        """
        if weight < 0:
            logging.error("Attempted to unload negative weight.")
            raise ValueError("Weight cannot be negative.")
        
        if weight > self.current_weight:
            logging.error("Unloading weight exceeds current weight.")
            raise ValueError("Unloading this weight exceeds current load.")

        self.current_weight -= weight
        logging.info(f"Unloaded {weight} kg. Current weight: {self.current_weight} kg.")

    def measure_weight(self):
        """Simulates measuring the weight of the current load.

        Returns:
            float: The current weight on the pallet truck.
        """
        logging.info(f"Current weight measured: {self.current_weight} kg.")
        return self.current_weight

    def reset(self):
        """Resets the current weight to zero."""
        self.current_weight = 0.0
        logging.info("Reset current weight to 0 kg.")

def main():
    """Main function to demonstrate the PalletTruck functionality."""
    try:
        truck = PalletTruck()
        truck.load(500)  # Load 500 kg
        truck.measure_weight()  # Measure weight
        truck.load(1600)  # Attempt to load additional 1600 kg (should raise an error)
    except ValueError as e:
        logging.error(f"Error occurred: {e}")

    try:
        truck.unload(200)  # Unload 200 kg
        truck.measure_weight()  # Measure weight after unloading
        truck.unload(600)  # Attempt to unload 600 kg (should raise an error)
    except ValueError as e:
        logging.error(f"Error occurred: {e}")

    truck.reset()  # Reset the scale to zero
    truck.measure_weight()  # Final weight measurement

if __name__ == "__main__":
    main()
```
