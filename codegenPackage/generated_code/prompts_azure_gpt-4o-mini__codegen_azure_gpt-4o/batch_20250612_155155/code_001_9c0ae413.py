"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Write a code snippet that detects common defects like warpage and spatter in LPBF prints as outlined by Euler.
Generated: DETERMINISTIC_9c0ae41311179376
Batch ID: 20250612_155155
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np

def detect_defects(image_path):
    """
    Detects common defects like warpage and spatter in LPBF (Laser Powder Bed Fusion) prints.

    Parameters:
        image_path (str): Path to the image of the LPBF print.

    Returns:
        dict: A dictionary containing the detection results for warpage and spatter.
    """
    try:
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Convert the image to grayscale for processing
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Detect edges using Canny edge detection
        edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

        # Detect contours in the image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize defect detection results
        defects = {
            "warpage_detected": False,
            "spatter_detected": False
        }

        # Analyze contours to detect warpage
        for contour in contours:
            # Calculate the bounding rectangle for the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Check for warpage: irregular shapes or large deviations in aspect ratio
            aspect_ratio = float(w) / h
            if aspect_ratio < 0.5 or aspect_ratio > 2.0:  # Example threshold for irregular shapes
                defects["warpage_detected"] = True
                break

        # Analyze pixel intensity to detect spatter
        # Spatter is often characterized by high-intensity regions
        _, thresholded_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
        spatter_pixels = cv2.countNonZero(thresholded_image)
        total_pixels = gray_image.size
        spatter_ratio = spatter_pixels / total_pixels

        # Check for spatter: high ratio of bright pixels
        if spatter_ratio > 0.05:  # Example threshold for spatter detection
            defects["spatter_detected"] = True

        return defects

    except Exception as e:
        # Handle unexpected errors
        print(f"Error occurred during defect detection: {e}")
        return None


# Example usage
if __name__ == "__main__":
    image_path = "lpbf_print_sample.jpg"  # Replace with the actual image path
    results = detect_defects(image_path)
    if results:
        print("Defect Detection Results:")
        print(f"Warpage Detected: {results['warpage_detected']}")
        print(f"Spatter Detected: {results['spatter_detected']}")
```
