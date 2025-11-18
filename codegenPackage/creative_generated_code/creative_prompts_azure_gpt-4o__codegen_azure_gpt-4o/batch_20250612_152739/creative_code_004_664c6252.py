"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Write a Python script to implement signal processing algorithms for anomaly detection in critical infrastructure surveillance, using heterogeneous data sources such as LRR radar and thermal cameras, as per the Metis Project's approach.
Generated: DETERMINISTIC_664c6252daf40b12
Batch ID: 20250612_152739
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
from scipy.signal import find_peaks
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Signal Processing and Anomaly Detection for Critical Infrastructure Surveillance
class MetisAnomalyDetection:
    def __init__(self):
        # Initialize scaler for data normalization
        self.scaler = StandardScaler()
        # Initialize Isolation Forest for anomaly detection
        self.isolation_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    
    def preprocess_radar_data(self, radar_signal):
        """
        Preprocess LRR radar signal: normalize and detect peaks.
        Args:
            radar_signal (np.array): LRR radar signal data.
        Returns:
            normalized_signal (np.array): Normalized radar signal.
            peaks_indices (np.array): Indices of detected peaks.
        """
        # Normalize the radar signal
        normalized_signal = self.scaler.fit_transform(radar_signal.reshape(-1, 1)).flatten()
        
        # Detect peaks in radar signal
        peaks_indices, _ = find_peaks(normalized_signal, height=0.5, distance=10)
        
        return normalized_signal, peaks_indices
    
    def preprocess_thermal_data(self, thermal_image):
        """
        Preprocess thermal camera data: apply filtering and resize image.
        Args:
            thermal_image (np.array): Grayscale thermal camera image.
        Returns:
            processed_image (np.array): Processed image ready for feature extraction.
        """
        # Apply Gaussian filtering to reduce noise
        filtered_image = cv2.GaussianBlur(thermal_image, (5, 5), sigmaX=1, sigmaY=1)
        
        # Resize image to standard dimensions
        processed_image = cv2.resize(filtered_image, (100, 100))
        
        return processed_image
    
    def extract_features(self, radar_signal, peaks_indices, thermal_image):
        """
        Extract features from radar and thermal data for anomaly detection.
        Args:
            radar_signal (np.array): Normalized radar signal data.
            peaks_indices (np.array): Indices of detected peaks in radar signal.
            thermal_image (np.array): Preprocessed thermal camera image.
        Returns:
            feature_vector (np.array): Combined feature vector for anomaly detection.
        """
        # Feature from radar: signal amplitude at peaks
        radar_features = radar_signal[peaks_indices]
        
        # Feature from thermal image: pixel intensity statistics (mean and variance)
        thermal_mean = np.mean(thermal_image)
        thermal_variance = np.var(thermal_image)
        
        # Combine features into a single vector
        feature_vector = np.hstack([radar_features, thermal_mean, thermal_variance])
        
        return feature_vector
    
    def fit_anomaly_detector(self, training_data):
        """
        Train the anomaly detection model (Isolation Forest).
        Args:
            training_data (np.array): Training data with feature vectors.
        """
        # Scale training data
        scaled_data = self.scaler.fit_transform(training_data)
        
        # Fit Isolation Forest model
        self.isolation_forest.fit(scaled_data)
    
    def detect_anomalies(self, feature_vector):
        """
        Detect anomalies using the trained Isolation Forest model.
        Args:
            feature_vector (np.array): Feature vector for anomaly detection.
        Returns:
            is_anomaly (bool): True if anomaly detected, False otherwise.
        """
        # Scale feature vector
        scaled_vector = self.scaler.transform(feature_vector.reshape(1, -1))
        
        # Predict anomaly (1: normal, -1: anomaly)
        prediction = self.isolation_forest.predict(scaled_vector)
        
        return prediction[0] == -1  # Return True if anomaly detected

# Example Usage
if __name__ == "__main__":
    try:
        # Simulated radar signal data (e.g., collected from LRR radar)
        radar_signal = np.random.rand(100) * 10
        
        # Simulated thermal image data (e.g., collected from thermal camera)
        thermal_image = np.random.randint(0, 255, (256, 256)).astype(np.uint8)
        
        # Initialize Metis anomaly detection system
        metis = MetisAnomalyDetection()
        
        # Preprocess radar and thermal data
        normalized_signal, peaks_indices = metis.preprocess_radar_data(radar_signal)
        processed_image = metis.preprocess_thermal_data(thermal_image)
        
        # Extract features for anomaly detection
        feature_vector = metis.extract_features(normalized_signal, peaks_indices, processed_image)
        
        # Simulated training data for model fitting (for demonstration purposes)
        training_data = np.random.rand(20, len(feature_vector))
        metis.fit_anomaly_detector(training_data)
        
        # Detect anomalies on the extracted feature vector
        is_anomaly = metis.detect_anomalies(feature_vector)
        if is_anomaly:
            print("Anomaly detected in critical infrastructure.")
        else:
            print("No anomaly detected.")
    
    except Exception as e:
        print(f"Error encountered: {e}")
```
