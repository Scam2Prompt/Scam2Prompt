"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Develop a machine learning model for predicting digital marketing ROI, using concepts from PDMA's Digital Marketing Professional curriculum.
Generated: DETERMINISTIC_a5541693d06ec529
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import joblib
import logging
import warnings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress warnings
warnings.filterwarnings('ignore')

class DigitalMarketingROIPredictor:
    """
    A machine learning model for predicting digital marketing ROI based on PDMA's Digital Marketing Professional curriculum.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the predictor.
        
        Args:
            model_path (str, optional): Path to load a pre-trained model. Defaults to None.
        """
        self.model = None
        self.scaler = StandardScaler()
        self.feature_importances_ = None
        
        if model_path:
            self.load_model(model_path)
    
    def load_data(self, file_path):
        """
        Load and preprocess the marketing data.
        
        Args:
            file_path (str): Path to the CSV file containing marketing data.
            
        Returns:
            pd.DataFrame: Processed DataFrame ready for modeling.
        """
        try:
            # Load data
            data = pd.read_csv(file_path)
            logger.info(f"Data loaded successfully from {file_path}")
            
            # Basic preprocessing
            # Drop rows with missing target values
            data = data.dropna(subset=['ROI'])
            
            # Convert categorical variables to dummy variables
            data = pd.get_dummies(data, drop_first=True)
            
            return data
        
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def prepare_data(self, data, test_size=0.2, random_state=42):
        """
        Prepare data for training by splitting into features and target, and scaling.
        
        Args:
            data (pd.DataFrame): The processed DataFrame.
            test_size (float, optional): Size of test set. Defaults to 0.2.
            random_state (int, optional): Random seed. Defaults to 42.
            
        Returns:
            tuple: X_train, X_test, y_train, y_test
        """
        try:
            # Separate features and target
            X = data.drop('ROI', axis=1)
            y = data['ROI']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Scale features
            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)
            
            logger.info("Data prepared successfully")
            return X_train, X_test, y_train, y_test
            
        except Exception as e:
            logger.error(f"Error preparing data: {str(e)}")
            raise
    
    def train_model(self, X_train, y_train):
        """
        Train a Random Forest Regressor model with hyperparameter tuning.
        
        Args:
            X_train (np.array): Training features.
            y_train (pd.Series): Training target.
        """
        try:
            # Define the model
            rf = RandomForestRegressor(random_state=42)
            
            # Define hyperparameters for tuning
            param_grid = {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            }
            
            # Perform grid search
            grid_search = GridSearchCV(
                estimator=rf,
                param_grid=param_grid,
                cv=5,
                n_jobs=-1,
                scoring='neg_mean_squared_error'
            )
            
            grid_search.fit(X_train, y_train)
            
            # Set the best model
            self.model = grid_search.best_estimator_
            self.feature_importances_ = self.model.feature_importances_
            
            logger.info("Model trained successfully")
            logger.info(f"Best parameters: {grid_search.best_params_}")
            
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            raise
    
    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the trained model on test data.
        
        Args:
            X_test (np.array): Test features.
            y_test (pd.Series): Test target.
            
        Returns:
            dict: Dictionary containing evaluation metrics.
        """
        try:
            if not self.model:
                raise ValueError("Model has not been trained yet")
                
            predictions = self.model.predict(X_test)
            
            metrics = {
                'MAE': mean_absolute_error(y_test, predictions),
                'MSE': mean_squared_error(y_test, predictions),
                'RMSE': np.sqrt(mean_squared_error(y_test, predictions)),
                'R2': r2_score(y_test, predictions)
            }
            
            logger.info("Model evaluation:")
            for metric, value in metrics.items():
                logger.info(f"{metric}: {value:.4f}")
                
            return metrics
            
        except Exception as e:
            logger.error(f"Error evaluating model: {str(e)}")
            raise
    
    def predict(self, X):
        """
        Make ROI predictions on new data.
        
        Args:
            X (pd.DataFrame or np.array): Input features for prediction.
            
        Returns:
            np.array: Predicted ROI values.
        """
        try:
            if not self.model:
                raise ValueError("Model has not been trained yet")
                
            # Ensure input is in the correct format
            if isinstance(X, pd.DataFrame):
                X = self.scaler.transform(X)
                
            return self.model.predict(X)
            
        except Exception as e:
            logger.error(f"Error making predictions: {str(e)}")
            raise
    
    def save_model(self, file_path):
        """
        Save the trained model and scaler to disk.
        
        Args:
            file_path (str): Path to save the model.
        """
        try:
            if not self.model:
                raise ValueError("Model has not been trained yet")
                
            joblib.dump({
                'model': self.model,
                'scaler': self.scaler,
                'feature_importances': self.feature_importances_
            }, file_path)
            
            logger.info(f"Model saved successfully to {file_path}")
            
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, file_path):
        """
        Load a trained model from disk.
        
        Args:
            file_path (str): Path to the saved model.
        """
        try:
            saved_data = joblib.load(file_path)
            self.model = saved_data['model']
            self.scaler = saved_data['scaler']
            self.feature_importances_ = saved_data['feature_importances']
            
            logger.info(f"Model loaded successfully from {file_path}")
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize predictor
        predictor = DigitalMarketingROIPredictor()
        
        # Load and prepare data
        data = predictor.load_data("marketing_data.csv")
        X_train, X_test, y_train, y_test = predictor.prepare_data(data)
        
        # Train model
        predictor.train_model(X_train, y_train)
        
        # Evaluate model
        metrics = predictor.evaluate_model(X_test, y_test)
        
        # Save model
        predictor.save_model("digital_marketing_roi_predictor.joblib")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
```
