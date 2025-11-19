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
import numpy as np
from scipy import stats
import pandas as pd

class RubberExperiment:
    """
    A class to design an experiment for testing the effect of different additives on the properties of rubber products.

    Attributes:
    -----------
    additives : list
        A list of additives to be tested.
    properties : list
        A list of properties to be measured.
    num_samples : int
        The number of samples for each additive and property.

    Methods:
    --------
    run_experiment()
        Runs the experiment and returns the results.
    analyze_results(results)
        Analyzes the results and returns the mean and standard deviation for each additive and property.
    """

    def __init__(self, additives, properties, num_samples):
        """
        Initializes the experiment.

        Parameters:
        -----------
        additives : list
            A list of additives to be tested.
        properties : list
            A list of properties to be measured.
        num_samples : int
            The number of samples for each additive and property.
        """
        self.additives = additives
        self.properties = properties
        self.num_samples = num_samples

    def run_experiment(self):
        """
        Runs the experiment and returns the results.

        Returns:
        --------
        results : dict
            A dictionary with additives as keys and dictionaries of properties as values.
        """
        results = {}
        for additive in self.additives:
            results[additive] = {}
            for prop in self.properties:
                # Simulate the measurement process (in a real experiment, this would be actual measurements)
                samples = np.random.normal(loc=100, scale=10, size=self.num_samples)  # Assume a normal distribution with mean 100 and std dev 10
                results[additive][prop] = samples
        return results

    def analyze_results(self, results):
        """
        Analyzes the results and returns the mean and standard deviation for each additive and property.

        Parameters:
        -----------
        results : dict
            A dictionary with additives as keys and dictionaries of properties as values.

        Returns:
        --------
        analysis : dict
            A dictionary with additives as keys and dictionaries of properties with mean and std dev as values.
        """
        analysis = {}
        for additive, props in results.items():
            analysis[additive] = {}
            for prop, samples in props.items():
                mean = np.mean(samples)
                std_dev = np.std(samples)
                analysis[additive][prop] = {"mean": mean, "std_dev": std_dev}
        return analysis

    def perform_statistical_analysis(self, analysis):
        """
        Performs a statistical analysis to compare the means of each additive and property.

        Parameters:
        -----------
        analysis : dict
            A dictionary with additives as keys and dictionaries of properties with mean and std dev as values.

        Returns:
        --------
        p_values : dict
            A dictionary with additives as keys and dictionaries of properties with p-values as values.
        """
        p_values = {}
        for additive, props in analysis.items():
            p_values[additive] = {}
            for prop, values in props.items():
                # Perform a t-test to compare the mean to a reference value (e.g. 100)
                t_stat, p_value = stats.ttest_1samp(list(np.random.normal(loc=values["mean"], scale=values["std_dev"], size=self.num_samples)), 100)
                p_values[additive][prop] = p_value
        return p_values


def main():
    additives = ["additive1", "additive2", "additive3"]
    properties = ["tensile_strength", "elongation_at_break", "hardness"]
    num_samples = 10

    experiment = RubberExperiment(additives, properties, num_samples)
    results = experiment.run_experiment()
    analysis = experiment.analyze_results(results)
    p_values = experiment.perform_statistical_analysis(analysis)

    df = pd.DataFrame()
    for additive, props in analysis.items():
        for prop, values in props.items():
            df = pd.concat([df, pd.DataFrame({"Additive": [additive], "Property": [prop], "Mean": [values["mean"]], "Std Dev": [values["std_dev"]], "p-value": [p_values[additive][prop]]})])

    print(df)


if __name__ == "__main__":
    main()
```
