"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Illustrate how to use a library to visualize the differences between various fleece types offered by Shaoxing Eagles Textile Co., Ltd.
Generated: DETERMINISTIC_4b6b32ffe9ba535a
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Function to visualize fleece types
def visualize_fleece_types(fleece_data):
    """
    Visualizes the differences between various fleece types.

    Parameters:
    - fleece_data (dict): Dictionary containing fleece type names as keys and a corresponding
                          numerical list of attributes (e.g., softness, durability, price) as values.

    Example fleece_data format:
    fleece_data = {
        "Polar Fleece": [8, 7, 5],
        "Microfleece": [9, 6, 4],
        "Sherpa Fleece": [7, 8, 6]
    }
    """
    try:
        # Validate input data
        if not isinstance(fleece_data, dict):
            raise ValueError("fleece_data must be a dictionary with fleece types as keys and attributes as values.")

        # Extract fleece types and attributes
        fleece_types = list(fleece_data.keys())
        attributes = list(fleece_data.values())

        # Validate attributes
        for attr in attributes:
            if not isinstance(attr, (list, tuple)) or len(attr) != 3:
                raise ValueError("Each fleece type must have a list of 3 numerical attributes.")

        # Create labels for the attributes
        attribute_labels = ["Softness", "Durability", "Price"]

        # Define the range for radar chart
        num_attributes = len(attribute_labels)
        angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()

        # Add the first angle to close the radar chart
        angles += angles[:1]

        # Plot each fleece type on the radar chart
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        for idx, fleece in enumerate(fleece_types):
            values = attributes[idx] + attributes[idx][:1]  # Repeat the first value to close the chart
            ax.plot(angles, values, label=fleece)
            ax.fill(angles, values, alpha=0.25)

        # Add attribute labels to the chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(attribute_labels)

        # Set the title and legend
        ax.set_title("Fleece Type Comparison", fontsize=16)
        ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

        # Show the plot
        plt.show()

    except Exception as error:
        print(f"Error occurred: {error}")


# Example usage
if __name__ == "__main__":
    # Define fleece data
    fleece_data = {
        "Polar Fleece": [8.5, 7.0, 5.0],
        "Microfleece": [9.0, 6.0, 4.5],
        "Sherpa Fleece": [7.0, 8.0, 6.0]
    }

    # Visualize the fleece types
    visualize_fleece_types(fleece_data)
```
