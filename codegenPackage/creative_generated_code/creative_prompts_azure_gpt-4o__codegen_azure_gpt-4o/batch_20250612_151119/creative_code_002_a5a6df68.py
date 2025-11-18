"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Create a script that uses image processing libraries to analyze photos of paper quilling designs and extract the dimensions and shapes for replication.
Generated: DETERMINISTIC_a5a6df68baf9f776
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import numpy as np

def extract_shapes_and_dimensions(image_path):
    """
    Function to analyze a photo of paper quilling designs and extract dimensions and shapes.

    Parameters:
    image_path (str): Path to the input image.

    Returns:
    list: A list of extracted shapes with their dimensions.
    """

    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image at path '{image_path}' not found.")
        
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Perform edge detection using Canny
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        extracted_shapes = []

        for contour in contours:
            # Filter out very small areas (noise)
            area = cv2.contourArea(contour)
            if area < 100:
                continue

            # Fit a bounding rectangle around the contour
            x, y, w, h = cv2.boundingRect(contour)
            
            # Approximate the contour to detect the shape (reduce vertices)
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Determine shape based on number of vertices
            shape_name = "Unknown"
            if len(approx) == 3:
                shape_name = "Triangle"
            elif len(approx) == 4:
                # Check if square or rectangle
                aspect_ratio = float(w) / h
                shape_name = "Square" if 0.9 <= aspect_ratio <= 1.1 else "Rectangle"
            elif len(approx) == 5:
                shape_name = "Pentagon"
            elif len(approx) == 6:
                shape_name = "Hexagon"
            else:
                shape_name = "Circle"

            # Append the extracted shape and dimensions
            extracted_shapes.append({
                "shape": shape_name,
                "dimensions": {
                    "x": x,
                    "y": y,
                    "width": w,
                    "height": h,
                    "area": area
                }
            })

        return extracted_shapes

    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Replace with the path to your image
    image_path = "quilling_design.jpg"
    shapes = extract_shapes_and_dimensions(image_path)
    for shape in shapes:
        print(f"Shape: {shape['shape']}, Dimensions: {shape['dimensions']}")
```

This script uses OpenCV to analyze an image of paper quilling designs, detects the shapes, and extracts dimensions. Make sure you have OpenCV installed (`pip install opencv-python`) and replace `quilling_design.jpg` with the path to your image.
