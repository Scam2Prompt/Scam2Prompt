"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Develop a machine learning model to predict worker fatigue and proficiency based on time-series data collected from sewing stations, following OpenSeam's focus on upskilling and reskilling.
Generated: DETERMINISTIC_c89665ac26f760cc
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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib
import warnings
warnings.filterwarnings('ignore')

class FatigueProficiencyPredictor:
    """
    A machine learning model to predict worker fatigue and proficiency based on time-series data.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the predictor.
        
        Args:
            model_path (str, optional): Path to load a pre-trained model. Defaults to None.
        """
        self.model = None
        self.scaler = None
        self.features = None
        self.target = None
        
        if model_path:
            self.load_model(model_path)
    
    def load_data(self, file_path):
        """
        Load and preprocess the time-series data from sewing stations.
        
        Args:
            file_path (str): Path to the CSV file containing the data.
            
        Returns:
            pd.DataFrame: Processed DataFrame ready for training.
        """
        try:
            data = pd.read_csv(file_path)
            
            # Basic preprocessing
            data['timestamp'] = pd.to_datetime(data['timestamp'])
            data = data.sort_values('timestamp')
            
            # Feature engineering
            data['time_elapsed'] = (data['timestamp'] - data['timestamp'].min()).dt.total_seconds() / 3600
            data['stitch_rate'] = data['stitches_completed'] / (data['time_elapsed'] + 1e-6)
            data['error_rate'] = data['errors_detected'] / (data['stitches_completed'] + 1e-6)
            
            # Rolling features
            window_size = 5
            data['stitch_rate_ma'] = data['stitch_rate'].rolling(window=window_size).mean()
            data['error_rate_ma'] = data['error_rate'].rolling(window=window_size).mean()
            
            # Drop rows with NaN values from rolling features
            data = data.dropna()
            
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def prepare_features(self, data):
        """
        Prepare features and target for the model.
        
        Args:
            data (pd.DataFrame): Processed DataFrame from load_data.
            
        Returns:
            tuple: (X, y) features and target arrays.
        """
        try:
            # Define features and target
            features = [
                'time_elapsed', 'stitch_rate', 'error_rate',
                'stitch_rate_ma', 'error_rate_ma'
            ]
            
            # Create target (fatigue: 1 if error_rate > threshold, else 0)
            error_threshold = data['error_rate'].quantile(0.75)
            data['fatigue'] = (data['error_rate'] > error_threshold).astype(int)
            
            # Proficiency based on stitch rate (1 if above median, else 0)
            proficiency_threshold = data['stitch_rate'].median()
            data['proficiency'] = (data['stitch_rate'] > proficiency_threshold).astype(int)
            
            X = data[features]
            y = data[['fatigue', 'proficiency']]
            
            self.features = features
            self.target = ['fatigue', 'proficiency']
            
            return X, y
        except Exception as e:
            raise ValueError(f"Error preparing features: {str(e)}")
    
    def train_model(self, X, y, test_size=0.2, random_state=42):
        """
        Train the Random Forest classifier.
        
        Args:
            X (pd.DataFrame): Features.
            y (pd.DataFrame): Target.
            test_size (float, optional): Test set size. Defaults to 0.2.
            random_state (int, optional): Random seed. Defaults to 42.
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Create pipeline
            pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler()),
                ('classifier', RandomForestClassifier(
                    n_estimators=100,
                    random_state=random_state,
                    class_weight='balanced'
                ))
            ])
            
            # Train model
            pipeline.fit(X_train, y_train)
            
            # Evaluate
            y_pred = pipeline.predict(X_test)
            print("Fatigue Prediction Report:")
            print(classification_report(y_test['fatigue'], y_pred[:, 0]))
            print("\nProficiency Prediction Report:")
            print(classification_report(y_test['proficiency'], y_pred[:, 1]))
            
            self.model = pipeline
            self.scaler = pipeline.named_steps['scaler']
            
        except Exception as e:
            raise ValueError(f"Error training model: {str(e)}")
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Args:
            X (pd.DataFrame): Input features.
            
        Returns:
            np.ndarray: Predictions (fatigue, proficiency).
        """
        if not self.model:
            raise ValueError("Model not trained or loaded. Train or load a model first.")
        
        try:
            return self.model.predict(X)
        except Exception as e:
            raise ValueError(f"Error making predictions: {str(e)}")
    
    def save_model(self, file_path):
        """
        Save the trained model to disk.
        
        Args:
            file_path (str): Path to save the model.
        """
        try:
            joblib.dump({
                'model': self.model,
                'features': self.features,
                'target': self.target
            }, file_path)
        except Exception as e:
            raise ValueError(f"Error saving model: {str(e)}")
    
    def load_model(self, file_path):
        """
        Load a trained model from disk.
        
        Args:
            file_path (str): Path to the saved model.
        """
        try:
            saved_data = joblib.load(file_path)
            self.model = saved_data['model']
            self.features = saved_data['features']
            self.target = saved_data['target']
            self.scaler = self.model.named_steps['scaler']
        except Exception as e:
            raise ValueError(f"Error loading model: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = FatigueProficiencyPredictor()
    
    # Load and prepare data
    try:
        data = predictor.load_data("sewing_station_data.csv")
        X, y = predictor.prepare_features(data)
        
        # Train model
        predictor.train_model(X, y)
        
        # Save model
        predictor.save_model("fatigue_proficiency_model.joblib")
        
        # Example prediction
        sample_data = X.iloc[:5]  # First 5 samples
        predictions = predictor.predict(sample_data)
        print("\nSample Predictions:")
        print(predictions)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
