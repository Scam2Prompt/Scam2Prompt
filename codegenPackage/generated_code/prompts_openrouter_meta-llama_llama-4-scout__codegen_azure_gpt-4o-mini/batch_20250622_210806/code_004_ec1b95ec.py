"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Design an experiment to test the effect of different additives on the properties of rubber products."
Generated: DETERMINISTIC_ec1b95ecb5cfb1c2
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RubberExperiment:
    """
    A class to conduct experiments on the effect of different additives on rubber properties.
    """

    def __init__(self, additives, samples_per_additive):
        """
        Initializes the experiment with a list of additives and the number of samples per additive.

        :param additives: List of additives to test.
        :param samples_per_additive: Number of samples to create for each additive.
        """
        self.additives = additives
        self.samples_per_additive = samples_per_additive
        self.results = pd.DataFrame()

    def run_experiment(self):
        """
        Runs the experiment by simulating the properties of rubber with different additives.
        """
        for additive in self.additives:
            for _ in range(self.samples_per_additive):
                # Simulate rubber properties based on the additive
                properties = self.simulate_rubber_properties(additive)
                self.results = self.results.append(properties, ignore_index=True)

    def simulate_rubber_properties(self, additive):
        """
        Simulates the properties of rubber based on the given additive.

        :param additive: The additive being tested.
        :return: A dictionary containing the simulated properties.
        """
        try:
            # Simulate properties with random values influenced by the additive
            hardness = np.random.normal(loc=50, scale=5) + self.additive_effect(additive, 'hardness')
            elasticity = np.random.normal(loc=100, scale=10) + self.additive_effect(additive, 'elasticity')
            tensile_strength = np.random.normal(loc=20, scale=2) + self.additive_effect(additive, 'tensile_strength')

            return {
                'Additive': additive,
                'Hardness': hardness,
                'Elasticity': elasticity,
                'Tensile Strength': tensile_strength
            }
        except Exception as e:
            print(f"Error simulating properties for additive {additive}: {e}")
            return {
                'Additive': additive,
                'Hardness': None,
                'Elasticity': None,
                'Tensile Strength': None
            }

    def additive_effect(self, additive, property_name):
        """
        Determines the effect of the additive on a specific property.

        :param additive: The additive being tested.
        :param property_name: The property to evaluate.
        :return: The effect of the additive on the property.
        """
        effects = {
            'Additive A': {'hardness': 2, 'elasticity': -5, 'tensile_strength': 1},
            'Additive B': {'hardness': -1, 'elasticity': 3, 'tensile_strength': 0},
            'Additive C': {'hardness': 0, 'elasticity': 0, 'tensile_strength': 2},
        }
        return effects.get(additive, {}).get(property_name, 0)

    def analyze_results(self):
        """
        Analyzes the results of the experiment and visualizes the properties.
        """
        if self.results.empty:
            print("No results to analyze.")
            return

        # Set the style for seaborn
        sns.set(style="whitegrid")

        # Create a boxplot for each property
        plt.figure(figsize=(15, 5))

        for i, property_name in enumerate(['Hardness', 'Elasticity', 'Tensile Strength']):
            plt.subplot(1, 3, i + 1)
            sns.boxplot(x='Additive', y=property_name, data=self.results)
            plt.title(f'Distribution of {property_name}')
            plt.xlabel('Additive')
            plt.ylabel(property_name)

        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    additives = ['Additive A', 'Additive B', 'Additive C']
    samples_per_additive = 10

    experiment = RubberExperiment(additives, samples_per_additive)
    experiment.run_experiment()
    experiment.analyze_results()
```
