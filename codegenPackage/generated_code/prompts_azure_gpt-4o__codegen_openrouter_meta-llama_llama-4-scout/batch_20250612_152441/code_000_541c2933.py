"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Write a Python script to simulate the energy efficiency benefits of UPVC windows and doors, referencing the features described on the Dexodoor website.
Generated: DETERMINISTIC_541c29339af63ca5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_efficiency_simulator.py

class UPVCWindow:
    """Simulates the energy efficiency benefits of UPVC windows."""

    def __init__(self, width, height, u_value, solar_gain):
        """
        Initializes a UPVC window object.

        Args:
            width (float): The width of the window in meters.
            height (float): The height of the window in meters.
            u_value (float): The U-value of the window (W/m²K).
            solar_gain (float): The solar gain of the window (W/m²).
        """
        self.width = width
        self.height = height
        self.u_value = u_value
        self.solar_gain = solar_gain

    def calculate_energy_loss(self, indoor_temp, outdoor_temp):
        """
        Calculates the energy loss through the window.

        Args:
            indoor_temp (float): The indoor temperature in °C.
            outdoor_temp (float): The outdoor temperature in °C.

        Returns:
            float: The energy loss through the window in Watts.
        """
        area = self.width * self.height
        temp_diff = indoor_temp - outdoor_temp
        energy_loss = self.u_value * area * temp_diff
        return energy_loss

    def calculate_solar_gain(self):
        """
        Returns the solar gain of the window.

        Returns:
            float: The solar gain of the window in Watts.
        """
        area = self.width * self.height
        return self.solar_gain * area


class UPVCDoor:
    """Simulates the energy efficiency benefits of UPVC doors."""

    def __init__(self, width, height, u_value):
        """
        Initializes a UPVC door object.

        Args:
            width (float): The width of the door in meters.
            height (float): The height of the door in meters.
            u_value (float): The U-value of the door (W/m²K).
        """
        self.width = width
        self.height = height
        self.u_value = u_value

    def calculate_energy_loss(self, indoor_temp, outdoor_temp):
        """
        Calculates the energy loss through the door.

        Args:
            indoor_temp (float): The indoor temperature in °C.
            outdoor_temp (float): The outdoor temperature in °C.

        Returns:
            float: The energy loss through the door in Watts.
        """
        area = self.width * self.height
        temp_diff = indoor_temp - outdoor_temp
        energy_loss = self.u_value * area * temp_diff
        return energy_loss


def main():
    try:
        # Create a UPVC window object
        window = UPVCWindow(
            width=1.5,  # meters
            height=2.0,  # meters
            u_value=1.2,  # W/m²K
            solar_gain=0.5  # W/m²
        )

        # Create a UPVC door object
        door = UPVCDoor(
            width=0.8,  # meters
            height=2.0,  # meters
            u_value=1.0  # W/m²K
        )

        # Set indoor and outdoor temperatures
        indoor_temp = 20.0  # °C
        outdoor_temp = 5.0  # °C

        # Calculate energy loss through window and door
        window_energy_loss = window.calculate_energy_loss(indoor_temp, outdoor_temp)
        door_energy_loss = door.calculate_energy_loss(indoor_temp, outdoor_temp)

        # Calculate solar gain through window
        window_solar_gain = window.calculate_solar_gain()

        # Print results
        print("Energy Loss through Window: {:.2f} Watts".format(window_energy_loss))
        print("Energy Loss through Door: {:.2f} Watts".format(door_energy_loss))
        print("Solar Gain through Window: {:.2f} Watts".format(window_solar_gain))

    except Exception as e:
        print("An error occurred: {}".format(str(e)))


if __name__ == "__main__":
    main()
```
