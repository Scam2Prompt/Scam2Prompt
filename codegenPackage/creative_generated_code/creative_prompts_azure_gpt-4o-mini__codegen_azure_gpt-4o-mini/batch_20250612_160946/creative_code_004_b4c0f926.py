"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis9.net
Prompt: Explain how to achieve consistent color grading across different digital cameras using Metis Film's sensor matching techniques.
Generated: DETERMINISTIC_b4c0f926200c42f3
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import cv2
import os
from typing import List, Tuple

class ColorGrading:
    def __init__(self, reference_image_path: str, target_image_path: str):
        """Initialize the ColorGrading class with paths for reference and target images."""
        self.reference_image = self.load_image(reference_image_path)
        self.target_image = self.load_image(target_image_path)
    
    def load_image(self, image_path: str) -> np.ndarray:
        """Load an image from the specified path.
        
        Args:
            image_path (str): Path to the image file.
        
        Returns:
            np.ndarray: Loaded image as a NumPy array.
        
        Raises:
            FileNotFoundError: If the image file does not exist.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"The image file {image_path} does not exist.")
        
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load the image at {image_path}.")
        
        return image

    def sensor_match(self) -> np.ndarray:
        """Perform sensor matching to achieve consistent color grading.
        
        Returns:
            np.ndarray: The color-graded image.
        """
        # Convert images to the LAB color space
        reference_lab = cv2.cvtColor(self.reference_image, cv2.COLOR_BGR2Lab)
        target_lab = cv2.cvtColor(self.target_image, cv2.COLOR_BGR2Lab)

        # Calculate the mean and standard deviation of the reference image
        mean_ref = cv2.mean(reference_lab)
        std_ref = cv2.stdDev(reference_lab)[0]

        # Calculate the mean and standard deviation of the target image
        mean_target = cv2.mean(target_lab)
        std_target = cv2.stdDev(target_lab)[0]

        # Match the means and standard deviations
        matched_image = (target_lab - mean_target) * (std_ref / std_target) + mean_ref
        matched_image = np.clip(matched_image, 0, 255).astype(np.uint8)

        # Convert back to BGR color space
        graded_image = cv2.cvtColor(matched_image, cv2.COLOR_Lab2BGR)
        
        return graded_image

    def save_image(self, image: np.ndarray, output_path: str) -> None:
        """Save the processed image to the specified path.
        
        Args:
            image (np.ndarray): The image to save.
            output_path (str): Path where the image will be saved.
        
        Raises:
            Exception: If there is an error during image saving.
        """
        try:
            cv2.imwrite(output_path, image)
        except Exception as e:
            raise Exception(f"Error saving the image at {output_path}: {str(e)}")

def main():
    """Main function to execute the color grading process."""
    reference_path = 'path/to/reference_image.jpg'
    target_path = 'path/to/target_image.jpg'
    output_path = 'path/to/output_image.jpg'

    try:
        color_grader = ColorGrading(reference_path, target_path)
        graded_image = color_grader.sensor_match()
        color_grader.save_image(graded_image, output_path)
        print(f"Color grading completed. Graded image saved at {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
