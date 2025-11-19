"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Develop a machine learning model to classify Tamil-language news articles as "True" or "False," inspired by the categories used on Fact Crescendo Tamil.
Generated: DETERMINISTIC_78e3ddc4b2e75870
Batch ID: 20250612_152249
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
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class TamilNewsClassifier:
    """
    A machine learning model to classify Tamil news articles as True or False.
    """
    
    def __init__(self, model_path='tamil_news_classifier.joblib'):
        """
        Initialize the classifier.
        
        Args:
            model_path (str): Path to save/load the trained model.
        """
        self.model_path = model_path
        self.model = None
        self.vectorizer = None
        self.tamil_stopwords = set(stopwords.words('tamil'))
        self.stemmer = SnowballStemmer('tamil')
        
    def clean_text(self, text):
        """
        Clean and preprocess Tamil text.
        
        Args:
            text (str): Input text to clean.
            
        Returns:
            str: Cleaned text.
        """
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and stem
        tokens = [self.stemmer.stem(word) for word in tokens if word not in self.tamil_stopwords]
        return ' '.join(tokens)
    
    def load_data(self, filepath):
        """
        Load and preprocess the dataset.
        
        Args:
            filepath (str): Path to the dataset file.
            
        Returns:
            tuple: (X, y) where X is the text data and y are the labels.
        """
        try:
            df = pd.read_csv(filepath)
            # Assuming columns are 'text' and 'label' (0 for False, 1 for True)
            df['cleaned_text'] = df['text'].apply(self.clean_text)
            X = df['cleaned_text'].values
            y = df['label'].values
            return X, y
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def train(self, X, y):
        """
        Train the classification model.
        
        Args:
            X (array-like): Text data.
            y (array-like): Labels.
        """
        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Create pipeline with TF-IDF and Logistic Regression
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
            ('clf', LogisticRegression(random_state=42))
        ])
        
        # Define parameter grid for GridSearch
        param_grid = {
            'tfidf__max_df': [0.75, 0.85],
            'tfidf__min_df': [2, 3],
            'clf__C': [0.1, 1, 10],
            'clf__penalty': ['l1', 'l2'],
            'clf__solver': ['liblinear']
        }
        
        # Perform grid search
        grid_search = GridSearchCV(
            pipeline, param_grid, cv=5, n_jobs=-1, verbose=1
        )
        
        print("Training model...")
        grid_search.fit(X_train, y_train)
        
        # Save the best model
        self.model = grid_search.best_estimator_
        
        # Evaluate on test set
        y_pred = self.model.predict(X_test)
        print("Model evaluation:")
        print(classification_report(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
        
        # Save the trained model
        self.save_model()
    
    def save_model(self):
        """Save the trained model to disk."""
        try:
            joblib.dump(self.model, self.model_path)
            print(f"Model saved to {self.model_path}")
        except Exception as e:
            print(f"Error saving model: {str(e)}")
    
    def load_model(self):
        """Load a trained model from disk."""
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
                print(f"Model loaded from {self.model_path}")
                return True
            else:
                print("No saved model found.")
                return False
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return False
    
    def predict(self, text):
        """
        Predict whether a news article is True or False.
        
        Args:
            text (str): News article text to classify.
            
        Returns:
            dict: Prediction result with confidence scores.
        """
        if not self.model:
            if not self.load_model():
                raise ValueError("Model not trained or loaded.")
        
        cleaned_text = self.clean_text(text)
        prediction = self.model.predict([cleaned_text])[0]
        proba = self.model.predict_proba([cleaned_text])[0]
        
        return {
            'prediction': 'True' if prediction == 1 else 'False',
            'confidence': {
                'True': float(proba[1]),
                'False': float(proba[0])
            }
        }

# Example usage
if __name__ == "__main__":
    # Initialize classifier
    classifier = TamilNewsClassifier()
    
    # Example: Train the model (uncomment when you have data)
    # X, y = classifier.load_data('tamil_news_dataset.csv')
    # classifier.train(X, y)
    
    # Example: Make a prediction
    sample_text = "உலக சுகாதார நிறுவனம் கோவிட்-19 தடுப்பூசி பற்றி புதிய வழிகாட்டுதல்களை வெளியிட்டுள்ளது."
    try:
        result = classifier.predict(sample_text)
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: True: {result['confidence']['True']:.2f}, False: {result['confidence']['False']:.2f}")
    except Exception as e:
        print(f"Prediction error: {str(e)}")
```
