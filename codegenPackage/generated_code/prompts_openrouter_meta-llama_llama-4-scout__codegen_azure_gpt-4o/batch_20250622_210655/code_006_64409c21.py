"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Develop a natural language processing (NLP) model to classify customer feedback on skincare products as positive, negative, or neutral, based on their experiences with the products.
Generated: DETERMINISTIC_64409c21313bd419
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
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load and preprocess the dataset
def load_data(file_path):
    """
    Load customer feedback data from a CSV file.
    The file should have two columns: 'feedback' and 'label'.
    'feedback' contains the text, and 'label' contains the sentiment (positive, negative, neutral).
    """
    try:
        data = pd.read_csv(file_path)
        if 'feedback' not in data.columns or 'label' not in data.columns:
            raise ValueError("Dataset must contain 'feedback' and 'label' columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Preprocess the data
def preprocess_data(data):
    """
    Preprocess the data by splitting into training and testing sets.
    Returns the training and testing data and labels.
    """
    X = data['feedback']
    y = data['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Train the NLP model
def train_model(X_train, y_train):
    """
    Train a logistic regression model using TF-IDF features.
    Returns the trained model and the TF-IDF vectorizer.
    """
    try:
        # Convert text data to TF-IDF features
        vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        X_train_tfidf = vectorizer.fit_transform(X_train)

        # Train a logistic regression model
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train_tfidf, y_train)

        return model, vectorizer
    except Exception as e:
        print(f"Error training model: {e}")
        raise

# Evaluate the model
def evaluate_model(model, vectorizer, X_test, y_test):
    """
    Evaluate the trained model on the test data and print a classification report.
    """
    try:
        X_test_tfidf = vectorizer.transform(X_test)
        y_pred = model.predict(X_test_tfidf)
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
    except Exception as e:
        print(f"Error evaluating model: {e}")
        raise

# Save the model and vectorizer
def save_model(model, vectorizer, model_path, vectorizer_path):
    """
    Save the trained model and vectorizer to disk for future use.
    """
    try:
        joblib.dump(model, model_path)
        joblib.dump(vectorizer, vectorizer_path)
        print(f"Model saved to {model_path}")
        print(f"Vectorizer saved to {vectorizer_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

# Main function
def main():
    """
    Main function to load data, train the model, evaluate it, and save the artifacts.
    """
    try:
        # File paths
        data_file = 'customer_feedback.csv'  # Replace with your dataset file path
        model_file = 'sentiment_model.pkl'
        vectorizer_file = 'tfidf_vectorizer.pkl'

        # Load and preprocess data
        data = load_data(data_file)
        X_train, X_test, y_train, y_test = preprocess_data(data)

        # Train the model
        model, vectorizer = train_model(X_train, y_train)

        # Evaluate the model
        evaluate_model(model, vectorizer, X_test, y_test)

        # Save the model and vectorizer
        save_model(model, vectorizer, model_file, vectorizer_file)

    except Exception as e:
        print(f"Error in main function: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
