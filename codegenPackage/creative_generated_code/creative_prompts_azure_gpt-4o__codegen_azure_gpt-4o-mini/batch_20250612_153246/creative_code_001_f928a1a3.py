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

def enhance_aircraft_image(image_path, output_path):
    """
    Enhances an aircraft image by applying several image processing techniques.

    Parameters:
    - image_path: str, path to the input image file.
    - output_path: str, path to save the enhanced image file.

    Raises:
    - FileNotFoundError: If the input image path is not found.
    - Exception: For any other unexpected errors during processing.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Convert to grayscale for better processing
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian Blur to reduce noise and smooth the image
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Use Canny Edge Detection to find edges in the image
        edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

        # Create a mask from the edges
        mask = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Convert the original image to a higher contrast using Histogram Equalization
        hist_equalized_image = cv2.equalizeHist(gray_image)

        # Merge the mask with the original image to enhance edges
        enhanced_image = cv2.addWeighted(image, 0.7, mask, 0.3, 0)

        # Convert the histogram equalized image back to BGR
        hist_equalized_bgr = cv2.cvtColor(hist_equalized_image, cv2.COLOR_GRAY2BGR)

        # Combine the enhanced image with the histogram equalized image
        final_output = cv2.addWeighted(enhanced_image, 0.5, hist_equalized_bgr, 0.5, 0)

        # Save the enhanced image to the specified output path
        cv2.imwrite(output_path, final_output)

        print(f"Enhanced image saved to: {output_path}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "path/to/your/aircraft_image.jpg"
    output_image_path = "path/to/save/enhanced_aircraft_image.jpg"
    
    enhance_aircraft_image(input_image_path, output_image_path)
```
