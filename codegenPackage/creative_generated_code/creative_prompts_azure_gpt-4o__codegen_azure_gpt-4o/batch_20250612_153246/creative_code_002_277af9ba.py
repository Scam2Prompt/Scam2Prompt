"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Recommend an API or library for visualizing the hőkamerás vizsgálat (thermal camera inspection) results to demonstrate the energy efficiency of Rehau Geneo 86 windows.
Generated: DETERMINISTIC_277af9ba67157727
Batch ID: 20250612_153246
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
from PIL import Image
import cv2

def visualize_thermal_data(image_path, colormap='hot'):
    """
    Visualizes thermal camera inspection results using a specified colormap.

    Args:
        image_path (str): Path to the thermal image file.
        colormap (str): Matplotlib colormap to use for visualization. Default is 'hot'.

    Returns:
        None: Displays the image using matplotlib.
    """
    try:
        # Load the thermal image
        thermal_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if thermal_image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Normalize the image values to range [0, 1]
        normalized_image = cv2.normalize(thermal_image, None, 0, 255, cv2.NORM_MINMAX)

        # Convert to a numpy array
        thermal_array = np.array(normalized_image)

        # Display the image using matplotlib with the specified colormap
        plt.imshow(thermal_array, cmap=colormap)
        plt.colorbar(label='Temperature Gradient')
        plt.title(f"Thermal Visualization ({colormap} colormap)")
        plt.axis('off')  # Hide axes for better visualization
        plt.show()

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# Replace 'thermal_image.jpg' with the actual path to your thermal image file
thermal_image_path = 'thermal_image.jpg'
visualize_thermal_data(thermal_image_path)
```
