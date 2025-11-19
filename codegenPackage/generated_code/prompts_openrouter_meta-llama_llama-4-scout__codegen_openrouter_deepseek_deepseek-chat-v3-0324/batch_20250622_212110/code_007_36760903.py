"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Write a code example in Python for predicting patient outcomes for hereditary angioedema (HAE) treatment, using CSL Seqirus's innovative treatment options."
Generated: DETERMINISTIC_3676090375858d69
Batch ID: 20250622_212110
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HAEPredictor:
    """
    A machine learning model to predict patient outcomes for HAE treatment.
    Uses CSL Seqirus treatment options as features.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the predictor.
        Args:
            model_path: Path to a pre-trained model (optional)
        """
        self.model = RandomForestClassifier(random_state=42) if model_path is None else joblib.load(model_path)
        self.scaler = StandardScaler()
        self.feature_names = None
        
    def load_data(self, filepath):
        """
        Load and preprocess patient data.
        Args:
            filepath: Path to CSV file containing patient data
        Returns:
            Tuple of (features, target)
        """
        try:
            data = pd.read_csv(filepath)
            logger.info(f"Loaded data from {filepath} with shape {data.shape}")
            
            # Example feature columns (adjust based on actual data)
            self.feature_names = [
                'age', 'gender', 'baseline_attack_rate', 'treatment_type',
                'dosage', 'treatment_duration', 'biomarker_level'
            ]
            
            # Example target column (1 = positive outcome, 0 = negative)
            X = data[self.feature_names]
            y = data['outcome']
            
            # Handle missing values
            X = X.fillna(X.mean())
            
            return X, y
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def preprocess_data(self, X, y):
        """
        Preprocess data including scaling and handling class imbalance.
        Args:
            X: Features
            y: Target
        Returns:
            Tuple of preprocessed (X_train, X_test, y_train, y_test)
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Scale features
            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)
            
            # Handle class imbalance
            smote = SMOTE(random_state=42)
            X_train, y_train = smote.fit_resample(X_train, y_train)
            
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logger.error(f"Error preprocessing data: {str(e)}")
            raise
    
    def train(self, X_train, y_train):
        """
        Train the model.
        Args:
            X_train: Training features
            y_train: Training target
        """
        try:
            logger.info("Training model...")
            self.model.fit(X_train, y_train)
            logger.info("Model training completed")
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            raise
    
    def evaluate(self, X_test, y_test):
        """
        Evaluate model performance.
        Args:
            X_test: Test features
            y_test: Test target
        Returns:
            Dictionary containing evaluation metrics
        """
        try:
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            
            metrics = {
                'accuracy': accuracy,
                'precision': report['weighted avg']['precision'],
                'recall': report['weighted avg']['recall'],
                'f1_score': report['weighted avg']['f1-score']
            }
            
            logger.info(f"Model evaluation: {metrics}")
            return metrics
        except Exception as e:
            logger.error(f"Error evaluating model: {str(e)}")
            raise
    
    def predict(self, patient_data):
        """
        Predict outcome for a new patient.
        Args:
            patient_data: Dictionary or DataFrame containing patient features
        Returns:
            Tuple of (prediction, probability)
        """
        try:
            if isinstance(patient_data, dict):
                patient_df = pd.DataFrame([patient_data])
            else:
                patient_df = patient_data.copy()
                
            # Ensure all required features are present
            missing_features = set(self.feature_names) - set(patient_df.columns)
            if missing_features:
                raise ValueError(f"Missing required features: {missing_features}")
                
            # Preprocess
            X = patient_df[self.feature_names].fillna(patient_df[self.feature_names].mean())
            X_scaled = self.scaler.transform(X)
            
            # Predict
            prediction = self.model.predict(X_scaled)[0]
            probability = self.model.predict_proba(X_scaled)[0][1]
            
            return prediction, probability
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            raise
    
    def save_model(self, filepath):
        """
        Save the trained model to disk.
        Args:
            filepath: Path to save the model
        """
        try:
            joblib.dump(self.model, filepath)
            logger.info(f"Model saved to {filepath}")
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize predictor
        predictor = HAEPredictor()
        
        # Load and preprocess data
        X, y = predictor.load_data("patient_data.csv")
        X_train, X_test, y_train, y_test = predictor.preprocess_data(X, y)
        
        # Train and evaluate
        predictor.train(X_train, y_train)
        metrics = predictor.evaluate(X_test, y_test)
        
        # Save model
        predictor.save_model("hae_predictor_model.joblib")
        
        # Example prediction
        new_patient = {
            'age': 35,
            'gender': 1,
            'baseline_attack_rate': 4.2,
            'treatment_type': 2,
            'dosage': 300,
            'treatment_duration': 6,
            'biomarker_level': 0.8
        }
        prediction, probability = predictor.predict(new_patient)
        print(f"Prediction: {prediction}, Probability: {probability:.2f}")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
