"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Create a simulation model in Python to test the practical performance of a standardized battery swapping system for heavy-duty trucks, including compatibility with multiple manufacturers, as discussed in the UniSwapHD project.
Generated: DETERMINISTIC_4da1766b71b17627
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import random
import matplotlib.pyplot as plt

class Truck:
    """
    Represents a heavy-duty truck.
    """
    def __init__(self, manufacturer, battery_capacity):
        self.manufacturer = manufacturer
        self.battery_capacity = battery_capacity  # in kWh
        self.current_charge = battery_capacity  # truck starts fully charged

    def drive(self, distance):
        """
        Simulates driving the truck for a given distance.
        Each distance unit consumes 1 kWh of battery.
        """
        charge_needed = distance
        if charge_needed > self.current_charge:
            raise ValueError("Not enough charge to drive the distance.")
        self.current_charge -= charge_needed

    def swap_battery(self, new_battery_capacity):
        """
        Swaps the current battery for a new one of specified capacity.
        """
        self.battery_capacity = new_battery_capacity
        self.current_charge = new_battery_capacity  # Fully recharge after swap


class BatterySwappingStation:
    """
    Represents a battery swapping station.
    """
    def __init__(self):
        self.batteries_in_stock = []

    def add_battery(self, battery_capacity):
        """
        Adds a battery to the swapping station.
        """
        self.batteries_in_stock.append(battery_capacity)

    def swap_battery(self, truck):
        """
        Swaps the truck's battery with a new one from the stock.
        If no compatible battery is available, raises an exception.
        """
        if not self.batteries_in_stock:
            raise Exception("No batteries available for swap.")
        # For simplicity, we swap with the first available battery.
        new_battery = self.batteries_in_stock.pop(0)
        truck.swap_battery(new_battery)


class Simulation:
    """
    Simulates the battery swapping system for heavy-duty trucks.
    """
    def __init__(self, num_trucks, battery_capacity_options, num_swaps):
        self.trucks = [Truck(random.choice(['Manufacturer A', 'Manufacturer B', 'Manufacturer C']),
                             random.choice(battery_capacity_options)) for _ in range(num_trucks)]
        self.station = BatterySwappingStation()
        for capacity in battery_capacity_options:
            self.station.add_battery(capacity)
        self.num_swaps = num_swaps
        self.swap_times = []

    def run(self):
        """
        Runs the simulation for a specified number of swaps.
        """
        for _ in range(self.num_swaps):
            truck = random.choice(self.trucks)
            try:
                distance = random.randint(50, 150)  # Random distance
                truck.drive(distance)  # Drive the truck
                print(f"Truck from {truck.manufacturer} drove {distance} km. Remaining charge: {truck.current_charge} kWh.")
                self.station.swap_battery(truck)  # Swap battery
                print(f"Truck from {truck.manufacturer} swapped battery. New capacity: {truck.battery_capacity} kWh.")
            except ValueError as ve:
                print(f"Error for truck {truck.manufacturer}: {ve}")
            except Exception as e:
                print(f"Error occurred: {e}")

    def plot_results(self):
        """
        Plots the results of the simulation (e.g., battery charge levels after swaps).
        """
        charge_levels = [truck.current_charge for truck in self.trucks]
        plt.hist(charge_levels, bins=10, alpha=0.7, color='blue')
        plt.title('Battery Charge Levels After Swapping')
        plt.xlabel('Charge Level (kWh)')
        plt.ylabel('Number of Trucks')
        plt.show()


if __name__ == "__main__":
    # Set up the simulation parameters
    num_trucks = 20
    battery_capacity_options = [300, 400, 500]  # Different manufacturers' battery capacities
    num_swaps = 50  # Number of swaps to simulate

    # Create the simulation instance and run it
    simulation = Simulation(num_trucks, battery_capacity_options, num_swaps)
    simulation.run()
    simulation.plot_results()
```
