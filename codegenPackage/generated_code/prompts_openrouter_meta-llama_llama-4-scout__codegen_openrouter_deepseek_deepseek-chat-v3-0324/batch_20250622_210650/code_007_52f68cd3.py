"""
Generated Code Metadata:
========================
Original URL: https://universalsolar1.com
Prompt: Generate a code example for comparing the benefits of manufacturing solar panels in the Americas versus Asia, considering factors mentioned by Universal Solar.
Generated: DETERMINISTIC_52f68cd3c2e6a133
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Panel Manufacturing Cost Comparison Tool
Compares manufacturing benefits between Americas and Asia based on various factors.
"""

import pandas as pd
import matplotlib.pyplot as plt

class SolarManufacturingComparison:
    """
    Compares solar panel manufacturing benefits between regions.
    Factors considered: labor costs, transportation, tariffs, incentives, supply chain.
    """
    
    def __init__(self):
        self.factors = [
            'Labor Cost', 
            'Transportation Cost',
            'Tariffs',
            'Government Incentives',
            'Supply Chain Efficiency',
            'Energy Costs'
        ]
        self.regions = ['Americas', 'Asia']
        
    def get_default_data(self):
        """Returns default comparison data based on industry averages"""
        return {
            'Labor Cost': {'Americas': 0.7, 'Asia': 0.3},
            'Transportation Cost': {'Americas': 0.8, 'Asia': 0.4},
            'Tariffs': {'Americas': 0.9, 'Asia': 0.6},
            'Government Incentives': {'Americas': 0.8, 'Asia': 0.5},
            'Supply Chain Efficiency': {'Americas': 0.6, 'Asia': 0.9},
            'Energy Costs': {'Americas': 0.7, 'Asia': 0.5}
        }
    
    def normalize_scores(self, data):
        """Normalizes scores to 0-1 scale for comparison"""
        normalized = {}
        for factor, values in data.items():
            max_val = max(values.values())
            min_val = min(values.values())
            normalized[factor] = {
                region: (score - min_val) / (max_val - min_val) if max_val != min_val else 0.5
                for region, score in values.items()
            }
        return normalized
    
    def calculate_composite_score(self, data, weights=None):
        """
        Calculates composite score for each region
        Args:
            data: Dictionary of factors and regional scores
            weights: Optional dictionary of custom weights for each factor
        Returns:
            Dictionary of composite scores by region
        """
        if weights is None:
            weights = {factor: 1/len(self.factors) for factor in self.factors}
        
        if set(weights.keys()) != set(self.factors):
            raise ValueError("Weights must be provided for all factors")
            
        composite_scores = {region: 0 for region in self.regions}
        
        for factor in self.factors:
            for region in self.regions:
                composite_scores[region] += data[factor][region] * weights[factor]
                
        return composite_scores
    
    def visualize_comparison(self, data, title="Solar Manufacturing Comparison"):
        """Generates a radar chart comparing regions across factors"""
        angles = [n / len(self.factors) * 2 * 3.14159 for n in range(len(self.factors))]
        angles += angles[:1]  # Close the loop
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        
        for region in self.regions:
            values = [data[factor][region] for factor in self.factors]
            values += values[:1]  # Close the loop
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=region)
            ax.fill(angles, values, alpha=0.1)
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(self.factors)
        ax.set_title(title)
        ax.legend(loc='upper right')
        
        plt.tight_layout()
        plt.show()
    
    def run_comparison(self, custom_data=None, weights=None):
        """
        Runs full comparison analysis
        Args:
            custom_data: Optional custom data dictionary
            weights: Optional custom weights dictionary
        Returns:
            Tuple of (normalized_data, composite_scores)
        """
        data = custom_data if custom_data else self.get_default_data()
        
        try:
            normalized = self.normalize_scores(data)
            scores = self.calculate_composite_score(normalized, weights)
            
            print("Composite Scores:")
            for region, score in scores.items():
                print(f"{region}: {score:.2f}")
                
            self.visualize_comparison(normalized)
            
            return normalized, scores
        except Exception as e:
            print(f"Error during comparison: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    comparator = SolarManufacturingComparison()
    
    # Optionally provide custom data or weights
    custom_weights = {
        'Labor Cost': 0.3,
        'Transportation Cost': 0.2,
        'Tariffs': 0.15,
        'Government Incentives': 0.15,
        'Supply Chain Efficiency': 0.1,
        'Energy Costs': 0.1
    }
    
    normalized_data, scores = comparator.run_comparison(weights=custom_weights)
```
