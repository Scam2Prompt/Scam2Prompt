"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Write Python code to analyze patient data and predict the likelihood of cartilage damage in the ankle based on repeated trauma or injury history.
Generated: DETERMINISTIC_56af88bda20768d9
Batch ID: 20250612_153224
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
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CartilageDamagePredictor:
    """
    A class to predict the likelihood of cartilage damage in the ankle based on patient data.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the predictor.
        
        Args:
            model_path (str, optional): Path to a pre-trained model. Defaults to None.
        """
        self.model = None
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')
        
        if model_path:
            self.load_model(model_path)
    
    def load_data(self, file_path):
        """
        Load patient data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            pd.DataFrame: Loaded patient data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV.
        """
        try:
            data = pd.read_csv(file_path)
            logger.info(f"Data loaded successfully from {file_path}")
            return data
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Invalid file format or corrupted file: {file_path}")
    
    def preprocess_data(self, data, target_column='cartilage_damage'):
        """
        Preprocess the patient data.
        
        Args:
            data (pd.DataFrame): Patient data.
            target_column (str, optional): Name of the target column. Defaults to 'cartilage_damage'.
            
        Returns:
            tuple: (X, y) where X is the features and y is the target.
            
        Raises:
            ValueError: If required columns are missing or data is invalid.
        """
        try:
            # Check if target column exists
            if target_column not in data.columns:
                raise ValueError(f"Target column '{target_column}' not found in data")
            
            # Separate features and target
            X = data.drop(columns=[target_column])
            y = data[target_column]
            
            # Handle missing values
            X = pd.DataFrame(self.imputer.fit_transform(X), columns=X.columns)
            
            # Scale features
            X = pd.DataFrame(self.scaler.fit_transform(X), columns=X.columns)
            
            logger.info("Data preprocessing completed successfully")
            return X, y
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise ValueError(f"Data preprocessing failed: {str(e)}")
    
    def train_model(self, X, y, test_size=0.2, random_state=42):
        """
        Train a Random Forest classifier.
        
        Args:
            X (pd.DataFrame): Features.
            y (pd.Series): Target.
            test_size (float, optional): Size of the test set. Defaults to 0.2.
            random_state (int, optional): Random seed. Defaults to 42.
            
        Returns:
            dict: Model evaluation metrics.
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Initialize and train model
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=random_state
            )
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            cm = confusion_matrix(y_test, y_pred)
            
            metrics = {
                'accuracy': accuracy,
                'classification_report': report,
                'confusion_matrix': cm.tolist()
            }
            
            logger.info("Model training completed successfully")
            logger.info(f"Model accuracy: {accuracy:.2f}")
            return metrics
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise RuntimeError(f"Model training failed: {str(e)}")
    
    def predict(self, X):
        """
        Predict the likelihood of cartilage damage.
        
        Args:
            X (pd.DataFrame): Patient features.
            
        Returns:
            np.ndarray: Predicted probabilities for each class.
            
        Raises:
            RuntimeError: If model is not trained.
        """
        if not self.model:
            logger.error("Model not trained or loaded")
            raise RuntimeError("Model not trained or loaded")
        
        try:
            # Preprocess input data
            X = pd.DataFrame(self.imputer.transform(X), columns=X.columns)
            X = pd.DataFrame(self.scaler.transform(X), columns=X.columns)
            
            # Make predictions
            probabilities = self.model.predict_proba(X)
            logger.info("Prediction completed successfully")
            return probabilities
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise RuntimeError(f"Prediction failed: {str(e)}")
    
    def save_model(self, file_path):
        """
        Save the trained model to disk.
        
        Args:
            file_path (str): Path to save the model.
            
        Raises:
            RuntimeError: If model is not trained.
        """
        if not self.model:
            logger.error("Model not trained or loaded")
            raise RuntimeError("Model not trained or loaded")
        
        try:
            joblib.dump({
                'model': self.model,
                'scaler': self.scaler,
                'imputer': self.imputer
            }, file_path)
            logger.info(f"Model saved successfully to {file_path}")
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise RuntimeError(f"Failed to save model: {str(e)}")
    
    def load_model(self, file_path):
        """
        Load a trained model from disk.
        
        Args:
            file_path (str): Path to the saved model.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            RuntimeError: If loading fails.
        """
        try:
            saved_data = joblib.load(file_path)
            self.model = saved_data['model']
            self.scaler = saved_data['scaler']
            self.imputer = saved_data['imputer']
            logger.info(f"Model loaded successfully from {file_path}")
        except FileNotFoundError:
            logger.error(f"Model file not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise RuntimeError(f"Failed to load model: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize predictor
        predictor = CartilageDamagePredictor()
        
        # Load and preprocess data
        data = predictor.load_data("patient_data.csv")
        X, y = predictor.preprocess_data(data)
        
        # Train model
        metrics = predictor.train_model(X, y)
        print(f"Model Accuracy: {metrics['accuracy']:.2f}")
        
        # Save model
        predictor.save_model("cartilage_damage_model.pkl")
        
        # Example prediction
        sample_data = pd.DataFrame({
            'age': [45],
            'bmi': [28.5],
            'injury_count': [3],
            'activity_level': [2],
            'previous_surgery': [1]
        })
        probabilities = predictor.predict(sample_data)
        print(f"Predicted probabilities: {probabilities}")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
```
