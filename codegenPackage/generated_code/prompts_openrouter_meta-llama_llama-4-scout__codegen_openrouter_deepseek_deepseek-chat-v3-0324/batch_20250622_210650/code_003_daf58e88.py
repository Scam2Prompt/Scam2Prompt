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
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import re
import string
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class BengaliTextClassifier:
    """
    Bengali language text classifier for news articles.
    """
    
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.classes_ = None
        self.stemmer = SnowballStemmer("bengali")
        self.stop_words = set(stopwords.words('bengali'))
        
    def clean_text(self, text):
        """
        Clean and preprocess Bengali text.
        """
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and stem
        tokens = [self.stemmer.stem(word) for word in tokens if word not in self.stop_words]
        return ' '.join(tokens)
    
    def load_data(self, filepath):
        """
        Load and preprocess dataset.
        Expected columns: 'text', 'category'
        """
        try:
            df = pd.read_csv(filepath)
            df['cleaned_text'] = df['text'].apply(self.clean_text)
            return df
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def train(self, X, y):
        """
        Train the classification model.
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Create pipeline
            pipeline = Pipeline([
                ('tfidf', TfidfVectorizer()),
                ('clf', LinearSVC())
            ])
            
            # Hyperparameter tuning
            parameters = {
                'tfidf__max_df': (0.5, 0.75, 1.0),
                'tfidf__ngram_range': ((1, 1), (1, 2)),
                'clf__C': (0.1, 1, 10)
            }
            
            grid_search = GridSearchCV(
                pipeline, parameters, cv=3, n_jobs=-1, verbose=1
            )
            
            grid_search.fit(X_train, y_train)
            
            # Save best model
            self.model = grid_search.best_estimator_
            self.classes_ = self.model.named_steps['clf'].classes_
            
            # Evaluate
            y_pred = self.model.predict(X_test)
            print(classification_report(y_test, y_pred))
            
            return grid_search.best_score_
        except Exception as e:
            raise Exception(f"Error during training: {str(e)}")
    
    def predict(self, text):
        """
        Predict category for new text.
        """
        if not self.model:
            raise Exception("Model not trained. Please train the model first.")
        
        cleaned_text = self.clean_text(text)
        return self.model.predict([cleaned_text])[0]
    
    def save_model(self, filepath):
        """
        Save trained model to file.
        """
        try:
            joblib.dump({
                'model': self.model,
                'classes': self.classes_
            }, filepath)
        except Exception as e:
            raise Exception(f"Error saving model: {str(e)}")
    
    def load_model(self, filepath):
        """
        Load trained model from file.
        """
        try:
            data = joblib.load(filepath)
            self.model = data['model']
            self.classes_ = data['classes']
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize classifier
    classifier = BengaliTextClassifier()
    
    # Load and prepare data (replace with your dataset)
    try:
        df = classifier.load_data("bengali_news_dataset.csv")
        X = df['cleaned_text']
        y = df['category']
        
        # Train model
        classifier.train(X, y)
        
        # Save model
        classifier.save_model("bengali_text_classifier.joblib")
        
        # Example prediction
        test_text = "রাজ্যের মুখ্যমন্ত্রী আজ একটি গুরুত্বপূর্ণ ঘোষণা করবেন"
        prediction = classifier.predict(test_text)
        print(f"Predicted category: {prediction}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
