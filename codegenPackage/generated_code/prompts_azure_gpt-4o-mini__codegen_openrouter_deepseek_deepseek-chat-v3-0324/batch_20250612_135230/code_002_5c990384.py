"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Write a code snippet that simulates the expression of olfactory receptors based on the research conducted at ChemCom, as described on the ULB website.
Generated: DETERMINISTIC_5c9903840f76966a
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.stats import poisson
import matplotlib.pyplot as plt

class OlfactoryReceptorSimulator:
    """
    Simulates the expression of olfactory receptors based on ChemCom research.
    Models receptor expression levels using Poisson distribution to mimic stochastic gene expression.
    """
    
    def __init__(self, num_receptors=400, baseline_expression=0.1, seed=None):
        """
        Initialize the simulator.
        
        Args:
            num_receptors (int): Number of olfactory receptors to simulate (default 400, typical for humans)
            baseline_expression (float): Baseline expression probability (0-1)
            seed (int): Random seed for reproducibility
        """
        self.num_receptors = num_receptors
        self.baseline_expression = baseline_expression
        self.rng = np.random.default_rng(seed)
        
        # Initialize receptor names (OR1D1, OR1D2, etc.)
        self.receptor_names = [f"OR{family}{member}" 
                             for family in range(1, 19) 
                             for member in range(1, 28)][:num_receptors]
    
    def simulate_expression(self, stimulus_intensity=1.0):
        """
        Simulate receptor expression levels in response to stimulus.
        
        Args:
            stimulus_intensity (float): Multiplier for expression levels (1.0 = baseline)
            
        Returns:
            pd.Series: Expression levels for each receptor
        """
        # Poisson-distributed expression counts with stimulus modulation
        lambda_params = self.baseline_expression * stimulus_intensity * np.ones(self.num_receptors)
        
        # Add some variability between receptors
        lambda_params *= self.rng.lognormal(mean=0, sigma=0.2, size=self.num_receptors)
        
        expression_levels = self.rng.poisson(lam=lambda_params)
        return pd.Series(expression_levels, index=self.receptor_names, name="Expression Level")
    
    def plot_expression_profile(self, expression_data, top_n=20):
        """
        Plot the expression profile of receptors.
        
        Args:
            expression_data (pd.Series): Expression levels from simulate_expression()
            top_n (int): Number of top receptors to display
        """
        sorted_data = expression_data.sort_values(ascending=False)[:top_n]
        
        plt.figure(figsize=(10, 6))
        sorted_data.plot(kind='bar', color='skyblue')
        plt.title(f"Top {top_n} Expressed Olfactory Receptors")
        plt.ylabel("Expression Level (counts)")
        plt.xlabel("Receptor")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize simulator with default parameters
    simulator = OlfactoryReceptorSimulator(seed=42)
    
    # Simulate baseline expression
    baseline_expression = simulator.simulate_expression()
    
    # Simulate expression with odor stimulus (2x intensity)
    stimulated_expression = simulator.simulate_expression(stimulus_intensity=2.0)
    
    # Plot results
    print("Baseline Expression:")
    simulator.plot_expression_profile(baseline_expression)
    
    print("\nStimulated Expression:")
    simulator.plot_expression_profile(stimulated_expression)
```
