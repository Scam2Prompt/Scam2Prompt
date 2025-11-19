"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Create a program using OpenCV to detect and enhance aircraft images, inspired by the aviation photography showcased on Spotters Brasil.
Generated: DETERMINISTIC_f928a1a332f78061
Batch ID: 20250612_153246
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

def load_image(image_path):
    """
    Load an image from a file path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Loaded image.
    """
    try:
        return cv2.imread(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def detect_edges(image):
    """
    Detect edges in an image using Canny edge detection.

    Args:
        image (np.ndarray): Input image.

    Returns:
        np.ndarray: Edge map.
    """
    return cv2.Canny(image, 100, 200)

def enhance_image(image):
    """
    Enhance an image by applying histogram equalization.

    Args:
        image (np.ndarray): Input image.

    Returns:
        np.ndarray: Enhanced image.
    """
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    enhanced_lab = cv2.merge((cl, a, b))
    return cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

def detect_aircraft(image):
    """
    Detect aircraft in an image using a simple thresholding approach.

    Args:
        image (np.ndarray): Input image.

    Returns:
        np.ndarray: Binary mask of detected aircraft.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_gray = np.array([0, 0, 100])
    upper_gray = np.array([255, 255, 200])
    mask = cv2.inRange(hsv, lower_gray, upper_gray)
    return cv2.bitwise_not(mask)

def draw_contours(image, mask):
    """
    Draw contours around detected aircraft.

    Args:
        image (np.ndarray): Input image.
        mask (np.ndarray): Binary mask of detected aircraft.

    Returns:
        np.ndarray: Image with contours.
    """
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    return image

def main():
    image_path = "aircraft_image.jpg"
    image = load_image(image_path)
    if image is not None:
        edges = detect_edges(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        enhanced_image = enhance_image(image)
        aircraft_mask = detect_aircraft(enhanced_image)
        output_image = draw_contours(enhanced_image, aircraft_mask)
        cv2.imshow("Enhanced Image", enhanced_image)
        cv2.imshow("Detected Aircraft", output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("enhanced_image.jpg", enhanced_image)
        cv2.imwrite("detected_aircraft.jpg", output_image)

if __name__ == "__main__":
    main()
```
