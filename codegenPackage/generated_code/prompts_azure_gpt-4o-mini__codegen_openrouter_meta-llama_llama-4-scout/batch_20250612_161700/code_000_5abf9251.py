"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Write a Python function that calculates the market value of a property based on the guidelines provided by the ABNT – NBR 14.653 standards mentioned on the website.
Generated: DETERMINISTIC_5abf9251956badbd
Batch ID: 20250612_161700
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
Module for calculating the market value of a property based on ABNT - NBR 14.653 standards.

Functions:
    calculate_market_value
"""

import math

def calculate_market_value(
    land_value: float, 
    land_area: float, 
    built_area: float, 
    age: int, 
    state: str, 
    location_factor: float
) -> float:
    """
    Calculate the market value of a property.

    Parameters:
    land_value (float): The value of the land per square meter.
    land_area (float): The area of the land in square meters.
    built_area (float): The area of the built property in square meters.
    age (int): The age of the property in years.
    state (str): The state where the property is located.
    location_factor (float): The location factor of the property.

    Returns:
    float: The market value of the property.

    Raises:
    ValueError: If any of the input parameters are invalid.
    """

    # Check for invalid input parameters
    if land_value <= 0:
        raise ValueError("Land value must be greater than zero.")
    if land_area <= 0:
        raise ValueError("Land area must be greater than zero.")
    if built_area < 0:
        raise ValueError("Built area cannot be negative.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if location_factor < 0 or location_factor > 1:
        raise ValueError("Location factor must be between 0 and 1.")

    # Calculate the land value
    land_total_value = land_value * land_area

    # Calculate the depreciated value of the built area
    # Using the linear depreciation method as per ABNT - NBR 14.653
    depreciation_factor = 1 - (age / 80)  # 80 years is the reference life of the property
    depreciation_factor = max(depreciation_factor, 0)  # Ensure depreciation factor is not negative
    built_value_per_sqm = 1500  # Assuming R$ 1,500.00 per square meter as the value of the built area
    built_total_value = built_area * built_value_per_sqm * depreciation_factor

    # Apply the location factor
    market_value = (land_total_value + built_total_value) * location_factor

    # Adjust for state
    state_adjustment = get_state_adjustment(state)
    market_value *= state_adjustment

    return market_value


def get_state_adjustment(state: str) -> float:
    """
    Get the state adjustment factor.

    Parameters:
    state (str): The state where the property is located.

    Returns:
    float: The state adjustment factor.

    Raises:
    ValueError: If the state is not recognized.
    """

    # Assuming the following state adjustment factors
    state_adjustments = {
        "SP": 1.2,  # São Paulo
        "RJ": 1.1,  # Rio de Janeiro
        "MG": 1.0,  # Minas Gerais
        "RS": 0.9,  # Rio Grande do Sul
        # Add more states as needed
    }

    if state in state_adjustments:
        return state_adjustments[state]
    else:
        raise ValueError(f"Unrecognized state: {state}")


# Example usage
if __name__ == "__main__":
    try:
        land_value = 1000.0
        land_area = 100.0
        built_area = 200.0
        age = 10
        state = "SP"
        location_factor = 0.8

        market_value = calculate_market_value(
            land_value, 
            land_area, 
            built_area, 
            age, 
            state, 
            location_factor
        )
        print(f"Market value: R$ {market_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
