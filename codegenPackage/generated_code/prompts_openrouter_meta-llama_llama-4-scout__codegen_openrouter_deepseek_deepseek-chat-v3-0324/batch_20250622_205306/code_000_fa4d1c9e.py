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
import os
import numpy as np
import cv2
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from glob import glob


class AnomalyDetector:
    """
    Anomaly detection in images using PCA and Isolation Forest.
    """
    
    def __init__(self, n_components=0.95, contamination=0.01):
        """
        Initialize the anomaly detector.
        
        Args:
            n_components (float): Variance ratio for PCA (0-1)
            contamination (float): Expected proportion of outliers
        """
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('pca', PCA(n_components=n_components)),
            ('clf', IsolationForest(
                contamination=contamination,
                random_state=42,
                n_jobs=-1
            ))
        ])
        self.is_trained = False
    
    def extract_features(self, image):
        """
        Extract features from an image using histogram of gradients (HOG).
        
        Args:
            image (np.array): Input image
            
        Returns:
            np.array: Feature vector
        """
        # Convert to grayscale if needed
        if len(image.shape) > 2:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
        # Resize to consistent size
        image = cv2.resize(image, (256, 256))
        
        # Compute HOG features
        hog = cv2.HOGDescriptor(
            _winSize=(256, 256),
            _blockSize=(64, 64),
            _blockStride=(32, 32),
            _cellSize=(32, 32),
            _nbins=9
        )
        features = hog.compute(image)
        
        return features.flatten()
    
    def fit(self, normal_images):
        """
        Train the anomaly detector on normal images.
        
        Args:
            normal_images (list): List of normal training images (np.arrays)
        """
        if not normal_images:
            raise ValueError("No training images provided")
            
        print("Extracting features from training images...")
        features = np.array([self.extract_features(img) for img in normal_images])
        
        print("Training anomaly detector...")
        self.pipeline.fit(features)
        self.is_trained = True
        print("Training completed.")
    
    def predict(self, image):
        """
        Predict if an image is anomalous.
        
        Args:
            image (np.array): Input image to evaluate
            
        Returns:
            tuple: (prediction, anomaly_score)
                   prediction: 1 for normal, -1 for anomaly
                   anomaly_score: confidence of prediction
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call fit() first.")
            
        features = self.extract_features(image)
        features = features.reshape(1, -1)
        
        pred = self.pipeline.predict(features)[0]
        score = self.pipeline.decision_function(features)[0]
        
        return pred, score
    
    def save_model(self, path):
        """
        Save the trained model to disk.
        
        Args:
            path (str): Path to save the model
        """
        import joblib
        joblib.dump(self.pipeline, path)
    
    def load_model(self, path):
        """
        Load a trained model from disk.
        
        Args:
            path (str): Path to saved model
        """
        import joblib
        self.pipeline = joblib.load(path)
        self.is_trained = True


def load_images_from_folder(folder_path, limit=None):
    """
    Load images from a folder.
    
    Args:
        folder_path (str): Path to folder containing images
        limit (int): Maximum number of images to load
        
    Returns:
        list: List of loaded images (np.arrays)
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder {folder_path} does not exist")
        
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob(os.path.join(folder_path, ext)))
    
    if limit:
        image_paths = image_paths[:limit]
    
    images = []
    for img_path in image_paths:
        try:
            img = cv2.imread(img_path)
            if img is not None:
                images.append(img)
        except Exception as e:
            print(f"Error loading image {img_path}: {str(e)}")
    
    return images


def main():
    # Example usage
    try:
        # Load normal training images
        print("Loading training images...")
        normal_images = load_images_from_folder("data/normal", limit=100)
        
        if not normal_images:
            raise ValueError("No training images found in 'data/normal'")
        
        # Initialize and train detector
        detector = AnomalyDetector()
        detector.fit(normal_images)
        
        # Save model
        detector.save_model("anomaly_detector_model.joblib")
        
        # Test on new images
        test_images = load_images_from_folder("data/test")
        for img in test_images:
            pred, score = detector.predict(img)
            status = "NORMAL" if pred == 1 else "ANOMALY"
            print(f"Image status: {status}, Score: {score:.4f}")
            
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
