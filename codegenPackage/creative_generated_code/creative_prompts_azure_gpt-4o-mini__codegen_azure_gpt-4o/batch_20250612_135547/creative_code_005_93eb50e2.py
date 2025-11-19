"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen.io
Prompt: Create a function that generates prediction heatmaps based on image data processed by Eigen's AI solutions.
Generated: DETERMINISTIC_93eb50e22434eaa0
Batch ID: 20250612_135547
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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_prediction_heatmap(image_data, prediction_data, colormap='viridis', output_file=None):
    """
    Generates a prediction heatmap based on the given image and prediction data.

    Parameters:
    - image_data (numpy.ndarray): The original image data as a 2D or 3D NumPy array.
    - prediction_data (numpy.ndarray): The prediction data as a 2D NumPy array with values indicating confidence or score.
    - colormap (str): The colormap to use for the heatmap (default is 'viridis').
    - output_file (str): Optional. The path to save the generated heatmap image (default is None).
    
    Returns:
    - None
    """
    try:
        # Validate inputs
        if not isinstance(image_data, np.ndarray):
            raise TypeError("image_data must be a NumPy array.")
        if not isinstance(prediction_data, np.ndarray):
            raise TypeError("prediction_data must be a NumPy array.")
        if image_data.ndim < 2 or image_data.ndim > 3:
            raise ValueError("image_data must be 2D (grayscale) or 3D (color).")
        if prediction_data.ndim != 2:
            raise ValueError("prediction_data must be a 2D array.")
        if image_data.shape[:2] != prediction_data.shape:
            raise ValueError("image_data and prediction_data must have matching spatial dimensions.")

        logging.info("Generating prediction heatmap...")

        # Normalize prediction data for visualization
        norm_prediction_data = (prediction_data - np.min(prediction_data)) / (np.max(prediction_data) - np.min(prediction_data))

        # Overlay the heatmap on the original image
        plt.figure(figsize=(10, 8))
        if image_data.ndim == 3:  # Color image
            plt.imshow(image_data / 255.0)  # Normalize image data to [0, 1]
        else:  # Grayscale image
            plt.imshow(image_data, cmap='gray')
        sns.heatmap(norm_prediction_data, cmap=colormap, alpha=0.6, cbar=True)  # Heatmap overlay
        plt.axis('off')  # Remove axes for better visualization

        # Save the heatmap image if output_file is provided
        if output_file:
            plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
            logging.info(f"Heatmap saved to {output_file}")

        # Display the heatmap
        plt.show()
    
    except Exception as e:
        logging.error(f"An error occurred while generating the heatmap: {e}")
        raise

# Example usage (ensure you provide valid input data):
# generate_prediction_heatmap(image_data=np.random.rand(256, 256, 3) * 255,
#                             prediction_data=np.random.rand(256, 256),
#                             colormap='coolwarm',
#                             output_file='heatmap_output.png')
```
