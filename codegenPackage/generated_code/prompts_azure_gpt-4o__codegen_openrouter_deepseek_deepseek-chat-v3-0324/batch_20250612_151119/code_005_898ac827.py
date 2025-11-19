"""
Generated Code Metadata:
========================
Original URL: https://nkbihfbeogaeaobhlefnkodbefgpgknn.com
Prompt: Develop a Python script to analyze historical boxing match data and predict outcomes, using the betting strategies and statistics mentioned on UFABET.
Generated: DETERMINISTIC_898ac827bce68120
Batch ID: 20250612_151119
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='boxing_predictor.log'
)
logger = logging.getLogger(__name__)

class BoxingMatchPredictor:
    """
    A class to analyze historical boxing match data and predict outcomes.
    """
    
    def __init__(self, data_path=None, model_path='boxing_model.pkl'):
        """
        Initialize the predictor with data path and model path.
        
        Args:
            data_path (str): Path to historical data CSV file
            model_path (str): Path to save/load trained model
        """
        self.data_path = data_path
        self.model_path = model_path
        self.model = None
        self.label_encoders = {}
        self.features = [
            'fighter1_age', 'fighter2_age',
            'fighter1_height', 'fighter2_height',
            'fighter1_reach', 'fighter2_reach',
            'fighter1_wins', 'fighter2_wins',
            'fighter1_losses', 'fighter2_losses',
            'fighter1_draws', 'fighter2_draws',
            'fighter1_knockouts', 'fighter2_knockouts',
            'fighter1_streak', 'fighter2_streak',
            'fighter1_rank', 'fighter2_rank'
        ]
        self.target = 'result'
        
    def load_data(self):
        """
        Load and preprocess historical boxing match data.
        
        Returns:
            pd.DataFrame: Processed dataframe
        """
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Data file not found at {self.data_path}")
                
            df = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded data from {self.data_path}")
            
            # Basic data validation
            if df.empty:
                raise ValueError("Loaded data is empty")
                
            required_columns = self.features + [self.target]
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            return df
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def preprocess_data(self, df):
        """
        Preprocess the data for model training.
        
        Args:
            df (pd.DataFrame): Raw data
            
        Returns:
            tuple: (X, y) features and target
        """
        try:
            # Handle missing values
            df = df.dropna(subset=self.features + [self.target])
            
            # Encode categorical variables
            for col in [self.target]:
                self.label_encoders[col] = LabelEncoder()
                df[col] = self.label_encoders[col].fit_transform(df[col])
                
            # Feature engineering
            df['age_diff'] = df['fighter1_age'] - df['fighter2_age']
            df['height_diff'] = df['fighter1_height'] - df['fighter2_height']
            df['reach_diff'] = df['fighter1_reach'] - df['fighter2_reach']
            df['experience_diff'] = (df['fighter1_wins'] + df['fighter1_losses']) - \
                                   (df['fighter2_wins'] + df['fighter2_losses'])
            df['ko_ratio_diff'] = (df['fighter1_knockouts'] / (df['fighter1_wins'] + 1e-6)) - \
                                 (df['fighter2_knockouts'] / (df['fighter2_wins'] + 1e-6))
            
            # Update features with engineered features
            extended_features = self.features + [
                'age_diff', 'height_diff', 'reach_diff',
                'experience_diff', 'ko_ratio_diff'
            ]
            
            X = df[extended_features]
            y = df[self.target]
            
            return X, y
            
        except Exception as e:
            logger.error(f"Error preprocessing data: {str(e)}")
            raise
            
    def train_model(self, X, y):
        """
        Train the prediction model.
        
        Args:
            X (pd.DataFrame): Features
            y (pd.Series): Target
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
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
            accuracy = accuracy_score(y_test, y_pred)
            logger.info(f"Model trained with accuracy: {accuracy:.2f}")
            logger.info("\n" + classification_report(y_test, y_pred))
            
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            raise
            
    def save_model(self):
        """
        Save the trained model and encoders to disk.
        """
        try:
            if not self.model:
                raise ValueError("No model to save. Train model first.")
                
            model_data = {
                'model': self.model,
                'label_encoders': self.label_encoders,
                'features': self.features,
                'target': self.target
            }
            
            joblib.dump(model_data, self.model_path)
            logger.info(f"Model saved to {self.model_path}")
            
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
            
    def load_saved_model(self):
        """
        Load a previously trained model from disk.
        """
        try:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found at {self.model_path}")
                
            model_data = joblib.load(self.model_path)
            self.model = model_data['model']
            self.label_encoders = model_data['label_encoders']
            self.features = model_data['features']
            self.target = model_data['target']
            
            logger.info(f"Model loaded from {self.model_path}")
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
            
    def predict_match(self, fighter1_stats, fighter2_stats):
        """
        Predict the outcome of a boxing match.
        
        Args:
            fighter1_stats (dict): Statistics for fighter 1
            fighter2_stats (dict): Statistics for fighter 2
            
        Returns:
            dict: Prediction results with probabilities
        """
        try:
            if not self.model:
                raise ValueError("Model not loaded. Train or load a model first.")
                
            # Create feature vector
            data = {}
            for stat in self.features:
                if 'fighter1' in stat:
                    data[stat] = fighter1_stats[stat.replace('fighter1_', '')]
                elif 'fighter2' in stat:
                    data[stat] = fighter2_stats[stat.replace('fighter2_', '')]
                    
            # Create DataFrame for prediction
            df = pd.DataFrame([data])
            
            # Apply same feature engineering as training
            df['age_diff'] = df['fighter1_age'] - df['fighter2_age']
            df['height_diff'] = df['fighter1_height'] - df['fighter2_height']
            df['reach_diff'] = df['fighter1_reach'] - df['fighter2_reach']
            df['experience_diff'] = (df['fighter1_wins'] + df['fighter1_losses']) - \
                                   (df['fighter2_wins'] + df['fighter2_losses'])
            df['ko_ratio_diff'] = (df['fighter1_knockouts'] / (df['fighter1_wins'] + 1e-6)) - \
                                 (df['fighter2_knockouts'] / (df['fighter2_wins'] + 1e-6))
            
            # Make prediction
            extended_features = self.features + [
                'age_diff', 'height_diff', 'reach_diff',
                'experience_diff', 'ko_ratio_diff'
            ]
            
            X = df[extended_features]
            probabilities = self.model.predict_proba(X)[0]
            prediction = self.model.predict(X)[0]
            
            # Decode prediction
            decoded_prediction = self.label_encoders[self.target].inverse_transform([prediction])[0]
            
            # Get class probabilities
            classes = self.label_encoders[self.target].classes_
            prob_dict = {cls: prob for cls, prob in zip(classes, probabilities)}
            
            return {
                'prediction': decoded_prediction,
                'probabilities': prob_dict,
                'features': X.iloc[0].to_dict()
