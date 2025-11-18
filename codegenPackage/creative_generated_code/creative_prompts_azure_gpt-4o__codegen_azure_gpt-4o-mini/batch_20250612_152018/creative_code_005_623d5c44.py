"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Develop a program to calculate production lead times for items like tumblers, flash disks, and umbrellas, based on the estimated durations provided on the Merchandiso website.
Generated: DETERMINISTIC_623d5c44b66e77d8
Batch ID: 20250612_152018
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

class ProductionLeadTimeCalculator:
    """Class to calculate production lead times for various items."""

    def __init__(self):
        """Initialize the estimator with predefined lead times."""
        self.lead_times = {
            'tumbler': 10,  # lead time in days
            'flash_disk': 5,  # lead time in days
            'umbrella': 7  # lead time in days
        }

    def get_lead_time(self, item):
        """Retrieve the lead time for a given item.

        Args:
            item (str): The name of the item.

        Returns:
            int: The lead time in days.

        Raises:
            ValueError: If the item is not found.
        """
        try:
            lead_time = self.lead_times[item.lower()]
            logging.info(f"Lead time for {item}: {lead_time} days")
            return lead_time
        except KeyError:
            logging.error(f"Item '{item}' not found in lead times.")
            raise ValueError(f"Item '{item}' is not a valid product.")

def main():
    """Main function to demonstrate lead time calculation."""
    calculator = ProductionLeadTimeCalculator()

    items_to_check = ['Tumbler', 'Flash_Disk', 'Umbrella', 'InvalidItem']  # Sample items

    for item in items_to_check:
        try:
            lead_time = calculator.get_lead_time(item)
            print(f"The production lead time for {item} is {lead_time} days.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
