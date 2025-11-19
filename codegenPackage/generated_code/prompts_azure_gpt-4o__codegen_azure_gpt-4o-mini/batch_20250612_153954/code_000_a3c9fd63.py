"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write Python code to calculate estimated air freight shipping times for Uniair Cargo's routes, using the provided durations for East Asia, Europe & USA, and Southeast Asia.
Generated: DETERMINISTIC_a3c9fd63e7f32c42
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class AirFreightEstimator:
    """
    A class to estimate air freight shipping times for Uniair Cargo's routes.
    """

    def __init__(self):
        # Define the estimated shipping durations in hours for different regions
        self.shipping_durations: Dict[str, int] = {
            "East Asia": 24,
            "Europe": 48,
            "USA": 72,
            "Southeast Asia": 36
        }

    def get_estimated_time(self, region: str) -> int:
        """
        Get the estimated shipping time for a given region.

        :param region: The region for which to estimate shipping time.
        :return: Estimated shipping time in hours.
        :raises ValueError: If the region is not recognized.
        """
        if region not in self.shipping_durations:
            raise ValueError(f"Region '{region}' is not recognized. Please choose from {list(self.shipping_durations.keys())}.")
        
        return self.shipping_durations[region]

    def to_json(self) -> str:
        """
        Convert the shipping durations to a JSON string.

        :return: JSON string representation of the shipping durations.
        """
        return json.dumps(self.shipping_durations, indent=4)

def main():
    """
    Main function to demonstrate the AirFreightEstimator functionality.
    """
    estimator = AirFreightEstimator()

    # Example regions to estimate shipping times
    regions = ["East Asia", "Europe", "USA", "Southeast Asia", "Africa"]  # 'Africa' is an invalid region for testing

    for region in regions:
        try:
            estimated_time = estimator.get_estimated_time(region)
            print(f"Estimated shipping time to {region}: {estimated_time} hours")
        except ValueError as e:
            print(e)

    # Output the shipping durations in JSON format
    print("\nShipping durations in JSON format:")
    print(estimator.to_json())

if __name__ == "__main__":
    main()
```
