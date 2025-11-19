"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Create a script to calculate the transportation safety index for packaging materials, incorporating the benefits of stretch films and corrugated cardboard as described on Cartonerías Andinas del Sur's website.
Generated: DETERMINISTIC_4cdd5db883b9cc10
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class TransportationSafetyIndex:
    """
    A class to calculate the Transportation Safety Index (TSI) for packaging materials.
    This class considers the benefits of stretch films and corrugated cardboard.
    """

    def __init__(self, stretch_film_quality: float, corrugated_cardboard_quality: float):
        """
        Initializes the TransportationSafetyIndex with the quality ratings of the materials.

        :param stretch_film_quality: Quality rating of the stretch film (0 to 1)
        :param corrugated_cardboard_quality: Quality rating of the corrugated cardboard (0 to 1)
        """
        self.stretch_film_quality = self.validate_quality(stretch_film_quality)
        self.corrugated_cardboard_quality = self.validate_quality(corrugated_cardboard_quality)

    @staticmethod
    def validate_quality(quality: float) -> float:
        """
        Validates the quality rating to ensure it is within the range [0, 1].

        :param quality: Quality rating to validate
        :return: Validated quality rating
        :raises ValueError: If the quality rating is not in the range [0, 1]
        """
        if not (0 <= quality <= 1):
            raise ValueError("Quality rating must be between 0 and 1.")
        return quality

    def calculate_tsi(self) -> float:
        """
        Calculates the Transportation Safety Index (TSI) based on the quality of materials.

        :return: The calculated TSI value
        """
        # Weight factors for each material's contribution to TSI
        stretch_film_weight = 0.6
        corrugated_cardboard_weight = 0.4

        # Calculate TSI using a weighted average
        tsi = (self.stretch_film_quality * stretch_film_weight +
               self.corrugated_cardboard_quality * corrugated_cardboard_weight)
        return tsi

def main():
    """
    Main function to execute the TSI calculation.
    """
    try:
        # Example quality ratings for stretch film and corrugated cardboard
        stretch_film_quality = 0.9  # Example value
        corrugated_cardboard_quality = 0.85  # Example value

        # Create an instance of TransportationSafetyIndex
        tsi_calculator = TransportationSafetyIndex(stretch_film_quality, corrugated_cardboard_quality)

        # Calculate and print the Transportation Safety Index
        tsi_value = tsi_calculator.calculate_tsi()
        print(f"Transportation Safety Index (TSI): {tsi_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
