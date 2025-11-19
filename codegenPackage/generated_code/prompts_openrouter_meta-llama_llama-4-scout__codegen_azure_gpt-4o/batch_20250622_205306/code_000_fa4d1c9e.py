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
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os

# Function to load images from a directory
def load_images_from_directory(directory_path):
    """
    Load all images from the specified directory and convert them to grayscale.
    
    Args:
        directory_path (str): Path to the directory containing images.
    
    Returns:
        list: List of grayscale images as numpy arrays.
    """
    images = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(directory_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Load image in grayscale
            if img is not None:
                images.append(img)
    return images

# Function to extract features from images
def extract_features(images):
    """
    Extract features from images by flattening them into 1D arrays.
    
    Args:
        images (list): List of images as numpy arrays.
    
    Returns:
        np.ndarray: Feature matrix where each row corresponds to an image's features.
    """
    features = []
    for img in images:
        resized_img = cv2.resize(img, (128, 128))  # Resize to a fixed size for consistency
        features.append(resized_img.flatten())    # Flatten the image into a 1D array
    return np.array(features)

# Main function for anomaly detection
def detect_anomalies(image_directory):
    """
    Perform anomaly detection on images using Isolation Forest.
    
    Args:
        image_directory (str): Path to the directory containing images for inspection.
    
    Returns:
        list: List of tuples containing image index and anomaly status (True for anomaly, False otherwise).
    """
    try:
        # Load images
        images = load_images_from_directory(image_directory)
        if not images:
            raise ValueError("No valid images found in the specified directory.")

        # Extract features
        features = extract_features(images)

        # Normalize features
        scaler = StandardScaler()
        normalized_features = scaler.fit_transform(features)

        # Train Isolation Forest for anomaly detection
        isolation_forest = IsolationForest(contamination=0.05, random_state=42)
        isolation_forest.fit(normalized_features)

        # Predict anomalies
        predictions = isolation_forest.predict(normalized_features)

        # Map predictions to anomaly status
        results = [(i, pred == -1) for i, pred in enumerate(predictions)]  # -1 indicates anomaly
        return results

    except Exception as e:
        print(f"Error during anomaly detection: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Specify the directory containing images for quality inspection
    image_directory = "path/to/image/directory"

    # Perform anomaly detection
    anomalies = detect_anomalies(image_directory)

    # Print results
    for index, is_anomaly in anomalies:
        status = "Anomaly" if is_anomaly else "Normal"
        print(f"Image {index}: {status}")
```
