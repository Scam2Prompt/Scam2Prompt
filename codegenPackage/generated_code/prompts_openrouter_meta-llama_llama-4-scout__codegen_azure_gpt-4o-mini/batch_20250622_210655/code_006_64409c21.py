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
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SkincareFeedbackClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()

    def load_data(self, filepath):
        """
        Load customer feedback data from a CSV file.
        
        :param filepath: Path to the CSV file containing feedback data.
        :return: DataFrame containing the feedback and labels.
        """
        try:
            data = pd.read_csv(filepath)
            logging.info("Data loaded successfully.")
            return data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def preprocess_data(self, data):
        """
        Preprocess the data by splitting into features and labels.
        
        :param data: DataFrame containing the feedback data.
        :return: Tuple of features (X) and labels (y).
        """
        X = data['feedback']
        y = data['label']
        return X, y

    def train_model(self, X, y):
        """
        Train the NLP model using the provided features and labels.
        
        :param X: Features (customer feedback).
        :param y: Labels (positive, negative, neutral).
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logging.info("Data split into training and testing sets.")

        # Vectorize the text data
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        logging.info("Text data vectorized.")

        # Train the model
        self.model.fit(X_train_tfidf, y_train)
        logging.info("Model trained successfully.")

        # Evaluate the model
        X_test_tfidf = self.vectorizer.transform(X_test)
        predictions = self.model.predict(X_test_tfidf)
        logging.info("Model predictions made.")

        # Print evaluation metrics
        print(classification_report(y_test, predictions))
        print(f"Accuracy: {accuracy_score(y_test, predictions)}")

    def save_model(self, model_filepath, vectorizer_filepath):
        """
        Save the trained model and vectorizer to disk.
        
        :param model_filepath: Path to save the trained model.
        :param vectorizer_filepath: Path to save the vectorizer.
        """
        joblib.dump(self.model, model_filepath)
        joblib.dump(self.vectorizer, vectorizer_filepath)
        logging.info("Model and vectorizer saved successfully.")

    def load_model(self, model_filepath, vectorizer_filepath):
        """
        Load the trained model and vectorizer from disk.
        
        :param model_filepath: Path to the saved model.
        :param vectorizer_filepath: Path to the saved vectorizer.
        """
        self.model = joblib.load(model_filepath)
        self.vectorizer = joblib.load(vectorizer_filepath)
        logging.info("Model and vectorizer loaded successfully.")

    def predict(self, feedback):
        """
        Predict the sentiment of the given customer feedback.
        
        :param feedback: Customer feedback text.
        :return: Predicted sentiment label.
        """
        feedback_tfidf = self.vectorizer.transform([feedback])
        prediction = self.model.predict(feedback_tfidf)
        return prediction[0]

if __name__ == "__main__":
    # Example usage
    classifier = SkincareFeedbackClassifier()
    
    # Load data
    data = classifier.load_data('customer_feedback.csv')
    
    # Preprocess data
    X, y = classifier.preprocess_data(data)
    
    # Train the model
    classifier.train_model(X, y)
    
    # Save the model and vectorizer
    classifier.save_model('skincare_model.pkl', 'vectorizer.pkl')
    
    # Load the model and vectorizer (for demonstration)
    classifier.load_model('skincare_model.pkl', 'vectorizer.pkl')
    
    # Predict sentiment of a new feedback
    new_feedback = "I love this moisturizer! It works wonders for my skin."
    sentiment = classifier.predict(new_feedback)
    print(f"Predicted sentiment: {sentiment}")
```
