"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Generate code to simulate the production capacity increase of TPCPLC's cement manufacturing, including milestones like the CM5 project reaching 2.0 million metric tons per year.
Generated: DETERMINISTIC_abc37df6ecfb89c0
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# production_capacity_simulator.py

class CementPlant:
    def __init__(self, name, initial_capacity):
        """
        Initialize a CementPlant object.

        Args:
            name (str): Name of the cement plant.
            initial_capacity (float): Initial production capacity in million metric tons per year.
        """
        self.name = name
        self.capacity = initial_capacity
        self.milestones = []

    def add_milestone(self, project_name, capacity_increase):
        """
        Add a milestone to the cement plant's production capacity.

        Args:
            project_name (str): Name of the project.
            capacity_increase (float): Increase in production capacity in million metric tons per year.
        """
        self.milestones.append((project_name, self.capacity, self.capacity + capacity_increase))
        self.capacity += capacity_increase

    def simulate_production(self):
        """
        Simulate the production capacity increase of the cement plant.

        Returns:
            list: A list of tuples containing the project name, previous capacity, and new capacity.
        """
        simulation_results = []
        for project_name, previous_capacity, new_capacity in self.milestones:
            simulation_results.append({
                "Project": project_name,
                "Previous Capacity (million metric tons/year)": previous_capacity,
                "New Capacity (million metric tons/year)": new_capacity
            })
        return simulation_results


def main():
    try:
        # Create a cement plant object
        tpcplc = CementPlant("TPCPLC", 1.5)

        # Add milestones
        tpcplc.add_milestone("CM1", 0.5)
        tpcplc.add_milestone("CM2", 1.0)
        tpcplc.add_milestone("CM3", 1.2)
        tpcplc.add_milestone("CM4", 0.8)
        tpcplc.add_milestone("CM5", 1.5)

        # Simulate production capacity increase
        simulation_results = tpcplc.simulate_production()

        # Print simulation results
        print("Production Capacity Increase Simulation Results:")
        for result in simulation_results:
            print(f"Project: {result['Project']}")
            print(f"Previous Capacity: {result['Previous Capacity (million metric tons/year)']} million metric tons/year")
            print(f"New Capacity: {result['New Capacity (million metric tons/year)']} million metric tons/year")
            print("-" * 50)

        # Check if CM5 project reached 2.0 million metric tons per year
        if tpcplc.capacity >= 2.0:
            print(f"\nCM5 project has reached a production capacity of {tpcplc.capacity} million metric tons per year.")
        else:
            print(f"\nCM5 project has not reached a production capacity of 2.0 million metric tons per year.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
