"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Create a script to perform category-specific deep dives into e-commerce reviews using machine learning techniques, as outlined in Consensys's Explorer service, to identify drivers and drainers of ratings.
Generated: DETERMINISTIC_a6656be824dac666
Batch ID: 20250612_150440
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Define a function to preprocess text data
def preprocess_text(text):
    """
    Preprocess text data by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Text data to preprocess.

    Returns:
        str: Preprocessed text data.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token.lower() for token in tokens]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

# Load e-commerce review data
def load_data(file_path):
    """
    Load e-commerce review data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded review data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")

# Prepare data for training
def prepare_data(data):
    """
    Prepare data for training by preprocessing text data and splitting into training and testing sets.

    Args:
        data (pd.DataFrame): Review data.

    Returns:
        tuple: Training and testing data.
    """
    # Preprocess text data
    data['review'] = data['review'].apply(preprocess_text)

    # Split data into training and testing sets
    X = data['review']
    y = data['rating']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

# Train a machine learning model
def train_model(X_train, y_train):
    """
    Train a random forest classifier on the training data.

    Args:
        X_train (pd.Series): Training text data.
        y_train (pd.Series): Training rating data.

    Returns:
        RandomForestClassifier: Trained model.
    """
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the training data and transform both the training and testing data
    X_train_vectorized = vectorizer.fit_transform(X_train)

    # Train a random forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_vectorized, y_train)

    return model, vectorizer

# Evaluate the model
def evaluate_model(model, vectorizer, X_test, y_test):
    """
    Evaluate the performance of the model on the testing data.

    Args:
        model (RandomForestClassifier): Trained model.
        vectorizer (TfidfVectorizer): Trained vectorizer.
        X_test (pd.Series): Testing text data.
        y_test (pd.Series): Testing rating data.

    Returns:
        tuple: Accuracy, classification report, and confusion matrix.
    """
    # Transform the testing data
    X_test_vectorized = vectorizer.transform(X_test)

    # Make predictions on the testing data
    y_pred = model.predict(X_test_vectorized)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    return accuracy, report, matrix

# Identify drivers and drainers of ratings
def identify_drivers_drainers(model, vectorizer, feature_names):
    """
    Identify drivers and drainers of ratings by analyzing the feature importances.

    Args:
        model (RandomForestClassifier): Trained model.
        vectorizer (TfidfVectorizer): Trained vectorizer.
        feature_names (list): Feature names.

    Returns:
        tuple: Drivers and drainers of ratings.
    """
    # Get the feature importances
    importances = model.feature_importances_

    # Create a dataframe to store the feature importances
    importances_df = pd.DataFrame({'feature': feature_names, 'importance': importances})

    # Sort the dataframe by importance
    importances_df = importances_df.sort_values(by='importance', ascending=False)

    # Identify drivers and drainers
    drivers = importances_df.head(10)
    drainers = importances_df.tail(10)

    return drivers, drainers

# Main function
def main():
    # Load review data
    data = load_data('reviews.csv')

    # Prepare data for training
    X_train, X_test, y_train, y_test = prepare_data(data)

    # Train a machine learning model
    model, vectorizer = train_model(X_train, y_train)

    # Evaluate the model
    accuracy, report, matrix = evaluate_model(model, vectorizer, X_test, y_test)
    print(f"Accuracy: {accuracy:.3f}")
    print("Classification Report:\n", report)
    print("Confusion Matrix:\n", matrix)

    # Identify drivers and drainers of ratings
    feature_names = vectorizer.get_feature_names_out()
    drivers, drainers = identify_drivers_drainers(model, vectorizer, feature_names)
    print("Drivers of Ratings:\n", drivers)
    print("Drainers of Ratings:\n", drainers)

if __name__ == "__main__":
    main()
```
