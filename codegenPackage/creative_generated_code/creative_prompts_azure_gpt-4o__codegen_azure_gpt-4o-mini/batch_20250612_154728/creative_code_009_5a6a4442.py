"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xxpp.org
Prompt: Suggest an approach to integrate the "心魄小说网" novel data into a personalized recommendation system using machine learning libraries like TensorFlow or Scikit-learn.
Generated: DETERMINISTIC_5a6a4442bf4fec9f
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Function to load novel data from a CSV file
def load_data(file_path):
    """
    Load novel data from a CSV file.
    
    Args:
    - file_path (str): The path to the CSV file containing novel data.
    
    Returns:
    - DataFrame: A Pandas DataFrame containing the novel data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Function to preprocess the data
def preprocess_data(data):
    """
    Preprocess the novel data for modeling.
    
    Args:
    - data (DataFrame): The DataFrame containing raw data.
    
    Returns:
    - X (array): Features for the model (TF-IDF vectors).
    - y (array): Labels for the model (encoded genres).
    """
    # Vectorizing the novel descriptions using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['description']).toarray()
    
    # Encoding the genres
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(data['genre'])
    
    return X, y

# Function to build a machine learning model
def build_model(X_train, y_train):
    """
    Build and train a Random Forest classifier on the training data.
    
    Args:
    - X_train (array): Feature data for training.
    - y_train (array): Label data for training.
    
    Returns:
    - model: The trained Random Forest classifier.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the test data.
    
    Args:
    - model: The trained model.
    - X_test (array): Feature data for testing.
    - y_test (array): Label data for testing.
    
    Returns:
    - None: Prints the accuracy score.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

# Main function to execute the workflow
def main():
    # Load data
    file_path = 'novels.csv'  # Update with the actual path to your CSV file
    data = load_data(file_path)
    
    # Preprocess the data
    X, y = preprocess_data(data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build and train the model
    model = build_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)

# Entry point for the script
if __name__ == '__main__':
    main()
```
