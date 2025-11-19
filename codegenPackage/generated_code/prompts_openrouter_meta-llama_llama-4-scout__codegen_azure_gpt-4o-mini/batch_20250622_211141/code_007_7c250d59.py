"""
Generated Code Metadata:
========================
Original URL: https://lpt-airdrop.com
Prompt: Develop a sentiment analysis model to classify news articles from El Mundo as positive, negative, or neutral, using a suitable machine learning library or framework.
Generated: DETERMINISTIC_7c250d5960129658
Batch ID: 20250622_211141
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

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO)

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    :param file_path: str, path to the CSV file containing news articles
    :return: DataFrame, containing the news articles and their sentiment labels
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
    Preprocess the data by cleaning and preparing it for analysis.
    
    :param data: DataFrame, containing the news articles
    :return: DataFrame, cleaned data with text and labels
    """
    # Drop rows with missing values
    data.dropna(subset=['text', 'label'], inplace=True)
    logging.info("Data preprocessed: missing values dropped.")
    return data

def train_model(X_train, y_train):
    """
    Train a sentiment analysis model using the Naive Bayes algorithm.
    
    :param X_train: array-like, training data features
    :param y_train: array-like, training data labels
    :return: model, trained Naive Bayes model
    """
    model = MultinomialNB()
    model.fit(X_train, y_train)
    logging.info("Model trained successfully.")
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test set.
    
    :param model: trained model
    :param X_test: array-like, test data features
    :param y_test: array-like, test data labels
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    logging.info(f"Model accuracy: {accuracy:.2f}")
    logging.info(f"Classification report:\n{report}")

def save_model(model, file_name):
    """
    Save the trained model to a file.
    
    :param model: trained model
    :param file_name: str, name of the file to save the model
    """
    joblib.dump(model, file_name)
    logging.info(f"Model saved to {file_name}")

def main(file_path):
    """
    Main function to execute the sentiment analysis workflow.
    
    :param file_path: str, path to the CSV file containing news articles
    """
    # Load and preprocess data
    data = load_data(file_path)
    data = preprocess_data(data)

    # Split data into features and labels
    X = data['text']
    y = data['label']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Vectorize the text data
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    # Train the model
    model = train_model(X_train_vectorized, y_train)

    # Evaluate the model
    evaluate_model(model, X_test_vectorized, y_test)

    # Save the model and vectorizer
    save_model(model, 'sentiment_model.joblib')
    save_model(vectorizer, 'vectorizer.joblib')

if __name__ == "__main__":
    # Specify the path to the dataset
    dataset_path = 'el_mundo_articles.csv'
    main(dataset_path)
```
