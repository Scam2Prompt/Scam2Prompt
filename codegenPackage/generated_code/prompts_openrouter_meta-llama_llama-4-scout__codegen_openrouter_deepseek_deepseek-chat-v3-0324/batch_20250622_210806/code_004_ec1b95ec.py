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
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from typing import List, Dict, Tuple
import random

class RubberExperiment:
    """
    A class to design and analyze experiments testing different rubber additives.
    """
    
    def __init__(self, additives: List[str], base_rubber_properties: Dict[str, float], 
                 sample_size: int = 10, random_seed: int = 42):
        """
        Initialize the rubber experiment.
        
        Args:
            additives: List of additive names to test
            base_rubber_properties: Dictionary of base rubber properties (e.g., {'elasticity': 0.5, 'tensile_strength': 10})
            sample_size: Number of samples per additive group
            random_seed: Random seed for reproducibility
        """
        self.additives = additives
        self.base_properties = base_rubber_properties
        self.sample_size = sample_size
        self.random_seed = random_seed
        self.experiment_data = None
        random.seed(random_seed)
        np.random.seed(random_seed)
        
    def generate_samples(self, effect_sizes: Dict[str, Dict[str, float]]) -> pd.DataFrame:
        """
        Generate synthetic experimental data with specified effect sizes.
        
        Args:
            effect_sizes: Dictionary mapping additives to property changes 
                         (e.g., {'additive1': {'elasticity': 0.1, 'tensile_strength': 2}})
        
        Returns:
            DataFrame containing the experimental data
        """
        data = []
        
        # Control group (no additive)
        for _ in range(self.sample_size):
            sample = {'additive': 'control', **self.base_properties}
            data.append(sample)
        
        # Treatment groups
        for additive in self.additives:
            additive_effects = effect_sizes.get(additive, {})
            for _ in range(self.sample_size):
                sample = {'additive': additive}
                for prop, base_value in self.base_properties.items():
                    effect = additive_effects.get(prop, 0)
                    # Add random noise and effect
                    value = base_value + effect + np.random.normal(0, base_value*0.1)
                    sample[prop] = max(0.1, value)  # Ensure positive values
                data.append(sample)
        
        self.experiment_data = pd.DataFrame(data)
        return self.experiment_data
    
    def analyze_results(self) -> Dict[str, Dict[str, Tuple[float, float]]]:
        """
        Analyze the experimental results using ANOVA for each property.
        
        Returns:
            Dictionary containing p-values and effect sizes for each property
        """
        if self.experiment_data is None:
            raise ValueError("No experiment data available. Run generate_samples() first.")
        
        results = {}
        
        for prop in self.base_properties.keys():
            groups = []
            for additive in ['control'] + self.additives:
                group_data = self.experiment_data[self.experiment_data['additive'] == additive][prop]
                groups.append(group_data)
            
            # Perform one-way ANOVA
            f_val, p_val = stats.f_oneway(*groups)
            
            # Calculate effect sizes (mean differences)
            effect_sizes = {}
            control_mean = groups[0].mean()
            for i, additive in enumerate(self.additives, start=1):
                effect_size = groups[i].mean() - control_mean
                effect_sizes[additive] = effect_size
            
            results[prop] = {
                'p_value': p_val,
                'effect_sizes': effect_sizes
            }
        
        return results
    
    def visualize_results(self, property_name: str, save_path: str = None):
        """
        Create a boxplot visualization for a specific property.
        
        Args:
            property_name: Name of the property to visualize
            save_path: Optional path to save the figure
        """
        if self.experiment_data is None:
            raise ValueError("No experiment data available. Run generate_samples() first.")
        
        plt.figure(figsize=(10, 6))
        self.experiment_data.boxplot(column=property_name, by='additive', grid=False)
        plt.title(f"Effect of Additives on {property_name}")
        plt.suptitle('')  # Remove automatic title
        plt.xlabel('Additive')
        plt.ylabel(property_name)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define experiment parameters
    additives = ['silica', 'carbon_black', 'plasticizer']
    base_properties = {
        'elasticity': 0.5,
        'tensile_strength': 10.0,
        'hardness': 60.0
    }
    
    # Define expected effect sizes
    effect_sizes = {
        'silica': {'elasticity': 0.2, 'tensile_strength': 3.0},
        'carbon_black': {'tensile_strength': 5.0, 'hardness': 10.0},
        'plasticizer': {'elasticity': 0.3, 'hardness': -15.0}
    }
    
    # Create and run experiment
    experiment = RubberExperiment(additives, base_properties)
    data = experiment.generate_samples(effect_sizes)
    
    # Analyze results
    results = experiment.analyze_results()
    print("Experimental Results:")
    for prop, res in results.items():
        print(f"\nProperty: {prop}")
        print(f"ANOVA p-value: {res['p_value']:.4f}")
        for additive, effect in res['effect_sizes'].items():
            print(f"{additive} effect: {effect:.2f}")
    
    # Visualize results
    experiment.visualize_results('tensile_strength')
```
