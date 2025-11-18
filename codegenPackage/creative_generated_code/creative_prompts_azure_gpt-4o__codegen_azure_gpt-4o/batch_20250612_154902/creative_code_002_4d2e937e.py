"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Generate code to simulate the blurring effect in a digital artwork using Python and a library like OpenCV. The code should allow users to adjust the intensity of the blur interactively.
Generated: DETERMINISTIC_4d2e937e540a6584
Batch ID: 20250612_154902
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

def interactive_blur(image_path):
    """
    Function to interactively apply a blurring effect to an image using OpenCV.
    Users can adjust the blur intensity via a trackbar.
    
    Parameters:
        image_path (str): Path to the input image file.
    """
    # Load the input image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at the specified path: {image_path}")
    
    # Function to update blur intensity based on trackbar position
    def update_blur(val):
        """
        Callback function for the trackbar to apply blur based on the intensity value.
        
        Parameters:
            val (int): Current trackbar position (blur intensity).
        """
        # Ensure kernel size is odd and greater than or equal to 1
        intensity = max(1, val)
        intensity = intensity if intensity % 2 == 1 else intensity + 1
        
        # Apply Gaussian blur to the image
        blurred_image = cv2.GaussianBlur(image, (intensity, intensity), 0)
        
        # Display the blurred image in the window
        cv2.imshow(window_name, blurred_image)

    # Window name for display
    window_name = "Interactive Blur Effect"
    cv2.namedWindow(window_name)

    # Trackbar name and initialization
    trackbar_name = "Blur Intensity"
    cv2.createTrackbar(trackbar_name, window_name, 1, 50, update_blur)

    # Display the original image initially
    cv2.imshow(window_name, image)

    # Wait until the user presses the 'Esc' key to exit
    print("Press 'Esc' to exit.")
    while True:
        key = cv2.waitKey(1)
        if key == 27:  # Esc key
            break

    # Clean up
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Replace 'example.jpg' with the path to your image file
    image_file_path = 'example.jpg'
    try:
        interactive_blur(image_file_path)
    except Exception as e:
        print(f"Error: {e}")
```
