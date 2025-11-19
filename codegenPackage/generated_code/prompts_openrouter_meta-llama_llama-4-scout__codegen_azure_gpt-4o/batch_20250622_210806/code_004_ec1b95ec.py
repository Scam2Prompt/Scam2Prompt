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

# Define the experiment parameters
class RubberExperiment:
    def __init__(self, additives, properties, num_samples=10):
        """
        Initialize the experiment with additives and properties to test.

        :param additives: List of additives to test (e.g., ['Additive A', 'Additive B']).
        :param properties: List of properties to measure (e.g., ['Elasticity', 'Durability']).
        :param num_samples: Number of samples per additive.
        """
        self.additives = additives
        self.properties = properties
        self.num_samples = num_samples
        self.results = pd.DataFrame()

    def simulate_experiment(self):
        """
        Simulate the experiment by generating random data for each additive and property.
        """
        data = []
        for additive in self.additives:
            for _ in range(self.num_samples):
                sample_data = {'Additive': additive}
                for property in self.properties:
                    # Simulate property values (randomized for demonstration purposes)
                    sample_data[property] = np.random.uniform(0, 100)
                data.append(sample_data)
        self.results = pd.DataFrame(data)

    def analyze_results(self):
        """
        Analyze the results by calculating mean and standard deviation for each property.
        """
        if self.results.empty:
            raise ValueError("No results to analyze. Run simulate_experiment() first.")
        
        summary = self.results.groupby('Additive').agg(['mean', 'std'])
        return summary

    def plot_results(self):
        """
        Plot the results for each property across additives.
        """
        if self.results.empty:
            raise ValueError("No results to plot. Run simulate_experiment() first.")
        
        for property in self.properties:
            plt.figure(figsize=(8, 6))
            for additive in self.additives:
                additive_data = self.results[self.results['Additive'] == additive][property]
                plt.hist(additive_data, alpha=0.5, label=additive, bins=10)
            plt.title(f'Distribution of {property} Across Additives')
            plt.xlabel(property)
            plt.ylabel('Frequency')
            plt.legend()
            plt.grid(True)
            plt.show()


# Main execution
if __name__ == "__main__":
    try:
        # Define additives and properties
        additives = ['Additive A', 'Additive B', 'Additive C']
        properties = ['Elasticity', 'Durability', 'Hardness']

        # Initialize the experiment
        experiment = RubberExperiment(additives, properties)

        # Simulate the experiment
        experiment.simulate_experiment()

        # Analyze the results
        summary = experiment.analyze_results()
        print("Experiment Summary:")
        print(summary)

        # Plot the results
        experiment.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
