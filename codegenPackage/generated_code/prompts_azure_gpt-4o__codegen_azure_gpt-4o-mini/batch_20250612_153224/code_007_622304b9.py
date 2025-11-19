"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Generate Python code to simulate the functionality of JECO's jetting and vacuum vehicles for cleaning operations.
Generated: DETERMINISTIC_622304b953d21a1d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JettingVehicle:
    """
    A class to represent a jetting vehicle used for cleaning operations.
    """

    def __init__(self, water_capacity: float, pressure: float):
        """
        Initializes the jetting vehicle with a specified water capacity and pressure.

        :param water_capacity: Maximum water capacity in liters.
        :param pressure: Pressure of the jetting system in PSI.
        """
        self.water_capacity = water_capacity
        self.current_water_level = water_capacity  # Start with full capacity
        self.pressure = pressure
        self.is_operational = True

    def jet_water(self, amount: float):
        """
        Simulates jetting water for cleaning.

        :param amount: Amount of water to jet in liters.
        :raises ValueError: If the amount exceeds the current water level.
        """
        if not self.is_operational:
            raise RuntimeError("The jetting vehicle is not operational.")
        
        if amount > self.current_water_level:
            raise ValueError("Not enough water in the tank to jet this amount.")

        self.current_water_level -= amount
        print(f"Jetted {amount} liters of water at {self.pressure} PSI.")

    def refill_water(self):
        """
        Refills the water tank to full capacity.
        """
        self.current_water_level = self.water_capacity
        print("Water tank refilled to full capacity.")

    def status(self):
        """
        Prints the current status of the jetting vehicle.
        """
        print(f"Jetting Vehicle Status: {self.current_water_level}/{self.water_capacity} liters available.")


class VacuumVehicle:
    """
    A class to represent a vacuum vehicle used for cleaning operations.
    """

    def __init__(self, tank_capacity: float):
        """
        Initializes the vacuum vehicle with a specified tank capacity.

        :param tank_capacity: Maximum tank capacity in liters.
        """
        self.tank_capacity = tank_capacity
        self.current_tank_level = 0  # Start with empty tank
        self.is_operational = True

    def vacuum(self, amount: float):
        """
        Simulates vacuuming a specified amount of debris.

        :param amount: Amount of debris to vacuum in liters.
        :raises ValueError: If the amount exceeds the available capacity.
        """
        if not self.is_operational:
            raise RuntimeError("The vacuum vehicle is not operational.")
        
        if self.current_tank_level + amount > self.tank_capacity:
            raise ValueError("Not enough capacity in the tank to vacuum this amount.")

        self.current_tank_level += amount
        print(f"Vacuumed {amount} liters of debris.")

    def empty_tank(self):
        """
        Empties the vacuum tank.
        """
        self.current_tank_level = 0
        print("Vacuum tank emptied.")

    def status(self):
        """
        Prints the current status of the vacuum vehicle.
        """
        print(f"Vacuum Vehicle Status: {self.current_tank_level}/{self.tank_capacity} liters used.")


def main():
    """
    Main function to simulate the operation of jetting and vacuum vehicles.
    """
    try:
        # Create instances of the vehicles
        jetting_vehicle = JettingVehicle(water_capacity=1000, pressure=150)
        vacuum_vehicle = VacuumVehicle(tank_capacity=800)

        # Display initial status
        jetting_vehicle.status()
        vacuum_vehicle.status()

        # Simulate operations
        jetting_vehicle.jet_water(200)
        vacuum_vehicle.vacuum(150)

        # Display status after operations
        jetting_vehicle.status()
        vacuum_vehicle.status()

        # Refill water and empty vacuum tank
        jetting_vehicle.refill_water()
        vacuum_vehicle.empty_tank()

        # Final status
        jetting_vehicle.status()
        vacuum_vehicle.status()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
