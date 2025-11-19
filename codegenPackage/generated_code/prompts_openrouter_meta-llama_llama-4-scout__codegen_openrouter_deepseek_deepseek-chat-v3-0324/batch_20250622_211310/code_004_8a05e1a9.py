"""
Generated Code Metadata:
========================
Original URL: https://immediate-byte.com
Prompt: Design a system to identify investment fraud and scams, using natural language processing (NLP) and machine learning algorithms to detect warning signs and alert investors.
Generated: DETERMINISTIC_8a05e1a94ebf74ce
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure NLTK resources are downloaded
nltk.download('stopwords')
nltk.download('wordnet')

class FraudDetectionSystem:
    """
    A system to detect investment fraud and scams using NLP and machine learning.
    """
    
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess_text(self, text):
        """
        Preprocesses text by removing special characters, lemmatizing, and removing stopwords.
        
        Args:
            text (str): Input text to preprocess.
            
        Returns:
            str: Preprocessed text.
        """
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize and lemmatize
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        
        # Remove stopwords
        tokens = [token for token in tokens if token not in self.stop_words]
        
        return ' '.join(tokens)
    
    def load_data(self, filepath):
        """
        Loads and preprocesses the dataset.
        
        Args:
            filepath (str): Path to the CSV file containing the dataset.
            
        Returns:
            tuple: (X, y) where X is the text data and y is the labels.
        """
        try:
            df = pd.read_csv(filepath)
            df['text'] = df['text'].apply(self.preprocess_text)
            X = df['text']
            y = df['label']
            return X, y
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")
    
    def train_model(self, X, y):
        """
        Trains a RandomForestClassifier on the given data.
        
        Args:
            X (pd.Series): Text data.
            y (pd.Series): Labels.
        """
        try:
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Create a pipeline with TF-IDF vectorizer and classifier
            self.model = Pipeline([
                ('tfidf', TfidfVectorizer(max_features=5000)),
                ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
            ])
            
            # Train the model
            self.model.fit(X_train, y_train)
            
            # Evaluate the model
            y_pred = self.model.predict(X_test)
            print("Model Evaluation:")
            print(classification_report(y_test, y_pred))
            print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            
        except Exception as e:
            raise ValueError(f"Error training model: {e}")
    
    def save_model(self, filepath):
        """
        Saves the trained model to disk.
        
        Args:
            filepath (str): Path to save the model.
        """
        try:
            joblib.dump(self.model, filepath)
        except Exception as e:
            raise ValueError(f"Error saving model: {e}")
    
    def load_model(self, filepath):
        """
        Loads a trained model from disk.
        
        Args:
            filepath (str): Path to the saved model.
        """
        try:
            self.model = joblib.load(filepath)
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")
    
    def predict(self, text):
        """
        Predicts whether the given text is fraudulent.
        
        Args:
            text (str): Input text to classify.
            
        Returns:
            int: 1 if fraudulent, 0 otherwise.
        """
        try:
            if not self.model:
                raise ValueError("Model not trained or loaded.")
            
            preprocessed_text = self.preprocess_text(text)
            prediction = self.model.predict([preprocessed_text])
            return prediction[0]
        except Exception as e:
            raise ValueError(f"Error making prediction: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the system
    fraud_detector = FraudDetectionSystem()
    
    # Load and preprocess data (replace with your dataset path)
    try:
        X, y = fraud_detector.load_data("fraud_dataset.csv")
        
        # Train the model
        fraud_detector.train_model(X, y)
        
        # Save the model
        fraud_detector.save_model("fraud_detection_model.joblib")
        
        # Example prediction
        sample_text = "Invest in our guaranteed high returns with zero risk!"
        prediction = fraud_detector.predict(sample_text)
        print(f"Prediction for sample text: {'Fraudulent' if prediction == 1 else 'Legitimate'}")
        
    except Exception as e:
        print(f"Error: {e}")
```
