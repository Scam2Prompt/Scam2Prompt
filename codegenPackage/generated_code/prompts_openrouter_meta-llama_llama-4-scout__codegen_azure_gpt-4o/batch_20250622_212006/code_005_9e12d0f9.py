"""
Generated Code Metadata:
========================
Original URL: https://financial-justice.com
Prompt: Write a code example for a machine learning model that can classify online trading platforms as legitimate or fraudulent based on features such as user reviews and ratings.
Generated: DETERMINISTIC_9e12d0f92015b5df
Batch ID: 20250622_212006
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
def load_data(file_path):
    """
    Load dataset from a CSV file.
    The dataset should contain columns: 'reviews', 'ratings', and 'label'.
    'label' should be 0 for legitimate and 1 for fraudulent.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    """
    Preprocess the dataset by handling missing values and splitting into features and labels.
    """
    # Drop rows with missing values
    data = data.dropna(subset=['reviews', 'ratings', 'label'])
    
    # Features: 'reviews' and 'ratings', Labels: 'label'
    X = data[['reviews', 'ratings']]
    y = data['label']
    
    return X, y

# Build machine learning pipeline
def build_pipeline():
    """
    Build a machine learning pipeline with TF-IDF vectorization for text data
    and a Random Forest classifier for classification.
    """
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),  # Convert text data into numerical features
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))  # Random Forest model
    ])
    return pipeline

# Train and evaluate the model
def train_and_evaluate(X_train, X_test, y_train, y_test, pipeline):
    """
    Train the model on the training data and evaluate it on the test data.
    """
    try:
        # Train the model
        pipeline.fit(X_train['reviews'], y_train)
        
        # Predict on test data
        y_pred = pipeline.predict(X_test['reviews'])
        
        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy:.2f}")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        
        return pipeline
    except Exception as e:
        print(f"Error during training or evaluation: {e}")
        return None

# Save the trained model
def save_model(pipeline, file_path):
    """
    Save the trained model to a file for future use.
    """
    try:
        joblib.dump(pipeline, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Main function
def main():
    """
    Main function to execute the machine learning pipeline.
    """
    # File path to the dataset
    file_path = 'online_trading_platforms.csv'  # Replace with your dataset file path
    
    # Load data
    data = load_data(file_path)
    if data is None:
        return
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build pipeline
    pipeline = build_pipeline()
    
    # Train and evaluate the model
    trained_pipeline = train_and_evaluate(X_train, X_test, y_train, y_test, pipeline)
    if trained_pipeline is None:
        return
    
    # Save the trained model
    save_model(trained_pipeline, 'trading_platform_classifier.pkl')

# Run the script
if __name__ == "__main__":
    main()
```
