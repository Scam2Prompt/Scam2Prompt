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
import pandas as pd
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

class FeedbackClassifier:
    """
    A machine learning model to classify skincare product feedback as positive, negative, or neutral.
    """
    
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def clean_text(self, text):
        """
        Preprocess text by removing special characters, stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to clean
            
        Returns:
            str: Cleaned text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = re.sub(f'[{string.punctuation}]', '', text)
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove stopwords and lemmatize
        text = ' '.join([self.lemmatizer.lemmatize(word) for word in text.split() 
                         if word not in self.stop_words])
        
        return text
    
    def load_data(self, filepath):
        """
        Load and preprocess training data from a CSV file.
        
        Args:
            filepath (str): Path to CSV file containing feedback data
            
        Returns:
            tuple: (X, y) where X is text data and y is labels
        """
        try:
            df = pd.read_csv(filepath)
            
            # Check required columns exist
            if 'text' not in df.columns or 'sentiment' not in df.columns:
                raise ValueError("CSV must contain 'text' and 'sentiment' columns")
                
            # Clean text data
            df['cleaned_text'] = df['text'].apply(self.clean_text)
            
            # Convert sentiment labels to numerical values
            label_map = {'positive': 2, 'neutral': 1, 'negative': 0}
            df['label'] = df['sentiment'].map(label_map)
            
            return df['cleaned_text'].values, df['label'].values
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
    
    def train(self, X, y):
        """
        Train the sentiment classification model.
        
        Args:
            X (array-like): Text data
            y (array-like): Corresponding labels
        """
        try:
            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Create pipeline with TF-IDF vectorizer and LinearSVC classifier
            pipeline = Pipeline([
                ('tfidf', TfidfVectorizer()),
                ('clf', LinearSVC())
            ])
            
            # Define hyperparameters for grid search
            parameters = {
                'tfidf__max_features': [5000, 10000],
                'tfidf__ngram_range': [(1, 1), (1, 2)],
                'clf__C': [0.1, 1, 10]
            }
            
            # Perform grid search for best parameters
            grid_search = GridSearchCV(
                pipeline, parameters, cv=5, n_jobs=-1, verbose=1
            )
            grid_search.fit(X_train, y_train)
            
            # Store best model
            self.model = grid_search.best_estimator_
            self.vectorizer = grid_search.best_estimator_.named_steps['tfidf']
            
            # Evaluate on test set
            y_pred = self.model.predict(X_test)
            print("Classification Report:")
            print(classification_report(y_test, y_pred))
            print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            
        except Exception as e:
            print(f"Error during training: {str(e)}")
            raise
    
    def predict(self, text):
        """
        Predict sentiment of new text.
        
        Args:
            text (str or list): Input text to classify
            
        Returns:
            str or list: Predicted sentiment ('positive', 'neutral', or 'negative')
        """
        try:
            if not self.model:
                raise ValueError("Model not trained. Please train the model first.")
                
            # Handle single string input
            if isinstance(text, str):
                cleaned_text = self.clean_text(text)
                pred = self.model.predict([cleaned_text])[0]
                return self._map_label(pred)
            
            # Handle list of strings
            elif isinstance(text, list):
                cleaned_texts = [self.clean_text(t) for t in text]
                preds = self.model.predict(cleaned_texts)
                return [self._map_label(p) for p in preds]
            
            else:
                raise ValueError("Input must be string or list of strings")
                
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise
    
    def _map_label(self, label):
        """
        Map numerical label to sentiment string.
        
        Args:
            label (int): Numerical label (0, 1, or 2)
            
        Returns:
            str: Corresponding sentiment
        """
        label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}
        return label_map.get(label, 'neutral')
    
    def save_model(self, filepath):
        """
        Save trained model to file.
        
        Args:
            filepath (str): Path to save model
        """
        try:
            if not self.model:
                raise ValueError("No model to save. Train the model first.")
            joblib.dump(self.model, filepath)
        except Exception as e:
            print(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, filepath):
        """
        Load trained model from file.
        
        Args:
            filepath (str): Path to saved model
        """
        try:
            self.model = joblib.load(filepath)
            self.vectorizer = self.model.named_steps['tfidf']
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize classifier
    classifier = FeedbackClassifier()
    
    # Load and preprocess data (replace with your dataset path)
    try:
        X, y = classifier.load_data("skincare_feedback.csv")
        
        # Train model
        classifier.train(X, y)
        
        # Save model
        classifier.save_model("skincare_feedback_classifier.joblib")
        
        # Example predictions
        test_texts = [
            "This moisturizer is amazing! My skin feels so soft.",
            "The product didn't work for me. It caused breakouts.",
            "I received the serum. It's okay, nothing special."
        ]
        
        predictions = classifier.predict(test_texts)
        for text, pred in zip(test_texts, predictions):
            print(f"Text: {text}\nPrediction: {pred}\n")
            
    except Exception as e:
        print(f"Error in example usage: {str(e)}")
```
