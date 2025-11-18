"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Create a script to perform category-specific deep dives into e-commerce reviews using machine learning techniques, as outlined in Consensys's Explorer service, to identify drivers and drainers of ratings.
Generated: DETERMINISTIC_a6656be824dac666
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewAnalyzer:
    def __init__(self, data_path):
        """
        Initialize the ReviewAnalyzer with the path to the review data.

        :param data_path: str, path to the CSV file containing reviews
        """
        self.data_path = data_path
        self.model = None
        self.vectorizer = None

    def load_data(self):
        """
        Load the review data from a CSV file.

        :returns: pd.DataFrame, containing the loaded reviews
        """
        try:
            data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")
            return data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def preprocess_data(self, data):
        """
        Preprocess the review data to make it suitable for training.

        :param data: pd.DataFrame, input review data
        :returns: tuple, (features, labels)
        """
        if 'review_text' not in data or 'rating' not in data:
            raise ValueError("Input data must contain 'review_text' and 'rating' columns.")

        features = data['review_text']
        labels = data['rating'].apply(lambda x: 'positive' if x > 3 else 'negative')
        logging.info("Data preprocessed successfully.")
        return features, labels

    def train_model(self, features, labels):
        """
        Train a machine learning model using the provided features and labels.

        :param features: pd.Series, the review texts
        :param labels: pd.Series, the corresponding labels
        """
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        # Creating a pipeline for vectorization and model training
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.model.fit(X_train, y_train)
        logging.info("Model trained successfully.")

        # Evaluate the model
        predictions = self.model.predict(X_test)
        report = classification_report(y_test, predictions)
        logging.info(f"Model evaluation report:\n{report}")

    def predict(self, new_reviews):
        """
        Make predictions on new reviews using the trained model.

        :param new_reviews: list, a list of new review texts
        :returns: list, predicted labels for the new reviews
        """
        if self.model is None:
            raise RuntimeError("Model has not been trained yet.")
        
        predictions = self.model.predict(new_reviews)
        logging.info("Predictions made successfully.")
        return predictions

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = ReviewAnalyzer('ecommerce_reviews.csv')
        review_data = analyzer.load_data()
        features, labels = analyzer.preprocess_data(review_data)
        analyzer.train_model(features, labels)

        # Example predictions on new reviews
        new_reviews = ["Great product!", "Terrible experience."]
        predictions = analyzer.predict(new_reviews)
        print("Predictions:", predictions)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
