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
import argparse
import os

def load_image(image_path):
    """
    Load an image from the given path.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        numpy.ndarray: Loaded image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image from {image_path}")
    
    return image

def enhance_contrast(image):
    """
    Enhance image contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization).
    
    Args:
        image (numpy.ndarray): Input image.
        
    Returns:
        numpy.ndarray: Contrast-enhanced image.
    """
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    
    enhanced_lab = cv2.merge((l, a, b))
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    return enhanced_image

def sharpen_image(image):
    """
    Sharpen the image using a kernel.
    
    Args:
        image (numpy.ndarray): Input image.
        
    Returns:
        numpy.ndarray: Sharpened image.
    """
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def detect_aircraft(image):
    """
    Detect aircraft in the image using a pre-trained cascade classifier.
    
    Args:
        image (numpy.ndarray): Input image.
        
    Returns:
        list: List of rectangles (x, y, w, h) where aircraft are detected.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    aircraft_cascade = cv2.CascadeClassifier(cascade_path)
    
    if aircraft_cascade.empty():
        raise RuntimeError("Failed to load cascade classifier.")
    
    aircrafts = aircraft_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    return aircrafts

def draw_detections(image, detections):
    """
    Draw rectangles around detected aircraft.
    
    Args:
        image (numpy.ndarray): Input image.
        detections (list): List of rectangles (x, y, w, h).
        
    Returns:
        numpy.ndarray: Image with detection rectangles.
    """
    for (x, y, w, h) in detections:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

def save_image(image, output_path):
    """
    Save the image to the specified path.
    
    Args:
        image (numpy.ndarray): Image to save.
        output_path (str): Path to save the image.
    """
    cv2.imwrite(output_path, image)

def main():
    parser = argparse.ArgumentParser(description='Aircraft Image Enhancement and Detection')
    parser.add_argument('input_image', help='Path to the input image')
    parser.add_argument('output_image', help='Path to save the enhanced image')
    args = parser.parse_args()
    
    try:
        # Load the image
        image = load_image(args.input_image)
        
        # Enhance contrast
        enhanced = enhance_contrast(image)
        
        # Sharpen the image
        sharpened = sharpen_image(enhanced)
        
        # Detect aircraft
        detections = detect_aircraft(sharpened)
        
        # Draw detections
        result = draw_detections(sharpened, detections)
        
        # Save the result
        save_image(result, args.output_image)
        
        print(f"Successfully processed image. Saved to {args.output_image}")
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()
```
