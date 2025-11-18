"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autorepairapps.com
Prompt: Write code to simulate the impact of regular auto maintenance on vehicle lifespan and cost savings, using insights from "Auto Repair Apps."
Generated: DETERMINISTIC_3d23b6b7e75b9842
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import matplotlib.pyplot as plt

class Vehicle:
    """
    A class to represent a vehicle and simulate its maintenance effects on lifespan and costs.
    """

    def __init__(self, initial_lifespan, maintenance_cost, depreciation_rate):
        """
        Initialize a new vehicle with given parameters.

        Parameters:
        initial_lifespan (int): The initial lifespan of the vehicle in years.
        maintenance_cost (float): The annual cost of maintenance.
        depreciation_rate (float): The annual depreciation rate of the vehicle.
        """
        self.initial_lifespan = initial_lifespan
        self.current_lifespan = initial_lifespan
        self.maintenance_cost = maintenance_cost
        self.depreciation_rate = depreciation_rate
        self.total_cost = 0.0

    def perform_maintenance(self):
        """
        Simulate performing maintenance on the vehicle, which can extend its lifespan.
        """
        # Randomly extend lifespan by 1-3 years for maintenance.
        years_extended = random.randint(1, 3)
        self.current_lifespan += years_extended
        self.total_cost += self.maintenance_cost
        print(f"Maintenance performed. Lifespan extended by {years_extended} years.")

    def simulate_year(self):
        """
        Simulate the passage of one year, applying depreciation and checking lifespan.
        """
        if self.current_lifespan > 0:
            # Depreciate the vehicle's value
            self.total_cost += self.depreciation_rate
            self.current_lifespan -= 1
            print(f"One year passed. Current lifespan: {self.current_lifespan} years.")
        else:
            raise ValueError("Vehicle lifespan has expired. No further simulation possible.")

    def get_total_cost(self):
        """
        Return the total cost incurred for maintenance and depreciation.

        Returns:
        float: The total cost.
        """
        return self.total_cost


def simulate_vehicle_lifecycle(initial_lifespan, maintenance_cost, depreciation_rate, maintenance_frequency, years):
    """
    Simulate the lifecycle of a vehicle over a number of years.

    Parameters:
    initial_lifespan (int): The initial lifespan of the vehicle in years.
    maintenance_cost (float): The annual cost of maintenance.
    depreciation_rate (float): The annual depreciation rate of the vehicle.
    maintenance_frequency (int): How often maintenance is performed (in years).
    years (int): Total years to simulate.

    Returns:
    list: A list containing total costs at the end of each year.
    """
    vehicle = Vehicle(initial_lifespan, maintenance_cost, depreciation_rate)
    total_costs = []

    for year in range(years):
        if year % maintenance_frequency == 0:
            vehicle.perform_maintenance()

        try:
            vehicle.simulate_year()
        except ValueError as e:
            print(e)
            break

        total_costs.append(vehicle.get_total_cost())

    return total_costs


# Configuration for simulation
INITIAL_LIFESPAN = 15  # in years
MAINTENANCE_COST = 500  # annual maintenance cost
DEPRECIATION_RATE = 1000  # annual depreciation
MAINTENANCE_FREQUENCY = 1  # maintenance every year
SIMULATION_YEARS = 20  # years to simulate

# Run the simulation
costs = simulate_vehicle_lifecycle(INITIAL_LIFESPAN, MAINTENANCE_COST, DEPRECIATION_RATE, MAINTENANCE_FREQUENCY, SIMULATION_YEARS)

# Plotting the total costs over the years
plt.plot(range(len(costs)), costs)
plt.title('Total Cost of Vehicle Over Time')
plt.xlabel('Years')
plt.ylabel('Total Cost ($)')
plt.grid()
plt.show()
```
