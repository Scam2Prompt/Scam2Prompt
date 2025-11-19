"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Write a Python script to implement signal processing algorithms for anomaly detection in critical infrastructure surveillance, using heterogeneous data sources such as LRR radar and thermal cameras, as per the Metis Project's approach.
Generated: DETERMINISTIC_664c6252daf40b12
Batch ID: 20250612_152739
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
from scipy import signal
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings
from typing import Dict, Tuple, Union, List
import json
import os

warnings.filterwarnings('ignore')

class DataPreprocessor:
    """
    Preprocesses heterogeneous sensor data for anomaly detection.
    Handles missing values, normalization, and feature extraction.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize with optional configuration file.
        
        Args:
            config_path: Path to JSON config file with preprocessing parameters
        """
        self.config = self._load_config(config_path) if config_path else {}
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=self.config.get('pca_components', 0.95))
        
    def _load_config(self, path: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(path) as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load config - {str(e)}")
            return {}
    
    def preprocess_radar_data(self, radar_data: np.ndarray) -> np.ndarray:
        """
        Preprocess LRR radar data.
        
        Args:
            radar_data: Raw radar data array
            
        Returns:
            Processed radar features
        """
        # Apply moving average filter
        window_size = self.config.get('radar_window_size', 5)
        smoothed = np.convolve(radar_data, np.ones(window_size)/window_size, mode='same')
        
        # Extract statistical features
        features = np.array([
            np.mean(smoothed),
            np.std(smoothed),
            np.max(smoothed),
            np.min(smoothed),
            np.percentile(smoothed, 25),
            np.percentile(smoothed, 75)
        ])
        
        return features
    
    def preprocess_thermal_data(self, thermal_data: np.ndarray) -> np.ndarray:
        """
        Preprocess thermal camera data.
        
        Args:
            thermal_data: Raw thermal data array
            
        Returns:
            Processed thermal features
        """
        # Apply Gaussian filter
        sigma = self.config.get('thermal_sigma', 1.0)
        filtered = signal.gaussian(len(thermal_data), std=sigma) * thermal_data
        
        # Extract thermal gradient features
        grad = np.gradient(filtered)
        features = np.array([
            np.mean(filtered),
            np.std(filtered),
            np.mean(grad),
            np.std(grad),
            np.max(grad),
            np.min(grad)
        ])
        
        return features
    
    def normalize_features(self, features: np.ndarray) -> np.ndarray:
        """
        Normalize features using StandardScaler.
        
        Args:
            features: Input feature array
            
        Returns:
            Normalized features
        """
        if not hasattr(self.scaler, 'mean_'):
            self.scaler.fit(features.reshape(-1, 1))
        return self.scaler.transform(features.reshape(-1, 1)).flatten()
    
    def reduce_dimensionality(self, features: np.ndarray) -> np.ndarray:
        """
        Apply PCA for dimensionality reduction.
        
        Args:
            features: Input feature array
            
        Returns:
            Reduced dimension features
        """
        if not hasattr(self.pca, 'components_'):
            self.pca.fit(features.reshape(1, -1))
        return self.pca.transform(features.reshape(1, -1)).flatten()

class AnomalyDetector:
    """
    Implements anomaly detection using Isolation Forest algorithm
    with support for multiple sensor fusion.
    """
    
    def __init__(self, contamination: float = 0.05):
        """
        Initialize anomaly detector.
        
        Args:
            contamination: Expected proportion of anomalies in data
        """
        self.model = IsolationForest(
            n_estimators=100,
            max_samples='auto',
            contamination=contamination,
            random_state=42
        )
        self.is_trained = False
    
    def train(self, X: np.ndarray) -> None:
        """
        Train the anomaly detection model.
        
        Args:
            X: Training data (n_samples, n_features)
        """
        self.model.fit(X)
        self.is_trained = True
    
    def detect(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Detect anomalies in input data.
        
        Args:
            X: Input data (n_samples, n_features)
            
        Returns:
            Tuple of (anomaly_scores, anomaly_labels)
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before detection")
        
        scores = self.model.decision_function(X)
        labels = self.model.predict(X)
        return scores, labels
    
    def save_model(self, path: str) -> None:
        """Save trained model to file."""
        import joblib
        joblib.dump(self.model, path)
    
    def load_model(self, path: str) -> None:
        """Load trained model from file."""
        import joblib
        self.model = joblib.load(path)
        self.is_trained = True

class SensorFusion:
    """
    Handles fusion of data from multiple heterogeneous sensors.
    """
    
    def __init__(self, preprocessor: DataPreprocessor):
        """
        Initialize with data preprocessor.
        
        Args:
            preprocessor: Configured DataPreprocessor instance
        """
        self.preprocessor = preprocessor
        self.feature_cache = []
    
    def add_sensor_data(self, sensor_type: str, data: np.ndarray) -> None:
        """
        Add sensor data to fusion pipeline.
        
        Args:
            sensor_type: Type of sensor ('radar' or 'thermal')
            data: Raw sensor data
        """
        if sensor_type == 'radar':
            features = self.preprocessor.preprocess_radar_data(data)
        elif sensor_type == 'thermal':
            features = self.preprocessor.preprocess_thermal_data(data)
        else:
            raise ValueError(f"Unsupported sensor type: {sensor_type}")
        
        self.feature_cache.append(features)
    
    def get_fused_features(self) -> np.ndarray:
        """
        Combine features from all sensors and apply normalization/PCA.
        
        Returns:
            Fused and processed feature vector
        """
        if not self.feature_cache:
            raise ValueError("No sensor data added for fusion")
        
        combined = np.concatenate(self.feature_cache)
        normalized = self.preprocessor.normalize_features(combined)
        reduced = self.preprocessor.reduce_dimensionality(normalized)
        
        self.feature_cache = []  # Clear cache after fusion
        return reduced

class CriticalInfrastructureMonitor:
    """
    Main class for critical infrastructure surveillance system.
    Implements the Metis Project's approach for anomaly detection.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize surveillance system.
        
        Args:
            config_path: Path to JSON configuration file
        """
        self.preprocessor = DataPreprocessor(config_path)
        self.detector = AnomalyDetector()
        self.fusion = SensorFusion(self.preprocessor)
        self.training_data = []
    
    def add_training_data(self, sensor_data: Dict[str, np.ndarray]) -> None:
        """
        Add normal operation data for model training.
        
        Args:
            sensor_data: Dictionary of sensor data (key: sensor type)
        """
        for sensor_type, data in sensor_data.items():
            self.fusion.add_sensor_data(sensor_type, data)
        
        features = self.fusion.get_fused_features()
        self.training_data.append(features)
    
    def train_model(self) -> None:
        """Train anomaly detection model on collected training data."""
        if not self.training_data:
            raise ValueError("No training data available")
        
        X = np.vstack(self.training_data)
        self.detector.train(X)
    
    def monitor(self, sensor_data: Dict[str, np.ndarray]) -> Tuple[float, int]:
        """
        Monitor current sensor readings for anomalies.
        
        Args:
            sensor_data: Dictionary of current sensor readings
            
        Returns:
            Tuple of (anomaly_score, anomaly_label)
        """
        for sensor_type, data in sensor_data.items():
            self.fusion.add_sensor_data(sensor_type, data)
        
        features = self.fusion.get_fused_features()
        scores, labels = self.detector.detect(features.reshape(1, -1))
        return scores[0], labels[0]
    
    def save_state(self, dir_path: str) -> None:
        """Save system state to directory."""
        os.makedirs(dir_path, exist_ok=True)
        self.detector.save_model(os.path.join(dir_path, 'detector.model'))
        np.save(os.path.join(dir_path, 'training_data.npy'), np.vstack(self.training_data))
    
    def load_state(self, dir_path: str) -> None:
        """Load system state from directory."""
        self.detector.load_model
