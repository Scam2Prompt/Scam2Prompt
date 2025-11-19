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
# Import required libraries
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.exceptions import ConvergenceWarning
import warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")

# Preprocess the text data
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the tokens back into a string
    text = ' '.join(tokens)
    return text

# Train the NLP model
def train_model(data):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

    # Create a pipeline with TF-IDF vectorizer and Multinomial Naive Bayes classifier
    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', MultinomialNB())
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = pipeline.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    return pipeline, accuracy, report, matrix

# Classify customer feedback
def classify_feedback(model, text):
    try:
        # Preprocess the text
        text = preprocess_text(text)
        
        # Make a prediction
        prediction = model.predict([text])
        
        return prediction[0]
    except Exception as e:
        print(f"Error classifying feedback: {e}")

# Main function
def main():
    # Load the dataset
    data = load_data('skincare_feedback.csv')

    # Map labels to numerical values
    label_mapping = {'positive': 0, 'neutral': 1, 'negative': 2}
    data['label'] = data['label'].map(label_mapping)

    # Preprocess the text data
    data['text'] = data['text'].apply(preprocess_text)

    # Train the model
    model, accuracy, report, matrix = train_model(data)

    # Print the results
    print(f"Model Accuracy: {accuracy:.3f}")
    print("Classification Report:\n", report)
    print("Confusion Matrix:\n", matrix)

    # Classify customer feedback
    text = "I love this moisturizer! It's so hydrating."
    prediction = classify_feedback(model, text)
    print(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
```
