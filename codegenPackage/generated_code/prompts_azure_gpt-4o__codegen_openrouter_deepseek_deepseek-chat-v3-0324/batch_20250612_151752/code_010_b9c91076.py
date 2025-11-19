"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Develop a Python script to track and optimize the performance of Kraken Media’s creative video ads, leveraging consumer psychology insights to improve click-through rates.
Generated: DETERMINISTIC_b9c91076ec42b6d1
Batch ID: 20250612_151752
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
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import json
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='ad_performance_tracker.log'
)
logger = logging.getLogger(__name__)

class AdPerformanceOptimizer:
    """
    A class to track and optimize video ad performance using consumer psychology insights.
    """
    
    def __init__(self, data_path='ad_performance_data.csv', model_path='ad_model.pkl'):
        """
        Initialize the optimizer with data and model paths.
        
        Args:
            data_path (str): Path to the ad performance data CSV file.
            model_path (str): Path to save/load the trained model.
        """
        self.data_path = data_path
        self.model_path = model_path
        self.model = None
        self.scaler = StandardScaler()
        self.features = [
            'duration', 'color_intensity', 'emotional_score', 
            'cta_clarity', 'social_proof', 'urgency_level'
        ]
        self.target = 'clicked'
        
    def load_data(self):
        """
        Load and preprocess the ad performance data.
        
        Returns:
            pd.DataFrame: Processed DataFrame with features and target.
        """
        try:
            df = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded data from {self.data_path}")
            
            # Basic data validation
            if df.empty:
                raise ValueError("Data file is empty")
                
            # Ensure required columns exist
            missing_cols = [col for col in self.features + [self.target] if col not in df.columns]
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
            df (pd.DataFrame): Raw input data.
            
        Returns:
            tuple: (X_train, X_test, y_train, y_test) split data.
        """
        try:
            # Handle missing values
            df = df.dropna(subset=self.features + [self.target])
            
            # Feature scaling
            X = df[self.features]
            y = df[self.target]
            
            X_scaled = self.scaler.fit_transform(X)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y, test_size=0.2, random_state=42
            )
            
            logger.info("Data preprocessing completed successfully")
            return X_train, X_test, y_train, y_test
            
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
            
    def train_model(self, X_train, y_train):
        """
        Train the Random Forest classifier.
        
        Args:
            X_train (np.array): Training features.
            y_train (np.array): Training target.
        """
        try:
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                class_weight='balanced'
            )
            
            self.model.fit(X_train, y_train)
            logger.info("Model training completed successfully")
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
            
    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the model performance.
        
        Args:
            X_test (np.array): Test features.
            y_test (np.array): Test target.
            
        Returns:
            dict: Evaluation metrics.
        """
        try:
            y_pred = self.model.predict(X_test)
            
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            
            metrics = {
                'accuracy': accuracy,
                'precision': report['weighted avg']['precision'],
                'recall': report['weighted avg']['recall'],
                'f1_score': report['weighted avg']['f1-score'],
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Model evaluation completed. Accuracy: {accuracy:.2f}")
            return metrics
            
        except Exception as e:
            logger.error(f"Error during model evaluation: {str(e)}")
            raise
            
    def save_model(self):
        """
        Save the trained model and scaler to disk.
        """
        try:
            if not self.model:
                raise ValueError("No model to save. Train the model first.")
                
            model_data = {
                'model': self.model,
                'scaler': self.scaler,
                'features': self.features,
                'target': self.target
            }
            
            joblib.dump(model_data, self.model_path)
            logger.info(f"Model saved successfully to {self.model_path}")
            
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
            
    def load_saved_model(self):
        """
        Load a previously saved model from disk.
        """
        try:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found at {self.model_path}")
                
            model_data = joblib.load(self.model_path)
            
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.features = model_data['features']
            self.target = model_data['target']
            
            logger.info(f"Model loaded successfully from {self.model_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            return False
            
    def predict_optimal_ad(self, ad_features):
        """
        Predict the optimal ad features for maximum click-through rate.
        
        Args:
            ad_features (dict): Dictionary of ad features to optimize.
            
        Returns:
            dict: Optimized ad features with predicted CTR.
        """
        try:
            if not self.model:
                raise ValueError("Model not loaded. Train or load a model first.")
                
            # Prepare input features
            input_data = pd.DataFrame([ad_features])
            missing_cols = [col for col in self.features if col not in input_data.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required features: {missing_cols}")
                
            # Scale features
            input_scaled = self.scaler.transform(input_data[self.features])
            
            # Predict probability
            proba = self.model.predict_proba(input_scaled)[0][1]
            
            # Generate recommendations based on consumer psychology
            recommendations = self._generate_recommendations(ad_features, proba)
            
            result = {
                'current_ctr_probability': float(proba),
                'recommendations': recommendations,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Prediction completed for ad features: {ad_features}")
            return result
            
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise
            
    def _generate_recommendations(self, ad_features, current_prob):
        """
        Generate consumer psychology-based recommendations to improve CTR.
        
        Args:
            ad_features (dict): Current ad features.
            current_prob (float): Current predicted CTR probability.
            
        Returns:
            list: List of recommendation dictionaries.
        """
        recommendations = []
        
        # Color intensity recommendation
        if ad_features['color_intensity'] < 0.7:
            recommendations.append({
                'feature': 'color_intensity',
                'suggestion': 'Increase color intensity by 20-30% to attract more attention',
                'expected_impact': 'Moderate increase in CTR'
            })
            
        # Emotional score recommendation
        if ad_features['emotional_score'] < 0.6:
            recommendations.append({
                'feature': 'emotional_score',
                'suggestion': 'Incorporate more emotional triggers (e.g., happiness, surprise)',
                'expected_impact': 'High increase in CTR'
            })
            
        # Social proof recommendation
        if ad_features['social_proof'] < 0.5:
            recommendations.append({
                'feature': 'social_proof',
                'suggestion': 'Add testimonials or user count to build trust',
                'expected_impact': 'Moderate increase in CTR'
            })
            
        # Urgency recommendation
        if ad_features['urgency_level'] < 0.4:
            recommendations.append({
                'feature': 'urgency_level',
                'suggestion': 'Add time-sensitive language or limited-time offers',
                'expected_impact': 'Moderate increase in CTR'
            })
            
        # Duration recommendation
        if ad_features['duration'] > 30:
            recommendations.append({
                'feature': 'duration',
                'suggestion': 'Reduce duration to under 30 seconds for better retention',
                'expected_impact': 'Small increase in CTR'
            })
            
        return recommendations
        
    def run_pipeline
