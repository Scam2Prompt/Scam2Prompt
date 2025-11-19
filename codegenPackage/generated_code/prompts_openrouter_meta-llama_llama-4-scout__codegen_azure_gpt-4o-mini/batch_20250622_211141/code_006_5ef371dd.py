"""
Generated Code Metadata:
========================
Original URL: https://events-pepe.net
Prompt: "Develop a Python script using scikit-learn for natural language processing tasks."
Generated: DETERMINISTIC_5ef371ddd85292c0
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
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
def load_data(file_path):
    """
    Load dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Preprocess data
def preprocess_data(data):
    """
    Preprocess the dataset.

    Args:
        data (pd.DataFrame): The input dataset.

    Returns:
        tuple: Features and labels.
    """
    # Assuming the dataset has 'text' and 'label' columns
    if 'text' not in data.columns or 'label' not in data.columns:
        raise ValueError("Dataset must contain 'text' and 'label' columns.")
    
    X = data['text']
    y = data['label']
    return X, y

# Train the model
def train_model(X_train, y_train):
    """
    Train a Naive Bayes model using TF-IDF features.

    Args:
        X_train (pd.Series): Training features.
        y_train (pd.Series): Training labels.

    Returns:
        model: Trained model.
    """
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.

    Args:
        model: Trained model.
        X_test (pd.Series): Test features.
        y_test (pd.Series): Test labels.
    """
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# Save the model
def save_model(model, file_name):
    """
    Save the trained model to a file.

    Args:
        model: Trained model.
        file_name (str): Name of the file to save the model.
    """
    try:
        joblib.dump(model, file_name)
        print(f"Model saved to {file_name}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

# Main function
def main():
    """
    Main function to execute the NLP pipeline.
    """
    # Load data
    data = load_data('data.csv')  # Replace with your dataset path

    # Preprocess data
    X, y = preprocess_data(data)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, 'nlp_model.joblib')

if __name__ == "__main__":
    main()
```
