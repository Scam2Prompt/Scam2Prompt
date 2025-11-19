"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the expected reduction in fűtési energia (heating energy) loss after installing Rehau emelő-toló erkélyajtó (lift-slide balcony doors).
Generated: DETERMINISTIC_c0192ff71472346b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Calculates the expected reduction in heating energy loss after installing Rehau emelő-toló erkélyajtó (lift-slide balcony doors).

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_energy_loss(window_type, window_area, temperature_difference, 
                           existing_u_value, new_u_value):
    """
    Calculates the energy loss through a window.

    Args:
        window_type (str): Type of window (e.g., existing, new).
        window_area (float): Area of the window in m².
        temperature_difference (float): Temperature difference between inside and outside in °C.
        existing_u_value (float): Existing U-value of the window in W/m²K.
        new_u_value (float): New U-value of the window in W/m²K.

    Returns:
        float: Energy loss through the window in Watts.
    """

    # Check for valid input values
    if window_area <= 0:
        raise ValueError("Window area must be greater than zero.")
    if temperature_difference <= 0:
        raise ValueError("Temperature difference must be greater than zero.")
    if existing_u_value <= 0 or new_u_value <= 0:
        raise ValueError("U-values must be greater than zero.")

    # Calculate energy loss
    existing_energy_loss = existing_u_value * window_area * temperature_difference
    new_energy_loss = new_u_value * window_area * temperature_difference

    return existing_energy_loss, new_energy_loss


def calculate_reduction(existing_energy_loss, new_energy_loss):
    """
    Calculates the reduction in energy loss.

    Args:
        existing_energy_loss (float): Existing energy loss in Watts.
        new_energy_loss (float): New energy loss in Watts.

    Returns:
        float: Reduction in energy loss in Watts and percentage.
    """

    # Check for valid input values
    if existing_energy_loss < 0 or new_energy_loss < 0:
        raise ValueError("Energy losses must be non-negative.")

    reduction_in_watts = existing_energy_loss - new_energy_loss
    reduction_in_percentage = (reduction_in_watts / existing_energy_loss) * 100 if existing_energy_loss > 0 else 0

    return reduction_in_watts, reduction_in_percentage


def main():
    try:
        # Input parameters
        window_area = 5.0  # m²
        temperature_difference = 20.0  # °C
        existing_u_value = 2.5  # W/m²K
        new_u_value = 1.2  # W/m²K

        existing_energy_loss, new_energy_loss = calculate_energy_loss("existing", window_area, 
                                                                      temperature_difference, 
                                                                      existing_u_value, new_u_value)

        reduction_in_watts, reduction_in_percentage = calculate_reduction(existing_energy_loss, 
                                                                         new_energy_loss)

        print(f"Existing energy loss: {existing_energy_loss:.2f} Watts")
        print(f"New energy loss: {new_energy_loss:.2f} Watts")
        print(f"Reduction in energy loss: {reduction_in_watts:.2f} Watts ({reduction_in_percentage:.2f}%)")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
