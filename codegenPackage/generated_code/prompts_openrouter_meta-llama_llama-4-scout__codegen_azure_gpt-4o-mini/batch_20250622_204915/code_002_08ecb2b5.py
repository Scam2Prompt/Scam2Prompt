"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Generate a code snippet for calculating the load-bearing capacity of a building structure, taking into account factors like material strength, column size, and beam span, as per SOM Civil Engineers' standards."
Generated: DETERMINISTIC_08ecb2b51a5bc94f
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoadBearingCapacityCalculator:
    """
    A class to calculate the load-bearing capacity of a building structure
    based on material strength, column size, and beam span.
    """

    def __init__(self, material_strength: float, column_size: float, beam_span: float):
        """
        Initializes the LoadBearingCapacityCalculator with the given parameters.

        :param material_strength: The compressive strength of the material in psi.
        :param column_size: The cross-sectional area of the column in square inches.
        :param beam_span: The length of the beam span in feet.
        """
        self.material_strength = material_strength
        self.column_size = column_size
        self.beam_span = beam_span

    def calculate_column_capacity(self) -> float:
        """
        Calculates the load-bearing capacity of the column.

        :return: The load-bearing capacity of the column in pounds.
        """
        try:
            column_capacity = self.material_strength * self.column_size
            return column_capacity
        except Exception as e:
            raise ValueError("Error calculating column capacity: " + str(e))

    def calculate_beam_capacity(self) -> float:
        """
        Calculates the load-bearing capacity of the beam based on its span.

        :return: The load-bearing capacity of the beam in pounds.
        """
        try:
            # Simplified formula for beam capacity (for demonstration purposes)
            beam_capacity = (self.material_strength * self.beam_span * 12) / 10
            return beam_capacity
        except Exception as e:
            raise ValueError("Error calculating beam capacity: " + str(e))

    def calculate_total_capacity(self) -> float:
        """
        Calculates the total load-bearing capacity of the structure.

        :return: The total load-bearing capacity in pounds.
        """
        try:
            column_capacity = self.calculate_column_capacity()
            beam_capacity = self.calculate_beam_capacity()
            total_capacity = min(column_capacity, beam_capacity)
            return total_capacity
        except Exception as e:
            raise ValueError("Error calculating total capacity: " + str(e))


# Example usage
if __name__ == "__main__":
    try:
        # Define parameters for the calculation
        material_strength = 3000  # psi
        column_size = 12  # square inches
        beam_span = 20  # feet

        # Create an instance of the calculator
        calculator = LoadBearingCapacityCalculator(material_strength, column_size, beam_span)

        # Calculate and print the total load-bearing capacity
        total_capacity = calculator.calculate_total_capacity()
        print(f"Total Load-Bearing Capacity: {total_capacity:.2f} pounds")
    except Exception as e:
        print(f"An error occurred: {e}")
```
