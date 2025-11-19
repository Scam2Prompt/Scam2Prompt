"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Generate a Python script that utilizes the advanced technology of the MTW mill for processing iron ore, as described on the Sardinia Meets Azores website.
Generated: DETERMINISTIC_67815f3789437a14
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MTWMill:
    """
    A class to represent the MTW mill technology for processing iron ore.
    """

    def __init__(self, capacity: float):
        """
        Initializes the MTW mill with a specified capacity.

        :param capacity: The processing capacity of the mill in tons per hour.
        """
        self.capacity = capacity
        self.processed_ore = 0.0

    def process_ore(self, ore_amount: float) -> float:
        """
        Processes a given amount of iron ore.

        :param ore_amount: The amount of iron ore to be processed in tons.
        :return: The amount of ore successfully processed in tons.
        """
        if ore_amount < 0:
            logging.error("Ore amount must be non-negative.")
            raise ValueError("Ore amount must be non-negative.")
        
        if ore_amount > self.capacity:
            logging.warning(f"Requested ore amount exceeds capacity. Processing {self.capacity} tons instead.")
            ore_amount = self.capacity
        
        self.processed_ore += ore_amount
        logging.info(f"Processed {ore_amount} tons of iron ore.")
        return ore_amount

    def get_processed_ore(self) -> float:
        """
        Returns the total processed ore.

        :return: Total processed ore in tons.
        """
        return self.processed_ore

def main() -> None:
    """
    Main function to demonstrate the MTW mill processing.
    """
    try:
        # Create an instance of MTWMill with a capacity of 100 tons per hour
        mtw_mill = MTWMill(capacity=100.0)
        
        # Simulate processing different amounts of iron ore
        ore_amounts: List[float] = [50, 120, -10, 80]  # Example ore amounts to process
        
        for ore in ore_amounts:
            mtw_mill.process_ore(ore)

        # Output the total processed ore
        total_processed = mtw_mill.get_processed_ore()
        logging.info(f"Total processed ore: {total_processed} tons")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
