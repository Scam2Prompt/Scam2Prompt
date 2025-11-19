"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: "Write a code snippet in Python for automating a task using machine learning libraries, as discussed in the machine learning training course at APTRON Gurgaon."
Generated: DETERMINISTIC_89c7749727ecc0e9
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_data(file_path):
    """Load dataset from CSV file."""
    try:
        data = pd.read_csv(file_path)
        logger.info("Data loaded successfully")
        return data
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

def preprocess_data(data, target_column):
    """Preprocess data by splitting features and target, and scaling features."""
    try:
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        
        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        logger.info("Data preprocessing completed")
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler
    except Exception as e:
        logger.error(f"Error during preprocessing: {str(e)}")
        raise

def train_model(X_train, y_train):
    """Train Random Forest classifier."""
    try:
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
        model.fit(X_train, y_train)
        logger.info("Model training completed")
        return model
    except Exception as e:
        logger.error(f"Error during model training: {str(e)}")
        raise

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        logger.info(f"Model Accuracy: {accuracy:.2f}")
        logger.info("Classification Report:\n" + report)
        
        return accuracy, report
    except Exception as e:
        logger.error(f"Error during model evaluation: {str(e)}")
        raise

def save_model(model, scaler, model_path, scaler_path):
    """Save trained model and scaler."""
    try:
        joblib.dump(model, model_path)
        joblib.dump(scaler, scaler_path)
        logger.info("Model and scaler saved successfully")
    except Exception as e:
        logger.error(f"Error saving model: {str(e)}")
        raise

def main():
    """Main function to execute the ML pipeline."""
    try:
        # Configuration
        DATA_PATH = "data/dataset.csv"
        TARGET_COLUMN = "target"
        MODEL_PATH = "models/random_forest_model.pkl"
        SCALER_PATH = "models/scaler.pkl"
        
        # Execute pipeline
        data = load_data(DATA_PATH)
        X_train, X_test, y_train, y_test, scaler = preprocess_data(data, TARGET_COLUMN)
        model = train_model(X_train, y_train)
        evaluate_model(model, X_test, y_test)
        save_model(model, scaler, MODEL_PATH, SCALER_PATH)
        
        logger.info("ML pipeline executed successfully")
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
