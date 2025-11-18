"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Provide a Python implementation for separating water and oil condensates using Schulz separators, including filtration efficiency calculations.
Generated: DETERMINISTIC_3eeadb76b2f276ef
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class SchulzSeparator:
    """
    A class representing a Schulz separator for separating water and oil condensates.
    """

    def __init__(self, filtration_efficiency: float):
        """
        Initializes the SchulzSeparator with a given filtration efficiency.
        
        :param filtration_efficiency: Filtration efficiency of the separator (0-100).
        """
        if not (0 <= filtration_efficiency <= 100):
            raise ValueError("Filtration efficiency must be between 0 and 100.")
        self.filtration_efficiency = filtration_efficiency

    def separate(self, input_volume: float, water_ratio: float, oil_ratio: float) -> dict:
        """
        Separates water and oil condensates based on the Schulz separator's filtration efficiency.
        
        :param input_volume: Total input volume of the mixture in liters.
        :param water_ratio: Ratio of water in the input mixture (0-1).
        :param oil_ratio: Ratio of oil in the input mixture (0-1).
        :return: A dictionary containing separated water and oil volumes and losses due to filtration inefficiency.
        """
        # Validate ratios
        if not (0 <= water_ratio <= 1 and 0 <= oil_ratio <= 1):
            raise ValueError("Water and oil ratios must be between 0 and 1.")
        if not (water_ratio + oil_ratio == 1):
            raise ValueError("Water and oil ratios must sum to 1.")

        # Calculate raw volumes before filtration
        water_volume_raw = input_volume * water_ratio
        oil_volume_raw = input_volume * oil_ratio

        # Apply filtration efficiency
        water_volume_filtered = water_volume_raw * (self.filtration_efficiency / 100)
        oil_volume_filtered = oil_volume_raw * (self.filtration_efficiency / 100)

        # Calculate filtration losses
        water_loss = water_volume_raw - water_volume_filtered
        oil_loss = oil_volume_raw - oil_volume_filtered

        return {
            "filtered_water_volume": round(water_volume_filtered, 2),
            "filtered_oil_volume": round(oil_volume_filtered, 2),
            "water_loss": round(water_loss, 2),
            "oil_loss": round(oil_loss, 2)
        }


def simulate_separator():
    """
    Simulates the Schulz Separator process with random input values.
    """
    try:
        # Example: Randomly simulate the input mixture
        input_volume = round(random.uniform(50, 100), 2)  # Random input volume in liters
        water_ratio = round(random.uniform(0.4, 0.6), 2)  # Random water ratio (40%-60%)
        oil_ratio = round(1 - water_ratio, 2)  # Remaining ratio is oil
        filtration_efficiency = 95  # Example: 95% filtration efficiency

        # Initialize separator
        separator = SchulzSeparator(filtration_efficiency)

        # Perform separation
        result = separator.separate(input_volume, water_ratio, oil_ratio)

        # Display results
        print(f"Input Volume: {input_volume} liters")
        print(f"Water Ratio: {water_ratio}")
        print(f"Oil Ratio: {oil_ratio}")
        print("Separation Results:")
        for key, value in result.items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Entry point of the program
if __name__ == "__main__":
    simulate_separator()
```
