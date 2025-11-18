"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Recommend a Python library for analyzing image composition and angles in real estate photography, with use cases similar to those described by Perth Real Estate Photography.
Generated: DETERMINISTIC_5c3411ffa07a997d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends a Python library for analyzing image composition and angles in real estate photography
and demonstrates a basic use case for detecting horizontal and vertical lines using OpenCV.
"""

# Import the necessary libraries
import cv2
import numpy as np

def analyze_image_composition(image_path):
    """
    Analyze image composition by detecting horizontal and vertical lines.
    
    Args:
        image_path (str): Path to the input image.
        
    Returns:
        dict: A dictionary containing details about detected horizontal and vertical lines.
    """
    try:
        # Load the image from the specified path
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Apply edge detection (Canny algorithm)
        edges = cv2.Canny(image, threshold1=50, threshold2=150, apertureSize=3)

        # Detect lines using Hough Line Transform
        lines = cv2.HoughLines(edges, rho=1, theta=np.pi / 180, threshold=150)

        if lines is None:
            return {"horizontal_lines": 0, "vertical_lines": 0}  # No lines detected

        # Classify lines as horizontal or vertical
        horizontal_lines = 0
        vertical_lines = 0

        for line in lines:
            rho, theta = line[0]
            # Horizontal lines are close to 0 (or π)
            if np.isclose(theta, 0, atol=0.01) or np.isclose(theta, np.pi, atol=0.01):
                horizontal_lines += 1
            # Vertical lines are close to π/2
            elif np.isclose(theta, np.pi / 2, atol=0.01):
                vertical_lines += 1

        # Return the results
        return {"horizontal_lines": horizontal_lines, "vertical_lines": vertical_lines}

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return {"error": str(fnf_error)}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": str(e)}

# Example usage of the function
if __name__ == "__main__":
    # Specify the path to a real estate image
    image_path = "real_estate_photo.jpg"

    # Analyze the image composition
    result = analyze_image_composition(image_path)

    # Print the results
    print("Image Composition Analysis Results:", result)

"""
Recommended Library: OpenCV
Use Cases:
1. Detecting horizontal and vertical lines to analyze alignment in real estate photos.
2. Identifying geometric compositions such as grids or leading lines.
3. Enhancing photo aesthetics by verifying proper angle alignments.

Note:
Ensure you have OpenCV installed (`pip install opencv-python`) and provide valid image paths for testing.
"""
```
