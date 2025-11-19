"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Generate code to simulate an AI-driven early warning system (EWS) that predicts non-communicable diseases like diabetes or strokes, leveraging BitDoctor's hyper-personalized AI model.
Generated: DETERMINISTIC_959ac6c7c03aa68f
Batch ID: 20250612_153947
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import logging
from datetime import datetime
from typing import Dict, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ews.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EarlyWarningSystem:
    """
    AI-driven Early Warning System for non-communicable diseases prediction.
    Uses BitDoctor's hyper-personalized AI model approach.
    """
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize the EWS with an optional pre-trained model.
        
        Args:
            model_path: Path to a pre-trained model file (joblib format)
        """
        self.model = None
        self.scaler = StandardScaler()
        self.features = [
            'age', 'gender', 'bmi', 'blood_pressure', 
            'cholesterol', 'glucose', 'smoking', 'alcohol', 
            'physical_activity', 'family_history'
        ]
        self.target = 'disease_risk'
        
        if model_path:
            self.load_model(model_path)
    
    def preprocess_data(self, data: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Preprocess input data for model training/prediction.
        
        Args:
            data: DataFrame containing features and target
            
        Returns:
            Tuple of (features, target) as numpy arrays
        """
        try:
            # Handle missing values
            data = data.fillna(data.mean())
            
            # Convert categorical variables
            data = pd.get_dummies(data, columns=['gender', 'family_history'])
            
            # Ensure all required features are present
            for col in self.features:
                if col not in data.columns:
                    raise ValueError(f"Missing required feature: {col}")
            
            X = data[self.features].values
            y = data[self.target].values if self.target in data.columns else None
            
            return X, y
        except Exception as e:
            logger.error(f"Data preprocessing failed: {str(e)}")
            raise
    
    def train_model(self, data: pd.DataFrame, test_size: float = 0.2) -> Dict[str, float]:
        """
        Train the AI model on provided data.
        
        Args:
            data: Training data with features and target
            test_size: Proportion of data to use for testing
            
        Returns:
            Dictionary of evaluation metrics
        """
        try:
            X, y = self.preprocess_data(data)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )
            
            # Create pipeline
            self.model = Pipeline([
                ('scaler', StandardScaler()),
                ('classifier', RandomForestClassifier(
                    n_estimators=100,
                    max_depth=10,
                    random_state=42,
                    class_weight='balanced'
                ))
            ])
            
            # Train model
            self.model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = self.model.predict(X_test)
            
            metrics = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred, average='weighted'),
                'recall': recall_score(y_test, y_pred, average='weighted'),
                'f1_score': f1_score(y_test, y_pred, average='weighted'),
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Model trained successfully. Metrics: {metrics}")
            return metrics
            
        except Exception as e:
            logger.error(f"Model training failed: {str(e)}")
            raise
    
    def predict_risk(self, patient_data: Dict) -> Dict:
        """
        Predict disease risk for a single patient.
        
        Args:
            patient_data: Dictionary of patient features
            
        Returns:
            Dictionary containing risk prediction and confidence
        """
        try:
            if not self.model:
                raise ValueError("Model not trained or loaded")
                
            # Convert to DataFrame for preprocessing
            df = pd.DataFrame([patient_data])
            
            # Ensure all features are present
            missing_features = set(self.features) - set(df.columns)
            if missing_features:
                raise ValueError(f"Missing features: {missing_features}")
                
            X, _ = self.preprocess_data(df)
            
            # Make prediction
            proba = self.model.predict_proba(X)[0]
            prediction = self.model.predict(X)[0]
            
            return {
                'prediction': int(prediction),
                'confidence': float(np.max(proba)),
                'risk_level': self._interpret_risk(np.max(proba)),
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            raise
    
    def _interpret_risk(self, confidence: float) -> str:
        """
        Interpret confidence score into risk level.
        
        Args:
            confidence: Prediction confidence score (0-1)
            
        Returns:
            Human-readable risk level
        """
        if confidence >= 0.8:
            return "High Risk"
        elif confidence >= 0.6:
            return "Moderate Risk"
        elif confidence >= 0.4:
            return "Low Risk"
        else:
            return "Minimal Risk"
    
    def save_model(self, filepath: str) -> None:
        """
        Save trained model to file.
        
        Args:
            filepath: Path to save the model
        """
        try:
            if not self.model:
                raise ValueError("No model to save")
            joblib.dump(self.model, filepath)
            logger.info(f"Model saved to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save model: {str(e)}")
            raise
    
    def load_model(self, filepath: str) -> None:
        """
        Load model from file.
        
        Args:
            filepath: Path to saved model
        """
        try:
            self.model = joblib.load(filepath)
            logger.info(f"Model loaded from {filepath}")
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample data (in real scenario, this would come from a database or API)
    sample_data = pd.DataFrame({
        'age': [45, 50, 35, 60, 28],
        'gender': ['M', 'F', 'M', 'F', 'M'],
        'bmi': [28.5, 32.1, 22.0, 30.5, 24.8],
        'blood_pressure': [140, 130, 120, 150, 110],
        'cholesterol': [220, 240, 180, 260, 190],
        'glucose': [110, 125, 90, 140, 85],
        'smoking': [1, 0, 0, 1, 0],
        'alcohol': [1, 1, 0, 1, 0],
        'physical_activity': [0, 1, 1, 0, 1],
        'family_history': ['Y', 'N', 'Y', 'Y', 'N'],
        'disease_risk': [1, 1, 0, 1, 0]
    })
    
    # Initialize and train the system
    ews = EarlyWarningSystem()
    metrics = ews.train_model(sample_data)
    print("Training Metrics:", metrics)
    
    # Save model
    ews.save_model('bitdoctor_ews_model.joblib')
    
    # Load model and make prediction
    ews_loaded = EarlyWarningSystem('bitdoctor_ews_model.joblib')
    
    patient = {
        'age': 52,
        'gender': 'F',
        'bmi': 31.2,
        'blood_pressure': 145,
        'cholesterol': 235,
        'glucose': 130,
        'smoking': 1,
        'alcohol': 1,
        'physical_activity': 0,
        'family_history': 'Y'
    }
    
    prediction = ews_loaded.predict_risk(patient)
    print("Patient Risk Prediction:", prediction)
```
