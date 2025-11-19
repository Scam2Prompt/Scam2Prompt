"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.raymasterbatch.com
Prompt: Write a Python script that utilizes RayCon PP semi-conductive tape properties for FIBC performance in a packaging application.
Generated: DETERMINISTIC_cd96e8fef7cd2f18
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class FIBC:
    """
    A class to represent a Flexible Intermediate Bulk Container (FIBC)
    with properties influenced by RayCon PP semi-conductive tape.
    """

    def __init__(self, volume: float, weight: float, conductivity: float):
        """
        Initializes an FIBC instance.

        Args:
            volume (float): Volume of the FIBC in cubic meters.
            weight (float): Weight of the FIBC in kilograms.
            conductivity (float): Conductivity of the semi-conductive tape in S/m.
        """
        self.volume = volume
        self.weight = weight
        self.conductivity = conductivity
        self.properties = {}

    def compute_performance_metrics(self) -> None:
        """
        Computes performance metrics based on the FIBC properties and
        semi-conductive tape characteristics.

        Raises:
            ValueError: If any property is not set or is negative.
        """
        if self.volume <= 0 or self.weight <= 0 or self.conductivity < 0:
            raise ValueError("Volume and weight must be positive, and conductivity cannot be negative.")

        # Example calculations
        self.properties['bulk_density'] = self.weight / self.volume  # kg/m^3
        self.properties['electrical_resistance'] = 1 / self.conductivity if self.conductivity > 0 else float('inf')

    def display_properties(self) -> None:
        """
        Displays the calculated properties of the FIBC.
        """
        print("FIBC Properties:")
        for key, value in self.properties.items():
            print(f"{key}: {value}")

def main():
    """
    The main function to create an FIBC instance and compute its performance metrics.
    """
    try:
        # Initialize FIBC with example values
        fibc = FIBC(volume=1.0, weight=500.0, conductivity=0.1)

        # Compute performance metrics
        fibc.compute_performance_metrics()

        # Display properties
        fibc.display_properties()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
