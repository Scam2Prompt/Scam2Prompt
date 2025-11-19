"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write Python code to simulate a water leakage detection system using sensor data, incorporating advanced algorithms for identifying leaks without physical damage, as described by شركة انجاز.
Generated: DETERMINISTIC_d6c84c8ecb87088a
Batch ID: 20250612_153224
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
from sklearn.svm import OneClassSVM
from typing import Tuple, List, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WaterLeakageDetector:
    """
    A class to detect water leaks using sensor data with advanced anomaly detection algorithms.
    """
    
    def __init__(self, contamination: float = 0.01, random_state: int = 42):
        """
        Initialize the detector with specified parameters.
        
        Args:
            contamination: Expected proportion of outliers in the data (default: 0.01)
            random_state: Random seed for reproducibility (default: 42)
        """
        self.contamination = contamination
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.model = None
        self.is_trained = False
        
    def preprocess_data(self, data: pd.DataFrame) -> np.ndarray:
        """
        Preprocess sensor data by scaling and normalizing.
        
        Args:
            data: DataFrame containing sensor readings with columns ['timestamp', 'pressure', 'flow_rate', 'temperature']
            
        Returns:
            numpy.ndarray: Scaled and normalized feature matrix
        """
        try:
            # Ensure required columns are present
            required_cols = ['pressure', 'flow_rate', 'temperature']
            if not all(col in data.columns for col in required_cols):
                raise ValueError(f"Data must contain columns: {required_cols}")
                
            # Extract features and scale
            features = data[required_cols].values
            scaled_features = self.scaler.fit_transform(features)
            return scaled_features
            
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
            
    def train_model(self, normal_data: pd.DataFrame, algorithm: str = 'isolation_forest') -> None:
        """
        Train the anomaly detection model on normal operation data.
        
        Args:
            normal_data: DataFrame containing normal operation sensor data
            algorithm: Detection algorithm to use ('isolation_forest' or 'one_class_svm')
        """
        try:
            logger.info("Training leak detection model...")
            
            # Preprocess the training data
            X_train = self.preprocess_data(normal_data)
            
            # Initialize and train the selected model
            if algorithm == 'isolation_forest':
                self.model = IsolationForest(
                    contamination=self.contamination,
                    random_state=self.random_state
                )
            elif algorithm == 'one_class_svm':
                self.model = OneClassSVM(nu=self.contamination)
            else:
                raise ValueError(f"Unknown algorithm: {algorithm}. Choose 'isolation_forest' or 'one_class_svm'")
                
            self.model.fit(X_train)
            self.is_trained = True
            logger.info("Model training completed successfully")
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
            
    def detect_leaks(self, new_data: pd.DataFrame) -> Tuple[pd.DataFrame, float]:
        """
        Detect potential leaks in new sensor data.
        
        Args:
            new_data: DataFrame containing new sensor readings to analyze
            
        Returns:
            Tuple containing:
                - DataFrame with original data and leak predictions
                - Leak probability score (0-1)
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before making predictions")
            
        try:
            # Preprocess the new data
            X_new = self.preprocess_data(new_data)
            
            # Make predictions
            if isinstance(self.model, IsolationForest):
                anomaly_scores = -self.model.decision_function(X_new)
                predictions = self.model.predict(X_new)
                leak_prob = (anomaly_scores - anomaly_scores.min()) / (anomaly_scores.max() - anomaly_scores.min())
            else:  # OneClassSVM
                predictions = self.model.predict(X_new)
                distances = self.model.decision_function(X_new)
                leak_prob = 1 / (1 + np.exp(-distances))  # Convert to probability-like score
                
            # Convert predictions to binary labels (1 = normal, -1 = anomaly)
            leak_detected = (predictions == -1).astype(int)
            
            # Add results to the original dataframe
            result_df = new_data.copy()
            result_df['leak_detected'] = leak_detected
            result_df['leak_probability'] = leak_prob
            
            # Calculate overall leak probability
            overall_leak_prob = np.mean(leak_prob[leak_detected == 1]) if np.any(leak_detected) else 0.0
            
            return result_df, overall_leak_prob
            
        except Exception as e:
            logger.error(f"Error during leak detection: {str(e)}")
            raise

class SensorDataSimulator:
    """
    A class to simulate sensor data for testing the leak detection system.
    """
    
    @staticmethod
    def generate_normal_data(num_samples: int = 1000) -> pd.DataFrame:
        """
        Generate normal operation sensor data.
        
        Args:
            num_samples: Number of samples to generate
            
        Returns:
            DataFrame with simulated normal sensor readings
        """
        timestamps = pd.date_range(
            start=datetime.now(),
            periods=num_samples,
            freq='T'  # Minute frequency
        )
        
        pressure = np.random.normal(50, 5, num_samples)
        flow_rate = np.random.normal(10, 1, num_samples)
        temperature = np.random.normal(20, 2, num_samples)
        
        return pd.DataFrame({
            'timestamp': timestamps,
            'pressure': pressure,
            'flow_rate': flow_rate,
            'temperature': temperature
        })
        
    @staticmethod
    def inject_leak(data: pd.DataFrame, leak_start: int, leak_duration: int) -> pd.DataFrame:
        """
        Inject simulated leak patterns into normal sensor data.
        
        Args:
            data: Original normal sensor data
            leak_start: Index where leak should start
            leak_duration: Duration of leak in samples
            
        Returns:
            DataFrame with injected leak patterns
        """
        leak_end = min(leak_start + leak_duration, len(data))
        
        # Create a copy to modify
        leak_data = data.copy()
        
        # Modify pressure (sudden drop)
        leak_data.loc[leak_start:leak_end, 'pressure'] *= 0.7
        
        # Modify flow rate (gradual increase)
        leak_range = leak_end - leak_start
        if leak_range > 0:
            leak_slope = np.linspace(1.2, 1.8, leak_range)
            leak_data.loc[leak_start:leak_end, 'flow_rate'] *= leak_slope
            
        # Modify temperature (small fluctuation)
        leak_data.loc[leak_start:leak_end, 'temperature'] += np.random.uniform(-1, 1, leak_range)
        
        return leak_data

def main():
    """
    Main function to demonstrate the water leakage detection system.
    """
    try:
        # Step 1: Generate and prepare data
        logger.info("Generating simulated sensor data...")
        normal_data = SensorDataSimulator.generate_normal_data(2000)
        test_data = SensorDataSimulator.inject_leak(normal_data.copy(), 1500, 100)
        
        # Step 2: Initialize and train detector
        detector = WaterLeakageDetector(contamination=0.02)
        detector.train_model(normal_data, algorithm='isolation_forest')
        
        # Step 3: Detect leaks in test data
        logger.info("Running leak detection on test data...")
        results, overall_prob = detector.detect_leaks(test_data)
        
        # Step 4: Analyze results
        leaks = results[results['leak_detected'] == 1]
        logger.info(f"Detected {len(leaks)} potential leaks")
        logger.info(f"Overall leak probability: {overall_prob:.2%}")
        
        # Return results for further analysis
        return results
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
