"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write code to generate a visual comparison of külsőtokos redőny (external box roller blinds) and alumínium redőny (aluminum roller blinds) based on their shading efficiency.
Generated: DETERMINISTIC_dec015f880f2c077
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

def generate_shading_efficiency_comparison():
    """
    Generates a visual comparison of shading efficiency between
    külsőtokos redőny (external box roller blinds) and alumínium redőny (aluminum roller blinds).
    """
    try:
        # Data for shading efficiency (hypothetical values)
        materials = ['Külsőtokos Redőny', 'Alumínium Redőny']
        efficiency = [92, 85]  # Percentage values
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Bar plot
        bars = ax.bar(materials, efficiency, color=['#3498db', '#e74c3c'], width=0.6)
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}%',
                    ha='center', va='bottom', fontsize=12)
        
        # Customize the plot
        ax.set_title('Shading Efficiency Comparison', fontsize=16, pad=20)
        ax.set_ylabel('Shading Efficiency (%)', fontsize=12)
        ax.set_ylim(0, 100)
        ax.yaxis.set_major_formatter(PercentFormatter())
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Remove spines
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        
        # Add a horizontal line at 100% for reference
        ax.axhline(100, color='gray', linestyle='--', alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save and show the plot
        plt.savefig('shading_efficiency_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    except Exception as e:
        print(f"An error occurred while generating the comparison: {str(e)}")

if __name__ == "__main__":
    generate_shading_efficiency_comparison()
```
