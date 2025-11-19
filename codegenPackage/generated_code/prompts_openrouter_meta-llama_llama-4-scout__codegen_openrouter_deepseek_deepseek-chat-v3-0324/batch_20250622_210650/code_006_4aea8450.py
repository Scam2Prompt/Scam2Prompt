"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Develop a natural language processing (NLP) model that can be used to analyze and understand the stories of women who have experienced sexual aggression, and provide them with relevant resources and support.
Generated: DETERMINISTIC_4aea84504f7fceaa
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
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class SexualAggressionSupportModel:
    """
    NLP model to analyze stories of sexual aggression survivors and provide resources.
    """
    
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.resource_mapping = {
            'legal': ["National Sexual Assault Hotline", "RAINN Legal Resources"],
            'emotional': ["Crisis Text Line", "Therapy for Sexual Trauma"],
            'medical': ["Local Hospital SANE Program", "Planned Parenthood"],
            'general': ["RAINN", "NSVRC", "Local Support Groups"]
        }
    
    def preprocess_text(self, text):
        """
        Clean and preprocess text data.
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Tokenize
        words = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
        
        return ' '.join(words)
    
    def train(self, data_path, test_size=0.2, random_state=42):
        """
        Train the model on labeled data.
        Data format: CSV with 'text' and 'label' columns
        Labels: legal, emotional, medical, general
        """
        try:
            # Load and preprocess data
            df = pd.read_csv(data_path)
            df['processed_text'] = df['text'].apply(self.preprocess_text)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                df['processed_text'], df['label'], test_size=test_size, random_state=random_state
            )
            
            # Create pipeline
            self.model = Pipeline([
                ('tfidf', TfidfVectorizer()),
                ('clf', LinearSVC())
            ])
            
            # Train model
            self.model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = self.model.predict(X_test)
            print(classification_report(y_test, y_pred))
            
            return True
        
        except Exception as e:
            print(f"Error during training: {str(e)}")
            return False
    
    def predict(self, text):
        """
        Predict the support category and return relevant resources.
        """
        try:
            if not self.model:
                raise ValueError("Model not trained. Please train the model first.")
            
            processed_text = self.preprocess_text(text)
            category = self.model.predict([processed_text])[0]
            resources = self.resource_mapping.get(category, [])
            
            return {
                'category': category,
                'resources': resources
            }
        
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return None
    
    def save_model(self, path):
        """
        Save trained model to disk.
        """
        try:
            joblib.dump(self.model, path)
            return True
        except Exception as e:
            print(f"Error saving model: {str(e)}")
            return False
    
    def load_model(self, path):
        """
        Load trained model from disk.
        """
        try:
            self.model = joblib.load(path)
            return True
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    model = SexualAggressionSupportModel()
    
    # Train model (uncomment with actual data path)
    # model.train('sexual_aggression_data.csv')
    
    # Example prediction
    test_story = "I was assaulted last night and need medical help"
    result = model.predict(test_story)
    print(f"Predicted category: {result['category']}")
    print("Suggested resources:")
    for resource in result['resources']:
        print(f"- {resource}")
```
