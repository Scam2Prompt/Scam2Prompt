"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Develop a machine learning model to classify Tamil-language news articles as "True" or "False," inspired by the categories used on Fact Crescendo Tamil.
Generated: DETERMINISTIC_78e3ddc4b2e75870
Batch ID: 20250612_152249
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.exceptions import ConvergenceWarning
import warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Load the dataset
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    # Assuming 'text' is the column with news article text and 'label' is the column with labels (True/False)
    X = data['text']
    y = data['label'].map({'True': 1, 'False': 0})
    return X, y

# Train the model
def train_model(X_train, y_train):
    try:
        # Create a pipeline with TF-IDF vectorizer and Multinomial Naive Bayes classifier
        pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer(stop_words='tamil')),
            ('clf', MultinomialNB())
        ])
        
        # Train the model
        pipeline.fit(X_train, y_train)
        return pipeline
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    try:
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)
        
        return accuracy, report, matrix
    except Exception as e:
        print(f"Error evaluating model: {e}")
        return None

# Main function
def main():
    # Load the dataset
    file_path = 'tamil_news_dataset.csv'  # replace with your dataset file path
    data = load_dataset(file_path)
    
    if data is not None:
        # Preprocess the data
        X, y = preprocess_data(data)
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        model = train_model(X_train, y_train)
        
        if model is not None:
            # Evaluate the model
            accuracy, report, matrix = evaluate_model(model, X_test, y_test)
            
            # Print the results
            print(f"Model Accuracy: {accuracy:.3f}")
            print("Classification Report:\n", report)
            print("Confusion Matrix:\n", matrix)

if __name__ == "__main__":
    main()
```
