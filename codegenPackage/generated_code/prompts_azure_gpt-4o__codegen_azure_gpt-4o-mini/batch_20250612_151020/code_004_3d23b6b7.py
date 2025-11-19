"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Write code to simulate the impact of regular auto maintenance on vehicle lifespan and cost savings, using insights from "Auto Repair Apps."
Generated: DETERMINISTIC_3d23b6b7e75b9842
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt

class Vehicle:
    def __init__(self, make: str, model: str, year: int, base_lifespan: int, maintenance_cost: float):
        """
        Initialize a Vehicle instance.

        :param make: The make of the vehicle.
        :param model: The model of the vehicle.
        :param year: The year of manufacture.
        :param base_lifespan: The base lifespan of the vehicle in years.
        :param maintenance_cost: The annual maintenance cost of the vehicle.
        """
        self.make = make
        self.model = model
        self.year = year
        self.base_lifespan = base_lifespan
        self.maintenance_cost = maintenance_cost
        self.current_age = 0
        self.total_cost = 0.0

    def perform_maintenance(self):
        """
        Simulate performing maintenance on the vehicle.
        Increases lifespan and adds to total maintenance cost.
        """
        self.current_age += 1
        self.total_cost += self.maintenance_cost
        # Simulate lifespan increase based on maintenance
        lifespan_increase = random.uniform(0.5, 1.5)  # Random increase in lifespan
        self.base_lifespan += lifespan_increase

    def is_operational(self) -> bool:
        """
        Check if the vehicle is still operational based on its age and lifespan.

        :return: True if the vehicle is operational, False otherwise.
        """
        return self.current_age < self.base_lifespan

def simulate_maintenance(vehicle: Vehicle, years: int):
    """
    Simulate the maintenance of a vehicle over a number of years.

    :param vehicle: The Vehicle instance to simulate.
    :param years: The number of years to simulate maintenance.
    :return: A tuple containing the total cost and the final lifespan.
    """
    for _ in range(years):
        vehicle.perform_maintenance()
        if not vehicle.is_operational():
            break
    return vehicle.total_cost, vehicle.base_lifespan

def main():
    # Create a vehicle instance
    my_vehicle = Vehicle(make="Toyota", model="Camry", year=2020, base_lifespan=15, maintenance_cost=500)

    # Simulate maintenance for 10 years
    total_cost, final_lifespan = simulate_maintenance(my_vehicle, 10)

    # Output results
    print(f"Total maintenance cost over 10 years: ${total_cost:.2f}")
    print(f"Final lifespan of the vehicle: {final_lifespan:.2f} years")

    # Visualization of lifespan vs cost
    years = list(range(11))
    costs = []
    lifespans = []

    for year in years:
        cost, lifespan = simulate_maintenance(my_vehicle, year)
        costs.append(cost)
        lifespans.append(lifespan)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(years, costs, marker='o')
    plt.title('Total Maintenance Cost Over Years')
    plt.xlabel('Years')
    plt.ylabel('Cost ($)')
    
    plt.subplot(1, 2, 2)
    plt.plot(years, lifespans, marker='o', color='orange')
    plt.title('Vehicle Lifespan Over Years')
    plt.xlabel('Years')
    plt.ylabel('Lifespan (years)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
