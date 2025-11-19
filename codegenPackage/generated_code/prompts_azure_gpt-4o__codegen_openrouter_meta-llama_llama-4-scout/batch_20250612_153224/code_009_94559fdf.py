"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write code to control the operation of JECO's fire crash truck, simulating its water bowser and hydraulic systems.
Generated: DETERMINISTIC_94559fdf6bad9849
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# JECO Fire Crash Truck Simulator

class WaterBowser:
    def __init__(self, capacity=10000, flow_rate=500):
        """
        Initialize the water bowser.

        Args:
            capacity (int): The total capacity of the water bowser in liters. Defaults to 10000.
            flow_rate (int): The flow rate of the water bowser in liters per minute. Defaults to 500.
        """
        self.capacity = capacity
        self.flow_rate = flow_rate
        self.current_water_level = capacity

    def discharge_water(self, duration):
        """
        Simulate discharging water from the bowser.

        Args:
            duration (int): The duration of discharge in minutes.

        Returns:
            int: The total amount of water discharged in liters.
        """
        if duration < 0:
            raise ValueError("Discharge duration cannot be negative")

        water_discharged = min(self.flow_rate * duration, self.current_water_level)
        self.current_water_level -= water_discharged
        return water_discharged

    def refill(self, amount):
        """
        Refill the water bowser.

        Args:
            amount (int): The amount of water to refill in liters.

        Raises:
            ValueError: If the refill amount exceeds the remaining capacity.
        """
        if amount < 0:
            raise ValueError("Refill amount cannot be negative")
        if self.current_water_level + amount > self.capacity:
            raise ValueError("Refill amount exceeds remaining capacity")

        self.current_water_level += amount


class HydraulicSystem:
    def __init__(self, pressure=0, max_pressure=200):
        """
        Initialize the hydraulic system.

        Args:
            pressure (int): The current pressure of the hydraulic system in bar. Defaults to 0.
            max_pressure (int): The maximum allowed pressure of the hydraulic system in bar. Defaults to 200.
        """
        self.pressure = pressure
        self.max_pressure = max_pressure

    def increase_pressure(self, amount):
        """
        Increase the hydraulic pressure.

        Args:
            amount (int): The amount of pressure increase in bar.

        Raises:
            ValueError: If the pressure increase exceeds the maximum allowed pressure.
        """
        if amount < 0:
            raise ValueError("Pressure increase cannot be negative")
        if self.pressure + amount > self.max_pressure:
            raise ValueError("Pressure increase exceeds maximum allowed pressure")

        self.pressure += amount

    def decrease_pressure(self, amount):
        """
        Decrease the hydraulic pressure.

        Args:
            amount (int): The amount of pressure decrease in bar.

        Raises:
            ValueError: If the pressure decrease is negative or exceeds the current pressure.
        """
        if amount < 0:
            raise ValueError("Pressure decrease cannot be negative")
        if amount > self.pressure:
            raise ValueError("Pressure decrease exceeds current pressure")

        self.pressure -= amount


class JECOFireCrashTruck:
    def __init__(self):
        """
        Initialize the JECO fire crash truck simulator.
        """
        self.water_bowser = WaterBowser()
        self.hydraulic_system = HydraulicSystem()

    def operate_water_bowser(self, duration):
        """
        Simulate operating the water bowser.

        Args:
            duration (int): The duration of operation in minutes.

        Returns:
            int: The total amount of water discharged in liters.
        """
        return self.water_bowser.discharge_water(duration)

    def operate_hydraulic_system(self, pressure_change):
        """
        Simulate operating the hydraulic system.

        Args:
            pressure_change (int): The change in hydraulic pressure in bar.

        Raises:
            ValueError: If the pressure change is invalid.
        """
        if pressure_change > 0:
            self.hydraulic_system.increase_pressure(pressure_change)
        elif pressure_change < 0:
            self.hydraulic_system.decrease_pressure(-pressure_change)

    def status(self):
        """
        Print the current status of the JECO fire crash truck simulator.
        """
        print("Water Bowser Status:")
        print(f"  - Current Water Level: {self.water_bowser.current_water_level} liters")
        print(f"  - Flow Rate: {self.water_bowser.flow_rate} liters/minute")
        print()
        print("Hydraulic System Status:")
        print(f"  - Current Pressure: {self.hydraulic_system.pressure} bar")
        print(f"  - Maximum Allowed Pressure: {self.hydraulic_system.max_pressure} bar")


def main():
    truck = JECOFireCrashTruck()

    while True:
        print("\nJECO Fire Crash Truck Simulator")
        print("1. Operate Water Bowser")
        print("2. Operate Hydraulic System")
        print("3. Refill Water Bowser")
        print("4. Status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            duration = int(input("Enter duration (minutes): "))
            water_discharged = truck.operate_water_bowser(duration)
            print(f"Water discharged: {water_discharged} liters")
        elif choice == "2":
            pressure_change = int(input("Enter pressure change (bar): "))
            try:
                truck.operate_hydraulic_system(pressure_change)
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            amount = int(input("Enter refill amount (liters): "))
            try:
                truck.water_bowser.refill(amount)
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            truck.status()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
