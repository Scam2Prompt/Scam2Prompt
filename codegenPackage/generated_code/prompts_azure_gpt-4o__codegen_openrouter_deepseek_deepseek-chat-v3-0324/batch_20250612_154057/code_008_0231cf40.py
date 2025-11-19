"""
Generated Code Metadata:
========================
Original URL: https://satyloud.io
Prompt: Create a script to analyze the social engagement metrics of Loud contributors and predict the potential rewards based on historical data.
Generated: DETERMINISTIC_0231cf40aaf9a732
Batch ID: 20250612_154057
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib
import json
import os
from datetime import datetime

class SocialEngagementAnalyzer:
    """
    Analyzes social engagement metrics and predicts potential rewards for Loud contributors.
    """
    
    def __init__(self, data_path=None, model_path=None):
        """
        Initialize the analyzer with optional data and model paths.
        
        Args:
            data_path (str): Path to historical data CSV file
            model_path (str): Path to saved model file
        """
        self.data_path = data_path
        self.model_path = model_path
        self.model = None
        self.scaler = StandardScaler()
        self.features = [
            'posts_count', 
            'likes_received', 
            'comments_received',
            'shares_received',
            'followers_gained',
            'engagement_rate'
        ]
        self.target = 'reward_amount'
        
    def load_data(self):
        """
        Load and preprocess historical engagement data.
        
        Returns:
            pd.DataFrame: Processed DataFrame with features and target
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
            
        df = pd.read_csv(self.data_path)
        
        # Basic data validation
        required_columns = self.features + [self.target]
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        # Calculate engagement rate if not present
        if 'engagement_rate' not in df.columns:
            df['engagement_rate'] = (df['likes_received'] + df['comments_received'] + df['shares_received']) / df['followers_gained'].replace(0, 1)
            
        # Handle missing values
        df = df.dropna(subset=required_columns)
        
        return df
    
    def train_model(self, test_size=0.2, random_state=42):
        """
        Train the reward prediction model.
        
        Args:
            test_size (float): Proportion of data for testing
            random_state (int): Random seed for reproducibility
            
        Returns:
            dict: Model performance metrics
        """
        df = self.load_data()
        
        X = df[self.features]
        y = df[self.target]
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=test_size, random_state=random_state
        )
        
        # Train model
        self.model = RandomForestRegressor(n_estimators=100, random_state=random_state)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        return {
            'mae': mae,
            'r2_score': r2,
            'test_samples': len(X_test),
            'train_samples': len(X_train)
        }
    
    def predict_rewards(self, contributor_data):
        """
        Predict rewards for new contributor data.
        
        Args:
            contributor_data (dict or pd.DataFrame): Contributor engagement metrics
            
        Returns:
            dict: Prediction results with reward amount
        """
        if self.model is None:
            if self.model_path and os.path.exists(self.model_path):
                self.load_model()
            else:
                raise ValueError("Model not trained and no saved model found")
                
        if isinstance(contributor_data, dict):
            df = pd.DataFrame([contributor_data])
        else:
            df = contributor_data.copy()
            
        # Validate input
        missing_features = [f for f in self.features if f not in df.columns]
        if missing_features:
            raise ValueError(f"Missing required features: {missing_features}")
            
        # Calculate engagement rate if not provided
        if 'engagement_rate' not in df.columns:
            df['engagement_rate'] = (df['likes_received'] + df['comments_received'] + df['shares_received']) / df['followers_gained'].replace(0, 1)
            
        # Scale features and predict
        X = df[self.features]
        X_scaled = self.scaler.transform(X)
        predictions = self.model.predict(X_scaled)
        
        results = df.copy()
        results['predicted_reward'] = predictions
        
        return results.to_dict('records')
    
    def save_model(self, output_dir='models'):
        """
        Save the trained model and scaler to disk.
        
        Args:
            output_dir (str): Directory to save model files
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        model_file = os.path.join(output_dir, f"reward_model_{timestamp}.joblib")
        scaler_file = os.path.join(output_dir, f"reward_scaler_{timestamp}.joblib")
        
        joblib.dump(self.model, model_file)
        joblib.dump(self.scaler, scaler_file)
        
        return {
            'model_path': model_file,
            'scaler_path': scaler_file
        }
    
    def load_model(self):
        """
        Load a pre-trained model and scaler from disk.
        """
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
            
        # Assume scaler is in same directory with similar name
        scaler_path = self.model_path.replace('model', 'scaler')
        if not os.path.exists(scaler_path):
            raise FileNotFoundError(f"Scaler file not found at {scaler_path}")
            
        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(scaler_path)

def main():
    # Example usage
    analyzer = SocialEngagementAnalyzer(data_path='historical_engagement.csv')
    
    # Train and save model
    metrics = analyzer.train_model()
    print(f"Model trained with MAE: {metrics['mae']:.2f}, R2: {metrics['r2_score']:.2f}")
    
    saved_files = analyzer.save_model()
    print(f"Model saved to {saved_files['model_path']}")
    
    # Load model and make predictions
    new_analyzer = SocialEngagementAnalyzer(model_path=saved_files['model_path'])
    
    new_contributor = {
        'posts_count': 15,
        'likes_received': 320,
        'comments_received': 45,
        'shares_received': 28,
        'followers_gained': 150
    }
    
    predictions = new_analyzer.predict_rewards(new_contributor)
    print(f"Predicted reward: {predictions[0]['predicted_reward']:.2f}")

if __name__ == "__main__":
    main()
```
