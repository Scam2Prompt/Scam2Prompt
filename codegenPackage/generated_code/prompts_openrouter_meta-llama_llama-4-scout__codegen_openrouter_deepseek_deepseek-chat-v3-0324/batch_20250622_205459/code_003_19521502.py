"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: "How can I use data from preventative health checks to create predictive models for chronic conditions using machine learning libraries like scikit-learn?"
Generated: DETERMINISTIC_195215029b212cdf
Batch ID: 20250622_205459
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
import joblib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ChronicConditionPredictor:
    """
    A machine learning pipeline for predicting chronic conditions from health check data.
    """
    
    def __init__(self, data_path, target_column, test_size=0.2, random_state=42):
        """
        Initialize the predictor with data path and configuration.
        
        Args:
            data_path (str): Path to the health check data CSV file
            target_column (str): Name of the target column to predict
            test_size (float): Proportion of data to use for testing
            random_state (int): Random seed for reproducibility
        """
        self.data_path = data_path
        self.target_column = target_column
        self.test_size = test_size
        self.random_state = random_state
        self.model = None
        self.scaler = None
        self.feature_columns = None
        
    def load_and_preprocess_data(self):
        """
        Load and preprocess the health check data.
        
        Returns:
            tuple: (X_train, X_test, y_train, y_test) split data
        """
        try:
            # Load data
            data = pd.read_csv(self.data_path)
            
            # Separate features and target
            X = data.drop(columns=[self.target_column])
            y = data[self.target_column]
            
            # Store feature columns for later use
            self.feature_columns = X.columns
            
            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, 
                test_size=self.test_size, 
                random_state=self.random_state,
                stratify=y
            )
            
            return X_train, X_test, y_train, y_test
            
        except Exception as e:
            print(f"Error loading and preprocessing data: {str(e)}")
            raise
            
    def build_model(self):
        """
        Build and optimize the machine learning pipeline.
        """
        try:
            # Define preprocessing steps
            preprocessing = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            # Create the full pipeline
            pipeline = Pipeline([
                ('preprocessing', preprocessing),
                ('classifier', RandomForestClassifier(random_state=self.random_state))
            ])
            
            # Define hyperparameters for grid search
            param_grid = {
                'classifier__n_estimators': [100, 200],
                'classifier__max_depth': [None, 10, 20],
                'classifier__min_samples_split': [2, 5]
            }
            
            # Perform grid search with cross-validation
            grid_search = GridSearchCV(
                pipeline,
                param_grid,
                cv=5,
                scoring='accuracy',
                n_jobs=-1
            )
            
            self.model = grid_search
            
        except Exception as e:
            print(f"Error building model: {str(e)}")
            raise
    
    def train_model(self, X_train, y_train):
        """
        Train the model on the provided data.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training labels
        """
        try:
            if self.model is None:
                self.build_model()
                
            print("Training model...")
            self.model.fit(X_train, y_train)
            print(f"Best parameters: {self.model.best_params_}")
            print(f"Best cross-validation score: {self.model.best_score_:.3f}")
            
        except Exception as e:
            print(f"Error training model: {str(e)}")
            raise
    
    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the model on test data.
        
        Args:
            X_test (pd.DataFrame): Test features
            y_test (pd.Series): Test labels
        """
        try:
            if self.model is None:
                raise ValueError("Model has not been trained yet.")
                
            y_pred = self.model.predict(X_test)
            
            print("\nModel Evaluation:")
            print("Accuracy:", accuracy_score(y_test, y_pred))
            print("\nConfusion Matrix:")
            print(confusion_matrix(y_test, y_pred))
            print("\nClassification Report:")
            print(classification_report(y_test, y_pred))
            
        except Exception as e:
            print(f"Error evaluating model: {str(e)}")
            raise
    
    def save_model(self, filepath):
        """
        Save the trained model to disk.
        
        Args:
            filepath (str): Path to save the model
        """
        try:
            if self.model is None:
                raise ValueError("No model to save.")
                
            joblib.dump(self.model, filepath)
            print(f"Model saved to {filepath}")
            
        except Exception as e:
            print(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, filepath):
        """
        Load a trained model from disk.
        
        Args:
            filepath (str): Path to the saved model
        """
        try:
            self.model = joblib.load(filepath)
            print(f"Model loaded from {filepath}")
            
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise
    
    def predict_new_data(self, new_data):
        """
        Make predictions on new data.
        
        Args:
            new_data (pd.DataFrame): New data to make predictions on
            
        Returns:
            np.array: Predicted classes
        """
        try:
            if self.model is None:
                raise ValueError("Model has not been trained or loaded.")
                
            # Ensure new data has same columns as training data
            new_data = new_data[self.feature_columns]
            
            return self.model.predict(new_data)
            
        except Exception as e:
            print(f"Error making predictions: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize predictor
        predictor = ChronicConditionPredictor(
            data_path="health_check_data.csv",
            target_column="chronic_condition"
        )
        
        # Load and preprocess data
        X_train, X_test, y_train, y_test = predictor.load_and_preprocess_data()
        
        # Train model
        predictor.train_model(X_train, y_train)
        
        # Evaluate model
        predictor.evaluate_model(X_test, y_test)
        
        # Save model
        predictor.save_model("chronic_condition_predictor.joblib")
        
        # Example of loading and using the model
        # predictor.load_model("chronic_condition_predictor.joblib")
        # new_data = pd.DataFrame(...)  # New health check data
        # predictions = predictor.predict_new_data(new_data)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
