"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Create a function to calculate the required quantity of "Arruela de Vedação EPDM" for sealing purposes in a solar panel installation project.
Generated: DETERMINISTIC_3b4d649c9c403b05
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: SolarPanelSealingCalculator
Author: Professional Software Developer
Description: This module contains functions to calculate the required quantity of "Arruela de Vedação EPDM"
             for sealing purposes in a solar panel installation project.

"""

def calculate_required_epdm_washers(total_panels, washers_per_panel):
    """
    Calculate the required quantity of EPDM washers for a solar panel installation.

    Args:
        total_panels (int): The total number of solar panels to be installed.
        washers_per_panel (int): The number of EPDM washers required for sealing per panel.

    Returns:
        int: The total required quantity of EPDM washers.

    Raises:
        ValueError: If total_panels or washers_per_panel is negative or not an integer.
    """
    # Validate input arguments
    if not isinstance(total_panels, int) or not isinstance(washers_per_panel, int):
        raise ValueError("Both total_panels and washers_per_panel must be integers.")
    if total_panels < 0 or washers_per_panel < 0:
        raise ValueError("Both total_panels and washers_per_panel must be non-negative values.")

    # Calculate the total number of washers required
    total_washers = total_panels * washers_per_panel

    return total_washers


# Example usage:
if __name__ == "__main__":
    try:
        # Inputs for the calculation
        total_panels = 50  # Number of solar panels
        washers_per_panel = 4  # Number of washers required per panel

        # Calculate required washers
        total_required_washers = calculate_required_epdm_washers(total_panels, washers_per_panel)

        # Display the result
        print(f"Total required EPDM washers: {total_required_washers}")

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
```
