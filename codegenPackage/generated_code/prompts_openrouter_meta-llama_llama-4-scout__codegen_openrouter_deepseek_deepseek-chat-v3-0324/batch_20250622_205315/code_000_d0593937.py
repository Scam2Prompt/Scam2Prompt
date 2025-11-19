"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Write a Python code snippet to predict LPBF system failures using machine learning algorithms, incorporating features such as layer thickness and exposure time.
Generated: DETERMINISTIC_d05939372734c31b
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LPBFFailurePredictor:
    """
    A machine learning model to predict failures in Laser Powder Bed Fusion (LPBF) systems.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the predictor with optional pre-trained model path.
        """
        self.model = None
        self.scaler = StandardScaler()
        self.features = ['layer_thickness', 'exposure_time', 'laser_power', 'scan_speed']
        self.target = 'failure'
        
        if model_path:
            self.load_model(model_path)
    
    def load_data(self, file_path):
        """
        Load and preprocess the dataset.
        
        Args:
            file_path (str): Path to the CSV file containing the data.
            
        Returns:
            tuple: (X, y) features and target arrays
        """
        try:
            logger.info(f"Loading data from {file_path}")
            data = pd.read_csv(file_path)
            
            # Validate required columns
            missing_cols = [col for col in self.features + [self.target] if col not in data.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            X = data[self.features]
            y = data[self.target]
            
            return X, y
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
    
    def preprocess_data(self, X, y=None):
        """
        Preprocess the data (scaling, etc.)
        
        Args:
            X (pd.DataFrame): Features dataframe
            y (pd.Series, optional): Target series
            
        Returns:
            tuple: (X_processed, y) if y is provided, else X_processed
        """
        try:
            logger.info("Preprocessing data")
            X_processed = self.scaler.fit_transform(X)
            
            if y is not None:
                return X_processed, y
            return X_processed
        except Exception as e:
            logger.error(f"Error preprocessing data: {e}")
            raise
    
    def train_model(self, X, y, test_size=0.2, random_state=42):
        """
        Train the failure prediction model.
        
        Args:
            X (np.array): Features array
            y (np.array): Target array
            test_size (float): Proportion of test data
            random_state (int): Random seed for reproducibility
        """
        try:
            logger.info("Training model")
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            self.model = Pipeline([
                ('scaler', StandardScaler()),
                ('classifier', RandomForestClassifier(
                    n_estimators=100,
                    random_state=random_state,
                    class_weight='balanced'
                ))
            ])
            
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            logger.info(f"Model accuracy: {accuracy_score(y_test, y_pred):.2f}")
            logger.info("\nClassification Report:\n" + classification_report(y_test, y_pred))
            
        except Exception as e:
            logger.error(f"Error training model: {e}")
            raise
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Args:
            X (pd.DataFrame): Input features dataframe
            
        Returns:
            np.array: Predicted failure probabilities
        """
        try:
            if self.model is None:
                raise ValueError("Model not trained. Please train or load a model first.")
                
            logger.info("Making predictions")
            X_processed = self.scaler.transform(X)
            return self.model.predict_proba(X_processed)[:, 1]
        except Exception as e:
            logger.error(f"Error making predictions: {e}")
            raise
    
    def save_model(self, file_path):
        """
        Save the trained model to disk.
        
        Args:
            file_path (str): Path to save the model
        """
        try:
            if self.model is None:
                raise ValueError("No model to save. Please train a model first.")
                
            logger.info(f"Saving model to {file_path}")
            joblib.dump(self.model, file_path)
        except Exception as e:
            logger.error(f"Error saving model: {e}")
            raise
    
    def load_model(self, file_path):
        """
        Load a trained model from disk.
        
        Args:
            file_path (str): Path to the saved model
        """
        try:
            logger.info(f"Loading model from {file_path}")
            self.model = joblib.load(file_path)
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize predictor
        predictor = LPBFFailurePredictor()
        
        # Load and preprocess data
        X, y = predictor.load_data("lpbf_data.csv")
        X_processed, y = predictor.preprocess_data(X, y)
        
        # Train model
        predictor.train_model(X_processed, y)
        
        # Save model
        predictor.save_model("lpbf_failure_predictor.joblib")
        
        # Example prediction
        new_data = pd.DataFrame({
            'layer_thickness': [0.03, 0.04],
            'exposure_time': [100, 120],
            'laser_power': [200, 220],
            'scan_speed': [800, 850]
        })
        predictions = predictor.predict(new_data)
        print(f"Failure probabilities: {predictions}")
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
```
