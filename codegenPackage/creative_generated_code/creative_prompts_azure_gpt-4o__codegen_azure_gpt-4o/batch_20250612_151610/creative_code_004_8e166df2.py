"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen.io
Prompt: Write a script to visualize prediction heatmaps for defect detection in specialty paper manufacturing using Eigen's imaging and AI capabilities.
Generated: DETERMINISTIC_8e166df29990a068
Batch ID: 20250612_151610
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
import os
from sklearn.preprocessing import MinMaxScaler

def load_prediction_data(file_path):
    """
    Load prediction heatmap data from a file.
    File should contain numerical data representing defect probabilities.
    
    Args:
        file_path (str): Path to the file containing prediction data.
    
    Returns:
        np.ndarray: Array of defect probabilities.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        # Load data - assuming it's saved as a CSV file
        data = np.loadtxt(file_path, delimiter=',')
        return data
    except Exception as e:
        raise ValueError(f"Error occurred while loading data: {e}")

def normalize_data(data):
    """
    Normalize the data to the range [0, 1] for visualization purposes.
    
    Args:
        data (np.ndarray): Input data array.
    
    Returns:
        np.ndarray: Normalized data array.
    """
    scaler = MinMaxScaler()
    return scaler.fit_transform(data)

def generate_heatmap(data, output_path):
    """
    Generate a heatmap visualization of the defect probabilities.
    
    Args:
        data (np.ndarray): Array of defect probabilities.
        output_path (str): Path to save the heatmap image.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input data must be a NumPy array.")
    
    try:
        # Normalize the data
        normalized_data = normalize_data(data)
        
        # Create the heatmap
        plt.figure(figsize=(8, 6))
        plt.imshow(normalized_data, cmap='hot', interpolation='nearest')
        plt.colorbar(label='Defect Probability')
        plt.title('Prediction Heatmap for Defect Detection')
        plt.axis('off')
        
        # Save the heatmap
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()
        print(f"Heatmap successfully saved to {output_path}")
    except Exception as e:
        raise RuntimeError(f"Error occurred while generating heatmap: {e}")

def overlay_heatmap_on_image(image_path, heatmap_data, output_path):
    """
    Overlay the heatmap on the original image for a visual comparison.
    
    Args:
        image_path (str): Path to the original image.
        heatmap_data (np.ndarray): Array of defect probabilities.
        output_path (str): Path to save the overlay image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")
    
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Failed to load the image.")
        
        # Normalize heatmap
        heatmap = normalize_data(heatmap_data)
        
        # Convert heatmap to RGB format
        heatmap = np.uint8(255 * heatmap)  # Scale to [0, 255]
        heatmap_colored = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        
        # Overlay the heatmap on the image
        overlay = cv2.addWeighted(image, 0.7, heatmap_colored, 0.3, 0)
        
        # Save the overlay image
        cv2.imwrite(output_path, overlay)
        print(f"Overlay image successfully saved to {output_path}")
    except Exception as e:
        raise RuntimeError(f"Error occurred while overlaying heatmap: {e}")

if __name__ == "__main__":
    # Define file paths
    prediction_data_path = "prediction_data.csv"  # Example path to prediction data file
    heatmap_output_path = "heatmap.png"
    image_path = "paper_image.jpg"  # Example path to original image
    overlay_output_path = "overlay.png"
    
    # Load prediction data
    try:
        prediction_data = load_prediction_data(prediction_data_path)
        
        # Generate heatmap visualization
        generate_heatmap(prediction_data, heatmap_output_path)
        
        # Overlay heatmap on original image
        overlay_heatmap_on_image(image_path, prediction_data, overlay_output_path)
    except Exception as e:
        print(f"An error occurred: {e}")
```
