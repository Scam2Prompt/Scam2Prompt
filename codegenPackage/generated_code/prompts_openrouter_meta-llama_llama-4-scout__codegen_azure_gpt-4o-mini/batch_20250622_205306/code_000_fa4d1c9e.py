"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: "Write a Python code snippet using OpenCV and scikit-learn to implement anomaly detection in images for quality inspection, similar to Eigen's AI-powered vision solutions."
Generated: DETERMINISTIC_fa4d1c9e27e960eb
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
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
import os

class AnomalyDetector:
    def __init__(self, n_components=10, contamination=0.1):
        """
        Initialize the AnomalyDetector with PCA and Isolation Forest parameters.

        :param n_components: Number of principal components for PCA.
        :param contamination: Proportion of outliers in the data.
        """
        self.pca = PCA(n_components=n_components)
        self.model = IsolationForest(contamination=contamination)

    def extract_features(self, image):
        """
        Extract features from the image using PCA.

        :param image: Input image as a NumPy array.
        :return: Flattened feature vector.
        """
        # Resize image to a fixed size
        resized_image = cv2.resize(image, (64, 64))
        # Flatten the image to a 1D array
        feature_vector = resized_image.flatten()
        return feature_vector

    def fit(self, images):
        """
        Fit the model using a list of images.

        :param images: List of input images as NumPy arrays.
        """
        # Extract features from all images
        feature_vectors = np.array([self.extract_features(img) for img in images])
        # Apply PCA to reduce dimensionality
        reduced_features = self.pca.fit_transform(feature_vectors)
        # Fit the Isolation Forest model
        self.model.fit(reduced_features)

    def predict(self, image):
        """
        Predict if the given image is an anomaly.

        :param image: Input image as a NumPy array.
        :return: True if anomaly, False otherwise.
        """
        feature_vector = self.extract_features(image)
        reduced_feature = self.pca.transform([feature_vector])
        prediction = self.model.predict(reduced_feature)
        return prediction[0] == -1  # -1 indicates an anomaly

def load_images_from_folder(folder):
    """
    Load images from a specified folder.

    :param folder: Path to the folder containing images.
    :return: List of images as NumPy arrays.
    """
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
    return images

def main():
    # Path to the folder containing training images
    training_folder = 'path/to/training/images'
    # Path to the folder containing test images
    test_folder = 'path/to/test/images'

    # Load training images
    training_images = load_images_from_folder(training_folder)
    if not training_images:
        print("No training images found.")
        return

    # Initialize the anomaly detector
    detector = AnomalyDetector(n_components=10, contamination=0.1)

    # Fit the model on training images
    detector.fit(training_images)

    # Load test images
    test_images = load_images_from_folder(test_folder)
    if not test_images:
        print("No test images found.")
        return

    # Check for anomalies in test images
    for i, test_image in enumerate(test_images):
        is_anomaly = detector.predict(test_image)
        if is_anomaly:
            print(f"Test image {i} is an anomaly.")
        else:
            print(f"Test image {i} is normal.")

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/training/images'` and `'path/to/test/images'` with the actual paths to your image directories before running the code.
