"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Create a Python script that analyzes sewing machine downtime data and predicts inefficiencies in production lines, inspired by OpenSeam's approach to capturing lost time.
Generated: DETERMINISTIC_9d127dfcada09fcc
Batch ID: 20250612_150323
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
import json
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sewing_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SewingMachineAnalyzer:
    """
    Analyzes sewing machine downtime data and predicts production inefficiencies.
    """
    
    def __init__(self, data_path=None, model_path=None):
        """
        Initialize the analyzer with optional data and model paths.
        
        Args:
            data_path (str): Path to CSV file containing sewing machine data
            model_path (str): Path to pre-trained model (optional)
        """
        self.data_path = data_path
        self.model_path = model_path
        self.model = None
        self.scaler = StandardScaler()
        self.features = None
        self.target = None
        
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
    
    def load_data(self, data_path=None):
        """
        Load and preprocess sewing machine data from CSV.
        
        Args:
            data_path (str): Path to CSV file. Uses instance path if None.
            
        Returns:
            pd.DataFrame: Processed DataFrame
        """
        try:
            path = data_path if data_path else self.data_path
            if not path:
                raise ValueError("No data path provided")
                
            logger.info(f"Loading data from {path}")
            df = pd.read_csv(path)
            
            # Basic data validation
            required_columns = {
                'timestamp', 'machine_id', 'status', 'downtime_minutes',
                'operator_id', 'operation_type', 'material_type'
            }
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert timestamp to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Feature engineering
            df['hour_of_day'] = df['timestamp'].dt.hour
            df['day_of_week'] = df['timestamp'].dt.dayofweek
            df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
            
            # Calculate cumulative downtime per machine
            df['cumulative_downtime'] = df.groupby('machine_id')['downtime_minutes'].cumsum()
            
            # One-hot encode categorical variables
            categorical_cols = ['operation_type', 'material_type', 'status']
            df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
            
            self.features = df.drop(columns=['timestamp', 'downtime_minutes'])
            self.target = df['downtime_minutes']
            
            return df
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def train_model(self, test_size=0.2, random_state=42):
        """
        Train a Random Forest model to predict downtime.
        
        Args:
            test_size (float): Proportion of data for testing
            random_state (int): Random seed for reproducibility
        """
        try:
            if self.features is None or self.target is None:
                raise ValueError("No data loaded. Call load_data() first.")
                
            logger.info("Training model...")
            
            # Scale features
            X_scaled = self.scaler.fit_transform(self.features)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, self.target, test_size=test_size, random_state=random_state
            )
            
            # Initialize and train model
            self.model = RandomForestRegressor(
                n_estimators=100,
                max_depth=10,
                random_state=random_state,
                n_jobs=-1
            )
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            
            logger.info(f"Model trained. MAE: {mae:.2f}, RMSE: {rmse:.2f}")
            
            return mae, rmse
            
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            raise
    
    def predict_downtime(self, input_data):
        """
        Predict downtime for new data.
        
        Args:
            input_data (dict or pd.DataFrame): Input data for prediction
            
        Returns:
            float: Predicted downtime in minutes
        """
        try:
            if self.model is None:
                raise ValueError("Model not trained. Call train_model() first.")
                
            # Convert dict to DataFrame if needed
            if isinstance(input_data, dict):
                input_df = pd.DataFrame([input_data])
            else:
                input_df = input_data.copy()
                
            # Apply same preprocessing as training data
            input_df['timestamp'] = pd.to_datetime(input_df['timestamp'])
            input_df['hour_of_day'] = input_df['timestamp'].dt.hour
            input_df['day_of_week'] = input_df['timestamp'].dt.dayofweek
            input_df['is_weekend'] = input_df['day_of_week'].isin([5, 6]).astype(int)
            
            # One-hot encode categorical variables
            categorical_cols = ['operation_type', 'material_type', 'status']
            input_df = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)
            
            # Ensure all expected columns are present
            missing_cols = set(self.features.columns) - set(input_df.columns)
            for col in missing_cols:
                input_df[col] = 0
                
            # Reorder columns to match training data
            input_df = input_df[self.features.columns]
            
            # Scale features and predict
            X_scaled = self.scaler.transform(input_df)
            prediction = self.model.predict(X_scaled)
            
            return prediction[0]
            
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            raise
    
    def save_model(self, output_path):
        """
        Save the trained model and scaler to disk.
        
        Args:
            output_path (str): Path to save the model
        """
        try:
            if not self.model:
                raise ValueError("No model to save. Train a model first.")
                
            model_data = {
                'model': self.model,
                'scaler': self.scaler,
                'features': list(self.features.columns),
                'timestamp': datetime.now().isoformat()
            }
            
            joblib.dump(model_data, output_path)
            logger.info(f"Model saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, model_path):
        """
        Load a pre-trained model from disk.
        
        Args:
            model_path (str): Path to the saved model
        """
        try:
            model_data = joblib.load(model_path)
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.features = pd.DataFrame(columns=model_data['features'])
            logger.info(f"Model loaded from {model_path}")
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def analyze_production_line(self, data_path=None):
        """
        Analyze production line efficiency and identify top inefficiency causes.
        
        Args:
            data_path (str): Path to data file. Uses instance path if None.
            
        Returns:
            dict: Analysis results with inefficiency insights
        """
        try:
            df = self.load_data(data_path)
            
            # Group by machine and calculate stats
            machine_stats = df.groupby('machine_id').agg({
                'downtime_minutes': ['sum', 'mean', 'count'],
                'status_Active': 'mean'
            }).reset_index()
            
            machine_stats.columns = [
                'machine_id', 'total_downtime', 'avg_downtime',
                'operation_count', 'uptime_ratio'
            ]
            
            # Identify worst performers
            worst_machines = machine_stats.sort_values(
                'total_downtime', ascending=False
            ).head(5)
            
            # Analyze by operation type
            if 'operation_type_Thread Change' in df.columns:
                thread_change_downtime = df[df['operation_type_Thread Change'] == 1]['downtime_minutes'].sum()
            else:
                thread_change_downtime = 0
                
            # Prepare results
            results = {
                'total_downtime_minutes': machine_stats
