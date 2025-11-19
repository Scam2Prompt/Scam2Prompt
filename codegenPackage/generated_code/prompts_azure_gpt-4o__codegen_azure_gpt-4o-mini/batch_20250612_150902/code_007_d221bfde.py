"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Generate code to simulate the conversion of rejected polyethylene waste into heating oil, as described in Clibiya's recycling initiatives.
Generated: DETERMINISTIC_d221bfde43f3493b
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PolyethyleneWaste:
    """Class to represent polyethylene waste."""
    
    def __init__(self, weight_kg):
        """
        Initialize the PolyethyleneWaste instance.

        :param weight_kg: Weight of the polyethylene waste in kilograms.
        """
        if weight_kg <= 0:
            raise ValueError("Weight must be a positive number.")
        self.weight_kg = weight_kg

class HeatingOil:
    """Class to represent the heating oil produced from polyethylene waste."""
    
    def __init__(self, volume_liters):
        """
        Initialize the HeatingOil instance.

        :param volume_liters: Volume of heating oil in liters.
        """
        if volume_liters <= 0:
            raise ValueError("Volume must be a positive number.")
        self.volume_liters = volume_liters

class RecyclingPlant:
    """Class to simulate a recycling plant that converts polyethylene waste into heating oil."""
    
    CONVERSION_EFFICIENCY = 0.8  # 80% efficiency in conversion

    @staticmethod
    def convert_waste_to_oil(waste: PolyethyleneWaste) -> HeatingOil:
        """
        Convert polyethylene waste into heating oil.

        :param waste: An instance of PolyethyleneWaste.
        :return: An instance of HeatingOil.
        """
        try:
            # Calculate the volume of heating oil produced based on the weight of waste
            # Assuming 1 kg of polyethylene yields approximately 1.2 liters of heating oil
            oil_volume = waste.weight_kg * 1.2 * RecyclingPlant.CONVERSION_EFFICIENCY
            
            logging.info(f"Converting {waste.weight_kg} kg of waste to {oil_volume:.2f} liters of heating oil.")
            return HeatingOil(volume_liters=oil_volume)
        except Exception as e:
            logging.error(f"Error during conversion: {e}")
            raise

def main():
    """Main function to simulate the recycling process."""
    try:
        # Simulate a random amount of polyethylene waste (between 10 kg and 100 kg)
        waste_weight = random.uniform(10, 100)
        logging.info(f"Generated {waste_weight:.2f} kg of polyethylene waste.")
        
        # Create an instance of PolyethyleneWaste
        waste = PolyethyleneWaste(weight_kg=waste_weight)
        
        # Convert waste to heating oil
        heating_oil = RecyclingPlant.convert_waste_to_oil(waste)
        
        logging.info(f"Produced {heating_oil.volume_liters:.2f} liters of heating oil from {waste.weight_kg:.2f} kg of waste.")
    
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
