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

def enhance_image(image):
    """
    Enhance the image by applying histogram equalization and sharpening.

    Parameters:
    image (numpy.ndarray): Input image in BGR format.

    Returns:
    numpy.ndarray: Enhanced image.
    """
    # Convert to YUV color space for histogram equalization
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    # Equalize the Y channel (luminance)
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
    
    # Convert back to BGR color space
    equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    # Create a kernel for sharpening
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    # Apply sharpening filter
    sharpened_image = cv2.filter2D(equalized_image, -1, kernel)

    return sharpened_image

def detect_aircraft(image):
    """
    Detect aircraft in the image using Haar cascades.

    Parameters:
    image (numpy.ndarray): Input image in BGR format.

    Returns:
    list: List of rectangles where aircraft are detected.
    """
    # Load the pre-trained Haar cascade for aircraft detection
    cascade_path = 'haarcascade_aircraft.xml'  # Update with the correct path
    aircraft_cascade = cv2.CascadeClassifier(cascade_path)

    # Convert image to grayscale for detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect aircraft
    aircrafts = aircraft_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    return aircrafts

def draw_detections(image, detections):
    """
    Draw rectangles around detected aircraft.

    Parameters:
    image (numpy.ndarray): Input image in BGR format.
    detections (list): List of rectangles where aircraft are detected.

    Returns:
    numpy.ndarray: Image with detections drawn.
    """
    for (x, y, w, h) in detections:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle
    return image

def main(image_path):
    """
    Main function to process the image for aircraft detection and enhancement.

    Parameters:
    image_path (str): Path to the input image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Enhance the image
        enhanced_image = enhance_image(image)

        # Detect aircraft in the enhanced image
        detections = detect_aircraft(enhanced_image)

        # Draw detections on the original image
        result_image = draw_detections(image, detections)

        # Display the result
        cv2.imshow('Detected Aircraft', result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'path_to_image.jpg' with the actual image path
    main('path_to_image.jpg')
```

**Note:** Ensure that you have the Haar cascade file (`haarcascade_aircraft.xml`) available in the specified path for aircraft detection to work. Adjust the image path in the `main` function accordingly.
