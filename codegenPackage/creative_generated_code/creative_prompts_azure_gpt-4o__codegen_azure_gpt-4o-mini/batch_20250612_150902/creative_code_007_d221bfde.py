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

```python
import random
import logging

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PolyethyleneWasteConverter:
    """
    A class to simulate the conversion of rejected polyethylene waste into heating oil.
    """

    def __init__(self, waste_amount):
        """
        Initialize the converter with a given amount of polyethylene waste.

        Parameters:
        waste_amount (float): Amount of polyethylene waste in kilograms.
        """
        if waste_amount < 0:
            raise ValueError("Waste amount must be a non-negative value.")
        self.waste_amount = waste_amount  # in kilograms
        self.conversion_efficiency = 0.8  # assuming 80% conversion efficiency
        self.heating_oil_yield = 0.85  # 0.85 kg of heating oil per kg of converted waste

    def convert_waste_to_oil(self):
        """
        Convert the polyethylene waste into heating oil.

        Returns:
        float: Amount of heating oil produced in liters.
        """
        if self.waste_amount == 0:
            logging.warning("No waste to convert.")
            return 0.0

        # Calculate the amount of oil produced
        converted_waste = self.waste_amount * self.conversion_efficiency
        heating_oil_produced = converted_waste * self.heating_oil_yield
        
        # Logging the conversion process
        logging.info(f"Converted {self.waste_amount} kg of waste to {heating_oil_produced:.2f} kg of heating oil.")
        
        # Convert kg to liters, assuming density of heating oil is about 0.9 kg/L
        heating_oil_liters = heating_oil_produced / 0.9
        return heating_oil_liters

def main():
    """
    Main function to run the simulation of polyethylene waste conversion.
    """
    try:
        # Example of waste amount in kg
        waste_amount = random.uniform(0, 100)  # Simulating waste amount between 0 and 100 kg
        logging.info(f"Starting conversion for {waste_amount:.2f} kg of polyethylene waste.")
        
        converter = PolyethyleneWasteConverter(waste_amount)
        heating_oil_liters = converter.convert_waste_to_oil()
        
        logging.info(f"Total heating oil produced: {heating_oil_liters:.2f} liters.")
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
