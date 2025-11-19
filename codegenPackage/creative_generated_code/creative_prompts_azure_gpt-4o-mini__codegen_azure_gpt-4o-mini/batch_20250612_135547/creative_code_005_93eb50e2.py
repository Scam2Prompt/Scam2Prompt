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
import cv2

def generate_prediction_heatmap(image_data: np.ndarray, predictions: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """
    Generates a heatmap overlay for given predictions on the input image data.

    Parameters:
    - image_data (np.ndarray): The original image data (H, W, C).
    - predictions (np.ndarray): The prediction data (H, W) where each value corresponds to the model's prediction score.
    - alpha (float): The transparency level of the heatmap overlay. Defaults to 0.5.

    Returns:
    - np.ndarray: The image with the heatmap overlay.
    
    Raises:
    - ValueError: If the shape of the predictions does not match the image data.
    """

    # Validate input shapes
    if image_data.ndim != 3 or predictions.ndim != 2:
        raise ValueError("Invalid input dimensions: image_data must be HxWxC and predictions must be HxW.")
    
    if image_data.shape[0:2] != predictions.shape:
        raise ValueError("The shape of predictions must match the spatial dimensions of image_data.")

    # Normalize predictions to range [0, 1]
    normalized_predictions = cv2.normalize(predictions, None, 0, 1, cv2.NORM_MINMAX)

    # Create a colormap (jet colormap is a common choice)
    heatmap = plt.cm.jet(normalized_predictions)[:, :, :3]  # Get RGB channels
    
    # Convert heatmap to uint8
    heatmap = (heatmap * 255).astype(np.uint8)

    # Blend the original image with the heatmap
    blended_image = cv2.addWeighted(image_data, 1 - alpha, heatmap, alpha, 0)

    return blended_image

# Example usage (uncomment to run):
# if __name__ == "__main__":
#     # Load an image (make sure to provide a valid path)
#     image = cv2.imread('path_to_image.jpg')

#     # Simulate predictions (for example, a 2D array with the same width and height as the image)
#     predictions = np.random.rand(image.shape[0], image.shape[1])

#     try:
#         heatmap_image = generate_prediction_heatmap(image, predictions, alpha=0.5)

#         # Display the original image and the heatmap
#         cv2.imshow('Original Image', image)
#         cv2.imshow('Heatmap Overlay', heatmap_image)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     except ValueError as e:
#         print(f"Error: {e}")
```
