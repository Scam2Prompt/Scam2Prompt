"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Create a program using OpenCV to detect and enhance aircraft images, inspired by the aviation photography showcased on Spotters Brasil.
Generated: DETERMINISTIC_f928a1a332f78061
Batch ID: 20250612_153246
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
import os


def detect_and_enhance_aircraft(image_path, output_path):
    """
    Detects aircraft in an image and enhances the image by applying 
    sharpening and brightness adjustment.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the enhanced image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Convert image to grayscale for processing
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Load pre-trained Haar Cascade classifier for aircraft detection
        # Assuming 'aircraft_cascade.xml' is available in the current directory
        cascade_path = 'aircraft_cascade.xml'
        if not os.path.exists(cascade_path):
            raise FileNotFoundError(f"Haar Cascade file not found at path: {cascade_path}")
        aircraft_cascade = cv2.CascadeClassifier(cascade_path)

        # Detect aircraft in the image
        aircrafts = aircraft_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Draw rectangles around detected aircrafts
        for (x, y, w, h) in aircrafts:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Enhance the image
        # 1. Sharpening the image
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # Sharpening kernel
        sharpened = cv2.filter2D(image, -1, kernel)

        # 2. Adjust brightness and contrast
        alpha = 1.2  # Contrast control (1.0-3.0)
        beta = 30    # Brightness control (0-100)
        enhanced = cv2.convertScaleAbs(sharpened, alpha=alpha, beta=beta)

        # Save the enhanced image
        cv2.imwrite(output_path, enhanced)
        print(f"Enhanced image saved at: {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Paths for input and output images
    input_image_path = 'aircraft.jpg'  # Replace with the path to your input image
    output_image_path = 'enhanced_aircraft.jpg'

    # Run the detection and enhancement function
    detect_and_enhance_aircraft(input_image_path, output_image_path)
```

**Note:**
Make sure to have the `aircraft_cascade.xml` file (trained Haar Cascade for aircraft detection) in the same directory as the script or provide its path in the `cascade_path` variable. You can use OpenCV's `haartraining` or `traincascade` utilities to train a custom Haar Cascade for aircraft detection, as OpenCV does not provide one by default.
