"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Write a Python script for data classification based on the techniques discussed in the "Classification with Python Live Course" from edukacija.net.
Generated: DETERMINISTIC_8aa61377f209d63c
Batch ID: 20250612_150920
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
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class DataClassifier:
    """
    A class for performing data classification using various machine learning algorithms.
    """
    
    def __init__(self, data_path, target_column, test_size=0.2, random_state=42):
        """
        Initialize the DataClassifier with dataset and parameters.
        
        Args:
            data_path (str): Path to the dataset file
            target_column (str): Name of the target column
            test_size (float): Proportion of dataset to include in test split
            random_state (int): Random seed for reproducibility
        """
        self.data_path = data_path
        self.target_column = target_column
        self.test_size = test_size
        self.random_state = random_state
        self.models = {}
        self.best_model = None
        self.scaler = StandardScaler()
        
        # Load and preprocess data
        self._load_data()
        self._preprocess_data()
        
    def _load_data(self):
        """Load and inspect the dataset."""
        try:
            self.data = pd.read_csv(self.data_path)
            print(f"Dataset loaded successfully with {self.data.shape[0]} rows and {self.data.shape[1]} columns.")
        except Exception as e:
            print(f"Error loading dataset: {e}")
            raise
            
    def _preprocess_data(self):
        """Preprocess the data by splitting into features and target, then scaling."""
        try:
            # Separate features and target
            self.X = self.data.drop(self.target_column, axis=1)
            self.y = self.data[self.target_column]
            
            # Split into train and test sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.X, self.y, test_size=self.test_size, random_state=self.random_state
            )
            
            # Scale features
            self.X_train = self.scaler.fit_transform(self.X_train)
            self.X_test = self.scaler.transform(self.X_test)
            
            print("Data preprocessing completed successfully.")
        except Exception as e:
            print(f"Error during data preprocessing: {e}")
            raise
    
    def train_models(self):
        """Train multiple classification models and store their performance."""
        try:
            # Initialize models
            models = {
                'Logistic Regression': LogisticRegression(max_iter=1000),
                'Decision Tree': DecisionTreeClassifier(),
                'Random Forest': RandomForestClassifier(),
                'SVM': SVC(),
                'KNN': KNeighborsClassifier()
            }
            
            # Train and evaluate each model
            for name, model in models.items():
                model.fit(self.X_train, self.y_train)
                y_pred = model.predict(self.X_test)
                
                # Store model and its metrics
                self.models[name] = {
                    'model': model,
                    'accuracy': accuracy_score(self.y_test, y_pred),
                    'report': classification_report(self.y_test, y_pred),
                    'confusion_matrix': confusion_matrix(self.y_test, y_pred)
                }
                
                print(f"{name} trained with accuracy: {self.models[name]['accuracy']:.4f}")
            
            # Select best model based on accuracy
            self.best_model = max(self.models.items(), key=lambda x: x[1]['accuracy'])
            print(f"\nBest model: {self.best_model[0]} with accuracy {self.best_model[1]['accuracy']:.4f}")
            
        except Exception as e:
            print(f"Error during model training: {e}")
            raise
    
    def tune_best_model(self):
        """Perform hyperparameter tuning on the best performing model."""
        if not self.best_model:
            print("No best model identified. Please train models first.")
            return
            
        try:
            model_name = self.best_model[0]
            model = self.best_model[1]['model']
            
            print(f"\nPerforming hyperparameter tuning for {model_name}...")
            
            # Define parameter grids for different models
            param_grids = {
                'Logistic Regression': {
                    'C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'penalty': ['l1', 'l2'],
                    'solver': ['liblinear']
                },
                'Decision Tree': {
                    'max_depth': [None, 5, 10, 20],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                },
                'Random Forest': {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [None, 5, 10],
                    'min_samples_split': [2, 5]
                },
                'SVM': {
                    'C': [0.1, 1, 10, 100],
                    'kernel': ['linear', 'rbf'],
                    'gamma': ['scale', 'auto']
                },
                'KNN': {
                    'n_neighbors': [3, 5, 7, 9],
                    'weights': ['uniform', 'distance'],
                    'algorithm': ['auto', 'ball_tree', 'kd_tree']
                }
            }
            
            # Get the appropriate parameter grid
            param_grid = param_grids.get(model_name, {})
            
            if not param_grid:
                print(f"No parameter grid defined for {model_name}")
                return
                
            # Perform grid search
            grid_search = GridSearchCV(
                estimator=model,
                param_grid=param_grid,
                cv=5,
                scoring='accuracy',
                n_jobs=-1
            )
            
            grid_search.fit(self.X_train, self.y_train)
            
            # Update best model with tuned parameters
            self.models[model_name]['model'] = grid_search.best_estimator_
            self.best_model = (model_name, self.models[model_name])
            
            print(f"Best parameters: {grid_search.best_params_}")
            print(f"Improved accuracy: {grid_search.best_score_:.4f}")
            
        except Exception as e:
            print(f"Error during hyperparameter tuning: {e}")
            raise
    
    def evaluate_model(self, model_name=None):
        """Evaluate a specific model or the best model if none specified."""
        try:
            if model_name:
                model_info = self.models.get(model_name)
                if not model_info:
                    print(f"Model {model_name} not found.")
                    return
            else:
                if not self.best_model:
                    print("No best model identified.")
                    return
                model_name = self.best_model[0]
                model_info = self.best_model[1]
            
            print(f"\nEvaluation for {model_name}:")
            print(f"Accuracy: {model_info['accuracy']:.4f}")
            print("\nClassification Report:")
            print(model_info['report'])
            print("\nConfusion Matrix:")
            print(model_info['confusion_matrix'])
            
        except Exception as e:
            print(f"Error during model evaluation: {e}")
            raise
    
    def predict(self, new_data):
        """Make predictions using the best model."""
        try:
            if not self.best_model:
                print("No model available for prediction. Please train models first.")
                return None
                
            # Scale the new data
            new_data_scaled = self.scaler.transform(new_data)
            
            # Make predictions
            predictions = self.best_model[1]['model'].predict(new_data_scaled)
            
            return predictions
            
        except Exception as e:
            print(f"Error during prediction: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize classifier with dataset and target column
    classifier = DataClassifier(
        data_path='sample_data.csv',  # Replace with your dataset path
        target_column='target'       # Replace with your target column name
    )
    
    # Train models
    classifier.train_models()
    
    # Tune best model
    classifier.tune_best_model()
    
    # Evaluate best model
    classifier.evaluate_model()
    
    # Example prediction (using test data as new data)
    sample_data = classifier.X_test[:5]  # Normally this would be new unseen data
    predictions = classifier.predict(sample_data)
    print(f"\nSample predictions: {predictions}")
```
