"""
Generated Code Metadata:
========================
Original URL: https://giitechcodes.com.ng
Prompt: Create a machine learning model in Python for classification tasks as outlined in the robotics and machine learning section of GII Tech Codes.
Generated: DETERMINISTIC_d2e6066bbb7f608c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import joblib
import os

class ClassificationModel:
    """
    A machine learning model for classification tasks.
    Supports Random Forest and SVM classifiers with hyperparameter tuning.
    """
    
    def __init__(self, model_type='random_forest', random_state=42):
        """
        Initialize the classification model.
        
        Parameters:
        - model_type: str, either 'random_forest' or 'svm' (default: 'random_forest')
        - random_state: int, random seed for reproducibility (default: 42)
        """
        self.model_type = model_type
        self.random_state = random_state
        self.model = None
        self.scaler = StandardScaler()
        self.best_params_ = None
        
    def load_data(self, file_path, target_column, test_size=0.2):
        """
        Load and preprocess data from a CSV file.
        
        Parameters:
        - file_path: str, path to the CSV file
        - target_column: str, name of the target column
        - test_size: float, proportion of data to use for testing (default: 0.2)
        
        Returns:
        - X_train, X_test, y_train, y_test: split datasets
        """
        try:
            data = pd.read_csv(file_path)
            X = data.drop(columns=[target_column])
            y = data[target_column]
            
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=self.random_state
            )
            
            # Scale features
            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)
            
            return X_train, X_test, y_train, y_test
            
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def train(self, X_train, y_train, cv=5):
        """
        Train the classification model with hyperparameter tuning.
        
        Parameters:
        - X_train: array-like, training features
        - y_train: array-like, training labels
        - cv: int, number of cross-validation folds (default: 5)
        """
        try:
            if self.model_type == 'random_forest':
                param_grid = {
                    'n_estimators': [100, 200, 300],
                    'max_depth': [None, 10, 20, 30],
                    'min_samples_split': [2, 5, 10]
                }
                base_model = RandomForestClassifier(random_state=self.random_state)
            elif self.model_type == 'svm':
                param_grid = {
                    'C': [0.1, 1, 10, 100],
                    'gamma': [1, 0.1, 0.01, 0.001],
                    'kernel': ['rbf', 'linear']
                }
                base_model = SVC(random_state=self.random_state)
            else:
                raise ValueError("Invalid model_type. Choose 'random_forest' or 'svm'.")
            
            # Perform grid search with cross-validation
            grid_search = GridSearchCV(
                estimator=base_model,
                param_grid=param_grid,
                cv=cv,
                n_jobs=-1,
                verbose=1
            )
            
            grid_search.fit(X_train, y_train)
            self.model = grid_search.best_estimator_
            self.best_params_ = grid_search.best_params_
            
        except Exception as e:
            raise Exception(f"Error during training: {str(e)}")
    
    def evaluate(self, X_test, y_test):
        """
        Evaluate the model on test data.
        
        Parameters:
        - X_test: array-like, test features
        - y_test: array-like, test labels
        
        Returns:
        - dict containing evaluation metrics
        """
        try:
            y_pred = self.model.predict(X_test)
            
            metrics = {
                'accuracy': accuracy_score(y_test, y_pred),
                'confusion_matrix': confusion_matrix(y_test, y_pred),
                'classification_report': classification_report(y_test, y_pred, output_dict=True)
            }
            
            return metrics
            
        except Exception as e:
            raise Exception(f"Error during evaluation: {str(e)}")
    
    def save_model(self, model_dir='saved_models'):
        """
        Save the trained model and scaler to disk.
        
        Parameters:
        - model_dir: str, directory to save the model (default: 'saved_models')
        """
        try:
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)
            
            model_path = os.path.join(model_dir, f'{self.model_type}_model.pkl')
            scaler_path = os.path.join(model_dir, 'scaler.pkl')
            
            joblib.dump(self.model, model_path)
            joblib.dump(self.scaler, scaler_path)
            
        except Exception as e:
            raise Exception(f"Error saving model: {str(e)}")
    
    def load_model(self, model_dir='saved_models'):
        """
        Load a trained model and scaler from disk.
        
        Parameters:
        - model_dir: str, directory containing the saved model (default: 'saved_models')
        """
        try:
            model_path = os.path.join(model_dir, f'{self.model_type}_model.pkl')
            scaler_path = os.path.join(model_dir, 'scaler.pkl')
            
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Parameters:
        - X: array-like, input features
        
        Returns:
        - array of predicted labels
        """
        try:
            X_scaled = self.scaler.transform(X)
            return self.model.predict(X_scaled)
            
        except Exception as e:
            raise Exception(f"Error during prediction: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize model
    model = ClassificationModel(model_type='random_forest')
    
    # Load data
    try:
        X_train, X_test, y_train, y_test = model.load_data(
            'sample_data.csv', 
            target_column='target'
        )
        
        # Train model
        model.train(X_train, y_train)
        
        # Evaluate model
        metrics = model.evaluate(X_test, y_test)
        print(f"Model Accuracy: {metrics['accuracy']}")
        print("Classification Report:")
        print(metrics['classification_report'])
        
        # Save model
        model.save_model()
        
        # Example prediction
        sample_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Example feature vector
        prediction = model.predict(sample_data)
        print(f"Prediction: {prediction}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
