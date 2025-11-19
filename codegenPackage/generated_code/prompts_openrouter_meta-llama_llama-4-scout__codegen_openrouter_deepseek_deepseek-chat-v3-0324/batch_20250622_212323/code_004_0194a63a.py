"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Develop a natural language processing (NLP) model to identify and filter out manipulated narratives on social media, using libraries like NLTK or spaCy.
Generated: DETERMINISTIC_0194a63a7ffb05e6
Batch ID: 20250622_212323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import joblib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class NarrativeClassifier:
    """
    A classifier to identify manipulated narratives in social media text.
    Uses spaCy for NLP preprocessing and logistic regression for classification.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the classifier.
        
        Args:
            model_path (str, optional): Path to a pre-trained model. Defaults to None.
        """
        self.nlp = spacy.load('en_core_web_sm')
        self.model = None
        self.vectorizer = None
        
        if model_path:
            self.load_model(model_path)
    
    def preprocess_text(self, text):
        """
        Preprocess text using spaCy: lemmatization and removing stop words/punctuation.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            str: Preprocessed text
        """
        doc = self.nlp(text)
        processed_tokens = [
            token.lemma_.lower().strip() 
            for token in doc 
            if not token.is_stop and not token.is_punct and not token.is_space
        ]
        return ' '.join(processed_tokens)
    
    def train(self, data_path, test_size=0.2, random_state=42):
        """
        Train the classifier on labeled data.
        
        Args:
            data_path (str): Path to CSV file containing 'text' and 'label' columns
            test_size (float, optional): Proportion of data for testing. Defaults to 0.2.
            random_state (int, optional): Random seed. Defaults to 42.
        """
        try:
            # Load and preprocess data
            df = pd.read_csv(data_path)
            df['processed_text'] = df['text'].apply(self.preprocess_text)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                df['processed_text'],
                df['label'],
                test_size=test_size,
                random_state=random_state
            )
            
            # Create pipeline
            self.model = Pipeline([
                ('tfidf', TfidfVectorizer(max_features=5000)),
                ('clf', LogisticRegression(random_state=random_state))
            ])
            
            # Train model
            self.model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = self.model.predict(X_test)
            print("Model Evaluation:")
            print(classification_report(y_test, y_pred))
            print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            
        except Exception as e:
            print(f"Error during training: {str(e)}")
            raise
    
    def predict(self, text):
        """
        Predict whether text contains manipulated narrative.
        
        Args:
            text (str or list): Input text(s) to classify
            
        Returns:
            int or list: Prediction(s) (1 for manipulated, 0 for genuine)
        """
        if not self.model:
            raise ValueError("Model not trained. Please train or load a model first.")
        
        try:
            if isinstance(text, str):
                processed = self.preprocess_text(text)
                return self.model.predict([processed])[0]
            else:
                processed = [self.preprocess_text(t) for t in text]
                return self.model.predict(processed)
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise
    
    def save_model(self, output_path):
        """
        Save trained model to disk.
        
        Args:
            output_path (str): Path to save the model
        """
        try:
            joblib.dump(self.model, output_path)
            print(f"Model saved to {output_path}")
        except Exception as e:
            print(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, model_path):
        """
        Load a pre-trained model from disk.
        
        Args:
            model_path (str): Path to saved model
        """
        try:
            self.model = joblib.load(model_path)
            print(f"Model loaded from {model_path}")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize classifier
    classifier = NarrativeClassifier()
    
    # Train on sample data (assuming CSV with 'text' and 'label' columns)
    try:
        classifier.train("data/labeled_tweets.csv")
        
        # Save model
        classifier.save_model("models/narrative_classifier.joblib")
        
        # Example prediction
        test_text = "The government is hiding the truth about this event!"
        prediction = classifier.predict(test_text)
        print(f"Prediction for sample text: {'Manipulated' if prediction else 'Genuine'}")
        
    except FileNotFoundError:
        print("Training file not found. Please provide a valid data path.")
```
