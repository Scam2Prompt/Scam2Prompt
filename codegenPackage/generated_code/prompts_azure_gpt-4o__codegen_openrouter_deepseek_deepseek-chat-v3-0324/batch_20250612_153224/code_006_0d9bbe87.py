"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Write code to automate the process of categorizing news articles based on human rights violations, inspired by Jusoor International's media advocacy efforts.
Generated: DETERMINISTIC_0d9bbe8773c12f45
Batch ID: 20250612_153224
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
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
import joblib
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('news_categorization.log'),
        logging.StreamHandler()
    ]
)

class NewsCategorizer:
    """
    A machine learning pipeline for categorizing news articles about human rights violations.
    """
    
    def __init__(self, model_path='models/news_categorizer.joblib'):
        self.model_path = model_path
        self.model = None
        self.categories = [
            'Arbitrary Arrest',
            'Torture',
            'Freedom of Expression',
            'Discrimination',
            'Extrajudicial Killing',
            'Forced Displacement',
            'Other'
        ]
        
    def load_data(self, filepath):
        """
        Load and preprocess training data from a CSV file.
        Expected columns: 'text', 'category'
        """
        try:
            df = pd.read_csv(filepath)
            df = df.dropna(subset=['text', 'category'])
            df['category'] = df['category'].str.strip().str.title()
            
            # Map categories to our predefined list
            df['category'] = df['category'].apply(
                lambda x: x if x in self.categories else 'Other'
            )
            
            logging.info(f"Loaded {len(df)} articles from {filepath}")
            return df['text'], df['category']
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise

    def train_model(self, X, y, test_size=0.2, random_state=42):
        """
        Train a text classification model using TF-IDF and LinearSVC.
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Create pipeline
            self.model = Pipeline([
                ('tfidf', TfidfVectorizer(
                    max_features=10000,
                    ngram_range=(1, 2),
                    stop_words='english'
                )),
                ('clf', LinearSVC(
                    class_weight='balanced',
                    max_iter=10000,
                    random_state=random_state
                ))
            ])
            
            # Train model
            self.model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = self.model.predict(X_test)
            report = classification_report(y_test, y_pred, target_names=self.categories)
            logging.info("\nClassification Report:\n" + report)
            
            return self.model
        except Exception as e:
            logging.error(f"Error training model: {str(e)}")
            raise

    def save_model(self):
        """Save the trained model to disk."""
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
            logging.info(f"Model saved to {self.model_path}")
        except Exception as e:
            logging.error(f"Error saving model: {str(e)}")
            raise

    def load_saved_model(self):
        """Load a previously trained model from disk."""
        try:
            self.model = joblib.load(self.model_path)
            logging.info(f"Model loaded from {self.model_path}")
            return self.model
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
            raise

    def predict_category(self, articles):
        """
        Predict categories for new articles.
        articles: List of strings (article texts)
        Returns: List of predicted categories
        """
        if not self.model:
            try:
                self.load_saved_model()
            except:
                raise ValueError("No trained model available")
        
        try:
            predictions = self.model.predict(articles)
            return predictions
        except Exception as e:
            logging.error(f"Error making predictions: {str(e)}")
            raise

def main():
    # Example usage
    categorizer = NewsCategorizer()
    
    try:
        # Train new model (uncomment when you have training data)
        # X, y = categorizer.load_data('data/training_articles.csv')
        # categorizer.train_model(X, y)
        # categorizer.save_model()
        
        # Or load existing model
        categorizer.load_saved_model()
        
        # Example predictions
        test_articles = [
            "Journalist detained without trial for criticizing government policies",
            "Ethnic minority village forcibly evacuated for dam construction",
            "Protestors beaten by police during peaceful demonstration"
        ]
        
        predictions = categorizer.predict_category(test_articles)
        for article, category in zip(test_articles, predictions):
            print(f"Article: {article[:60]}...")
            print(f"Predicted Category: {category}\n")
            
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
```
