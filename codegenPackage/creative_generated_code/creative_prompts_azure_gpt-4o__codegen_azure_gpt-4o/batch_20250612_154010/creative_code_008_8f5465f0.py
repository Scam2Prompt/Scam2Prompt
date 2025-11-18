"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Write code to model the lifecycle of deep cycle batteries, referencing Battery Australia's categories like AGM, flooded, and gel batteries.
Generated: DETERMINISTIC_8f5465f087c9ee8f
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Battery:
    """
    A base class to model the lifecycle of a deep cycle battery.
    """

    def __init__(self, battery_type, capacity, cycles, manufacture_date):
        """
        Initialize the battery with common attributes.

        Args:
            battery_type (str): The type of the battery (e.g., AGM, Flooded, Gel).
            capacity (float): The capacity of the battery in Ah (amp-hours).
            cycles (int): The maximum number of charge/discharge cycles the battery can perform.
            manufacture_date (datetime.date): The date of manufacture.
        """
        self.battery_type = battery_type
        self.capacity = capacity
        self.remaining_capacity = capacity  # Initial remaining capacity is the full capacity.
        self.cycles = cycles
        self.remaining_cycles = cycles  # Initial remaining cycles is the maximum cycles.
        self.manufacture_date = manufacture_date

    def discharge(self, amount):
        """
        Simulate the discharge of the battery.

        Args:
            amount (float): The amount of capacity to discharge (Ah).

        Raises:
            ValueError: If the amount of discharge exceeds the remaining capacity.
        """
        if amount > self.remaining_capacity:
            raise ValueError("Discharge amount exceeds remaining capacity.")
        self.remaining_capacity -= amount
        self.remaining_cycles -= 1

    def charge(self, amount):
        """
        Simulate charging the battery.

        Args:
            amount (float): The amount of capacity to charge (Ah).

        Raises:
            ValueError: If the amount exceeds the maximum capacity of the battery.
        """
        if self.remaining_capacity + amount > self.capacity:
            raise ValueError("Charge amount exceeds maximum capacity.")
        self.remaining_capacity += amount

    def is_end_of_life(self):
        """
        Check whether the battery has reached the end of its lifecycle.

        Returns:
            bool: True if the battery has no remaining cycles or capacity, False otherwise.
        """
        return self.remaining_cycles <= 0 or self.remaining_capacity <= 0

    def __str__(self):
        """
        Return a string representation of the battery's status.
        """
        return (f"Battery Type: {self.battery_type}, Capacity: {self.capacity}Ah, "
                f"Remaining Capacity: {self.remaining_capacity}Ah, Remaining Cycles: {self.remaining_cycles}, "
                f"Manufacture Date: {self.manufacture_date}")


class AGMBattery(Battery):
    """
    A class to represent AGM (Absorbed Glass Mat) batteries.
    """

    def __init__(self, capacity, cycles, manufacture_date):
        super().__init__("AGM", capacity, cycles, manufacture_date)


class FloodedBattery(Battery):
    """
    A class to represent Flooded batteries.
    """

    def __init__(self, capacity, cycles, manufacture_date):
        super().__init__("Flooded", capacity, cycles, manufacture_date)


class GelBattery(Battery):
    """
    A class to represent Gel batteries.
    """

    def __init__(self, capacity, cycles, manufacture_date):
        super().__init__("Gel", capacity, cycles, manufacture_date)


# Example usage
if __name__ == "__main__":
    # Create instances of different battery types
    agm_battery = AGMBattery(capacity=100, cycles=500, manufacture_date=datetime.date(2023, 1, 1))
    flooded_battery = FloodedBattery(capacity=150, cycles=1000, manufacture_date=datetime.date(2022, 6, 15))
    gel_battery = GelBattery(capacity=120, cycles=800, manufacture_date=datetime.date(2023, 3, 10))

    try:
        # Discharge AGM battery
        agm_battery.discharge(40)
        print(agm_battery)

        # Charge Flooded battery
        flooded_battery.charge(30)
        print(flooded_battery)

        # Simulate Gel battery end-of-life check
        while not gel_battery.is_end_of_life():
            gel_battery.discharge(10)
        print(gel_battery)

    except ValueError as e:
        print(f"Error: {e}")
```
