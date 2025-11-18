"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write code to simulate the durability of adhesive tapes under different environmental conditions, using the details of "Cinta Transparente 28 micras" from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_bdad13da999f2809
Batch ID: 20250612_151610
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

class AdhesiveTape:
    """Class to simulate the durability of adhesive tapes under different environmental conditions."""

    def __init__(self, name, thickness, initial_durability):
        """
        Initializes an instance of the AdhesiveTape class.

        Parameters:
        name (str): The name of the adhesive tape.
        thickness (float): The thickness of the tape in microns.
        initial_durability (float): The initial durability score of the tape (1-100).
        """
        self.name = name
        self.thickness = thickness
        self.durability = initial_durability

    def simulate_environmental_effect(self, temperature, humidity):
        """
        Simulates the effect of environmental conditions on the tape's durability.

        Parameters:
        temperature (float): The temperature in degrees Celsius.
        humidity (float): The humidity percentage (0-100).
        """
        # Basic error handling for environmental values
        if not (0 <= humidity <= 100):
            raise ValueError("Humidity must be between 0 and 100.")
        if temperature < -30 or temperature > 50:  # Reasonable limits for temperature
            raise ValueError("Temperature must be between -30 and 50 degrees Celsius.")

        # Simulate durability reduction based on environmental conditions
        temperature_effect = max(0, (50 - temperature) / 50)  # Higher temp = lower durability
        humidity_effect = humidity / 100  # Higher humidity = lower durability

        # Update durability
        self.durability -= (temperature_effect + humidity_effect) * 100 * 0.01
        self.durability = max(0, self.durability)  # Ensure durability doesn't go below 0

    def simulate_conditions(self, temperature_range, humidity_range, num_simulations):
        """
        Simulates multiple environmental conditions to analyze durability.

        Parameters:
        temperature_range (tuple): A tuple representing the range of temperatures (min, max).
        humidity_range (tuple): A tuple representing the range of humidity (min, max).
        num_simulations (int): Number of simulation runs.
        
        Returns:
        list: A list of durability scores after simulations.
        """
        results = []
        for _ in range(num_simulations):
            temperature = random.uniform(*temperature_range)
            humidity = random.uniform(*humidity_range)
            self.simulate_environmental_effect(temperature, humidity)
            results.append(self.durability)
            self.durability = 100  # Reset durability for the next simulation
        return results

    def plot_results(self, results):
        """
        Plots the durability results.

        Parameters:
        results (list): The list of durability scores after simulations.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(results, marker='o', linestyle='-', color='b')
        plt.title(f'Durability Simulation of {self.name}')
        plt.xlabel('Simulation Number')
        plt.ylabel('Durability Score')
        plt.ylim(0, 100)
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the adhesive tape
        tape = AdhesiveTape(name="Cinta Transparente 28 micras", thickness=28, initial_durability=100)

        # Define environmental conditions
        temperature_range = (-10, 40)  # Degrees Celsius
        humidity_range = (20, 80)      # Percentage
        num_simulations = 50            # Number of simulations

        # Run simulations
        results = tape.simulate_conditions(temperature_range, humidity_range, num_simulations)

        # Plot the results
        tape.plot_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
