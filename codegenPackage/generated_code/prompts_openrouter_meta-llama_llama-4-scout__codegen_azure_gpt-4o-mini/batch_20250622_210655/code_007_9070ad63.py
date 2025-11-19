"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Suggest a suitable machine learning model for detecting fake or misleading health product advertisements in Thai social media.
Generated: DETERMINISTIC_9070ad63c9df2c93
Batch ID: 20250622_210655
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib
import logging

# Set up logging for tracking the process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load dataset from a CSV file.

    :param file_path: str, path to the CSV file containing the data
    :return: DataFrame, loaded data
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess the data for model training.

    :param data: DataFrame, input data
    :return: tuple, features and labels
    """
    # Assuming the DataFrame has 'text' and 'label' columns
    X = data['text']
    y = data['label']
    return X, y

def train_model(X_train, y_train):
    """
    Train a Naive Bayes model on the training data.

    :param X_train: array-like, training features
    :param y_train: array-like, training labels
    :return: model, trained model
    """
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)

    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    logging.info("Model trained successfully.")
    return model, vectorizer

def evaluate_model(model, vectorizer, X_test, y_test):
    """
    Evaluate the trained model on the test data.

    :param model: trained model
    :param vectorizer: fitted vectorizer
    :param X_test: array-like, test features
    :param y_test: array-like, test labels
    """
    X_test_tfidf = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_tfidf)

    logging.info("Model evaluation completed.")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

def save_model(model, vectorizer, model_path, vectorizer_path):
    """
    Save the trained model and vectorizer to disk.

    :param model: trained model
    :param vectorizer: fitted vectorizer
    :param model_path: str, path to save the model
    :param vectorizer_path: str, path to save the vectorizer
    """
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    logging.info("Model and vectorizer saved successfully.")

def main():
    # File paths
    data_file = 'health_ads_data.csv'
    model_file = 'fake_health_ads_model.pkl'
    vectorizer_file = 'tfidf_vectorizer.pkl'

    # Load and preprocess data
    data = load_data(data_file)
    X, y = preprocess_data(data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model, vectorizer = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, vectorizer, X_test, y_test)

    # Save the model and vectorizer
    save_model(model, vectorizer, model_file, vectorizer_file)

if __name__ == "__main__":
    main()
```
