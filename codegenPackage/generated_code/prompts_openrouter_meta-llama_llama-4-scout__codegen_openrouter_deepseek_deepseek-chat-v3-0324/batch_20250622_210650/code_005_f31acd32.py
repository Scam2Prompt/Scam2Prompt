"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Develop a machine learning model in Python to predict patient dropout rates in DBT therapy based on demographic and clinical factors."
Generated: DETERMINISTIC_f31acd324250b68c
Batch ID: 20250622_210650
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
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer
import joblib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class DBTDropoutPredictor:
    """
    A machine learning model to predict patient dropout rates in DBT therapy.
    """
    
    def __init__(self):
        """
        Initialize the model with default parameters.
        """
        self.model = None
        self.preprocessor = None
        self.feature_columns = None
        self.target_column = None
        
    def load_data(self, filepath):
        """
        Load data from a CSV file.
        
        Args:
            filepath (str): Path to the CSV file containing the data.
            
        Returns:
            pd.DataFrame: Loaded data as a pandas DataFrame.
        """
        try:
            data = pd.read_csv(filepath)
            return data
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def preprocess_data(self, data, target_column='dropout'):
        """
        Preprocess the data by handling missing values, encoding categorical variables,
        and scaling numerical features.
        
        Args:
            data (pd.DataFrame): Input data.
            target_column (str): Name of the target column.
            
        Returns:
            tuple: (X_processed, y_processed) - Processed features and target.
        """
        try:
            # Separate features and target
            X = data.drop(columns=[target_column])
            y = data[target_column]
            self.target_column = target_column
            self.feature_columns = X.columns.tolist()
            
            # Identify numerical and categorical columns
            numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
            categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
            
            # Create preprocessing pipeline
            numerical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            categorical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])
            
            self.preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_transformer, numerical_cols),
                    ('cat', categorical_transformer, categorical_cols)
                ])
            
            # Fit and transform the data
            X_processed = self.preprocessor.fit_transform(X)
            return X_processed, y
            
        except Exception as e:
            raise Exception(f"Error preprocessing data: {str(e)}")
    
    def train_model(self, X, y, test_size=0.2, random_state=42):
        """
        Train a RandomForestClassifier model.
        
        Args:
            X (array-like): Processed features.
            y (array-like): Target values.
            test_size (float): Proportion of data to use for testing.
            random_state (int): Random seed for reproducibility.
            
        Returns:
            tuple: (model, X_test, y_test) - Trained model and test data.
        """
        try:
            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Initialize and train the model
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=random_state,
                class_weight='balanced'
            )
            
            self.model.fit(X_train, y_train)
            
            return X_test, y_test
            
        except Exception as e:
            raise Exception(f"Error training model: {str(e)}")
    
    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the model performance on test data.
        
        Args:
            X_test (array-like): Test features.
            y_test (array-like): True labels for test data.
            
        Returns:
            dict: Dictionary containing evaluation metrics.
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
            raise Exception(f"Error evaluating model: {str(e)}")
    
    def predict(self, new_data):
        """
        Make predictions on new data.
        
        Args:
            new_data (pd.DataFrame): New data to make predictions on.
            
        Returns:
            np.array: Predicted probabilities for dropout.
        """
        try:
            if not isinstance(new_data, pd.DataFrame):
                new_data = pd.DataFrame(new_data, columns=self.feature_columns)
            
            # Preprocess the new data
            processed_data = self.preprocessor.transform(new_data)
            
            # Make predictions
            predictions = self.model.predict_proba(processed_data)[:, 1]
            return predictions
            
        except Exception as e:
            raise Exception(f"Error making predictions: {str(e)}")
    
    def save_model(self, filepath):
        """
        Save the trained model and preprocessor to disk.
        
        Args:
            filepath (str): Path to save the model.
        """
        try:
            joblib.dump({
                'model': self.model,
                'preprocessor': self.preprocessor,
                'feature_columns': self.feature_columns,
                'target_column': self.target_column
            }, filepath)
        except Exception as e:
            raise Exception(f"Error saving model: {str(e)}")
    
    def load_model(self, filepath):
        """
        Load a trained model from disk.
        
        Args:
            filepath (str): Path to the saved model.
        """
        try:
            saved_data = joblib.load(filepath)
            self.model = saved_data['model']
            self.preprocessor = saved_data['preprocessor']
            self.feature_columns = saved_data['feature_columns']
            self.target_column = saved_data['target_column']
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the predictor
        predictor = DBTDropoutPredictor()
        
        # Load and preprocess data (replace with actual data path)
        data = predictor.load_data('patient_data.csv')
        X, y = predictor.preprocess_data(data)
        
        # Train the model
        X_test, y_test = predictor.train_model(X, y)
        
        # Evaluate the model
        metrics = predictor.evaluate_model(X_test, y_test)
        print(f"Model Accuracy: {metrics['accuracy']:.2f}")
        print("\nClassification Report:")
        print(classification_report(y_test, predictor.model.predict(X_test)))
        
        # Save the model
        predictor.save_model('dbt_dropout_predictor.joblib')
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
