"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Write a script to visualize prediction heatmaps for defect detection in specialty paper manufacturing using Eigen's imaging and AI capabilities.
Generated: DETERMINISTIC_8e166df29990a068
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import eigen
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Define a function to load and preprocess the image
def load_image(image_path):
    """
    Load and preprocess the image for prediction.

    Args:
        image_path (str): Path to the image file.

    Returns:
        numpy array: Preprocessed image.
    """
    try:
        # Load the image using PIL
        image = Image.open(image_path)
        
        # Convert the image to an array
        image_array = img_to_array(image)
        
        # Normalize the pixel values
        image_array = image_array / 255.0
        
        return image_array
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Define a function to generate the prediction heatmap
def generate_heatmap(model, image_array):
    """
    Generate the prediction heatmap using the provided model.

    Args:
        model: Loaded Keras model.
        image_array (numpy array): Preprocessed image array.

    Returns:
        numpy array: Prediction heatmap.
    """
    try:
        # Make predictions on the image
        predictions = model.predict(np.expand_dims(image_array, axis=0))
        
        # Extract the defect probability
        defect_probability = predictions[0, 1]
        
        # Generate a heatmap
        heatmap = np.zeros((image_array.shape[0], image_array.shape[1]))
        heatmap = eigen.imshow(image_array, cmap='hot', interpolation='nearest')
        
        # Overlay the defect probability on the heatmap
        plt.title(f"Defect Probability: {defect_probability:.2f}")
        plt.colorbar()
        
        return heatmap
    except Exception as e:
        print(f"Error generating heatmap: {e}")
        return None

# Define the main function
def main():
    # Load the Keras model
    model_path = "defect_detection_model.h5"
    model = load_model(model_path)

    # Load the image
    image_path = "input_image.jpg"
    image_array = load_image(image_path)

    if image_array is not None:
        # Generate the prediction heatmap
        heatmap = generate_heatmap(model, image_array)

        # Display the heatmap
        if heatmap is not None:
            plt.show()

if __name__ == "__main__":
    main()
```
