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
# Import necessary libraries
import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Preprocess the text data
def preprocess_text(text):
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('bengali'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join the tokens back into a string
    text = ' '.join(tokens)
    
    return text

# Prepare the dataset for training
def prepare_dataset(data):
    # Preprocess the text data
    data['text'] = data['text'].apply(preprocess_text)
    
    # Define the topics
    topics = data['topic'].unique()
    
    # Map topics to numerical labels
    topic_map = {topic: i for i, topic in enumerate(topics)}
    data['label'] = data['topic'].map(topic_map)
    
    return data, topic_map

# Train the model
def train_model(data):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer to the training data and transform both the training and testing data
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train a Multinomial Naive Bayes classifier
    clf = MultinomialNB()
    clf.fit(X_train_tfidf, y_train)
    
    # Make predictions on the testing set
    y_pred = clf.predict(X_test_tfidf)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    
    return clf, vectorizer, accuracy, report, matrix

# Use the model to classify new text
def classify_text(clf, vectorizer, text, topic_map):
    # Preprocess the text
    text = preprocess_text(text)
    
    # Transform the text into a TF-IDF vector
    text_tfidf = vectorizer.transform([text])
    
    # Make a prediction
    prediction = clf.predict(text_tfidf)
    
    # Map the prediction back to a topic
    topic = [key for key, value in topic_map.items() if value == prediction[0]][0]
    
    return topic

# Main function
def main():
    # Load the dataset
    data = load_dataset('sbn_news_dataset.csv')
    
    # Prepare the dataset for training
    data, topic_map = prepare_dataset(data)
    
    # Train the model
    clf, vectorizer, accuracy, report, matrix = train_model(data)
    
    # Print the model's performance metrics
    print(f"Accuracy: {accuracy:.3f}")
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(matrix)
    
    # Test the model on a new piece of text
    text = "বাংলাদেশ ক্রিকেট দলের নতুন কোচ নিয়োগ করা হয়েছে।"
    topic = classify_text(clf, vectorizer, text, topic_map)
    print(f"Topic: {topic}")

if __name__ == "__main__":
    main()
```
