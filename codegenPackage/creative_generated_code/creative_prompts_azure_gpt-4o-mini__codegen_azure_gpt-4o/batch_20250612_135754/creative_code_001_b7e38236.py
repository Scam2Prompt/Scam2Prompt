"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Write a tutorial on how to implement a photo editing functionality similar to the Blur App, including features like eraser and size changer.
Generated: DETERMINISTIC_b7e382369926583d
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Photo Editing Application with Blur, Eraser, and Size Changer Functionality

This script demonstrates how to implement basic photo editing features using Python and OpenCV.
Features:
1. Blur Tool
2. Eraser Tool
3. Size Changer for the editing brush
"""

import cv2
import numpy as np

# Constants
WINDOW_NAME = "Photo Editor"
DEFAULT_BRUSH_SIZE = 15
MAX_BRUSH_SIZE = 50

# Global variables to track state
brush_size = DEFAULT_BRUSH_SIZE
editing_mode = "blur"  # Modes: "blur", "erase"
drawing = False
last_point = None

def apply_blur(image, point, brush_size):
    """
    Apply blur effect at a specific point on the image.
    """
    x, y = point
    # Define the region of interest (ROI) for blurring
    x1, y1 = max(0, x - brush_size), max(0, y - brush_size)
    x2, y2 = min(image.shape[1], x + brush_size), min(image.shape[0], y + brush_size)

    # Apply Gaussian blur on the ROI
    roi = image[y1:y2, x1:x2]
    blurred_roi = cv2.GaussianBlur(roi, (15, 15), 0)
    image[y1:y2, x1:x2] = blurred_roi

def apply_eraser(image, point, brush_size, original_image):
    """
    Erase edits by restoring the original image at a specific point.
    """
    x, y = point
    # Define the region of interest (ROI) for erasing
    x1, y1 = max(0, x - brush_size), max(0, y - brush_size)
    x2, y2 = min(image.shape[1], x + brush_size), min(image.shape[0], y + brush_size)

    # Restore the original image in the ROI
    image[y1:y2, x1:x2] = original_image[y1:y2, x1:x2]

def draw(event, x, y, flags, param):
    """
    Mouse callback function to handle user input for editing the image.
    """
    global drawing, last_point, brush_size, editing_mode

    if event == cv2.EVENT_LBUTTONDOWN:  # Start drawing
        drawing = True
        last_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:  # Draw as the mouse moves
        if editing_mode == "blur":
            apply_blur(param['image'], (x, y), brush_size)
        elif editing_mode == "erase":
            apply_eraser(param['image'], (x, y), brush_size, param['original_image'])
        last_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:  # Stop drawing
        drawing = False

def update_brush_size(key):
    """
    Update the brush size based on user input.
    """
    global brush_size
    if key == ord('+') and brush_size < MAX_BRUSH_SIZE:
        brush_size += 1
    elif key == ord('-') and brush_size > 1:
        brush_size -= 1

def main():
    """
    Main function to run the photo editing application.
    """
    global editing_mode

    # Load the image
    image = cv2.imread("example.jpg")
    if image is None:
        print("Error: Unable to load image.")
        return

    # Create a copy of the original image for eraser functionality
    original_image = image.copy()

    # Create a window and set mouse callback
    cv2.namedWindow(WINDOW_NAME)
    cv2.setMouseCallback(WINDOW_NAME, draw, param={'image': image, 'original_image': original_image})

    print("Instructions:")
    print("Press 'b' to switch to Blur mode.")
    print("Press 'e' to switch to Eraser mode.")
    print("Press '+' to increase brush size.")
    print("Press '-' to decrease brush size.")
    print("Press 'q' to quit.")

    while True:
        # Display the image
        cv2.imshow(WINDOW_NAME, image)

        # Wait for user input
        key = cv2.waitKey(1) & 0xFF

        # Handle mode switching
        if key == ord('b'):
            editing_mode = "blur"
            print("Switched to Blur mode.")
        elif key == ord('e'):
            editing_mode = "erase"
            print("Switched to Eraser mode.")

        # Handle brush size adjustment
        update_brush_size(key)

        # Exit the application
        if key == ord('q'):
            break

    # Clean up
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
