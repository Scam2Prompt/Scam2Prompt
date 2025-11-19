"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: "Write a Python code snippet for anomaly detection in surveillance data using multimodal machine learning and signal processing techniques, specifically incorporating data from optical cameras, thermal cameras, and radar systems."
Generated: DETERMINISTIC_733e938eaee8f656
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy import signal
from scipy.stats import zscore
import pywt
import warnings
warnings.filterwarnings('ignore')

class MultimodalAnomalyDetector:
    """
    Anomaly detection system for multimodal surveillance data (optical, thermal, radar).
    Combines signal processing and machine learning techniques for robust detection.
    """
    
    def __init__(self, contamination=0.01, n_estimators=100):
        """
        Initialize the detector with Isolation Forest parameters.
        
        Args:
            contamination (float): Expected proportion of anomalies in the data
            n_estimators (int): Number of trees in the Isolation Forest
        """
        self.contamination = contamination
        self.n_estimators = n_estimators
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=0.95)
        self.detector = IsolationForest(
            n_estimators=n_estimators,
            contamination=contamination,
            random_state=42
        )
    
    def _process_optical_data(self, optical_data):
        """Process optical camera data with edge detection and feature extraction."""
        # Edge detection using Sobel filter
        edges = np.array([signal.sobel(frame) for frame in optical_data])
        # Wavelet transform for feature extraction
        coeffs = [pywt.wavedec2(frame, 'db1', level=2) for frame in optical_data]
        features = [np.concatenate([c.flatten() for c in coeff]) for coeff in coeffs]
        return np.array(features)
    
    def _process_thermal_data(self, thermal_data):
        """Process thermal camera data with temperature analysis."""
        # Temperature threshold features
        threshold_features = np.array([
            np.mean(frame > np.percentile(frame, 90)) for frame in thermal_data
        ]).reshape(-1, 1)
        # Statistical features
        stat_features = np.array([
            [np.mean(frame), np.std(frame), np.max(frame), np.min(frame)]
            for frame in thermal_data
        ])
        return np.concatenate([threshold_features, stat_features], axis=1)
    
    def _process_radar_data(self, radar_data):
        """Process radar data with Doppler analysis and signal processing."""
        # Doppler shift analysis
        f, t, Sxx = signal.spectrogram(radar_data, fs=1e3, nperseg=256)
        spectral_features = np.array([
            np.mean(Sxx, axis=1),
            np.std(Sxx, axis=1),
            np.max(Sxx, axis=1)
        ]).T.flatten()
        
        # Time-domain features
        time_features = [
            np.mean(radar_data),
            np.std(radar_data),
            zscore(radar_data).max()
        ]
        
        return np.concatenate([spectral_features, time_features])
    
    def preprocess_data(self, optical_data, thermal_data, radar_data):
        """
        Preprocess and fuse multimodal data into a feature matrix.
        
        Args:
            optical_data: Array of optical camera frames
            thermal_data: Array of thermal camera frames
            radar_data: Array of radar signal readings
            
        Returns:
            np.array: Combined feature matrix
        """
        # Process each modality
        optical_features = self._process_optical_data(optical_data)
        thermal_features = self._process_thermal_data(thermal_data)
        radar_features = self._process_radar_data(radar_data)
        
        # Combine features
        combined_features = np.concatenate([
            optical_features,
            thermal_features,
            np.tile(radar_features, (len(optical_data), 1))
        ], axis=1)
        
        # Normalize and reduce dimensionality
        scaled_features = self.scaler.fit_transform(combined_features)
        reduced_features = self.pca.fit_transform(scaled_features)
        
        return reduced_features
    
    def fit(self, optical_data, thermal_data, radar_data):
        """
        Train the anomaly detector on normal data.
        
        Args:
            optical_data: Array of normal optical camera frames
            thermal_data: Array of normal thermal camera frames
            radar_data: Array of normal radar signal readings
        """
        features = self.preprocess_data(optical_data, thermal_data, radar_data)
        self.detector.fit(features)
    
    def detect(self, optical_data, thermal_data, radar_data):
        """
        Detect anomalies in new multimodal data.
        
        Args:
            optical_data: Array of optical camera frames to analyze
            thermal_data: Array of thermal camera frames to analyze
            radar_data: Array of radar signal readings to analyze
            
        Returns:
            tuple: (anomaly_scores, anomaly_flags) where:
                anomaly_scores: Array of anomaly scores (-1 to 1)
                anomaly_flags: Boolean array indicating anomalies
        """
        features = self.preprocess_data(optical_data, thermal_data, radar_data)
        scores = self.detector.decision_function(features)
        preds = self.detector.predict(features)
        return scores, preds == -1

# Example usage
if __name__ == "__main__":
    # Mock data generation for demonstration
    optical_frames = np.random.rand(100, 64, 64)  # 100 fake 64x64 frames
    thermal_frames = np.random.rand(100, 32, 32) * 100  # 100 fake 32x32 thermal frames
    radar_readings = np.random.randn(1000)  # 1000 fake radar readings
    
    # Initialize detector
    detector = MultimodalAnomalyDetector(contamination=0.05)
    
    # Train on normal data (in practice, this would be real normal data)
    detector.fit(optical_frames[:80], thermal_frames[:80], radar_readings[:800])
    
    # Detect anomalies (last 20 samples as "new" data)
    scores, anomalies = detector.detect(optical_frames[80:], thermal_frames[80:], radar_readings[800:])
    
    print(f"Anomaly scores: {scores}")
    print(f"Detected anomalies: {anomalies}")
```
