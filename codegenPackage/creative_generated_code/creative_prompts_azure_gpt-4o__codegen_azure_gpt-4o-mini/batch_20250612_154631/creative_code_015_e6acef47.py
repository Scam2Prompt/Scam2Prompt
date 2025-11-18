"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Generate a script to simulate the adsorption process in Econopure's activated carbon filters for removing organic contaminants from water.
Generated: DETERMINISTIC_e6acef4785eaa364
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class ActivatedCarbonFilter:
    def __init__(self, filter_capacity, adsorption_rate):
        """
        Initialize the ActivatedCarbonFilter.

        :param filter_capacity: Maximum capacity of the filter (in mg/L)
        :param adsorption_rate: Rate of adsorption (in mg/L/hour)
        """
        self.filter_capacity = filter_capacity
        self.adsorption_rate = adsorption_rate
        self.adsorbed_contaminants = 0.0

    def simulate_adsorption(self, initial_concentration, duration):
        """
        Simulate the adsorption process over a given duration.

        :param initial_concentration: Initial concentration of contaminants (in mg/L)
        :param duration: Duration of simulation (in hours)
        :return: List of concentrations over time
        """
        concentrations = []
        current_concentration = initial_concentration

        for hour in range(duration):
            if self.adsorbed_contaminants < self.filter_capacity:
                # Calculate how much can be adsorbed this hour
                adsorbed = min(self.adsorption_rate, current_concentration)
                self.adsorbed_contaminants += adsorbed
                
                # Update remaining concentration
                current_concentration -= adsorbed

                # Ensure we do not go negative
                current_concentration = max(current_concentration, 0)

            concentrations.append(current_concentration)

        return concentrations

def plot_results(concentrations):
    """
    Plot the results of the adsorption simulation.

    :param concentrations: List of concentrations over time
    """
    plt.figure(figsize=(10, 5))
    plt.plot(concentrations, marker='o')
    plt.title('Adsorption of Organic Contaminants Over Time')
    plt.xlabel('Time (hours)')
    plt.ylabel('Remaining Concentration (mg/L)')
    plt.grid()
    plt.ylim(0, max(concentrations) * 1.1)  # Extend y-axis for visibility
    plt.show()

def main():
    """
    Main function to run the adsorption simulation.
    """
    # Parameters for the simulation
    filter_capacity = 1000.0  # in mg/L
    adsorption_rate = 50.0     # in mg/L/hour
    initial_concentration = 2000.0  # initial concentration of the contaminant in mg/L
    duration = 10  # duration in hours

    try:
        # Create an instance of the ActivatedCarbonFilter
        filter_system = ActivatedCarbonFilter(filter_capacity, adsorption_rate)
        
        # Run the adsorption simulation
        concentrations = filter_system.simulate_adsorption(initial_concentration, duration)
        
        # Plot the results
        plot_results(concentrations)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
