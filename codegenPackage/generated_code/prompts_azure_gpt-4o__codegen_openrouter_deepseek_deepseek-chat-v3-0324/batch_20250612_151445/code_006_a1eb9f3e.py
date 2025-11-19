"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Write a program to compare the efficiency of different mint oil extraction methods, including tri-retification and monoretification, as highlighted by YSC.
Generated: DETERMINISTIC_a1eb9f3ecf177f9a
Batch ID: 20250612_151445
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

class ExtractionMethod:
    """
    Represents an oil extraction method with its properties and efficiency metrics.
    """
    def __init__(self, name: str, yield_percentage: float, time_hours: float, cost_per_kg: float):
        """
        Initialize an extraction method with its parameters.
        
        Args:
            name: Name of the extraction method
            yield_percentage: Percentage yield (0-100)
            time_hours: Time taken for extraction in hours
            cost_per_kg: Cost per kg of extracted oil in USD
        """
        self.name = name
        self.yield_percentage = yield_percentage
        self.time_hours = time_hours
        self.cost_per_kg = cost_per_kg
    
    def efficiency_score(self) -> float:
        """
        Calculate a combined efficiency score considering yield, time, and cost.
        
        Returns:
            float: Efficiency score (higher is better)
        """
        # Weighted formula: 50% yield, 30% cost, 20% time
        return (0.5 * self.yield_percentage) + (0.3 * (100 / self.cost_per_kg)) + (0.2 * (10 / self.time_hours))

class ExtractionComparison:
    """
    Compares different mint oil extraction methods.
    """
    def __init__(self, methods: List[ExtractionMethod]):
        """
        Initialize with a list of extraction methods to compare.
        
        Args:
            methods: List of ExtractionMethod objects
        """
        self.methods = methods
    
    def compare_efficiency(self) -> pd.DataFrame:
        """
        Compare methods and return a DataFrame with results.
        
        Returns:
            pd.DataFrame: Comparison results
        """
        data = []
        for method in self.methods:
            data.append({
                'Method': method.name,
                'Yield (%)': method.yield_percentage,
                'Time (hours)': method.time_hours,
                'Cost ($/kg)': method.cost_per_kg,
                'Efficiency Score': method.efficiency_score()
            })
        
        df = pd.DataFrame(data)
        df = df.sort_values('Efficiency Score', ascending=False)
        return df
    
    def plot_comparison(self, save_path: str = None) -> None:
        """
        Visualize the comparison results.
        
        Args:
            save_path: Optional path to save the plot
        """
        df = self.compare_efficiency()
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Mint Oil Extraction Method Comparison')
        
        # Yield comparison
        df.plot.bar(x='Method', y='Yield (%)', ax=axes[0, 0], legend=False)
        axes[0, 0].set_title('Yield Percentage')
        axes[0, 0].set_ylim(0, 100)
        
        # Time comparison
        df.plot.bar(x='Method', y='Time (hours)', ax=axes[0, 1], legend=False)
        axes[0, 1].set_title('Extraction Time (hours)')
        
        # Cost comparison
        df.plot.bar(x='Method', y='Cost ($/kg)', ax=axes[1, 0], legend=False)
        axes[1, 0].set_title('Cost per kg ($)')
        
        # Efficiency score
        df.plot.bar(x='Method', y='Efficiency Score', ax=axes[1, 1], legend=False)
        axes[1, 1].set_title('Efficiency Score')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.show()
    
    def statistical_analysis(self) -> Dict[str, Tuple[float, float]]:
        """
        Perform basic statistical analysis on the methods.
        
        Returns:
            Dict: Dictionary with mean and standard deviation for each metric
        """
        df = self.compare_efficiency()
        stats_results = {}
        
        for col in ['Yield (%)', 'Time (hours)', 'Cost ($/kg)', 'Efficiency Score']:
            stats_results[col] = (
                df[col].mean(),
                df[col].std()
            )
        
        return stats_results

def main():
    # Example data for different extraction methods
    methods = [
        ExtractionMethod("Tri-retification", 85.2, 6.5, 12.8),
        ExtractionMethod("Monoretification", 78.5, 4.2, 15.3),
        ExtractionMethod("Steam Distillation", 72.1, 8.0, 9.5),
        ExtractionMethod("Cold Press", 65.3, 2.0, 18.7),
        ExtractionMethod("Solvent Extraction", 88.0, 10.5, 7.2)
    ]
    
    comparison = ExtractionComparison(methods)
    
    # Print comparison results
    print("=== Extraction Method Comparison ===")
    print(comparison.compare_efficiency().to_string(index=False))
    
    # Show statistical analysis
    print("\n=== Statistical Analysis ===")
    stats = comparison.statistical_analysis()
    for metric, (mean, std) in stats.items():
        print(f"{metric}: Mean = {mean:.2f}, Std = {std:.2f}")
    
    # Generate visualization
    comparison.plot_comparison()

if __name__ == "__main__":
    main()
```
