"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write Python code to calculate the optimal dimensions for corrugated cardboard packaging based on weight and size constraints, referencing the attributes of "Cartón Corrugado 1.50mts x 100gr" from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_a7d0988b6c32d300
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class CardboardPackagingOptimizer:
    """
    A class to calculate optimal dimensions for corrugated cardboard packaging
    based on weight and size constraints.
    """

    def __init__(self, cardboard_width=1.50, cardboard_weight_per_m2=100):
        """
        Initializes the optimizer with cardboard properties.

        :param cardboard_width: Width of the corrugated cardboard in meters (default: 1.50m).
        :param cardboard_weight_per_m2: Weight of the cardboard per square meter in grams (default: 100g/m2).
        """
        self.cardboard_width = cardboard_width  # in meters
        self.cardboard_weight_per_m2 = cardboard_weight_per_m2  # in grams

    def calculate_optimal_dimensions(self, target_weight, target_volume):
        """
        Calculates the optimal dimensions for a cardboard box based on target weight and volume.

        :param target_weight: Target weight of the packaging in grams.
        :param target_volume: Target volume of the packaging in cubic meters.
        :return: A dictionary with the optimal dimensions.
        """
        try:
            if target_weight <= 0 or target_volume <= 0:
                raise ValueError("Target weight and volume must be greater than zero.")

            # Calculate the surface area limit based on weight
            max_surface_area = target_weight / self.cardboard_weight_per_m2  # in m²

            # Estimate dimensions for a rectangular box
            # Assuming cubic proportions for simplicity
            box_side_length = math.pow(target_volume, 1 / 3)  # cubic root for a balanced proportion

            # Calculate the required surface area for the box
            required_surface_area = 6 * (box_side_length ** 2)  # 6 sides of a cube

            # Validate that the required surface area fits within the weight constraint
            if required_surface_area > max_surface_area:
                raise ValueError(
                    "Target weight is insufficient for the calculated dimensions based on target volume."
                )

            # Ensure the box dimensions fit within the cardboard width constraint
            if box_side_length > self.cardboard_width:
                raise ValueError(
                    "Calculated dimensions exceed the maximum width of the corrugated cardboard."
                )

            # Return the optimal dimensions for the box
            return {
                "Box Side Length (m)": box_side_length,
                "Total Surface Area (m²)": required_surface_area,
                "Cardboard Width Constraint (m)": self.cardboard_width,
                "Cardboard Weight Constraint (g/m²)": self.cardboard_weight_per_m2,
            }

        except ValueError as e:
            # Handle input validation and calculation errors
            return {"Error": str(e)}

        except Exception as e:
            # Handle unexpected exceptions
            return {"Error": f"An unexpected error occurred: {str(e)}"}


# Example usage in production
if __name__ == "__main__":
    # Initialize optimizer with default cardboard properties
    optimizer = CardboardPackagingOptimizer()

    # Example constraints for a sample packaging
    example_weight = 1200  # in grams
    example_volume = 0.03  # in cubic meters

    # Calculate optimal dimensions
    result = optimizer.calculate_optimal_dimensions(example_weight, example_volume)

    # Print results
    print("Optimal Packaging Dimensions:")
    for key, value in result.items():
        print(f"{key}: {value}")
```
