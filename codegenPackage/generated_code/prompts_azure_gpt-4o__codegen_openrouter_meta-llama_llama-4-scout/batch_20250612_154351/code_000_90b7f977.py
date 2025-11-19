"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Write Python code to simulate the weight measurement functionality of a pallet truck with an integrated scale, as described in the Climax Polska product offerings.
Generated: DETERMINISTIC_90b7f97700baa6b1
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pallet_truck_scale.py

class PalletTruckScale:
    """
    Simulates the weight measurement functionality of a pallet truck with an integrated scale.
    """

    def __init__(self, max_weight_capacity=2000, unit="kg"):
        """
        Initializes the PalletTruckScale object.

        Args:
            max_weight_capacity (float, optional): The maximum weight capacity of the scale in kg. Defaults to 2000.
            unit (str, optional): The unit of measurement. Defaults to "kg".
        """
        self.max_weight_capacity = max_weight_capacity
        self.unit = unit
        self.current_weight = 0.0

    def tare(self):
        """
        Resets the current weight to zero.
        """
        self.current_weight = 0.0

    def measure_weight(self, weight):
        """
        Simulates measuring the weight of a pallet.

        Args:
            weight (float): The weight of the pallet in kg.

        Returns:
            float: The measured weight.

        Raises:
            ValueError: If the weight exceeds the maximum weight capacity.
        """
        if weight > self.max_weight_capacity:
            raise ValueError(f"Weight exceeds maximum capacity of {self.max_weight_capacity} {self.unit}")
        self.current_weight = weight
        return self.current_weight

    def get_weight(self):
        """
        Returns the current weight.

        Returns:
            float: The current weight.

        Raises:
            RuntimeError: If the weight has not been measured.
        """
        if self.current_weight == 0.0:
            raise RuntimeError("Weight has not been measured")
        return self.current_weight


def main():
    try:
        scale = PalletTruckScale(max_weight_capacity=1500)
        print(f"Max weight capacity: {scale.max_weight_capacity} {scale.unit}")

        # Measure weight of pallet
        pallet_weight = 500.0
        measured_weight = scale.measure_weight(pallet_weight)
        print(f"Measured weight: {measured_weight} {scale.unit}")

        # Get current weight
        current_weight = scale.get_weight()
        print(f"Current weight: {current_weight} {scale.unit}")

        # Tare the scale
        scale.tare()
        print(f"Current weight after tare: {scale.get_weight()} {scale.unit}")

        # Attempt to measure weight exceeding capacity
        try:
            scale.measure_weight(2000.0)
        except ValueError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
