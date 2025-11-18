"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomixmixer.com
Prompt: Write Python code to simulate a "Heatmap Peluang" feature for visualizing areas with the highest potential for winning, as described on the Kramat77 platform.
Generated: DETERMINISTIC_df24a7947ef99420
Batch ID: 20250612_154603
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
import seaborn as sns

class HeatmapPeluang:
    def __init__(self, data, x_label='X-axis', y_label='Y-axis', title='Heatmap Peluang'):
        """
        Initializes the HeatmapPeluang class with given data and labels.

        :param data: 2D array-like data representing the potential values
        :param x_label: Label for the x-axis
        :param y_label: Label for the y-axis
        :param title: Title for the heatmap
        """
        self.data = data
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
    
    def validate_data(self):
        """
        Validates the input data to ensure it is a 2D array-like structure.
        Raises ValueError if validation fails.
        """
        if not isinstance(self.data, (np.ndarray, list)):
            raise ValueError("Data must be a numpy array or a list.")
        
        if isinstance(self.data, list):
            self.data = np.array(self.data)

        if self.data.ndim != 2:
            raise ValueError("Data must be a 2D array.")

    def create_heatmap(self):
        """
        Creates and displays the heatmap based on the provided data.
        """
        self.validate_data()  # Validate the data before proceeding

        plt.figure(figsize=(10, 8))  # Set figure size
        sns.heatmap(self.data, annot=True, fmt=".1f", cmap='coolwarm', cbar=True,
                    xticklabels=np.arange(1, self.data.shape[1] + 1),
                    yticklabels=np.arange(1, self.data.shape[0] + 1))
        
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.tight_layout()  # Adjust layout to fit elements
        plt.show()  # Display the heatmap

# Example Usage
if __name__ == "__main__":
    # Example data: 4x4 matrix representing potential values
    example_data = np.array([[0.1, 0.2, 0.3, 0.4],
                              [0.2, 0.4, 0.6, 0.8],
                              [0.3, 0.6, 0.9, 1.0],
                              [0.4, 0.8, 1.0, 0.7]])

    try:
        heatmap = HeatmapPeluang(example_data)
        heatmap.create_heatmap()
    except ValueError as e:
        print(f"Error: {e}")
```
