"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Create a machine learning model to classify social media posts as constructive or divisive based on their text content. Provide code and suggest libraries for natural language processing.
Generated: DETERMINISTIC_4356098b087f01e3
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import re
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import joblib

# Download NLTK data files (stopwords and punkt tokenizer)
nltk.download('stopwords')
nltk.download('punkt')

# Function to clean and preprocess text
def preprocess_text(text):
    """Cleans and preprocesses the input text."""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove punctuation and numbers
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(filtered_tokens)

# Load dataset
def load_data(file_path):
    """Loads dataset from the specified CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Main function to train the model
def train_model(data):
    """Trains a Naive Bayes model to classify social media posts."""
    # Preprocess the text data
    data['cleaned_text'] = data['text'].apply(preprocess_text)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data['cleaned_text'], 
        data['label'], 
        test_size=0.2, 
        random_state=42
    )

    # Create a pipeline that first vectorizes the text and then applies the classifier
    model_pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # Train the model
    model_pipeline.fit(X_train, y_train)

    # Make predictions
    y_pred = model_pipeline.predict(X_test)

    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save the model for future use
    joblib.dump(model_pipeline, 'social_media_classifier.joblib')

# Entry point of the script
if __name__ == "__main__":
    # Load data (ensure the CSV file exists with 'text' and 'label' columns)
    dataset_path = 'social_media_posts.csv'
    data = load_data(dataset_path)
    
    if data is not None and 'text' in data.columns and 'label' in data.columns:
        # Train the model
        train_model(data)
    else:
        print("Dataset is missing required columns or could not be loaded.")
```
