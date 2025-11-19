"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler.is
Prompt: Write a code snippet that detects common defects like warpage and spatter in LPBF prints as outlined by Euler.
Generated: DETERMINISTIC_9c0ae41311179376
Batch ID: 20250612_155155
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
import logging

# Initialize logging for defect detection
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_defects(image_path):
    """
    Detects common LPBF defects like warpage and spatter in a given image.
    
    Parameters:
        image_path (str): Path to the image file.
    
    Returns:
        dict: Dictionary containing defect analysis results.
    """
    try:
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError("Image could not be loaded. Please check the file path.")

        # Preprocess the image: Gaussian blur to reduce noise
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

        # Detect edges using Canny edge detection
        edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

        # Find contours in the image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize defect flags
        warpage_detected = False
        spatter_detected = False

        for contour in contours:
            # Compute the area and perimeter of the contour
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)

            # Detect warpage: Irregular shapes with high perimeter-area ratio
            if perimeter > 0 and area > 0:
                ratio = perimeter / area
                if ratio > 0.1:  # Threshold for warpage detection (adjustable)
                    warpage_detected = True
                    logging.info("Warpage detected in the print.")

            # Detect spatter: Small isolated blobs
            if area < 50:  # Threshold for spatter detection (adjustable)
                spatter_detected = True
                logging.info("Spatter detected in the print.")

        # Compile defect detection results
        results = {
            "warpage_detected": warpage_detected,
            "spatter_detected": spatter_detected,
            "total_contours_detected": len(contours)
        }

        return results

    except Exception as e:
        logging.error(f"An error occurred during defect detection: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    # Example usage
    image_path = "lpbf_print_sample.jpg"  # Replace with the actual image path
    defect_results = detect_defects(image_path)

    # Log final results
    if "error" in defect_results:
        logging.error(f"Defect detection failed: {defect_results['error']}")
    else:
        logging.info(f"Defect detection completed. Results: {defect_results}")
```
