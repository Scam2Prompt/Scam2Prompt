"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Recommend a Python library for analyzing image composition and angles in real estate photography, with use cases similar to those described by Perth Real Estate Photography.
Generated: DETERMINISTIC_5c3411ffa07a997d
Batch ID: 20250612_152620
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
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class ImageAnalyzer:
    """
    A class to analyze image composition and angles for real estate photography.
    """

    def __init__(self, image_path):
        """
        Initializes the ImageAnalyzer with the path to the image.
        
        :param image_path: str - The file path to the image to be analyzed.
        """
        self.image_path = image_path
        self.image = self.load_image()

    def load_image(self):
        """
        Loads an image from the specified path.

        :return: np.ndarray - The loaded image.
        :raises FileNotFoundError: If the image file does not exist.
        """
        image = cv2.imread(self.image_path)
        if image is None:
            raise FileNotFoundError(f"Image file {self.image_path} not found.")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def calculate_angle(self):
        """
        Calculates the dominant angle of the image using edge detection.

        :return: float - The dominant angle in degrees.
        """
        edges = cv2.Canny(self.image, 100, 200)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

        angle_sum = 0
        count = 0

        if lines is not None:
            for rho, theta in lines[:, 0]:
                angle = (theta * 180) / np.pi
                angle_sum += angle
                count += 1

        return angle_sum / count if count > 0 else 0

    def analyze_composition(self, n_colors=3):
        """
        Analyzes the image composition by clustering colors.

        :param n_colors: int - The number of dominant colors to find.
        :return: list - List of dominant colors in RGB format.
        """
        pixels = self.image.reshape(-1, 3)
        kmeans = KMeans(n_clusters=n_colors)
        kmeans.fit(pixels)

        return kmeans.cluster_centers_.astype(int).tolist()

    def show_results(self):
        """
        Displays the image with the dominant angle and colors.
        """
        angle = self.calculate_angle()
        colors = self.analyze_composition()

        # Displaying results
        plt.imshow(self.image)
        plt.title(f'Dominant Angle: {angle:.2f}°\nDominant Colors: {colors}')
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    # Example usage of the ImageAnalyzer
    try:
        analyzer = ImageAnalyzer('path/to/real_estate_image.jpg')
        analyzer.show_results()
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
Make sure to replace `'path/to/real_estate_image.jpg'` with the actual path to your image file when using this script.
