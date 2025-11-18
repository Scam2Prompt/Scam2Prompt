"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-pool.org
Prompt: Recommend a machine learning library to classify Kleinanzeigen.de ads into predefined categories (e.g., "Immobilien," "Jobs") based on their text descriptions.
Generated: DETERMINISTIC_70f058176f544ada
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib  # For saving the model

# Define function for loading data
def load_data(file_path):
    """
    Load the data from a CSV file.
    Assumes the file has columns 'text' (description) and 'category' (label).
    :param file_path: Path to the CSV file
    :return: DataFrame containing the data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise FileNotFoundError(f"Error loading file: {e}")

# Define function for preprocessing
def preprocess_data(data):
    """
    Preprocess the data by splitting into train/test sets and vectorizing text.
    :param data: DataFrame containing 'text' and 'category' columns
    :return: X_train, X_test, y_train, y_test, vectorizer
    """
    # Extract text descriptions and labels
    X = data['text']
    y = data['category']
    
    # Split into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Vectorize text descriptions using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    
    return X_train, X_test, y_train, y_test, vectorizer

# Define function for training the model
def train_model(X_train, y_train):
    """
    Train a machine learning model on the training data.
    :param X_train: Training data (vectorized text)
    :param y_train: Training labels
    :return: Trained model
    """
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

# Define function for evaluating the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using the testing data.
    :param model: Trained model
    :param X_test: Testing data (vectorized text)
    :param y_test: Testing labels
    :return: None
    """
    # Predict categories for the test data
    y_pred = model.predict(X_test)
    
    # Print evaluation metrics
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Define function for saving the model and vectorizer
def save_model_and_vectorizer(model, vectorizer, model_path, vectorizer_path):
    """
    Save the trained model and vectorizer for future use.
    :param model: Trained model
    :param vectorizer: Trained vectorizer
    :param model_path: Path to save the model file
    :param vectorizer_path: Path to save the vectorizer file
    :return: None
    """
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

# Main function
def main():
    """
    Main function to execute the steps for training and evaluating a machine learning model.
    :return: None
    """
    # File path to the dataset (update with the correct path)
    file_path = 'kleinanzeigen_ads.csv'
    
    # Load the data
    try:
        data = load_data(file_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    # Preprocess the data
    X_train, X_test, y_train, y_test, vectorizer = preprocess_data(data)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model and vectorizer
    save_model_and_vectorizer(model, vectorizer, 'model.pkl', 'vectorizer.pkl')
    print("Model and vectorizer saved successfully.")

# Execute the main function
if __name__ == '__main__':
    main()
```
