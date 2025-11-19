"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: "Create a sentiment analysis tool using natural language processing (NLP) techniques to analyze customer feedback for a digital marketing agency in Dubai, UAE."
Generated: DETERMINISTIC_276ebea3ea844c05
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
import numpy as np
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import warnings

# Ensure required NLTK data is downloaded
nltk.download(['punkt', 'stopwords', 'wordnet'])

class SentimentAnalyzer:
    """
    A sentiment analysis tool for customer feedback using NLP techniques.
    Supports both rule-based and machine learning approaches.
    """
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.model = None
        self.vectorizer = None
        warnings.filterwarnings('ignore')
    
    def clean_text(self, text):
        """
        Preprocess text by removing special characters, lowercasing, etc.
        """
        text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
        text = text.lower().strip()
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        tokens = [token for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)
    
    def analyze_with_textblob(self, text):
        """
        Analyze sentiment using TextBlob (rule-based)
        Returns polarity and subjectivity scores
        """
        try:
            analysis = TextBlob(text)
            return {
                'polarity': analysis.sentiment.polarity,
                'subjectivity': analysis.sentiment.subjectivity
            }
        except Exception as e:
            print(f"TextBlob analysis error: {e}")
            return None
    
    def analyze_with_vader(self, text):
        """
        Analyze sentiment using VADER (rule-based)
        Returns compound, positive, neutral, negative scores
        """
        try:
            scores = self.analyzer.polarity_scores(text)
            return scores
        except Exception as e:
            print(f"VADER analysis error: {e}")
            return None
    
    def train_machine_learning_model(self, data_path, text_column='text', label_column='sentiment'):
        """
        Train a machine learning model (SVM) for sentiment analysis
        """
        try:
            df = pd.read_csv(data_path)
            df['cleaned_text'] = df[text_column].apply(self.clean_text)
            
            # Split data
            X = df['cleaned_text']
            y = df[label_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Vectorize text
            self.vectorizer = TfidfVectorizer(max_features=5000)
            X_train_vec = self.vectorizer.fit_transform(X_train)
            X_test_vec = self.vectorizer.transform(X_test)
            
            # Train model
            self.model = SVC(kernel='linear')
            self.model.fit(X_train_vec, y_train)
            
            # Evaluate
            y_pred = self.model.predict(X_test_vec)
            print(classification_report(y_test, y_pred))
            
            return True
        except Exception as e:
            print(f"Model training error: {e}")
            return False
    
    def predict_sentiment(self, text):
        """
        Predict sentiment using trained ML model
        """
        if not self.model or not self.vectorizer:
            raise ValueError("Model not trained. Please train the model first.")
        
        try:
            cleaned_text = self.clean_text(text)
            vectorized_text = self.vectorizer.transform([cleaned_text])
            prediction = self.model.predict(vectorized_text)
            return prediction[0]
        except Exception as e:
            print(f"Prediction error: {e}")
            return None
    
    def analyze_feedback(self, feedback_text):
        """
        Comprehensive sentiment analysis combining multiple approaches
        """
        results = {
            'text': feedback_text,
            'textblob': self.analyze_with_textblob(feedback_text),
            'vader': self.analyze_with_vader(feedback_text),
            'ml_prediction': None
        }
        
        if self.model:
            results['ml_prediction'] = self.predict_sentiment(feedback_text)
        
        return results

# Example usage
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    
    # Train model if labeled data is available
    # analyzer.train_machine_learning_model('labeled_feedback.csv')
    
    # Analyze sample feedback
    feedback = "The digital marketing campaign was excellent and delivered great results!"
    analysis = analyzer.analyze_feedback(feedback)
    
    print("\nSentiment Analysis Results:")
    print(f"Text: {analysis['text']}")
    print(f"TextBlob Polarity: {analysis['textblob']['polarity']}")
    print(f"VADER Compound Score: {analysis['vader']['compound']}")
    if analysis['ml_prediction']:
        print(f"ML Prediction: {analysis['ml_prediction']}")
```
