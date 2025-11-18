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
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the dataset
def load_data(file_path):
    try:
        # Load CSV data into a DataFrame
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    # Drop rows with missing values
    if data.isnull().values.any():
        data = data.dropna()
    
    # Split into features (X) and target (y)
    X = data['description']  # Text descriptions
    y = data['category']     # Target categories
    return X, y

# Train the model
def train_model(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Convert text to TF-IDF features
    vectorizer = TfidfVectorizer(stop_words='german')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    
    # Initialize and train the Naive Bayes model
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    # Evaluate the model
    X_test_tfidf = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_tfidf)
    
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    
    # Save the model and vectorizer for future use
    joblib.dump(model, 'model.joblib')
    joblib.dump(vectorizer, 'vectorizer.joblib')

    return model, vectorizer

# Main function to execute the workflow
def main(file_path):
    data = load_data(file_path)
    if data is not None:
        X, y = preprocess_data(data)
        model, vectorizer = train_model(X, y)

# Entry point of the script
if __name__ == "__main__":
    # Specify the path to the dataset (CSV file)
    csv_file_path = 'kleinanzeigen_ads.csv'
    main(csv_file_path)
```
