"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Design a college football prediction model using Python and the provided 2025 college football picks data, including the FPI and projected win totals from FanDuel.
Generated: DETERMINISTIC_af0827f9d5e0d34c
Batch ID: 20250622_212817
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib
import os

class CollegeFootballPredictor:
    """
    A machine learning model to predict college football outcomes based on FPI and projected win totals.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the predictor.
        
        Args:
            data_path (str): Path to the CSV file containing the football data.
        """
        self.model = None
        self.scaler = None
        self.features = None
        self.target = None
        self.data_path = data_path or 'college_football_data.csv'
        
    def load_data(self):
        """
        Load and preprocess the football data.
        
        Returns:
            pd.DataFrame: Processed football data.
        """
        try:
            data = pd.read_csv(self.data_path)
            
            # Basic data validation
            required_columns = ['team', 'fpi', 'projected_wins', 'actual_wins']
            if not all(col in data.columns for col in required_columns):
                raise ValueError("Data missing required columns")
                
            # Clean data
            data = data.dropna()
            data = data[data['fpi'].notna() & data['projected_wins'].notna() & data['actual_wins'].notna()]
            
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
            
    def prepare_features(self, data):
        """
        Prepare features and target for model training.
        
        Args:
            data (pd.DataFrame): The football data.
            
        Returns:
            tuple: (X, y) features and target arrays.
        """
        try:
            self.features = data[['fpi', 'projected_wins']]
            self.target = data['actual_wins']
            
            # Scale features
            self.scaler = StandardScaler()
            X_scaled = self.scaler.fit_transform(self.features)
            
            return X_scaled, self.target.values
        except Exception as e:
            print(f"Error preparing features: {e}")
            raise
    
    def train_model(self, X, y):
        """
        Train the prediction model.
        
        Args:
            X (np.array): Features array.
            y (np.array): Target array.
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Initialize and train model
            self.model = RandomForestRegressor(
                n_estimators=100,
                random_state=42,
                max_depth=5,
                min_samples_split=5
            )
            
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            
            print(f"Model trained successfully. MAE: {mae:.2f}, MSE: {mse:.2f}")
            
        except Exception as e:
            print(f"Error training model: {e}")
            raise
    
    def predict(self, fpi, projected_wins):
        """
        Make a prediction for a given team's stats.
        
        Args:
            fpi (float): The team's FPI rating.
            projected_wins (float): The team's projected win total.
            
        Returns:
            float: Predicted actual wins.
        """
        try:
            if self.model is None:
                raise ValueError("Model not trained. Please train the model first.")
                
            # Prepare input
            input_data = np.array([[fpi, projected_wins]])
            scaled_input = self.scaler.transform(input_data)
            
            # Make prediction
            prediction = self.model.predict(scaled_input)
            return prediction[0]
        except Exception as e:
            print(f"Error making prediction: {e}")
            raise
    
    def save_model(self, path='model.pkl'):
        """
        Save the trained model to disk.
        
        Args:
            path (str): Path to save the model.
        """
        try:
            joblib.dump({
                'model': self.model,
                'scaler': self.scaler,
                'features': self.features.columns.tolist()
            }, path)
            print(f"Model saved to {path}")
        except Exception as e:
            print(f"Error saving model: {e}")
            raise
    
    def load_saved_model(self, path='model.pkl'):
        """
        Load a trained model from disk.
        
        Args:
            path (str): Path to the saved model.
        """
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Model file not found at {path}")
                
            saved_data = joblib.load(path)
            self.model = saved_data['model']
            self.scaler = saved_data['scaler']
            self.features = saved_data['features']
            print("Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def run_training_pipeline(self):
        """
        Run the complete training pipeline from data loading to model training.
        """
        try:
            data = self.load_data()
            X, y = self.prepare_features(data)
            self.train_model(X, y)
            self.save_model()
        except Exception as e:
            print(f"Pipeline failed: {e}")
            raise


# Example usage
if __name__ == "__main__":
    predictor = CollegeFootballPredictor()
    
    # Train and save model (run once)
    # predictor.run_training_pipeline()
    
    # Load existing model
    predictor.load_saved_model()
    
    # Make a prediction
    sample_fpi = 10.5
    sample_projected_wins = 8.5
    prediction = predictor.predict(sample_fpi, sample_projected_wins)
    print(f"Predicted actual wins: {prediction:.2f}")
```
