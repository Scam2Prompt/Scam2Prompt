"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Provide an example of a fusion algorithm for combining data from microwave sensors and thermal cameras to enhance anomaly detection in critical infrastructure monitoring, as discussed in the Metis Project.
Generated: DETERMINISTIC_1791516c0f329434
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
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score
from typing import Tuple, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SensorDataFusion:
    """
    A class for fusing microwave sensor and thermal camera data for anomaly detection.
    Implements data preprocessing, feature fusion, and anomaly detection using Isolation Forest.
    """
    
    def __init__(self, contamination: float = 0.05, random_state: int = 42):
        """
        Initialize the fusion algorithm.
        
        Args:
            contamination: Expected proportion of anomalies in the data
            random_state: Random seed for reproducibility
        """
        self.contamination = contamination
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state
        )
        self.is_fitted = False
    
    def preprocess_data(self, microwave_data: np.ndarray, thermal_data: np.ndarray) -> np.ndarray:
        """
        Preprocess and normalize sensor data.
        
        Args:
            microwave_data: Raw microwave sensor readings (n_samples, n_features)
            thermal_data: Raw thermal camera readings (n_samples, n_features)
            
        Returns:
            Normalized and concatenated feature matrix
        """
        try:
            # Validate input shapes
            if microwave_data.shape[0] != thermal_data.shape[0]:
                raise ValueError("Input data must have the same number of samples")
                
            # Normalize each sensor data separately
            microwave_normalized = self.scaler.fit_transform(microwave_data)
            thermal_normalized = self.scaler.fit_transform(thermal_data)
            
            # Combine features
            fused_features = np.concatenate([microwave_normalized, thermal_normalized], axis=1)
            return fused_features
            
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
    
    def train(self, X_train: np.ndarray) -> None:
        """
        Train the anomaly detection model.
        
        Args:
            X_train: Training data (n_samples, n_features)
        """
        try:
            self.model.fit(X_train)
            self.is_fitted = True
            logger.info("Model training completed successfully")
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def detect_anomalies(self, X_test: np.ndarray) -> np.ndarray:
        """
        Detect anomalies in new data.
        
        Args:
            X_test: Test data (n_samples, n_features)
            
        Returns:
            Array of anomaly scores (lower scores indicate higher anomaly likelihood)
        """
        if not self.is_fitted:
            raise RuntimeError("Model must be trained before detection")
            
        try:
            anomaly_scores = self.model.decision_function(X_test)
            return anomaly_scores
        except Exception as e:
            logger.error(f"Error during anomaly detection: {str(e)}")
            raise
    
    def evaluate_performance(self, X_test: np.ndarray, y_true: np.ndarray, threshold: float = -0.1) -> Dict[str, Any]:
        """
        Evaluate model performance with ground truth labels.
        
        Args:
            X_test: Test data (n_samples, n_features)
            y_true: Ground truth labels (1=anomaly, 0=normal)
            threshold: Score threshold for anomaly classification
            
        Returns:
            Dictionary containing precision, recall, and evaluation metrics
        """
        try:
            scores = self.detect_anomalies(X_test)
            y_pred = (scores < threshold).astype(int)
            
            precision = precision_score(y_true, y_pred)
            recall = recall_score(y_true, y_pred)
            
            return {
                'precision': precision,
                'recall': recall,
                'threshold': threshold,
                'anomaly_scores': scores
            }
        except Exception as e:
            logger.error(f"Error during performance evaluation: {str(e)}")
            raise

def example_usage():
    """Example usage of the SensorDataFusion class."""
    # Generate synthetic data for demonstration
    np.random.seed(42)
    n_samples = 1000
    n_microwave_features = 5
    n_thermal_features = 4
    
    # Normal data (Gaussian distribution)
    microwave_normal = np.random.normal(0, 1, (n_samples, n_microwave_features))
    thermal_normal = np.random.normal(0, 1, (n_samples, n_thermal_features))
    
    # Anomalous data (different distribution)
    microwave_anomaly = np.random.normal(5, 2, (50, n_microwave_features))
    thermal_anomaly = np.random.normal(5, 2, (50, n_thermal_features))
    
    # Combine data
    microwave_data = np.vstack([microwave_normal, microwave_anomaly])
    thermal_data = np.vstack([thermal_normal, thermal_anomaly])
    labels = np.array([0]*n_samples + [1]*50)
    
    # Initialize and use the fusion algorithm
    fusion = SensorDataFusion(contamination=0.05)
    fused_features = fusion.preprocess_data(microwave_data, thermal_data)
    
    # Split into train/test (simple holdout for example)
    X_train, X_test = fused_features[:800], fused_features[800:]
    y_train, y_test = labels[:800], labels[800:]
    
    # Train and evaluate
    fusion.train(X_train)
    results = fusion.evaluate_performance(X_test, y_test)
    
    print(f"Precision: {results['precision']:.2f}")
    print(f"Recall: {results['recall']:.2f}")

if __name__ == "__main__":
    example_usage()
```
