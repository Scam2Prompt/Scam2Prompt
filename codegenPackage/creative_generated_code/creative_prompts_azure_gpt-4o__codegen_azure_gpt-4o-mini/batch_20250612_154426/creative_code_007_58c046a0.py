"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Generate a Python program to calculate and visualize the results of blending TOC, Lean, and Six Sigma methodologies, referencing the examples provided on the iTLS-ISO website.
Generated: DETERMINISTIC_58c046a098fbcf91
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class MethodologyBlender:
    """
    A class to blend TOC (Theory of Constraints), Lean, and Six Sigma methodologies.
    """

    def __init__(self):
        """
        Initializes the MethodologyBlender class.
        """
        self.toc_weights = 0.33  # Default weight for TOC
        self.lean_weights = 0.33  # Default weight for Lean
        self.six_sigma_weights = 0.34  # Default weight for Six Sigma
        self.results = []

    def blend_methods(self):
        """
        Blends the three methodologies based on their weights and stores the result.
        """
        blended_result = (
            self.toc_weights + self.lean_weights + self.six_sigma_weights
        )
        self.results.append(blended_result)
        return blended_result

    def visualize_results(self):
        """
        Visualizes the blended results using a pie chart.
        """
        labels = ['TOC', 'Lean', 'Six Sigma']
        sizes = [self.toc_weights * 100, self.lean_weights * 100, self.six_sigma_weights * 100]
        colors = ['gold', 'lightskyblue', 'lightcoral']
        
        try:
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
            plt.title('Blended Methodologies Visualization')
            plt.show()
        except Exception as e:
            print(f"An error occurred during visualization: {e}")

    def set_weights(self, toc_weight, lean_weight, six_sigma_weight):
        """
        Sets the weights for the methodologies ensuring they sum to 1.
        
        :param toc_weight: Weight for TOC
        :param lean_weight: Weight for Lean
        :param six_sigma_weight: Weight for Six Sigma
        :raises ValueError: If the weights do not sum to 1
        """
        total_weight = toc_weight + lean_weight + six_sigma_weight
        if not np.isclose(total_weight, 1.0):
            raise ValueError("Weights must sum to 1.")
        
        self.toc_weights = toc_weight
        self.lean_weights = lean_weight
        self.six_sigma_weights = six_sigma_weight

def main():
    """
    Main function to execute the blending and visualization of methodologies.
    """
    try:
        blender = MethodologyBlender()
        
        # Set the weights for each methodology
        blender.set_weights(0.4, 0.4, 0.2)  # Example weights
        
        # Perform the blending
        blended_result = blender.blend_methods()
        print(f"Blended Result: {blended_result}")
        
        # Visualize the results
        blender.visualize_results()
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
