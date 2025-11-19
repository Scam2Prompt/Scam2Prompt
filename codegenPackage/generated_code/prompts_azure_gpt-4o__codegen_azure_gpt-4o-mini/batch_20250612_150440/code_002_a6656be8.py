"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Create a script to perform category-specific deep dives into e-commerce reviews using machine learning techniques, as outlined in Consensys's Explorer service, to identify drivers and drainers of ratings.
Generated: DETERMINISTIC_a6656be824dac666
Batch ID: 20250612_150440
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewAnalyzer:
    def __init__(self, reviews_df):
        """
        Initialize the ReviewAnalyzer with a DataFrame of reviews.

        :param reviews_df: DataFrame containing 'review_text', 'rating', and 'category' columns
        """
        self.reviews_df = reviews_df
        self.model = None
        self.vectorizer = None

    def preprocess_data(self):
        """
        Preprocess the review data by filtering out rows with missing values
        and separating features and labels.
        """
        logging.info("Preprocessing data...")
        self.reviews_df.dropna(subset=['review_text', 'rating'], inplace=True)
        self.reviews_df['rating'] = self.reviews_df['rating'].apply(lambda x: 1 if x > 3 else 0)  # Binary classification
        self.X = self.reviews_df['review_text']
        self.y = self.reviews_df['rating']

    def vectorize_data(self):
        """
        Convert the review text into numerical format using TF-IDF vectorization.
        """
        logging.info("Vectorizing data...")
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.X_vectorized = self.vectorizer.fit_transform(self.X)

    def train_model(self):
        """
        Train a logistic regression model on the vectorized review data.
        """
        logging.info("Training model...")
        X_train, X_test, y_train, y_test = train_test_split(self.X_vectorized, self.y, test_size=0.2, random_state=42)
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        logging.info("Model evaluation:")
        logging.info(classification_report(y_test, y_pred))
        logging.info("Confusion Matrix:\n%s", confusion_matrix(y_test, y_pred))

    def save_model(self, model_path='review_model.pkl'):
        """
        Save the trained model and vectorizer to disk.

        :param model_path: Path to save the model
        """
        logging.info("Saving model to %s...", model_path)
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, 'vectorizer.pkl')

    def load_model(self, model_path='review_model.pkl'):
        """
        Load a trained model and vectorizer from disk.

        :param model_path: Path to load the model from
        """
        logging.info("Loading model from %s...", model_path)
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load('vectorizer.pkl')

    def predict(self, new_reviews):
        """
        Predict the ratings for new reviews.

        :param new_reviews: List of review texts to predict
        :return: List of predicted ratings
        """
        logging.info("Predicting ratings for new reviews...")
        new_reviews_vectorized = self.vectorizer.transform(new_reviews)
        predictions = self.model.predict(new_reviews_vectorized)
        return predictions

if __name__ == "__main__":
    # Example usage
    try:
        # Load your e-commerce reviews dataset
        reviews_data = pd.read_csv('ecommerce_reviews.csv')  # Ensure this file exists and has the correct format
        analyzer = ReviewAnalyzer(reviews_data)
        
        # Preprocess, vectorize, train, and save the model
        analyzer.preprocess_data()
        analyzer.vectorize_data()
        analyzer.train_model()
        analyzer.save_model()

        # Example prediction
        new_reviews = ["Great product, very satisfied!", "Terrible experience, will not buy again."]
        predictions = analyzer.predict(new_reviews)
        print("Predicted ratings:", predictions)

    except Exception as e:
        logging.error("An error occurred: %s", e)
```
