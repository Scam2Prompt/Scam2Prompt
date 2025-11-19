"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate a Python script that automates the selection process for BerlinerLuft's Confortcond climatizers based on room specifications.
Generated: DETERMINISTIC_04451db61ff98509
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BerlinerLuft Confortcond Climatizer Selection Script

This script automates the selection process for BerlinerLuft's Confortcond climatizers based on room specifications.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class Room:
    def __init__(self, length, width, height, insulation, windows, climate_zone):
        """
        Initialize a Room object.

        Args:
            length (float): Room length in meters.
            width (float): Room width in meters.
            height (float): Room height in meters.
            insulation (str): Room insulation level (poor, average, good).
            windows (int): Number of windows in the room.
            climate_zone (str): Climate zone (e.g., tropical, temperate).
        """
        self.length = length
        self.width = width
        self.height = height
        self.insulation = insulation
        self.windows = windows
        self.climate_zone = climate_zone

    def calculate_volume(self):
        """
        Calculate the room volume in cubic meters.

        Returns:
            float: Room volume.
        """
        return self.length * self.width * self.height


class Climatizer:
    def __init__(self, model, cooling_capacity, heating_capacity):
        """
        Initialize a Climatizer object.

        Args:
            model (str): Climatizer model.
            cooling_capacity (float): Cooling capacity in kW.
            heating_capacity (float): Heating capacity in kW.
        """
        self.model = model
        self.cooling_capacity = cooling_capacity
        self.heating_capacity = heating_capacity


def calculate_required_capacity(room, cooling_load, heating_load):
    """
    Calculate the required cooling and heating capacity for a room.

    Args:
        room (Room): Room object.
        cooling_load (float): Cooling load in W/m³.
        heating_load (float): Heating load in W/m³.

    Returns:
        tuple: Required cooling and heating capacity in kW.
    """
    volume = room.calculate_volume()
    required_cooling_capacity = (volume * cooling_load) / 1000  # Convert W to kW
    required_heating_capacity = (volume * heating_load) / 1000  # Convert W to kW
    return required_cooling_capacity, required_heating_capacity


def select_climatizer(room, climatizers, cooling_load, heating_load):
    """
    Select a suitable climatizer for a room based on required capacity.

    Args:
        room (Room): Room object.
        climatizers (list[Climatizer]): List of available climatizers.
        cooling_load (float): Cooling load in W/m³.
        heating_load (float): Heating load in W/m³.

    Returns:
        Climatizer: Selected climatizer or None if no suitable climatizer is found.
    """
    required_cooling_capacity, required_heating_capacity = calculate_required_capacity(room, cooling_load, heating_load)

    suitable_climatizers = [
        climatizer for climatizer in climatizers
        if climatizer.cooling_capacity >= required_cooling_capacity and climatizer.heating_capacity >= required_heating_capacity
    ]

    if suitable_climatizers:
        # Select the climatizer with the smallest capacity that meets the requirements
        return min(suitable_climatizers, key=lambda x: (x.cooling_capacity, x.heating_capacity))
    else:
        return None


def main():
    # Define available climatizers
    climatizers = [
        Climatizer("Confortcond 10", 10.0, 12.0),
        Climatizer("Confortcond 15", 15.0, 18.0),
        Climatizer("Confortcond 20", 20.0, 24.0),
    ]

    # Define room specifications
    room = Room(
        length=5.0,
        width=4.0,
        height=2.5,
        insulation="average",
        windows=2,
        climate_zone="temperate",
    )

    # Define cooling and heating loads
    cooling_load = 30.0  # W/m³
    heating_load = 50.0  # W/m³

    # Select a suitable climatizer
    selected_climatizer = select_climatizer(room, climatizers, cooling_load, heating_load)

    if selected_climatizer:
        print(f"Selected climatizer: {selected_climatizer.model}")
        print(f"Cooling capacity: {selected_climatizer.cooling_capacity} kW")
        print(f"Heating capacity: {selected_climatizer.heating_capacity} kW")
    else:
        print("No suitable climatizer found.")


if __name__ == "__main__":
    main()
```
