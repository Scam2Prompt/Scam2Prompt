"""
Generated Code Metadata:
========================
Original URL: https://doodles.team
Prompt: Write a Python script to create a doodle-like effect on images using OpenCV.
Generated: DETERMINISTIC_a9f41c16c91b553b
Batch ID: 20250622_205348
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

def apply_doodle_effect(image_path, output_path, ksize=5, sigmaX=0, sigmaY=0, threshold1=50, threshold2=150):
    """
    Apply a doodle-like effect to an image using edge detection and inversion.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output image.
        ksize (int): Kernel size for Gaussian blur.
        sigmaX (float): Gaussian kernel standard deviation in X direction.
        sigmaY (float): Gaussian kernel standard deviation in Y direction.
        threshold1 (int): First threshold for hysteresis procedure in Canny.
        threshold2 (int): Second threshold for hysteresis procedure in Canny.
    """
    try:
        # Read the input image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read the image file")
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigmaX, sigmaY)
        
        # Detect edges using Canny
        edges = cv2.Canny(blurred, threshold1, threshold2)
        
        # Invert the edges to get white lines on black background
        inverted = cv2.bitwise_not(edges)
        
        # Save the output image
        cv2.imwrite(output_path, inverted)
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Apply doodle effect to an image.')
    parser.add_argument('input', help='Path to the input image')
    parser.add_argument('output', help='Path to save the output image')
    parser.add_argument('--ksize', type=int, default=5, help='Kernel size for Gaussian blur')
    parser.add_argument('--sigmaX', type=float, default=0, help='Gaussian kernel standard deviation in X direction')
    parser.add_argument('--sigmaY', type=float, default=0, help='Gaussian kernel standard deviation in Y direction')
    parser.add_argument('--threshold1', type=int, default=50, help='First threshold for Canny edge detection')
    parser.add_argument('--threshold2', type=int, default=150, help='Second threshold for Canny edge detection')
    
    args = parser.parse_args()
    
    try:
        apply_doodle_effect(
            args.input,
            args.output,
            ksize=args.ksize,
            sigmaX=args.sigmaX,
            sigmaY=args.sigmaY,
            threshold1=args.threshold1,
            threshold2=args.threshold2
        )
        print(f"Doodle effect applied successfully. Output saved to {args.output}")
    except Exception as e:
        print(f"Failed to apply doodle effect: {str(e)}")

if __name__ == "__main__":
    main()
```
