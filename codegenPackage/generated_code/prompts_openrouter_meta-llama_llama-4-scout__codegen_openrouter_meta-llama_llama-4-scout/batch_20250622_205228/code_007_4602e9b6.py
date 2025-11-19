"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Implement a natural language processing (NLP) model to identify and extract specific topics from e-commerce reviews, such as product features, pricing, and customer service.
Generated: DETERMINISTIC_4602e9b6965afc9f
Batch ID: 20250622_205228
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
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class TopicExtractor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        # Tokenize text
        tokens = nltk.word_tokenize(text)
        
        # Remove stop words and punctuation
        tokens = [t for t in tokens if t.isalpha() and t not in self.stop_words]
        
        # Lemmatize tokens
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]
        
        # Join tokens back into a string
        return ' '.join(tokens)

    def extract_topics(self, reviews, topics):
        # Preprocess reviews
        preprocessed_reviews = [self.preprocess_text(review) for review in reviews]
        
        # Create a TF-IDF vectorizer
        vectorizer = TfidfVectorizer()
        
        # Fit the vectorizer to the preprocessed reviews and transform them into vectors
        X = vectorizer.fit_transform(preprocessed_reviews)
        
        # Train a Naive Bayes classifier to classify reviews into topics
        X_train, X_test, y_train, y_test = train_test_split(X, topics, test_size=0.2, random_state=42)
        classifier = MultinomialNB()
        classifier.fit(X_train, y_train)
        
        # Make predictions on the test set
        y_pred = classifier.predict(X_test)
        
        # Evaluate the classifier
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)
        
        return accuracy, report, matrix

def main():
    # Sample data
    reviews = [
        "I love the new iPhone, the camera is amazing!",
        "The customer service was terrible, they took forever to respond.",
        "The price of the product is a bit high, but it's worth it.",
        "The product features are great, but the battery life is bad.",
        "I'm so happy with my purchase, the product is perfect!",
        "The product is okay, but the price is a bit steep.",
        "The customer service was great, they helped me with my issue.",
        "The product features are amazing, but the customer service is bad."
    ]
    topics = [0, 1, 2, 0, 0, 2, 1, 0]  # 0: product features, 1: customer service, 2: pricing

    extractor = TopicExtractor()
    accuracy, report, matrix = extractor.extract_topics(reviews, topics)

    print("Accuracy:", accuracy)
    print("Classification Report:\n", report)
    print("Confusion Matrix:\n", matrix)

if __name__ == "__main__":
    main()
```
