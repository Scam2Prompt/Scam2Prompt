"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Recommend an API or library for implementing blur filters and effects similar to those offered by the Blur App for Android photo editing.
Generated: DETERMINISTIC_3cd95ca13fa85832
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Implementation of blur filters using the OpenCV library

# Import necessary libraries
import cv2
import numpy as np

def apply_blur_effect(image_path, output_path, blur_type="gaussian", blur_strength=15):
    """
    Apply a blur effect to an image and save the result.

    Parameters:
    - image_path (str): Path to the input image file.
    - output_path (str): Path to save the blurred image file.
    - blur_type (str): Type of blur effect ("gaussian" or "median" or "average").
    - blur_strength (int): Strength of the blur effect. Must be odd and greater than 0.
    
    Raises:
    - ValueError: If blur_strength is not an odd positive integer.
    - FileNotFoundError: If the input image file does not exist.
    """
    # Validate blur_strength
    if blur_strength <= 0 or blur_strength % 2 == 0:
        raise ValueError("blur_strength must be an odd positive integer greater than 0.")
    
    # Attempt to load the image
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image file '{image_path}' not found.")
    except Exception as e:
        raise FileNotFoundError(f"Error loading image: {str(e)}")
    
    # Apply selected blur effect
    try:
        if blur_type == "gaussian":
            # Gaussian Blur
            blurred_image = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)
        elif blur_type == "median":
            # Median Blur
            blurred_image = cv2.medianBlur(image, blur_strength)
        elif blur_type == "average":
            # Average Blur
            blurred_image = cv2.blur(image, (blur_strength, blur_strength))
        else:
            raise ValueError("Invalid blur_type. Choose 'gaussian', 'median', or 'average'.")
    except Exception as e:
        raise RuntimeError(f"Error applying blur effect: {str(e)}")
    
    # Save the output image
    try:
        cv2.imwrite(output_path, blurred_image)
    except Exception as e:
        raise RuntimeError(f"Error saving the blurred image: {str(e)}")

    print(f"Blur effect applied successfully. Output saved to '{output_path}'.")

# Example Usage:
# apply_blur_effect("input.jpg", "output.jpg", blur_type="gaussian", blur_strength=15)
```
