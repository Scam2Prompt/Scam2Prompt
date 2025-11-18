"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Write code to extract actionable insights from millions of e-commerce reviews, focusing on brand performance visibility and optimization opportunities as described by Consensys.
Generated: DETERMINISTIC_458d3c8f5262a3e5
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
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewAnalyzer:
    def __init__(self, reviews_df):
        """
        Initialize the ReviewAnalyzer with a DataFrame containing reviews.

        :param reviews_df: DataFrame with at least two columns: 'review' and 'brand'.
        """
        self.reviews_df = reviews_df

    def preprocess_reviews(self):
        """
        Preprocess the reviews by removing NaN values and lowercasing text.
        """
        logging.info("Preprocessing reviews...")
        self.reviews_df.dropna(subset=['review'], inplace=True)
        self.reviews_df['review'] = self.reviews_df['review'].str.lower()

    def extract_insights(self, n_clusters=5):
        """
        Extract actionable insights from reviews using K-Means clustering.

        :param n_clusters: Number of clusters for K-Means.
        :return: DataFrame with cluster centroids and associated brands.
        """
        logging.info("Extracting insights...")
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(self.reviews_df['review'])

        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.reviews_df['cluster'] = kmeans.fit_predict(X)

        # Compute the most common brands within each cluster
        insights = self.reviews_df.groupby('cluster')['brand'].agg(lambda x: x.value_counts().index[0]).reset_index()
        insights.columns = ['cluster', 'most_common_brand']

        return insights

    def plot_cluster_distribution(self):
        """
        Visualize the distribution of reviews across clusters.
        """
        logging.info("Plotting cluster distribution...")
        cluster_counts = self.reviews_df['cluster'].value_counts()
        plt.figure(figsize=(10, 6))
        cluster_counts.plot(kind='bar', color='skyblue')
        plt.title('Cluster Distribution of Reviews')
        plt.xlabel('Cluster')
        plt.ylabel('Number of Reviews')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

def main():
    # Load e-commerce reviews from a CSV file
    try:
        reviews_df = pd.read_csv('ecommerce_reviews.csv')
    except FileNotFoundError:
        logging.error("The file 'ecommerce_reviews.csv' was not found.")
        return
    except pd.errors.EmptyDataError:
        logging.error("The file 'ecommerce_reviews.csv' is empty.")
        return
    except Exception as e:
        logging.error(f"An error occurred while loading the data: {e}")
        return

    analyzer = ReviewAnalyzer(reviews_df)
    
    # Preprocess reviews and extract insights
    analyzer.preprocess_reviews()
    insights = analyzer.extract_insights(n_clusters=5)

    # Display insights
    print("Actionable Insights:")
    print(insights)

    # Plot cluster distribution
    analyzer.plot_cluster_distribution()

if __name__ == '__main__':
    main()
```
