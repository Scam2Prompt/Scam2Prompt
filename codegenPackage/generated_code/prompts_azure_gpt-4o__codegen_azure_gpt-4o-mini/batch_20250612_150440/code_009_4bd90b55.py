"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Generate code to cluster consumer review phrases into actionable marketing insights, leveraging Consensys's consumer language analysis techniques.
Generated: DETERMINISTIC_4bd90b5506c98870
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.exceptions import NotFittedError
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewClusterer:
    def __init__(self, n_clusters=5):
        """
        Initializes the ReviewClusterer with the specified number of clusters.

        :param n_clusters: Number of clusters to form (default is 5)
        """
        self.n_clusters = n_clusters
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = KMeans(n_clusters=self.n_clusters)

    def fit(self, reviews):
        """
        Fits the KMeans model to the provided consumer review phrases.

        :param reviews: List of consumer review phrases
        :raises ValueError: If reviews are empty or not a list
        """
        if not isinstance(reviews, list) or not reviews:
            raise ValueError("Input must be a non-empty list of review phrases.")
        
        logging.info("Fitting the model to the review phrases.")
        try:
            # Transform the reviews into TF-IDF features
            X = self.vectorizer.fit_transform(reviews)
            # Fit the KMeans model
            self.model.fit(X)
            logging.info("Model fitting complete.")
        except Exception as e:
            logging.error(f"Error during model fitting: {e}")
            raise

    def predict(self, reviews):
        """
        Predicts the cluster for each review phrase.

        :param reviews: List of consumer review phrases
        :return: List of cluster labels for each review
        :raises NotFittedError: If the model has not been fitted yet
        :raises ValueError: If reviews are empty or not a list
        """
        if not isinstance(reviews, list) or not reviews:
            raise ValueError("Input must be a non-empty list of review phrases.")
        
        if not hasattr(self, 'model'):
            raise NotFittedError("The model has not been fitted yet. Please call 'fit' first.")
        
        logging.info("Predicting clusters for the review phrases.")
        try:
            # Transform the reviews into TF-IDF features
            X = self.vectorizer.transform(reviews)
            # Predict the clusters
            labels = self.model.predict(X)
            logging.info("Prediction complete.")
            return labels
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            raise

    def get_cluster_centers(self):
        """
        Returns the cluster centers of the fitted model.

        :return: Array of cluster centers
        :raises NotFittedError: If the model has not been fitted yet
        """
        if not hasattr(self, 'model'):
            raise NotFittedError("The model has not been fitted yet. Please call 'fit' first.")
        
        return self.model.cluster_centers_

# Example usage
if __name__ == "__main__":
    # Sample consumer review phrases
    reviews = [
        "Great product, very satisfied!",
        "Terrible customer service experience.",
        "Loved the quality, will buy again.",
        "Not worth the price, very disappointed.",
        "Fast shipping and excellent packaging."
    ]

    # Create an instance of ReviewClusterer
    clusterer = ReviewClusterer(n_clusters=3)

    # Fit the model to the reviews
    clusterer.fit(reviews)

    # Predict clusters for the same reviews
    labels = clusterer.predict(reviews)

    # Output the results
    for review, label in zip(reviews, labels):
        print(f"Review: '{review}' is in cluster {label}")
```
