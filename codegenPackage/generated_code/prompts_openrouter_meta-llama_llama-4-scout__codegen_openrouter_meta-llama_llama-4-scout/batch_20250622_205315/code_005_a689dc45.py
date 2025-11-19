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
from typing import List, Tuple

def load_image(image_path: str) -> np.ndarray:
    """
    Loads an image from a file path.

    Args:
    image_path (str): The path to the image file.

    Returns:
    np.ndarray: The loaded image.
    """
    try:
        return cv2.imread(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def preprocess_image(image: np.ndarray) -> np.ndarray:
    """
    Preprocesses the image by converting it to grayscale and applying a Gaussian blur.

    Args:
    image (np.ndarray): The input image.

    Returns:
    np.ndarray: The preprocessed image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

def detect_defects(image: np.ndarray, threshold: int = 127) -> List[np.ndarray]:
    """
    Detects defects in the image using thresholding.

    Args:
    image (np.ndarray): The preprocessed image.
    threshold (int): The threshold value for defect detection. Defaults to 127.

    Returns:
    List[np.ndarray]: A list of contours representing the detected defects.
    """
    _, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def annotate_defects(image: np.ndarray, defects: List[np.ndarray]) -> np.ndarray:
    """
    Annotates the defects on the original image.

    Args:
    image (np.ndarray): The original image.
    defects (List[np.ndarray]): A list of contours representing the detected defects.

    Returns:
    np.ndarray: The annotated image.
    """
    annotated_image = image.copy()
    for defect in defects:
        cv2.drawContours(annotated_image, [defect], -1, (0, 255, 0), 2)
    return annotated_image

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Saves an image to a file path.

    Args:
    image (np.ndarray): The image to save.
    output_path (str): The path to save the image.
    """
    try:
        cv2.imwrite(output_path, image)
    except Exception as e:
        print(f"Error saving image: {e}")

def main() -> None:
    image_path = "input_image.jpg"
    output_path = "output_image.jpg"

    image = load_image(image_path)
    if image is None:
        return

    preprocessed_image = preprocess_image(image)
    defects = detect_defects(preprocessed_image)
    annotated_image = annotate_defects(image, defects)

    save_image(annotated_image, output_path)

if __name__ == "__main__":
    main()
```
