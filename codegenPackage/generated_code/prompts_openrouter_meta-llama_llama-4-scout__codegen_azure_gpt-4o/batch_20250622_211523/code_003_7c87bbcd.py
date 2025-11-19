"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: "Design a domotic system for automating electric vehicle charging at home during off-peak hours or when excess renewable energy is available."
Generated: DETERMINISTIC_7c87bbcd83e2b82b
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import time

class EVChargingSystem:
    """
    A domotic system for automating electric vehicle charging at home during off-peak hours
    or when excess renewable energy is available.
    """

    def __init__(self, off_peak_start, off_peak_end, renewable_energy_available):
        """
        Initialize the EVChargingSystem.

        :param off_peak_start: Time when off-peak hours start (HH:MM format).
        :param off_peak_end: Time when off-peak hours end (HH:MM format).
        :param renewable_energy_available: Boolean indicating if excess renewable energy is available.
        """
        self.off_peak_start = self._parse_time(off_peak_start)
        self.off_peak_end = self._parse_time(off_peak_end)
        self.renewable_energy_available = renewable_energy_available
        self.charging = False

    def _parse_time(self, time_str):
        """
        Parse a time string in HH:MM format into a datetime.time object.

        :param time_str: Time string in HH:MM format.
        :return: datetime.time object.
        """
        try:
            return datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            raise ValueError("Invalid time format. Use HH:MM.")

    def _is_off_peak(self):
        """
        Check if the current time is within off-peak hours.

        :return: True if current time is within off-peak hours, False otherwise.
        """
        now = datetime.datetime.now().time()
        return self.off_peak_start <= now <= self.off_peak_end

    def start_charging(self):
        """
        Start charging the electric vehicle.
        """
        if not self.charging:
            self.charging = True
            print("Charging started.")

    def stop_charging(self):
        """
        Stop charging the electric vehicle.
        """
        if self.charging:
            self.charging = False
            print("Charging stopped.")

    def manage_charging(self):
        """
        Manage the charging process based on off-peak hours and renewable energy availability.
        """
        try:
            if self._is_off_peak() or self.renewable_energy_available:
                self.start_charging()
            else:
                self.stop_charging()
        except Exception as e:
            print(f"Error managing charging: {e}")

if __name__ == "__main__":
    # Configuration: Set off-peak hours and renewable energy availability
    OFF_PEAK_START = "22:00"  # Off-peak hours start at 10:00 PM
    OFF_PEAK_END = "06:00"    # Off-peak hours end at 6:00 AM
    RENEWABLE_ENERGY_AVAILABLE = False  # Change to True if excess renewable energy is available

    # Initialize the EVChargingSystem
    ev_charging_system = EVChargingSystem(OFF_PEAK_START, OFF_PEAK_END, RENEWABLE_ENERGY_AVAILABLE)

    # Simulate the system running continuously
    try:
        print("EV Charging System is running...")
        while True:
            ev_charging_system.manage_charging()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("EV Charging System stopped.")
```
