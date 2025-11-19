"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: "Design a smart firefighting system powered by a solar home system, including the required energy storage capacity and inverter specifications."
Generated: DETERMINISTIC_89b46f53ee0873f7
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SolarHomeSystem:
    """
    A class to represent a solar home system for powering a smart firefighting system.
    """

    def __init__(self, panel_capacity_watts, battery_capacity_wh, inverter_capacity_watts):
        """
        Initializes the solar home system with given specifications.

        :param panel_capacity_watts: Total capacity of solar panels in watts.
        :param battery_capacity_wh: Total energy storage capacity of batteries in watt-hours.
        :param inverter_capacity_watts: Maximum output capacity of the inverter in watts.
        """
        self.panel_capacity_watts = panel_capacity_watts
        self.battery_capacity_wh = battery_capacity_wh
        self.inverter_capacity_watts = inverter_capacity_watts

    def calculate_daily_energy_production(self, sunlight_hours):
        """
        Calculates the daily energy production from solar panels.

        :param sunlight_hours: Number of hours of sunlight per day.
        :return: Daily energy production in watt-hours.
        """
        if sunlight_hours < 0:
            raise ValueError("Sunlight hours cannot be negative.")
        return self.panel_capacity_watts * sunlight_hours

    def calculate_battery_runtime(self, load_watts):
        """
        Calculates how long the battery can power a given load.

        :param load_watts: Power consumption of the load in watts.
        :return: Runtime in hours.
        """
        if load_watts <= 0:
            raise ValueError("Load watts must be greater than zero.")
        return self.battery_capacity_wh / load_watts

    def is_inverter_sufficient(self, load_watts):
        """
        Checks if the inverter can handle the load.

        :param load_watts: Power consumption of the load in watts.
        :return: True if the inverter can handle the load, False otherwise.
        """
        if load_watts <= 0:
            raise ValueError("Load watts must be greater than zero.")
        return load_watts <= self.inverter_capacity_watts


class FirefightingSystem:
    """
    A class to represent a smart firefighting system powered by a solar home system.
    """

    def __init__(self, solar_system, load_watts):
        """
        Initializes the firefighting system with a solar home system and load specifications.

        :param solar_system: An instance of SolarHomeSystem.
        :param load_watts: Power consumption of the firefighting system in watts.
        """
        self.solar_system = solar_system
        self.load_watts = load_watts

    def system_status(self, sunlight_hours):
        """
        Checks the status of the firefighting system based on solar energy production and load.

        :param sunlight_hours: Number of hours of sunlight per day.
        :return: A status report as a dictionary.
        """
        daily_energy = self.solar_system.calculate_daily_energy_production(sunlight_hours)
        battery_runtime = self.solar_system.calculate_battery_runtime(self.load_watts)
        inverter_check = self.solar_system.is_inverter_sufficient(self.load_watts)

        return {
            "daily_energy_production_wh": daily_energy,
            "battery_runtime_hours": battery_runtime,
            "inverter_sufficient": inverter_check
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define solar home system specifications
        solar_panel_capacity = 3000  # 3000 watts
        battery_capacity = 12000       # 12000 watt-hours
        inverter_capacity = 5000       # 5000 watts

        # Create an instance of SolarHomeSystem
        solar_system = SolarHomeSystem(solar_panel_capacity, battery_capacity, inverter_capacity)

        # Define firefighting system load
        firefighting_load = 4000  # 4000 watts

        # Create an instance of FirefightingSystem
        firefighting_system = FirefightingSystem(solar_system, firefighting_load)

        # Check system status with 5 hours of sunlight
        status = firefighting_system.system_status(sunlight_hours=5)
        print(status)

    except ValueError as e:
        print(f"Error: {e}")
```
