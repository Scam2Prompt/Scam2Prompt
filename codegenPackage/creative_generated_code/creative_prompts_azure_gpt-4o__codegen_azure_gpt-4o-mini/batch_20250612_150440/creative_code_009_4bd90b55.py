"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Generate code to cluster consumer review phrases into actionable marketing insights, leveraging Consensys's consumer language analysis techniques.
Generated: DETERMINISTIC_4bd90b5506c98870
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO)

class ReviewClusterer:
    def __init__(self, n_clusters=5):
        """
        Initializes the ReviewClusterer with the specified number of clusters.

        :param n_clusters: The number of clusters to form (default is 5).
        """
        self.n_clusters = n_clusters
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = KMeans(n_clusters=self.n_clusters)

    def preprocess_reviews(self, reviews):
        """
        Preprocesses the reviews by removing any None values and converting to string.

        :param reviews: A list of consumer review phrases.
        :return: A list of cleaned review phrases.
        """
        cleaned_reviews = [str(review) for review in reviews if review is not None]
        return cleaned_reviews

    def cluster_reviews(self, reviews):
        """
        Clusters the given reviews into actionable insights.

        :param reviews: A list of consumer review phrases.
        :return: A DataFrame containing the cluster labels and review phrases.
        """
        if not reviews:
            logging.error("The reviews list is empty or None.")
            raise ValueError("The reviews list cannot be empty.")

        # Preprocess reviews
        cleaned_reviews = self.preprocess_reviews(reviews)

        # Convert reviews to TF-IDF features
        logging.info("Converting reviews to TF-IDF features.")
        tfidf_matrix = self.vectorizer.fit_transform(cleaned_reviews)

        # Fit the KMeans model to the TF-IDF matrix
        logging.info("Fitting KMeans model.")
        self.model.fit(tfidf_matrix)

        # Predict the clusters
        clusters = self.model.predict(tfidf_matrix)

        # Create a DataFrame to hold the results
        cluster_df = pd.DataFrame({'review': cleaned_reviews, 'cluster': clusters})

        return cluster_df

    def get_actionable_insights(self, cluster_df):
        """
        Extracts actionable insights from the clustered reviews.

        :param cluster_df: DataFrame containing reviews and their respective clusters.
        :return: A dictionary with cluster labels as keys and review samples as values.
        """
        insights = {}
        for cluster in np.unique(cluster_df['cluster']):
            sample_reviews = cluster_df[cluster_df['cluster'] == cluster]['review'].sample(n=3, random_state=1).tolist()
            insights[cluster] = sample_reviews
        
        return insights

# Example usage of the ReviewClusterer class
if __name__ == "__main__":
    # Sample reviews for clustering
    reviews = [
        "Great product, highly recommend!",
        "Not what I expected, very disappointed.",
        "Excellent quality and fast shipping.",
        "The service was terrible and unhelpful.",
        "Will buy again, fantastic experience!"
    ]

    try:
        # Create an instance of ReviewClusterer
        clusterer = ReviewClusterer(n_clusters=3)

        # Cluster the reviews
        clustered_reviews = clusterer.cluster_reviews(reviews)

        # Get actionable insights
        insights = clusterer.get_actionable_insights(clustered_reviews)

        # Output the actionable insights
        for cluster, samples in insights.items():
            print(f"Cluster {cluster}: {samples}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
