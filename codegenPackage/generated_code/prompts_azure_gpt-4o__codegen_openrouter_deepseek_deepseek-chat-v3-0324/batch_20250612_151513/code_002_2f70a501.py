"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Generate code to analyze user health data, including symptoms and lifestyle habits, and provide personalized recommendations using Python and a machine learning library like TensorFlow.
Generated: DETERMINISTIC_2f70a501b473bba2
Batch ID: 20250612_151513
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
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report
import joblib
import json
import os

# Constants
DATA_FILE = 'health_data.csv'
MODEL_FILE = 'health_recommendation_model.h5'
SCALER_FILE = 'scaler.pkl'
LABEL_ENCODER_FILE = 'label_encoder.pkl'
CONFIG_FILE = 'config.json'

class HealthDataAnalyzer:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.label_encoder = None
        self.config = None
        
    def load_config(self):
        """Load configuration from JSON file"""
        try:
            with open(CONFIG_FILE, 'r') as f:
                self.config = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading config: {e}")
            return False
    
    def load_data(self):
        """Load and preprocess health data"""
        try:
            data = pd.read_csv(DATA_FILE)
            
            # Handle missing values
            data.fillna(data.mean(numeric_only=True), inplace=True)
            
            # Encode categorical features
            categorical_cols = data.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                if col != 'Recommendation':
                    data[col] = data[col].astype('category').cat.codes
            
            # Separate features and target
            X = data.drop('Recommendation', axis=1)
            y = data['Recommendation']
            
            # Encode target labels
            self.label_encoder = LabelEncoder()
            y_encoded = self.label_encoder.fit_transform(y)
            
            # Scale features
            self.scaler = StandardScaler()
            X_scaled = self.scaler.fit_transform(X)
            
            return X_scaled, y_encoded
        except Exception as e:
            print(f"Error loading data: {e}")
            return None, None
    
    def build_model(self, input_shape, num_classes):
        """Build TensorFlow model"""
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(num_classes, activation='softmax')
        ])
        
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def train_model(self, X, y):
        """Train the recommendation model"""
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Get model parameters from config
            if not self.load_config():
                raise ValueError("Failed to load configuration")
                
            input_shape = X_train.shape[1]
            num_classes = len(np.unique(y))
            
            # Build and train model
            self.model = self.build_model(input_shape, num_classes)
            
            early_stopping = keras.callbacks.EarlyStopping(
                monitor='val_loss', patience=5, restore_best_weights=True
            )
            
            history = self.model.fit(
                X_train, y_train,
                epochs=self.config.get('epochs', 50),
                batch_size=self.config.get('batch_size', 32),
                validation_split=0.1,
                callbacks=[early_stopping],
                verbose=1
            )
            
            # Evaluate model
            test_loss, test_acc = self.model.evaluate(X_test, y_test, verbose=0)
            print(f"Test accuracy: {test_acc:.4f}")
            
            # Save model and artifacts
            self.save_artifacts()
            
            return True
        except Exception as e:
            print(f"Error training model: {e}")
            return False
    
    def save_artifacts(self):
        """Save model and preprocessing artifacts"""
        try:
            self.model.save(MODEL_FILE)
            joblib.dump(self.scaler, SCALER_FILE)
            joblib.dump(self.label_encoder, LABEL_ENCODER_FILE)
            print("Model and artifacts saved successfully")
        except Exception as e:
            print(f"Error saving artifacts: {e}")
    
    def load_artifacts(self):
        """Load saved model and preprocessing artifacts"""
        try:
            if not all(os.path.exists(f) for f in [MODEL_FILE, SCALER_FILE, LABEL_ENCODER_FILE]):
                return False
                
            self.model = keras.models.load_model(MODEL_FILE)
            self.scaler = joblib.load(SCALER_FILE)
            self.label_encoder = joblib.load(LABEL_ENCODER_FILE)
            return True
        except Exception as e:
            print(f"Error loading artifacts: {e}")
            return False
    
    def predict_recommendation(self, user_data):
        """Generate personalized health recommendation"""
        try:
            if not self.load_artifacts():
                raise ValueError("Failed to load model artifacts")
            
            # Convert user data to DataFrame
            user_df = pd.DataFrame([user_data])
            
            # Preprocess input data
            categorical_cols = user_df.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                user_df[col] = user_df[col].astype('category').cat.codes
            
            # Scale features
            X_scaled = self.scaler.transform(user_df)
            
            # Make prediction
            pred_probs = self.model.predict(X_scaled)
            pred_class = np.argmax(pred_probs, axis=1)
            
            # Decode recommendation
            recommendation = self.label_encoder.inverse_transform(pred_class)[0]
            
            return recommendation
        except Exception as e:
            print(f"Error generating recommendation: {e}")
            return None

# Example usage
if __name__ == "__main__":
    analyzer = HealthDataAnalyzer()
    
    # Train model (run once)
    X, y = analyzer.load_data()
    if X is not None and y is not None:
        analyzer.train_model(X, y)
    
    # Example user data (should match training data features)
    example_user = {
        'Age': 35,
        'Gender': 'Male',
        'BMI': 24.5,
        'BloodPressure': 120,
        'Cholesterol': 180,
        'Glucose': 95,
        'Smoking': 'No',
        'Alcohol': 'Occasionally',
        'Exercise': 'Moderate',
        'SleepHours': 7,
        'StressLevel': 'Medium',
        'Diet': 'Balanced'
    }
    
    # Get recommendation
    recommendation = analyzer.predict_recommendation(example_user)
    if recommendation:
        print(f"Personalized Health Recommendation: {recommendation}")
```
