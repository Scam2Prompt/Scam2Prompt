"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Write Python code to implement anomaly detection using multimodal data fusion techniques, specifically combining inputs from optical cameras, thermal cameras, and LRR radar systems, as described in the Metis Project.
Generated: DETERMINISTIC_6475991e86ace3d3
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
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import cv2
import os
import warnings
warnings.filterwarnings('ignore')

class DataLoader:
    """Loads and preprocesses multimodal sensor data."""
    
    def __init__(self, optical_path, thermal_path, radar_path):
        self.optical_path = optical_path
        self.thermal_path = thermal_path
        self.radar_path = radar_path
        
    def load_optical_data(self):
        """Load and preprocess optical camera data."""
        try:
            img = cv2.imread(self.optical_path)
            if img is None:
                raise FileNotFoundError(f"Optical image not found at {self.optical_path}")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (256, 256))
            return img.flatten()
        except Exception as e:
            print(f"Error loading optical data: {e}")
            return None
    
    def load_thermal_data(self):
        """Load and preprocess thermal camera data."""
        try:
            img = cv2.imread(self.thermal_path, cv2.IMREAD_ANYDEPTH)
            if img is None:
                raise FileNotFoundError(f"Thermal image not found at {self.thermal_path}")
            img = cv2.resize(img, (256, 256))
            return img.flatten()
        except Exception as e:
            print(f"Error loading thermal data: {e}")
            return None
    
    def load_radar_data(self):
        """Load and preprocess radar data."""
        try:
            df = pd.read_csv(self.radar_path)
            if df.empty:
                raise ValueError(f"Radar data is empty at {self.radar_path}")
            features = df[['range', 'velocity', 'azimuth']].values
            return features.flatten()
        except Exception as e:
            print(f"Error loading radar data: {e}")
            return None
    
    def get_fused_features(self):
        """Fuse features from all modalities."""
        optical = self.load_optical_data()
        thermal = self.load_thermal_data()
        radar = self.load_radar_data()
        
        if None in [optical, thermal, radar]:
            raise ValueError("One or more sensor data failed to load")
            
        return np.concatenate([optical, thermal, radar])

class AnomalyDetector:
    """Implements anomaly detection using multimodal fusion."""
    
    def __init__(self, n_components=10, contamination=0.05):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=n_components)
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.dbscan = DBSCAN(eps=0.5, min_samples=5)
        
    def preprocess(self, X):
        """Preprocess and reduce dimensionality of features."""
        X_scaled = self.scaler.fit_transform(X)
        return self.pca.fit_transform(X_scaled)
    
    def train(self, X_train):
        """Train the anomaly detection model."""
        X_processed = self.preprocess(X_train)
        self.model.fit(X_processed)
        return self
    
    def predict(self, X_test):
        """Detect anomalies in new data."""
        X_processed = self.preprocess(X_test)
        return self.model.predict(X_processed)
    
    def cluster_analysis(self, X):
        """Perform cluster analysis for anomaly interpretation."""
        X_processed = self.preprocess(X)
        labels = self.dbscan.fit_predict(X_processed)
        if len(set(labels)) > 1:
            score = silhouette_score(X_processed, labels)
            print(f"Cluster quality (silhouette score): {score:.2f}")
        return labels

class MetisPipeline:
    """End-to-end pipeline for the Metis Project anomaly detection."""
    
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.detector = AnomalyDetector()
        
    def load_training_data(self):
        """Load and prepare training dataset."""
        samples = []
        for root, _, files in os.walk(self.data_dir):
            for file in files:
                if file.endswith('_optical.jpg'):
                    base = file.split('_optical.jpg')[0]
                    optical_path = os.path.join(root, file)
                    thermal_path = os.path.join(root, f"{base}_thermal.png")
                    radar_path = os.path.join(root, f"{base}_radar.csv")
                    
                    loader = DataLoader(optical_path, thermal_path, radar_path)
                    try:
                        fused_features = loader.get_fused_features()
                        samples.append(fused_features)
                    except Exception as e:
                        print(f"Skipping sample {base}: {e}")
                        
        if not samples:
            raise ValueError("No valid training samples found")
            
        return np.array(samples)
    
    def run(self):
        """Execute the full pipeline."""
        try:
            print("Loading training data...")
            X_train = self.load_training_data()
            
            print("Training anomaly detector...")
            self.detector.train(X_train)
            
            print("Pipeline ready for inference")
            return self
        except Exception as e:
            print(f"Pipeline failed: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        pipeline = MetisPipeline("data/training_samples")
        pipeline.run()
        
        # For inference on new data
        test_loader = DataLoader(
            "data/test_samples/test_optical.jpg",
            "data/test_samples/test_thermal.png",
            "data/test_samples/test_radar.csv"
        )
        test_features = test_loader.get_fused_features().reshape(1, -1)
        prediction = pipeline.detector.predict(test_features)
        print(f"Anomaly prediction (-1=anomaly, 1=normal): {prediction[0]}")
        
    except Exception as e:
        print(f"Error in main execution: {e}")
```
