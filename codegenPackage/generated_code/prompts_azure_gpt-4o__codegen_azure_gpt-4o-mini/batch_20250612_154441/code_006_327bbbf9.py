"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write a script to simulate the durability of rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) under heavy usage conditions, referencing the use cases like gym fitness and playgrounds mentioned on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_327bbbf9848668e4
Batch ID: 20250612_154441
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

class RubberFlooring:
    """
    A class to simulate the durability of rubber flooring materials under heavy usage conditions.
    """

    def __init__(self, material_type, initial_durability):
        """
        Initializes the RubberFlooring instance.

        :param material_type: str - Type of rubber flooring (e.g., 'TPV Rubber', 'Rubber Tiles')
        :param initial_durability: float - Initial durability score (0 to 100)
        """
        self.material_type = material_type
        self.durability = initial_durability
        self.usage_conditions = {
            'gym': {'impact': 0.5, 'abrasion': 0.3},
            'playground': {'impact': 0.7, 'abrasion': 0.5}
        }

    def simulate_usage(self, usage_type, cycles):
        """
        Simulates the durability reduction over a number of usage cycles.

        :param usage_type: str - Type of usage ('gym' or 'playground')
        :param cycles: int - Number of usage cycles to simulate
        :return: list - Durability scores after each cycle
        """
        if usage_type not in self.usage_conditions:
            raise ValueError(f"Invalid usage type: {usage_type}. Choose from {list(self.usage_conditions.keys())}.")

        durability_scores = []
        for cycle in range(cycles):
            impact = self.usage_conditions[usage_type]['impact']
            abrasion = self.usage_conditions[usage_type]['abrasion']
            wear = random.uniform(0.01, 0.05) * (impact + abrasion)
            self.durability -= wear * 100  # Scale durability reduction
            self.durability = max(self.durability, 0)  # Ensure durability does not go below 0
            durability_scores.append(self.durability)

        return durability_scores

    def plot_durability(self, durability_scores):
        """
        Plots the durability scores over the usage cycles.

        :param durability_scores: list - Durability scores to plot
        """
        plt.figure(figsize=(10, 5))
        plt.plot(durability_scores, marker='o')
        plt.title(f'Durability Simulation of {self.material_type}')
        plt.xlabel('Usage Cycles')
        plt.ylabel('Durability Score')
        plt.ylim(0, 100)
        plt.grid()
        plt.show()


def main():
    """
    Main function to run the durability simulation.
    """
    try:
        # Create instances for different rubber flooring materials
        tpv_rubber = RubberFlooring('TPV Rubber', initial_durability=100)
        rubber_tiles = RubberFlooring('Rubber Tiles', initial_durability=100)

        # Simulate usage for gym and playground
        gym_cycles = 20
        playground_cycles = 20

        tpv_durability = tpv_rubber.simulate_usage('gym', gym_cycles)
        tiles_durability = rubber_tiles.simulate_usage('playground', playground_cycles)

        # Plot the results
        tpv_rubber.plot_durability(tpv_durability)
        rubber_tiles.plot_durability(tiles_durability)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
