"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Write Python code to simulate the detection of water leaks using thermal imaging techniques, as described on the "شمس المملكة" website. Include methods for analyzing temperature variations in walls and floors.
Generated: DETERMINISTIC_de8c475e45cb417c
Batch ID: 20250612_153224
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
import matplotlib.pyplot as plt

class ThermalLeakDetector:
    def __init__(self, image_path):
        """
        Initializes the ThermalLeakDetector with the path to a thermal image.
        
        Args:
            image_path (str): Path to the thermal image file.
        """
        self.image_path = image_path
        self.image = self.load_image()

    def load_image(self):
        """
        Loads the thermal image from the specified path.
        
        Returns:
            np.ndarray: The loaded image in BGR format.
        """
        try:
            image = cv2.imread(self.image_path)
            if image is None:
                raise FileNotFoundError(f"Image not found at {self.image_path}")
            return image
        except Exception as e:
            print(f"Error loading image: {e}")
            raise

    def convert_to_grayscale(self):
        """
        Converts the loaded thermal image to grayscale for easier analysis.
        
        Returns:
            np.ndarray: Grayscale image.
        """
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def analyze_temperature_variations(self, threshold=5):
        """
        Analyzes temperature variations in the thermal image to detect potential leaks.
        
        Args:
            threshold (float): Temperature variation threshold for leak detection.

        Returns:
            np.ndarray: Binary image showing areas with potential leaks.
        """
        grayscale_image = self.convert_to_grayscale()
        # Calculate the mean temperature
        mean_temp = np.mean(grayscale_image)
        print(f"Mean temperature: {mean_temp}")

        # Create a binary image where variations exceed the threshold
        leak_mask = np.abs(grayscale_image - mean_temp) > threshold
        return leak_mask.astype(np.uint8) * 255  # Convert boolean mask to binary image

    def display_results(self, leak_mask):
        """
        Displays the original image and the leak detection results.
        
        Args:
            leak_mask (np.ndarray): Binary mask of detected leaks.
        """
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.title("Original Thermal Image")
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.title("Leak Detection Mask")
        plt.imshow(leak_mask, cmap='gray')
        plt.axis('off')

        plt.show()

    def run_detection(self):
        """
        Executes the leak detection process and displays the results.
        """
        try:
            leak_mask = self.analyze_temperature_variations()
            self.display_results(leak_mask)
        except Exception as e:
            print(f"Error during leak detection: {e}")

if __name__ == "__main__":
    # Example usage: replace 'path_to_thermal_image.jpg' with the actual image path
    detector = ThermalLeakDetector('path_to_thermal_image.jpg')
    detector.run_detection()
```
