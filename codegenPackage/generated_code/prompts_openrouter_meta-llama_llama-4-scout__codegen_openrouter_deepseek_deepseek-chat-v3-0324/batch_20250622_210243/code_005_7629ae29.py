"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Develop a predictive model using machine learning to forecast demand for logistics services in Costa Rica, based on historical data and trends, as PLM might use to optimize their operations."
Generated: DETERMINISTIC_7629ae29f109be55
Batch ID: 20250622_210243
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import warnings
warnings.filterwarnings('ignore')

class DemandForecaster:
    """
    A machine learning model to forecast demand for logistics services in Costa Rica.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the DemandForecaster.
        
        Args:
            data_path (str): Path to the historical data CSV file.
        """
        self.model = None
        self.scaler = None
        self.features = None
        self.target = None
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path):
        """
        Load and preprocess historical demand data.
        
        Args:
            data_path (str): Path to the historical data CSV file.
        """
        try:
            # Load data
            self.data = pd.read_csv(data_path)
            
            # Basic preprocessing
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data.set_index('date', inplace=True)
            
            # Feature engineering (example features - adjust based on actual data)
            self.data['month'] = self.data.index.month
            self.data['quarter'] = self.data.index.quarter
            self.data['year'] = self.data.index.year
            self.data['day_of_week'] = self.data.index.dayofweek
            
            # Define features and target
            self.features = ['month', 'quarter', 'year', 'day_of_week', 'prev_demand', 'economic_index']
            self.target = 'demand'
            
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def train_model(self):
        """
        Train the predictive model using Random Forest Regressor.
        """
        if not hasattr(self, 'data'):
            raise Exception("No data loaded. Please load data first.")
        
        try:
            # Prepare data
            X = self.data[self.features]
            y = self.data[self.target]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Create pipeline with scaling and model
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', RandomForestRegressor(random_state=42))
            ])
            
            # Hyperparameter tuning
            param_grid = {
                'model__n_estimators': [100, 200],
                'model__max_depth': [None, 10, 20],
                'model__min_samples_split': [2, 5]
            }
            
            grid_search = GridSearchCV(
                pipeline, param_grid, cv=5, scoring='neg_mean_squared_error'
            )
            
            # Train model
            grid_search.fit(X_train, y_train)
            
            # Store best model
            self.model = grid_search.best_estimator_
            self.scaler = self.model.named_steps['scaler']
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            
            print(f"Model trained successfully. MAE: {mae:.2f}, MSE: {mse:.2f}")
            
        except Exception as e:
            raise Exception(f"Error training model: {str(e)}")
    
    def predict(self, input_data):
        """
        Make a demand prediction based on input features.
        
        Args:
            input_data (dict or DataFrame): Input features for prediction.
            
        Returns:
            float: Predicted demand value.
        """
        if self.model is None:
            raise Exception("Model not trained. Please train the model first.")
        
        try:
            # Convert input to DataFrame if it's a dict
            if isinstance(input_data, dict):
                input_df = pd.DataFrame([input_data])
            else:
                input_df = input_data.copy()
            
            # Ensure all required features are present
            missing_features = set(self.features) - set(input_df.columns)
            if missing_features:
                raise ValueError(f"Missing required features: {missing_features}")
            
            # Select and order features correctly
            input_df = input_df[self.features]
            
            # Make prediction
            prediction = self.model.predict(input_df)
            
            return prediction[0] if len(prediction) == 1 else prediction
        
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")
    
    def save_model(self, filepath):
        """
        Save the trained model to a file.
        
        Args:
            filepath (str): Path to save the model.
        """
        try:
            joblib.dump(self.model, filepath)
            print(f"Model saved successfully to {filepath}")
        except Exception as e:
            raise Exception(f"Error saving model: {str(e)}")
    
    def load_model(self, filepath):
        """
        Load a trained model from a file.
        
        Args:
            filepath (str): Path to the saved model file.
        """
        try:
            self.model = joblib.load(filepath)
            print(f"Model loaded successfully from {filepath}")
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize forecaster
    forecaster = DemandForecaster()
    
    try:
        # Load data (replace with actual path)
        forecaster.load_data("historical_demand_data.csv")
        
        # Train model
        forecaster.train_model()
        
        # Save model
        forecaster.save_model("demand_forecaster_model.joblib")
        
        # Example prediction
        input_features = {
            'month': 6,
            'quarter': 2,
            'year': 2023,
            'day_of_week': 2,
            'prev_demand': 1500,
            'economic_index': 1.2
        }
        
        prediction = forecaster.predict(input_features)
        print(f"Predicted demand: {prediction:.2f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
