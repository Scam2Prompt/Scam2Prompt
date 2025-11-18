"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamil.factcrescendo.com
Prompt: Develop a machine learning model to classify Tamil-language news articles as "True" or "False," inspired by the categories used on Fact Crescendo Tamil.
Generated: DETERMINISTIC_78e3ddc4b2e75870
Batch ID: 20250612_152249
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the dataset
def load_data(file_path):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from {}".format(file_path))
        return data
    except Exception as e:
        logging.error("Error loading data: {}".format(e))
        raise

# Preprocess the data
def preprocess_data(data):
    """Preprocess the data to prepare for training."""
    # Drop rows with missing values
    data = data.dropna()
    
    # Ensure the columns are correctly named
    if 'text' not in data.columns or 'label' not in data.columns:
        logging.error("Dataset must contain 'text' and 'label' columns")
        raise ValueError("Dataset must contain 'text' and 'label' columns")
    
    return data['text'], data['label']

# Train the model
def train_model(X_train, y_train):
    """Train a Naive Bayes model using a pipeline."""
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    logging.info("Model trained successfully")
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, target_names=["False", "True"])
    
    logging.info("Model evaluation completed")
    logging.info("Accuracy: {:.2f}%".format(accuracy * 100))
    logging.info("Classification Report:\n{}".format(report))

# Save the model
def save_model(model, file_path):
    """Save the trained model to a file."""
    joblib.dump(model, file_path)
    logging.info("Model saved to {}".format(file_path))

# Main function to execute the workflow
def main():
    """Main function to execute the news article classification workflow."""
    # Load data
    data = load_data('tamil_news_articles.csv')
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model
    save_model(model, 'tamil_news_classifier.pkl')

if __name__ == "__main__":
    main()
```

This code defines a workflow for loading, preprocessing, training, evaluating, and saving a machine learning model that classifies Tamil-language news articles. It includes error handling, logs important execution steps, and follows best practices for maintainability and readability.
