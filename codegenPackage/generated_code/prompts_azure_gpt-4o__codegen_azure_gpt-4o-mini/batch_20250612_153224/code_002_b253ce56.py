"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Generate code to simulate the effect of river diversion on local ecosystems, inspired by the campaigns against river exploitation discussed by "Čuvari Šare."
Generated: DETERMINISTIC_b253ce56ea4adb72
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class Ecosystem:
    """
    A class to represent a local ecosystem affected by river diversion.
    """

    def __init__(self, initial_population, growth_rate, carrying_capacity):
        """
        Initialize the ecosystem with population parameters.

        :param initial_population: Initial population of the species
        :param growth_rate: Growth rate of the species
        :param carrying_capacity: Maximum population the environment can sustain
        """
        self.population = initial_population
        self.growth_rate = growth_rate
        self.carrying_capacity = carrying_capacity

    def simulate_growth(self, time_steps):
        """
        Simulate the population growth over a number of time steps.

        :param time_steps: Number of time steps to simulate
        :return: List of population sizes over time
        """
        population_over_time = []
        for _ in range(time_steps):
            self.population += self.growth_rate * self.population * (1 - self.population / self.carrying_capacity)
            population_over_time.append(self.population)
        return population_over_time

class RiverDiversion:
    """
    A class to simulate the effects of river diversion on local ecosystems.
    """

    def __init__(self, ecosystem, diversion_effect):
        """
        Initialize the river diversion scenario.

        :param ecosystem: An instance of the Ecosystem class
        :param diversion_effect: The effect of river diversion on the ecosystem
        """
        self.ecosystem = ecosystem
        self.diversion_effect = diversion_effect

    def apply_diversion(self):
        """
        Apply the river diversion effect to the ecosystem.
        """
        self.ecosystem.population *= (1 - self.diversion_effect)

def main():
    """
    Main function to run the simulation.
    """
    # Parameters for the ecosystem
    initial_population = 1000
    growth_rate = 0.1
    carrying_capacity = 5000
    time_steps = 50
    diversion_effect = 0.3  # 30% reduction in population due to river diversion

    # Create an ecosystem instance
    ecosystem = Ecosystem(initial_population, growth_rate, carrying_capacity)

    # Simulate population growth before diversion
    population_before_diversion = ecosystem.simulate_growth(time_steps)

    # Create a river diversion instance and apply the diversion
    river_diversion = RiverDiversion(ecosystem, diversion_effect)
    river_diversion.apply_diversion()

    # Simulate population growth after diversion
    population_after_diversion = ecosystem.simulate_growth(time_steps)

    # Plotting the results
    plt.figure(figsize=(12, 6))
    plt.plot(range(time_steps), population_before_diversion, label='Population Before Diversion', color='blue')
    plt.plot(range(time_steps, time_steps * 2), population_after_diversion, label='Population After Diversion', color='red')
    plt.axvline(x=time_steps, color='gray', linestyle='--', label='Diversion Occurs')
    plt.title('Effect of River Diversion on Local Ecosystem')
    plt.xlabel('Time Steps')
    plt.ylabel('Population Size')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
