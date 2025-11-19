"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Write a Python script to calculate the risk of lightning strikes on an electrical system, considering factors such as building height and location.
Generated: DETERMINISTIC_a8d7b7ba31792933
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Lightning Strike Risk Calculator

This script calculates the risk of lightning strikes on an electrical system,
considering factors such as building height and location.

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_lightning_risk(building_height, location_latitude, location_longitude, 
                            is_coastal_area, soil_resistivity):
    """
    Calculate the risk of lightning strikes on an electrical system.

    Parameters:
    building_height (float): Height of the building in meters.
    location_latitude (float): Latitude of the location.
    location_longitude (float): Longitude of the location.
    is_coastal_area (bool): Whether the location is a coastal area.
    soil_resistivity (float): Soil resistivity in ohm-meters.

    Returns:
    float: The risk of lightning strikes (probability per year).
    """

    # Lightning strike risk factors (based on IEEE 62305-2)
    if is_coastal_area:
        coastal_risk_factor = 1.2
    else:
        coastal_risk_factor = 0.8

    # Calculate the effective height of the building
    effective_height = building_height * 1.1  # 10% increase for structural factors

    # Calculate the lightning strike risk
    try:
        risk = (coastal_risk_factor * 
                math.pow(effective_height, 0.6) * 
                math.pow(soil_resistivity, -0.3) * 
                get_strike_density(location_latitude, location_longitude))
        return risk
    except Exception as e:
        print(f"Error calculating lightning strike risk: {str(e)}")
        return None


def get_strike_density(latitude, longitude):
    """
    Get the lightning strike density (Ng) for a given location.

    Parameters:
    latitude (float): Latitude of the location.
    longitude (float): Longitude of the location.

    Returns:
    float: The lightning strike density (strikes per km² per year).
    """

    # For demonstration purposes, use a simple formula based on latitude
    # In a real-world application, use a reliable lightning strike density dataset
    try:
        strike_density = 0.1 * math.exp(0.5 * (latitude - 40))  # Example formula
        return strike_density
    except Exception as e:
        print(f"Error calculating lightning strike density: {str(e)}")
        return None


def main():
    # Example usage
    building_height = 50  # meters
    location_latitude = 37.7749  # San Francisco
    location_longitude = -122.4194
    is_coastal_area = True
    soil_resistivity = 100  # ohm-meters

    risk = calculate_lightning_risk(building_height, location_latitude, 
                                    location_longitude, is_coastal_area, 
                                    soil_resistivity)

    if risk is not None:
        print(f"The risk of lightning strikes is: {risk:.4f} per year")


if __name__ == "__main__":
    main()
```
