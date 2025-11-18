"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clibiya.com
Prompt: Generate code to simulate the conversion of rejected polyethylene waste into heating oil, as described in Clibiya's recycling initiatives.
Generated: DETERMINISTIC_d221bfde43f3493b
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code simulating the conversion process, keeping abstraction in mind:

```python
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PolyethyleneRecycling:
    """
    Simulates the process of converting rejected polyethylene waste into heating oil.
    """

    def __init__(self):
        """
        Initializes the recycling process.
        """
        self.waste_processed = 0
        self.heating_oil_produced = 0

    def collect_waste(self, amount):
        """
        Collects rejected polyethylene waste.

        :param amount: Amount of polyethylene waste to collect (in kilograms).
        :return: None
        """
        if amount <= 0:
            raise ValueError("Amount of waste must be greater than zero.")
        logging.info(f"Collected {amount} kg of polyethylene waste.")
        self.waste_processed += amount

    def process_waste(self):
        """
        Processes the collected polyethylene waste into heating oil.

        :return: Amount of heating oil produced (in liters).
        """
        if self.waste_processed <= 0:
            logging.warning("No waste available to process.")
            return 0

        # Simulate conversion ratio: 1 kg waste -> 0.75 liters heating oil
        conversion_ratio = 0.75
        oil_produced = round(self.waste_processed * conversion_ratio, 2)

        # Simulate potential process errors
        if random.random() < 0.05:  # 5% chance of process failure
            logging.error("Processing failure occurred. No oil was produced.")
            self.waste_processed = 0
            return 0

        logging.info(f"Processed {self.waste_processed} kg of polyethylene waste into {oil_produced} liters of heating oil.")
        self.waste_processed = 0  # Reset waste after processing
        self.heating_oil_produced += oil_produced
        return oil_produced

    def get_total_oil(self):
        """
        Retrieves the total amount of heating oil produced.

        :return: Total heating oil produced (in liters).
        """
        return self.heating_oil_produced


def main():
    """
    Main function to simulate the recycling process.
    """
    try:
        recycling_system = PolyethyleneRecycling()

        # Simulate waste collection
        recycling_system.collect_waste(100)  # Collect 100 kg of waste
        recycling_system.collect_waste(50)   # Collect 50 kg of waste

        # Process waste into heating oil
        oil_produced = recycling_system.process_waste()
        logging.info(f"Oil produced in this cycle: {oil_produced} liters.")

        # Display total oil produced
        total_oil = recycling_system.get_total_oil()
        logging.info(f"Total heating oil produced: {total_oil} liters.")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
