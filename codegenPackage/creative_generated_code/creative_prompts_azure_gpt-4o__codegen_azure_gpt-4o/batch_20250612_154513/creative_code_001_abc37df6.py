"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Generate code to simulate the production capacity increase of TPCPLC's cement manufacturing, including milestones like the CM5 project reaching 2.0 million metric tons per year.
Generated: DETERMINISTIC_abc37df6ecfb89c0
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

# Function to simulate production capacity over years
def simulate_production_capacity(years, initial_capacity, milestones):
    """
    Simulates the production capacity increase of a cement manufacturing plant.

    Parameters:
        years (list): List of years to simulate.
        initial_capacity (float): Initial production capacity in million metric tons per year.
        milestones (dict): Dictionary of milestones with year as key and target capacity as value.

    Returns:
        dict: Dictionary with year as key and simulated production capacity as value.
    """
    # Initialize capacity dictionary with initial capacity
    capacity = {}
    current_capacity = initial_capacity

    for year in years:
        if year in milestones:
            # If milestone year, update current capacity to the milestone target
            current_capacity = milestones[year]
        capacity[year] = current_capacity

    return capacity

# Function to plot production capacity over years
def plot_capacity_simulation(capacity_data, title="Production Capacity Simulation"):
    """
    Plots the simulated production capacity over years.

    Parameters:
        capacity_data (dict): Dictionary with year as key and production capacity as value.
        title (str): Title of the plot.
    """
    years = list(capacity_data.keys())
    capacities = list(capacity_data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(years, capacities, marker='o', linestyle='-', color='blue', label="Production Capacity")
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Capacity (Million Metric Tons/Year)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main simulation parameters
try:
    years = list(range(2020, 2031))  # Simulate from 2020 to 2030
    initial_capacity = 1.5  # Initial production capacity in million metric tons/year
    milestones = {
        2025: 2.0,  # CM5 project milestone reaching 2.0 million metric tons/year
        2030: 2.5  # Another future milestone for capacity increase
    }

    # Run the simulation
    capacity_simulation = simulate_production_capacity(years, initial_capacity, milestones)

    # Plot the results
    plot_capacity_simulation(capacity_simulation, title="TPCPLC Cement Manufacturing Capacity Simulation")

except Exception as e:
    # Handle any unexpected errors
    print(f"An error occurred: {str(e)}")
```
