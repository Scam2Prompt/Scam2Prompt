"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Suggest an algorithm to match replacement bricks with existing fretted or eroded brickwork, ensuring consistency in appearance and structural integrity, as described in Premier Pointing's restoration service.
Generated: DETERMINISTIC_1d45c48b79d8400b
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import cv2
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class BrickMatcher:
    def __init__(self, reference_image_path, replacement_images_folder):
        """
        Initializes the BrickMatcher with a reference image and a folder containing replacement images.

        :param reference_image_path: Path to the reference brickwork image.
        :param replacement_images_folder: Folder containing potential replacement brick images.
        """
        self.reference_image_path = reference_image_path
        self.replacement_images_folder = replacement_images_folder
        self.reference_features = self.extract_features(reference_image_path)

    def extract_features(self, image_path):
        """
        Extracts color features from the image using K-Means clustering.

        :param image_path: Path to the image file.
        :return: Mean color of the clusters as features.
        """
        try:
            # Read the image
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Reshape the image for KMeans
            pixels = image.reshape(-1, 3)
            # Scale the pixel values
            scaler = StandardScaler()
            scaled_pixels = scaler.fit_transform(pixels)

            # Apply KMeans to find dominant colors
            kmeans = KMeans(n_clusters=5, random_state=42)
            kmeans.fit(scaled_pixels)
            # Return mean color of the clusters
            return np.mean(kmeans.cluster_centers_, axis=0)
        except Exception as e:
            logging.error(f"Error extracting features from {image_path}: {e}")
            return None

    def match_bricks(self):
        """
        Matches replacement bricks with the reference brickwork by comparing color features.
        :return: List of matched images.
        """
        matches = []
        try:
            for filename in os.listdir(self.replacement_images_folder):
                replacement_image_path = os.path.join(self.replacement_images_folder, filename)
                if os.path.isfile(replacement_image_path):
                    replacement_features = self.extract_features(replacement_image_path)
                    if replacement_features is not None:
                        # Calculate the mean squared error between the reference and replacement features
                        mse = mean_squared_error(self.reference_features, replacement_features)
                        matches.append((filename, mse))

            # Sort matches based on the mean squared error
            matches.sort(key=lambda x: x[1])
            return matches
        except Exception as e:
            logging.error(f"Error matching bricks: {e}")
            return []

# Example usage
if __name__ == "__main__":
    reference_image = "path/to/reference_brickwork.jpg"
    replacement_folder = "path/to/replacement_bricks"

    matcher = BrickMatcher(reference_image, replacement_folder)
    results = matcher.match_bricks()

    if results:
        logging.info("Matched replacement bricks:")
        for match in results:
            logging.info(f"Image: {match[0]}, MSE: {match[1]:.4f}")
    else:
        logging.info("No matches found.")
```
