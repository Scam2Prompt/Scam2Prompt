"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Write code to extract actionable insights from millions of e-commerce reviews, focusing on brand performance visibility and optimization opportunities as described by Consensys.
Generated: DETERMINISTIC_458d3c8f5262a3e5
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
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Set up visualization style
sns.set(style="whitegrid")

class ReviewAnalyzer:
    def __init__(self, reviews_df):
        """
        Initialize the ReviewAnalyzer with a DataFrame of reviews.

        :param reviews_df: DataFrame containing e-commerce reviews with 'review_text' and 'brand' columns.
        """
        self.reviews_df = reviews_df
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.kmeans = None
        self.pca = None

    def preprocess_reviews(self):
        """
        Preprocess the reviews by removing NaN values and ensuring the text is clean.
        """
        # Drop rows with NaN values in 'review_text'
        self.reviews_df.dropna(subset=['review_text'], inplace=True)

    def vectorize_reviews(self):
        """
        Convert the review texts into TF-IDF vectors.
        """
        try:
            tfidf_matrix = self.vectorizer.fit_transform(self.reviews_df['review_text'])
            return tfidf_matrix
        except Exception as e:
            print(f"Error during vectorization: {e}")
            return None

    def cluster_reviews(self, n_clusters=5):
        """
        Cluster the reviews using KMeans.

        :param n_clusters: Number of clusters to form.
        """
        tfidf_matrix = self.vectorize_reviews()
        if tfidf_matrix is None:
            return
        
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.kmeans.fit(tfidf_matrix)
        self.reviews_df['cluster'] = self.kmeans.labels_

    def reduce_dimensions(self):
        """
        Reduce the dimensions of the TF-IDF matrix for visualization using PCA.
        """
        if self.kmeans is None:
            print("Clustering has not been performed yet.")
            return None
        
        tfidf_matrix = self.vectorize_reviews()
        self.pca = PCA(n_components=2)
        reduced_data = self.pca.fit_transform(tfidf_matrix.toarray())
        return reduced_data

    def visualize_clusters(self):
        """
        Visualize the clustered reviews in a 2D space.
        """
        reduced_data = self.reduce_dimensions()
        if reduced_data is None:
            return
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], hue=self.reviews_df['cluster'], palette='viridis', s=100)
        plt.title('Clustered E-commerce Reviews')
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.legend(title='Cluster')
        plt.show()

    def extract_insights(self):
        """
        Extract actionable insights based on brand performance and optimization opportunities.
        """
        brand_performance = self.reviews_df.groupby('brand')['cluster'].value_counts().unstack().fillna(0)
        print("Brand Performance Visibility:\n", brand_performance)

        # Identify brands with the most reviews in each cluster
        optimization_opportunities = self.reviews_df.groupby('brand')['cluster'].value_counts().idxmax(level=0)
        print("Optimization Opportunities:\n", optimization_opportunities)

# Example usage
if __name__ == "__main__":
    # Load the reviews dataset
    try:
        reviews_data = pd.read_csv('ecommerce_reviews.csv')  # Ensure the CSV file exists
        analyzer = ReviewAnalyzer(reviews_data)
        analyzer.preprocess_reviews()
        analyzer.cluster_reviews(n_clusters=5)
        analyzer.visualize_clusters()
        analyzer.extract_insights()
    except FileNotFoundError:
        print("The specified file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
