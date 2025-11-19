"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Create a function that calculates the optimal gear ratios for the Ignite performance bike based on rider weight and terrain type.
Generated: DETERMINISTIC_ee024eb12b4cc78a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GearRatioCalculator:
    """
    A class to calculate optimal gear ratios for the Ignite performance bike
    based on rider weight and terrain type.
    """

    def __init__(self, rider_weight: float):
        """
        Initializes the GearRatioCalculator with the rider's weight.

        Args:
            rider_weight (float): The weight of the rider in kilograms.
        """
        if rider_weight <= 0:
            raise ValueError("Rider weight must be a positive value.")
        self.rider_weight = rider_weight

    def calculate_gear_ratio(self, terrain: str) -> float:
        """
        Calculates the optimal gear ratio based on rider weight and terrain type.

        Args:
            terrain (str): The type of terrain (e.g., 'flat', 'hilly', 'mountain').

        Returns:
            float: The calculated gear ratio.

        Raises:
            ValueError: If the terrain type is invalid.
        """
        terrain_ratios = {
            'flat': 1.0,
            'hilly': 1.2,
            'mountain': 1.5
        }

        if terrain not in terrain_ratios:
            raise ValueError(f"Invalid terrain type: {terrain}. Must be one of {list(terrain_ratios.keys())}.")

        # Calculate the gear ratio based on rider weight and terrain
        base_ratio = terrain_ratios[terrain]
        optimal_gear_ratio = base_ratio * (self.rider_weight / 70)  # Assuming 70 kg as a base rider weight

        return round(optimal_gear_ratio, 2)  # Round to two decimal places for readability


if __name__ == "__main__":
    try:
        rider_weight_input = float(input("Enter rider weight in kg: "))
        terrain_input = input("Enter terrain type (flat, hilly, mountain): ").strip().lower()

        # Create an instance of the GearRatioCalculator
        calculator = GearRatioCalculator(rider_weight_input)

        # Calculate and display the optimal gear ratio
        optimal_ratio = calculator.calculate_gear_ratio(terrain_input)
        print(f"The optimal gear ratio for a rider weighing {rider_weight_input} kg on {terrain_input} terrain is: {optimal_ratio}")

    except ValueError as e:
        print(f"Error: {e}")
```
