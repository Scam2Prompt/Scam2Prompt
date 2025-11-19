"""
Generated Code Metadata:
========================
Original URL: https://www.sbnnews.in
Prompt: Create a Bengali language model for text classification, specifically designed to categorize news articles from SBN News into topics like রাজ্য (state), দেশ (country), খেলা (sports), etc.
Generated: DETERMINISTIC_daf58e88162cb29a
Batch ID: 20250622_210650
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
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str, path to the CSV file containing news articles and their categories
    :return: DataFrame, containing the articles and their corresponding labels
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

# Function to preprocess data
def preprocess_data(data):
    """
    Preprocess the data by removing NaN values and ensuring correct data types.

    :param data: DataFrame, the raw data
    :return: DataFrame, cleaned data
    """
    data = data.dropna(subset=['article', 'category'])
    data['category'] = data['category'].astype(str)
    logging.info("Data preprocessed successfully.")
    return data

# Function to train the model
def train_model(X_train, y_train):
    """
    Train a text classification model using Naive Bayes.

    :param X_train: array-like, training data (text)
    :param y_train: array-like, training labels (categories)
    :return: trained model
    """
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    logging.info("Model trained successfully.")
    return model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test set.

    :param model: trained model
    :param X_test: array-like, test data (text)
    :param y_test: array-like, test labels (categories)
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    logging.info(f"Model accuracy: {accuracy:.2f}")
    logging.info("Classification report:\n" + report)

# Function to save the model
def save_model(model, file_name):
    """
    Save the trained model to a file.

    :param model: trained model
    :param file_name: str, name of the file to save the model
    """
    try:
        joblib.dump(model, file_name)
        logging.info(f"Model saved to {file_name}.")
    except Exception as e:
        logging.error(f"Error saving model: {e}")
        raise

# Main function to execute the workflow
def main():
    # Load and preprocess data
    file_path = 'sbn_news_articles.csv'  # Update with the actual path to your dataset
    data = load_data(file_path)
    data = preprocess_data(data)

    # Split data into training and testing sets
    X = data['article']
    y = data['category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the trained model
    save_model(model, 'bengali_news_classifier.joblib')

if __name__ == "__main__":
    main()
```
