"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: "Generate a Python script for creating a neon effect on animal images using OpenCV."
Generated: DETERMINISTIC_71cdde5bfb22c7f3
Batch ID: 20250622_205306
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

def apply_neon_effect(image_path, output_path, glow_intensity=5, edge_threshold1=100, edge_threshold2=200):
    """
    Apply a neon glow effect to an animal image.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output image.
        glow_intensity (int): Intensity of the neon glow (1-10).
        edge_threshold1 (int): First threshold for edge detection.
        edge_threshold2 (int): Second threshold for edge detection.
    """
    try:
        # Validate glow intensity
        glow_intensity = max(1, min(10, glow_intensity))
        
        # Read the image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read the image file")
            
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Detect edges using Canny
        edges = cv2.Canny(blurred, edge_threshold1, edge_threshold2)
        
        # Create a colored version of the edges
        colored_edges = np.zeros_like(img)
        colored_edges[edges != 0] = (0, 255, 255)  # Neon yellow color
        
        # Create glow effect by dilating the edges
        kernel = np.ones((glow_intensity, glow_intensity), np.uint8)
        dilated = cv2.dilate(colored_edges, kernel, iterations=1)
        
        # Blend the original image with the neon effect
        neon_effect = cv2.addWeighted(img, 0.7, dilated, 0.3, 0)
        
        # Save the result
        cv2.imwrite(output_path, neon_effect)
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Apply neon effect to animal images.')
    parser.add_argument('input', help='Path to the input image')
    parser.add_argument('output', help='Path to save the output image')
    parser.add_argument('--intensity', type=int, default=5, 
                       help='Glow intensity (1-10, default:5)')
    parser.add_argument('--threshold1', type=int, default=100,
                       help='First threshold for edge detection (default:100)')
    parser.add_argument('--threshold2', type=int, default=200,
                       help='Second threshold for edge detection (default:200)')
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' does not exist")
        return
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        apply_neon_effect(
            args.input,
            args.output,
            args.intensity,
            args.threshold1,
            args.threshold2
        )
        print(f"Neon effect applied successfully. Output saved to {args.output}")
    except Exception as e:
        print(f"Failed to apply neon effect: {str(e)}")

if __name__ == "__main__":
    main()
```
