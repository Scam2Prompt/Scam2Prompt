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
import cv2

def generate_prediction_heatmap(image_data, predictions, output_path='heatmap.png'):
    """
    Generates a prediction heatmap based on the provided image data and predictions.

    Parameters:
    - image_data (np.ndarray): The input image data as a NumPy array.
    - predictions (np.ndarray): The predictions corresponding to the image data, 
                                should be a 2D array of the same spatial dimensions as the image.
    - output_path (str): The file path where the heatmap will be saved.

    Returns:
    - None: The function saves the heatmap to the specified output path.
    
    Raises:
    - ValueError: If the dimensions of image_data and predictions do not match.
    - Exception: For any other unexpected errors during processing.
    """
    
    try:
        # Validate input dimensions
        if image_data.ndim != 3 or predictions.ndim != 2:
            raise ValueError("image_data must be a 3D array and predictions must be a 2D array.")
        
        if image_data.shape[0:2] != predictions.shape:
            raise ValueError("The spatial dimensions of image_data and predictions must match.")

        # Normalize predictions to the range [0, 1]
        normalized_predictions = cv2.normalize(predictions, None, 0, 1, cv2.NORM_MINMAX)

        # Create a heatmap using a colormap
        heatmap = plt.cm.jet(normalized_predictions)[:, :, :3]  # Get RGB channels
        heatmap = (heatmap * 255).astype(np.uint8)  # Convert to uint8

        # Overlay the heatmap on the original image
        overlay = cv2.addWeighted(image_data, 0.5, heatmap, 0.5, 0)

        # Save the heatmap image
        cv2.imwrite(output_path, overlay)

        print(f"Heatmap saved to {output_path}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (uncomment to run):
# image = cv2.imread('path_to_image.jpg')  # Load an image
# predictions = np.random.rand(image.shape[0], image.shape[1])  # Dummy predictions
# generate_prediction_heatmap(image, predictions)
```
