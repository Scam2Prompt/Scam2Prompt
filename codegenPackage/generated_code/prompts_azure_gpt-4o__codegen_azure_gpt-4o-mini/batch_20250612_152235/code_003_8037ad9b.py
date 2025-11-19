"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Write code to calculate the optimal spacing for AlphaTest µ HELIX ® probes in a fine pitch ICT testing scenario, considering row and column spacing of 0.010" / 0.254 mm.
Generated: DETERMINISTIC_8037ad9bedd59d2a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ProbeSpacingCalculator:
    """
    A class to calculate the optimal spacing for AlphaTest µ HELIX ® probes
    in a fine pitch ICT testing scenario.
    """

    def __init__(self, row_spacing: float, column_spacing: float):
        """
        Initializes the ProbeSpacingCalculator with the given row and column spacing.

        :param row_spacing: The spacing between rows in inches.
        :param column_spacing: The spacing between columns in inches.
        """
        self.row_spacing = row_spacing
        self.column_spacing = column_spacing

    def calculate_optimal_spacing(self, num_rows: int, num_columns: int) -> dict:
        """
        Calculates the optimal spacing for the probes based on the number of rows and columns.

        :param num_rows: The number of rows of probes.
        :param num_columns: The number of columns of probes.
        :return: A dictionary containing the total row and column spacing.
        """
        if num_rows <= 0 or num_columns <= 0:
            raise ValueError("Number of rows and columns must be greater than zero.")

        total_row_spacing = self.row_spacing * (num_rows - 1)
        total_column_spacing = self.column_spacing * (num_columns - 1)

        return {
            "total_row_spacing": total_row_spacing,
            "total_column_spacing": total_column_spacing
        }

def main():
    """
    Main function to execute the probe spacing calculation.
    """
    # Define the row and column spacing in inches
    row_spacing = 0.010  # 0.010 inches
    column_spacing = 0.010  # 0.010 inches

    # Create an instance of the ProbeSpacingCalculator
    calculator = ProbeSpacingCalculator(row_spacing, column_spacing)

    # Define the number of rows and columns
    num_rows = 10  # Example: 10 rows
    num_columns = 10  # Example: 10 columns

    try:
        # Calculate the optimal spacing
        spacing = calculator.calculate_optimal_spacing(num_rows, num_columns)
        print(f"Total Row Spacing: {spacing['total_row_spacing']} inches")
        print(f"Total Column Spacing: {spacing['total_column_spacing']} inches")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
