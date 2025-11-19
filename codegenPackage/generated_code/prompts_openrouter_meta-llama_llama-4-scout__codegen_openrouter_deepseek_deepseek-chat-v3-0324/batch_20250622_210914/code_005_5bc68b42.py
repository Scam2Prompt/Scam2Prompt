"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: How can machine learning models be used to predict the effectiveness of programs like Kibera Hamlets' Girl Empowerment Programme in reducing early marriage and teenage pregnancy rates?
Generated: DETERMINISTIC_5bc68b42151b57cb
Batch ID: 20250622_210914
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import joblib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ProgramEffectivenessPredictor:
    """
    A machine learning model to predict the effectiveness of empowerment programs
    in reducing early marriage and teenage pregnancy rates.
    """
    
    def __init__(self):
        self.model = None
        self.scaler = None
        self.label_encoders = {}
        self.imputer = None
        
    def load_data(self, file_path):
        """
        Load and preprocess the dataset.
        
        Args:
            file_path (str): Path to the CSV file containing the data
            
        Returns:
            pd.DataFrame: Processed dataframe
        """
        try:
            # Load data
            data = pd.read_csv(file_path)
            
            # Basic preprocessing
            data = self._preprocess_data(data)
            
            return data
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def _preprocess_data(self, data):
        """
        Preprocess the data by handling missing values, encoding categorical variables,
        and scaling numerical features.
        
        Args:
            data (pd.DataFrame): Raw input data
            
        Returns:
            pd.DataFrame: Processed data
        """
        # Handle missing values
        self.imputer = SimpleImputer(strategy='median')
        numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
        data[numeric_cols] = self.imputer.fit_transform(data[numeric_cols])
        
        # Encode categorical variables
        for col in data.select_dtypes(include=['object']).columns:
            if col != 'effectiveness':  # Skip target variable if it's categorical
                self.label_encoders[col] = LabelEncoder()
                data[col] = self.label_encoders[col].fit_transform(data[col])
        
        return data
    
    def train_model(self, data, target_col='effectiveness'):
        """
        Train a Random Forest classifier to predict program effectiveness.
        
        Args:
            data (pd.DataFrame): Processed dataset
            target_col (str): Name of the target column
            
        Returns:
            bool: True if training succeeds, False otherwise
        """
        try:
            # Split data into features and target
            X = data.drop(columns=[target_col])
            y = data[target_col]
            
            # Split into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Scale numerical features
            self.scaler = StandardScaler()
            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)
            
            # Initialize and train model
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                class_weight='balanced'
            )
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            print("Model Evaluation:")
            print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            print("\nClassification Report:")
            print(classification_report(y_test, y_pred))
            print("\nConfusion Matrix:")
            print(confusion_matrix(y_test, y_pred))
            
            return True
        except Exception as e:
            print(f"Error training model: {str(e)}")
            return False
    
    def predict_effectiveness(self, new_data):
        """
        Predict the effectiveness of a new program.
        
        Args:
            new_data (pd.DataFrame): Data for the new program
            
        Returns:
            np.ndarray: Predicted effectiveness values
        """
        try:
            # Preprocess new data
            new_data = self._preprocess_data(new_data.copy())
            
            # Scale features
            new_data_scaled = self.scaler.transform(new_data)
            
            # Make prediction
            predictions = self.model.predict(new_data_scaled)
            
            return predictions
        except Exception as e:
            print(f"Error making prediction: {str(e)}")
            return None
    
    def save_model(self, model_path):
        """
        Save the trained model and preprocessing objects.
        
        Args:
            model_path (str): Path to save the model
        """
        try:
            joblib.dump({
                'model': self.model,
                'scaler': self.scaler,
                'label_encoders': self.label_encoders,
                'imputer': self.imputer
            }, model_path)
            print(f"Model saved successfully to {model_path}")
        except Exception as e:
            print(f"Error saving model: {str(e)}")
    
    def load_saved_model(self, model_path):
        """
        Load a previously saved model.
        
        Args:
            model_path (str): Path to the saved model
        """
        try:
            saved_objects = joblib.load(model_path)
            self.model = saved_objects['model']
            self.scaler = saved_objects['scaler']
            self.label_encoders = saved_objects['label_encoders']
            self.imputer = saved_objects['imputer']
            print(f"Model loaded successfully from {model_path}")
        except Exception as e:
            print(f"Error loading model: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = ProgramEffectivenessPredictor()
    
    # Load and preprocess data (replace with actual data path)
    data = predictor.load_data("program_data.csv")
    
    if data is not None:
        # Train model
        predictor.train_model(data)
        
        # Save model
        predictor.save_model("program_effectiveness_model.joblib")
        
        # Example prediction with new data
        new_program_data = pd.DataFrame({
            'program_duration': [12],
            'community_engagement': ['high'],
            'education_component': ['yes'],
            'economic_empowerment': ['yes'],
            'mentorship': ['yes'],
            'baseline_marriage_rate': [25.5],
            'baseline_pregnancy_rate': [30.2]
        })
        
        prediction = predictor.predict_effectiveness(new_program_data)
        print(f"\nPredicted effectiveness: {prediction[0]}")
```
