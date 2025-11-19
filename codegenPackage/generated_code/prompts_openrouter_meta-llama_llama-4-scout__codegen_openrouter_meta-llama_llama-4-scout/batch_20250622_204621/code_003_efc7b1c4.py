"""
Generated Code Metadata:
========================
Original URL: https://simonscat.pages.dev
Prompt: Create a Simon's Cat character recommendation system using natural language processing (NLP) and machine learning.
Generated: DETERMINISTIC_efc7b1c46c8052d6
Batch ID: 20250622_204621
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
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Preprocess text data
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back into a string
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

# Prepare data for training
def prepare_data(data):
    # Preprocess text data
    data['text'] = data['text'].apply(preprocess_text)
    
    # Define features and target
    X = data['text']
    y = data['character']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Train a Naive Bayes classifier
def train_model(X_train, y_train):
    try:
        # Create a TF-IDF vectorizer
        vectorizer = TfidfVectorizer()
        
        # Fit the vectorizer to the training data and transform both the training and testing data
        X_train_tfidf = vectorizer.fit_transform(X_train)
        
        # Train a Naive Bayes classifier
        clf = MultinomialNB()
        clf.fit(X_train_tfidf, y_train)
        
        return clf, vectorizer
    except Exception as e:
        print(f"Error training model: {e}")

# Make predictions
def make_predictions(clf, vectorizer, X_test):
    try:
        # Transform testing data
        X_test_tfidf = vectorizer.transform(X_test)
        
        # Make predictions
        y_pred = clf.predict(X_test_tfidf)
        
        return y_pred
    except Exception as e:
        print(f"Error making predictions: {e}")

# Evaluate model performance
def evaluate_model(y_test, y_pred):
    try:
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.3f}")
        
        # Print classification report
        print(classification_report(y_test, y_pred))
    except Exception as e:
        print(f"Error evaluating model: {e}")

# Main function
def main():
    # Load dataset
    data = load_dataset('simons_cat_characters.csv')
    
    # Prepare data for training
    X_train, X_test, y_train, y_test = prepare_data(data)
    
    # Train a Naive Bayes classifier
    clf, vectorizer = train_model(X_train, y_train)
    
    # Make predictions
    y_pred = make_predictions(clf, vectorizer, X_test)
    
    # Evaluate model performance
    evaluate_model(y_test, y_pred)

    # Example usage: Get character recommendation
    def get_character_recommendation(text):
        # Preprocess text
        text = preprocess_text(text)
        
        # Transform text
        text_tfidf = vectorizer.transform([text])
        
        # Make prediction
        prediction = clf.predict(text_tfidf)
        
        return prediction[0]

    # Test the function
    text = "I love lazy cats"
    recommended_character = get_character_recommendation(text)
    print(f"Recommended character: {recommended_character}")

if __name__ == "__main__":
    main()
```
