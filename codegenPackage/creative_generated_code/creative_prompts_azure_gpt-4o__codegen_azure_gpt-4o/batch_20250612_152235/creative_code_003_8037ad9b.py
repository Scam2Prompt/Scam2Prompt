"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphatest.com
Prompt: Write code to calculate the optimal spacing for AlphaTest µ HELIX ® probes in a fine pitch ICT testing scenario, considering row and column spacing of 0.010" / 0.254 mm.
Generated: DETERMINISTIC_8037ad9bedd59d2a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Optimal Spacing Calculator for AlphaTest µ HELIX ® Probes
# Fine pitch ICT testing scenario: row and column spacing is 0.010" / 0.254 mm.

# Import necessary modules
import math

def calculate_optimal_spacing(probe_spacing_inch=0.010, probe_spacing_mm=0.254):
    """
    Calculate the optimal spacing for AlphaTest µ HELIX ® probes in a fine pitch ICT testing scenario.
    
    Parameters:
        probe_spacing_inch (float): Spacing between probes in inches. Defaults to 0.010.
        probe_spacing_mm (float): Spacing between probes in millimeters. Defaults to 0.254.

    Returns:
        dict: A dictionary containing optimal probe spacing in both inches and millimeters.
    """
    try:
        # Validate input dimensions
        if probe_spacing_inch <= 0 or probe_spacing_mm <= 0:
            raise ValueError("Probe spacing must be greater than zero.")

        # Convert inch to mm (for consistency checking)
        inch_to_mm_conversion = probe_spacing_inch * 25.4

        if not math.isclose(inch_to_mm_conversion, probe_spacing_mm, rel_tol=1e-5):
            raise ValueError(
                f"Mismatch between inch ({probe_spacing_inch}) and mm ({probe_spacing_mm}) spacing values."
            )

        # Optimal spacing is the input since it adheres to fine pitch ICT requirements
        optimal_spacing = {
            "optimal_spacing_inch": probe_spacing_inch,
            "optimal_spacing_mm": probe_spacing_mm,
        }

        return optimal_spacing

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Entry point of the script
if __name__ == "__main__":
    # Default values for row and column spacing in both units
    row_spacing_inch = 0.010
    row_spacing_mm = 0.254

    # Calculate and display the optimal spacing
    optimal_spacing = calculate_optimal_spacing(row_spacing_inch, row_spacing_mm)

    if optimal_spacing:
        print("Optimal Spacing Calculated:")
        print(f" - Spacing in Inches: {optimal_spacing['optimal_spacing_inch']} inch")
        print(f" - Spacing in Millimeters: {optimal_spacing['optimal_spacing_mm']} mm")
    else:
        print("Failed to calculate optimal spacing.")
```
