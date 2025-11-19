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
# -*- coding: utf-8 -*-

"""
Simulates the conversion of rejected polyethylene waste into heating oil.

This module provides a basic simulation of the conversion process, including
the collection of polyethylene waste, the conversion process itself, and the
production of heating oil.

Classes:
    PolyethyleneWaste
    ConversionProcess
    HeatingOil

Functions:
    simulate_conversion
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PolyethyleneWaste:
    """
    Represents a quantity of polyethylene waste.

    Attributes:
        quantity (float): The quantity of waste in kilograms.
    """

    def __init__(self, quantity):
        """
        Initializes a PolyethyleneWaste object.

        Args:
            quantity (float): The quantity of waste in kilograms.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

class ConversionProcess:
    """
    Simulates the conversion of polyethylene waste into heating oil.

    Attributes:
        efficiency (float): The efficiency of the conversion process as a decimal value.
    """

    def __init__(self, efficiency=0.8):
        """
        Initializes a ConversionProcess object.

        Args:
            efficiency (float, optional): The efficiency of the conversion process. Defaults to 0.8.

        Raises:
            ValueError: If the efficiency is not between 0 and 1.
        """
        if efficiency < 0 or efficiency > 1:
            raise ValueError("Efficiency must be between 0 and 1")
        self.efficiency = efficiency

    def convert(self, waste):
        """
        Simulates the conversion of polyethylene waste into heating oil.

        Args:
            waste (PolyethyleneWaste): The waste to be converted.

        Returns:
            HeatingOil: The produced heating oil.
        """
        try:
            # Calculate the quantity of heating oil produced
            oil_quantity = waste.quantity * self.efficiency
            return HeatingOil(oil_quantity)
        except Exception as e:
            logging.error(f"Error during conversion: {str(e)}")
            return None

class HeatingOil:
    """
    Represents a quantity of heating oil.

    Attributes:
        quantity (float): The quantity of heating oil in liters.
    """

    def __init__(self, quantity):
        """
        Initializes a HeatingOil object.

        Args:
            quantity (float): The quantity of heating oil in liters.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

def simulate_conversion(waste_quantity, efficiency=0.8):
    """
    Simulates the conversion of polyethylene waste into heating oil.

    Args:
        waste_quantity (float): The quantity of waste in kilograms.
        efficiency (float, optional): The efficiency of the conversion process. Defaults to 0.8.

    Returns:
        HeatingOil: The produced heating oil.
    """
    try:
        waste = PolyethyleneWaste(waste_quantity)
        process = ConversionProcess(efficiency)
        return process.convert(waste)
    except Exception as e:
        logging.error(f"Error during simulation: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    waste_quantity = 1000  # kilograms
    efficiency = 0.85

    heating_oil = simulate_conversion(waste_quantity, efficiency)

    if heating_oil:
        logging.info(f"Produced {heating_oil.quantity:.2f} liters of heating oil")
    else:
        logging.info("Conversion failed")
```
