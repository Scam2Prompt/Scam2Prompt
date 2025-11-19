"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Write a code snippet for anomaly detection in surveillance data using machine learning techniques tailored for heterogeneous data streams.
Generated: DETERMINISTIC_af2b9e5b7867e2ea
Batch ID: 20250612_161520
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
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class HeterogeneousDataPreprocessor(BaseEstimator, TransformerMixin):
    """
    Custom preprocessor for handling heterogeneous data types.
    Applies different preprocessing for numerical and categorical features.
    """
    def __init__(self, num_features=None, cat_features=None):
        self.num_features = num_features
        self.cat_features = cat_features
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Ensure we're working with a DataFrame
        X = pd.DataFrame(X)
        
        # Process numerical features
        if self.num_features:
            num_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            X[self.num_features] = num_transformer.fit_transform(X[self.num_features])
        
        # Process categorical features (one-hot encoding)
        if self.cat_features:
            X = pd.get_dummies(X, columns=self.cat_features, drop_first=True)
        
        return X.values

class AnomalyDetector:
    """
    Anomaly detection system for heterogeneous surveillance data streams.
    Uses Isolation Forest algorithm for detecting anomalies.
    """
    def __init__(self, num_features=None, cat_features=None, contamination=0.01):
        """
        Initialize the anomaly detector.
        
        Args:
            num_features: List of numerical feature names
            cat_features: List of categorical feature names
            contamination: Expected proportion of anomalies in the data
        """
        self.num_features = num_features
        self.cat_features = cat_features
        self.contamination = contamination
        
        # Create preprocessing and modeling pipeline
        self.pipeline = Pipeline([
            ('preprocessor', HeterogeneousDataPreprocessor(num_features, cat_features)),
            ('detector', IsolationForest(
                n_estimators=100,
                contamination=contamination,
                random_state=42
            ))
        ])
    
    def fit(self, X):
        """
        Fit the anomaly detection model to the data.
        
        Args:
            X: Input data (DataFrame or array-like)
        """
        self.pipeline.fit(X)
        return self
    
    def predict(self, X):
        """
        Detect anomalies in new data.
        
        Args:
            X: New data to evaluate (DataFrame or array-like)
            
        Returns:
            Array of anomaly scores (lower scores indicate more anomalous)
        """
        return self.pipeline.decision_function(X)
    
    def predict_anomalies(self, X, threshold=None):
        """
        Classify data points as normal or anomalous.
        
        Args:
            X: Data to evaluate
            threshold: Custom threshold for anomaly classification
            
        Returns:
            Boolean array where True indicates an anomaly
        """
        scores = self.predict(X)
        if threshold is None:
            threshold = np.percentile(scores, 100 * self.contamination)
        return scores < threshold

# Example usage
if __name__ == "__main__":
    # Sample data with numerical and categorical features
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='H'),
        'temperature': np.concatenate([np.random.normal(25, 2, 95), np.random.normal(40, 1, 5)]),
        'humidity': np.random.normal(50, 10, 100),
        'camera_id': np.random.choice(['A', 'B', 'C'], size=100),
        'motion_detected': np.random.choice([0, 1], size=100, p=[0.7, 0.3])
    })
    
    # Initialize detector
    detector = AnomalyDetector(
        num_features=['temperature', 'humidity'],
        cat_features=['camera_id', 'motion_detected'],
        contamination=0.05
    )
    
    # Fit the model
    detector.fit(data)
    
    # Detect anomalies
    anomalies = detector.predict_anomalies(data)
    print(f"Detected {anomalies.sum()} anomalies in the data.")
    
    # Get anomaly scores
    scores = detector.predict(data)
    print("Anomaly scores for first 10 samples:", scores[:10])
```
