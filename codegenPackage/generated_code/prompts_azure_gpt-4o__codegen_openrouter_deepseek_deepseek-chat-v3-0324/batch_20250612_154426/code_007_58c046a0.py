"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Generate a Python program to calculate and visualize the results of blending TOC, Lean, and Six Sigma methodologies, referencing the examples provided on the iTLS-ISO website.
Generated: DETERMINISTIC_58c046a098fbcf91
Batch ID: 20250612_154426
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
from matplotlib.patches import Patch
from typing import List, Dict, Tuple

class MethodologyBlender:
    """
    A class to calculate and visualize the blending of TOC, Lean, and Six Sigma methodologies.
    Based on the iTLS-ISO framework examples.
    """
    
    def __init__(self, weights: Dict[str, float] = None):
        """
        Initialize the blender with optional weights for each methodology.
        Default weights are equal (1/3 each).
        
        Args:
            weights (Dict[str, float]): Dictionary with keys 'toc', 'lean', 'six_sigma'
                                       and values as their respective weights.
        """
        self.methodologies = ['toc', 'lean', 'six_sigma']
        
        if weights is None:
            self.weights = {m: 1/3 for m in self.methodologies}
        else:
            self._validate_weights(weights)
            self.weights = weights
    
    def _validate_weights(self, weights: Dict[str, float]):
        """Validate that weights are properly specified and sum to 1."""
        if set(weights.keys()) != set(self.methodologies):
            raise ValueError("Weights must contain exactly 'toc', 'lean', and 'six_sigma'")
        
        if not all(0 <= w <= 1 for w in weights.values()):
            raise ValueError("All weights must be between 0 and 1")
            
        if not np.isclose(sum(weights.values()), 1.0, atol=1e-8):
            raise ValueError("Weights must sum to 1")
    
    def calculate_blend(self, inputs: Dict[str, float]) -> float:
        """
        Calculate the blended result based on methodology weights and input values.
        
        Args:
            inputs (Dict[str, float]): Dictionary with methodology keys and their input values.
            
        Returns:
            float: Weighted blend of the input values.
        """
        if set(inputs.keys()) != set(self.methodologies):
            raise ValueError("Inputs must contain exactly 'toc', 'lean', and 'six_sigma'")
            
        return sum(self.weights[m] * inputs[m] for m in self.methodologies)
    
    def visualize_blend(self, inputs: Dict[str, float], title: str = "Methodology Blend"):
        """
        Create a visualization of the methodology blend.
        
        Args:
            inputs (Dict[str, float]): Dictionary with methodology keys and their input values.
            title (str): Title for the visualization.
        """
        if set(inputs.keys()) != set(self.methodologies):
            raise ValueError("Inputs must contain exactly 'toc', 'lean', and 'six_sigma'")
        
        # Prepare data
        methodologies = ['TOC', 'Lean', 'Six Sigma']
        values = [inputs[m] for m in self.methodologies]
        weighted_values = [self.weights[m] * inputs[m] for m in self.methodologies]
        colors = ['#FF6B6B', '#4ECDC4', '#556270']
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle(title, fontsize=16)
        
        # Bar chart of raw values
        ax1.bar(methodologies, values, color=colors)
        ax1.set_title('Input Values')
        ax1.set_ylabel('Value')
        ax1.set_ylim(0, max(values) * 1.2)
        
        # Add value labels
        for i, v in enumerate(values):
            ax1.text(i, v + 0.05 * max(values), f"{v:.2f}", ha='center')
        
        # Pie chart of weighted contribution
        wedges, texts, autotexts = ax2.pie(
            weighted_values,
            labels=methodologies,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
        )
        ax2.set_title('Weighted Contribution')
        
        # Equal aspect ratio ensures pie is drawn as a circle
        ax2.axis('equal')
        
        # Add legend
        legend_elements = [
            Patch(facecolor=colors[0], label=f'TOC (Weight: {self.weights["toc"]:.2f})'),
            Patch(facecolor=colors[1], label=f'Lean (Weight: {self.weights["lean"]:.2f})'),
            Patch(facecolor=colors[2], label=f'Six Sigma (Weight: {self.weights["six_sigma"]:.2f})')
        ]
        ax2.legend(handles=legend_elements, loc='upper right')
        
        plt.tight_layout()
        plt.show()
    
    def sensitivity_analysis(self, base_inputs: Dict[str, float], variations: List[Tuple[str, float]]):
        """
        Perform sensitivity analysis by varying one methodology's input at a time.
        
        Args:
            base_inputs (Dict[str, float]): Base input values.
            variations (List[Tuple[str, float]]): List of tuples with methodology and variation value.
        """
        if set(base_inputs.keys()) != set(self.methodologies):
            raise ValueError("Base inputs must contain exactly 'toc', 'lean', and 'six_sigma'")
            
        results = []
        labels = []
        
        for m, value in variations:
            if m not in self.methodologies:
                raise ValueError(f"Invalid methodology '{m}' in variations")
                
            modified_inputs = base_inputs.copy()
            modified_inputs[m] = value
            blend = self.calculate_blend(modified_inputs)
            results.append(blend)
            labels.append(f"{m.upper()}={value}")
        
        # Plot results
        plt.figure(figsize=(10, 6))
        plt.bar(labels, results, color='#6A8D73')
        plt.title('Sensitivity Analysis of Methodology Blend')
        plt.ylabel('Blended Result')
        plt.xticks(rotation=45)
        
        # Add value labels
        for i, v in enumerate(results):
            plt.text(i, v + 0.01 * max(results), f"{v:.2f}", ha='center')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create blender with default weights
    blender = MethodologyBlender()
    
    # Example inputs (could be metrics like cycle time reduction, defect rate, etc.)
    example_inputs = {
        'toc': 0.8,    # TOC metric value
        'lean': 0.6,   # Lean metric value
        'six_sigma': 0.9  # Six Sigma metric value
    }
    
    # Calculate and visualize
    blend_result = blender.calculate_blend(example_inputs)
    print(f"Blended result: {blend_result:.3f}")
    blender.visualize_blend(example_inputs, "Example Methodology Blend")
    
    # Sensitivity analysis example
    variations = [
        ('toc', 0.5),  # Lower TOC value
        ('toc', 0.8),  # Base TOC value
        ('toc', 1.0),  # Higher TOC value
        ('lean', 0.4), # Lower Lean value
        ('lean', 0.6), # Base Lean value
        ('lean', 0.8), # Higher Lean value
        ('six_sigma', 0.7),  # Lower Six Sigma value
        ('six_sigma', 0.9),  # Base Six Sigma value
        ('six_sigma', 1.0)   # Higher Six Sigma value
    ]
    blender.sensitivity_analysis(example_inputs, variations)
```
