"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Generate code to simulate fishery dynamics using openMSE, explaining how reference points are calculated and used in the simulation.
Generated: DETERMINISTIC_eee19a7944c464ff
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Define fishery dynamics simulation
class FisherySimulation:
    def __init__(self, initial_population, growth_rate, carrying_capacity, harvest_rate):
        """
        Initialize the fishery simulation parameters.

        Parameters:
        - initial_population (float): Starting fish population.
        - growth_rate (float): Intrinsic growth rate of the fish population.
        - carrying_capacity (float): Maximum carrying capacity of the environment.
        - harvest_rate (float): Rate of fish harvesting (as a proportion of population per unit time).
        """
        self.population = initial_population
        self.growth_rate = growth_rate
        self.carrying_capacity = carrying_capacity
        self.harvest_rate = harvest_rate
        self.population_history = [initial_population]

    def calculate_reference_points(self):
        """
        Calculate reference points for the fishery:
        - Maximum Sustainable Yield (MSY)
        - Biomass at MSY (Bmsy)
        - Fishing rate at MSY (Fmsy)

        Returns:
        A dictionary containing MSY, Bmsy, and Fmsy.
        """
        # Biomass at MSY is half the carrying capacity
        Bmsy = self.carrying_capacity / 2
        # Fishing rate at MSY is the intrinsic growth rate divided by 2
        Fmsy = self.growth_rate / 2
        # Maximum Sustainable Yield (MSY) formula: MSY = Bmsy * Fmsy
        MSY = Bmsy * Fmsy

        return {"MSY": MSY, "Bmsy": Bmsy, "Fmsy": Fmsy}

    def simulate(self, time_steps):
        """
        Simulate fishery dynamics over a given number of time steps.

        Parameters:
        - time_steps (int): Number of time steps to simulate.

        Returns:
        - population_history (list): Population size at each time step.
        """
        for _ in range(time_steps):
            # Calculate population growth using logistic growth model
            growth = self.growth_rate * self.population * (1 - self.population / self.carrying_capacity)
            # Calculate population reduction due to harvesting
            harvest = self.harvest_rate * self.population
            # Update population size (ensuring it doesn't go below zero)
            self.population = max(self.population + growth - harvest, 0)
            # Store population in history
            self.population_history.append(self.population)

        return self.population_history

    def plot_population(self):
        """
        Plot the population dynamics over time.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.population_history, label="Fish Population", color="blue")
        plt.axhline(y=self.calculate_reference_points()['Bmsy'], color="orange", linestyle="--", label="Bmsy")
        plt.title("Fishery Dynamics Simulation")
        plt.xlabel("Time Step")
        plt.ylabel("Population Size")
        plt.legend()
        plt.grid()
        plt.show()


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize simulation parameters
        initial_population = 1000  # Initial fish population
        growth_rate = 0.2         # Intrinsic growth rate
        carrying_capacity = 5000  # Environmental carrying capacity
        harvest_rate = 0.1        # Harvesting rate

        # Create simulation object
        fishery = FisherySimulation(initial_population, growth_rate, carrying_capacity, harvest_rate)

        # Calculate reference points
        reference_points = fishery.calculate_reference_points()
        print("Reference Points:")
        print(f"MSY: {reference_points['MSY']:.2f}")
        print(f"Bmsy: {reference_points['Bmsy']:.2f}")
        print(f"Fmsy: {reference_points['Fmsy']:.2f}")

        # Run the simulation for 50 time steps
        population_history = fishery.simulate(time_steps=50)

        # Plot population dynamics
        fishery.plot_population()

    except Exception as e:
        # Handle any errors that occur during simulation
        print(f"An error occurred: {e}")
```
