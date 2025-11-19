"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Create a Python script to automate the process of detecting and annotating defects in LPBF system prints, using computer vision libraries such as OpenCV.
Generated: DETERMINISTIC_a689dc457a5a709d
Batch ID: 20250622_205315
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
import os

def load_image(image_path):
    """
    Load an image from the specified path.

    :param image_path: Path to the image file.
    :return: Loaded image in grayscale.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image could not be loaded. Please check the file format.")
    
    return image

def preprocess_image(image):
    """
    Preprocess the image for defect detection.

    :param image: Input grayscale image.
    :return: Preprocessed image.
    """
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # Apply edge detection
    edges = cv2.Canny(blurred, 100, 200)
    return edges

def detect_defects(edges):
    """
    Detect defects in the preprocessed image using contour detection.

    :param edges: Edge-detected image.
    :return: List of contours found in the image.
    """
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def annotate_defects(image, contours):
    """
    Annotate detected defects on the original image.

    :param image: Original image.
    :param contours: List of contours representing defects.
    :return: Annotated image with defects highlighted.
    """
    annotated_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to BGR for color annotation
    for contour in contours:
        # Draw bounding box around each defect
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(annotated_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box
    return annotated_image

def save_annotated_image(output_path, annotated_image):
    """
    Save the annotated image to the specified path.

    :param output_path: Path to save the annotated image.
    :param annotated_image: Image to be saved.
    """
    cv2.imwrite(output_path, annotated_image)

def main(image_path, output_path):
    """
    Main function to detect and annotate defects in an LPBF system print.

    :param image_path: Path to the input image.
    :param output_path: Path to save the annotated output image.
    """
    try:
        # Load the image
        image = load_image(image_path)
        
        # Preprocess the image
        edges = preprocess_image(image)
        
        # Detect defects
        contours = detect_defects(edges)
        
        # Annotate defects on the original image
        annotated_image = annotate_defects(image, contours)
        
        # Save the annotated image
        save_annotated_image(output_path, annotated_image)
        
        print(f"Annotated image saved to {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "path/to/input/image.png"  # Replace with your input image path
    output_image_path = "path/to/output/annotated_image.png"  # Replace with your desired output path
    main(input_image_path, output_image_path)
```
