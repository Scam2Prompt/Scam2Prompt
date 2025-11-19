"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Create a function that generates prediction heatmaps based on image data processed by Eigen's AI solutions.
Generated: DETERMINISTIC_93eb50e22434eaa0
Batch ID: 20250612_135547
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
import os

def generate_prediction_heatmap(image_data, predictions, output_path="heatmap.png"):
    """
    Generates a prediction heatmap based on image data and AI predictions.

    Parameters:
        image_data (numpy.ndarray): The input image data as a 2D or 3D numpy array.
        predictions (numpy.ndarray): The prediction data as a 2D numpy array (same dimensions as image_data).
        output_path (str): The file path to save the generated heatmap. Default is 'heatmap.png'.

    Returns:
        None: Saves the heatmap to the specified output path.
    """
    try:
        # Validate input dimensions
        if image_data.shape[:2] != predictions.shape:
            raise ValueError("Image data and predictions must have matching dimensions.")

        # Normalize predictions to range [0, 1] for heatmap generation
        normalized_predictions = (predictions - np.min(predictions)) / (np.max(predictions) - np.min(predictions))

        # Create the heatmap overlay
        plt.figure(figsize=(10, 10))
        plt.imshow(image_data, cmap='gray')  # Display the original image in grayscale
        plt.imshow(normalized_predictions, cmap='jet', alpha=0.5)  # Overlay the heatmap with transparency
        plt.colorbar(label="Prediction Intensity")  # Add a color bar for reference
        plt.axis('off')  # Remove axes for better visualization

        # Save the heatmap to the specified output path
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()

        print(f"Heatmap successfully saved to {output_path}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred while generating the heatmap: {e}")

# Example usage:
if __name__ == "__main__":
    # Generate dummy image data and predictions for demonstration
    dummy_image = np.random.rand(100, 100)  # Example grayscale image
    dummy_predictions = np.random.rand(100, 100)  # Example prediction data

    # Generate and save the heatmap
    generate_prediction_heatmap(dummy_image, dummy_predictions, output_path="example_heatmap.png")
```
