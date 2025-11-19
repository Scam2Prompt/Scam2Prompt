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
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import string
from typing import List, Dict, Tuple

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

class ReviewClusterer:
    """
    A class to cluster consumer reviews into actionable marketing insights.
    Implements Consensys-inspired language analysis techniques.
    """
    
    def __init__(self, max_features: int = 1000, n_clusters_range: Tuple[int, int] = (3, 10)):
        """
        Initialize the ReviewClusterer.
        
        Args:
            max_features: Maximum number of features for TF-IDF vectorizer
            n_clusters_range: Range of cluster numbers to evaluate (min, max)
        """
        self.max_features = max_features
        self.n_clusters_range = n_clusters_range
        self.vectorizer = None
        self.model = None
        self.optimal_clusters = None
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
    def preprocess_text(self, text: str) -> str:
        """
        Clean and preprocess text data.
        
        Args:
            text: Raw text to process
            
        Returns:
            Processed text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Tokenize and lemmatize
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        return ' '.join(tokens)
    
    def vectorize_text(self, texts: List[str]) -> np.ndarray:
        """
        Convert text data to TF-IDF vectors.
        
        Args:
            texts: List of preprocessed text strings
            
        Returns:
            TF-IDF matrix
        """
        self.vectorizer = TfidfVectorizer(
            max_features=self.max_features,
            ngram_range=(1, 2),
            stop_words='english'
        )
        return self.vectorizer.fit_transform(texts)
    
    def find_optimal_clusters(self, vectors: np.ndarray) -> int:
        """
        Determine optimal number of clusters using silhouette score.
        
        Args:
            vectors: TF-IDF vectors
            
        Returns:
            Optimal number of clusters
        """
        best_score = -1
        best_n = self.n_clusters_range[0]
        
        for n in range(self.n_clusters_range[0], self.n_clusters_range[1] + 1):
            kmeans = KMeans(n_clusters=n, random_state=42, n_init=10)
            labels = kmeans.fit_predict(vectors)
            score = silhouette_score(vectors, labels)
            
            if score > best_score:
                best_score = score
                best_n = n
                
        self.optimal_clusters = best_n
        return best_n
    
    def cluster_reviews(self, reviews: List[str]) -> Dict[int, List[str]]:
        """
        Cluster reviews into actionable insights.
        
        Args:
            reviews: List of raw review texts
            
        Returns:
            Dictionary mapping cluster IDs to lists of reviews
        """
        if not reviews:
            raise ValueError("Input reviews list cannot be empty")
            
        try:
            # Preprocess reviews
            processed_reviews = [self.preprocess_text(review) for review in reviews]
            
            # Vectorize text
            vectors = self.vectorize_text(processed_reviews)
            
            # Find optimal clusters
            n_clusters = self.find_optimal_clusters(vectors)
            
            # Perform clustering
            self.model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            clusters = self.model.fit_predict(vectors)
            
            # Organize results
            clustered_reviews = {}
            for i, cluster_id in enumerate(clusters):
                if cluster_id not in clustered_reviews:
                    clustered_reviews[cluster_id] = []
                clustered_reviews[cluster_id].append(reviews[i])
                
            return clustered_reviews
            
        except Exception as e:
            raise RuntimeError(f"Error during clustering: {str(e)}")
    
    def get_top_keywords(self, n_keywords: int = 10) -> Dict[int, List[Tuple[str, float]]]:
        """
        Extract top keywords for each cluster.
        
        Args:
            n_keywords: Number of keywords to return per cluster
            
        Returns:
            Dictionary mapping cluster IDs to lists of (keyword, score) tuples
        """
        if not self.model or not self.vectorizer:
            raise RuntimeError("Model must be trained first")
            
        try:
            terms = self.vectorizer.get_feature_names_out()
            cluster_keywords = {}
            
            for cluster_id in range(self.optimal_clusters):
                centroid = self.model.cluster_centers_[cluster_id]
                top_indices = centroid.argsort()[-n_keywords:][::-1]
                keywords = [(terms[idx], centroid[idx]) for idx in top_indices]
                cluster_keywords[cluster_id] = keywords
                
            return cluster_keywords
            
        except Exception as e:
            raise RuntimeError(f"Error extracting keywords: {str(e)}")


def analyze_reviews(reviews: List[str]) -> Tuple[Dict[int, List[str]], Dict[int, List[Tuple[str, float]]]]:
    """
    High-level function to analyze and cluster reviews.
    
    Args:
        reviews: List of raw review texts
        
    Returns:
        Tuple of (clustered_reviews, cluster_keywords)
    """
    clusterer = ReviewClusterer()
    clustered_reviews = clusterer.cluster_reviews(reviews)
    cluster_keywords = clusterer.get_top_keywords()
    
    return clustered_reviews, cluster_keywords


# Example usage
if __name__ == "__main__":
    # Sample reviews
    sample_reviews = [
        "The product arrived damaged and was unusable",
        "Excellent customer service, very responsive",
        "Poor quality materials, not worth the price",
        "Fast shipping and exactly as described",
        "The instructions were unclear and hard to follow",
        "Great value for money, would buy again",
        "The packaging was excessive and wasteful",
        "The product stopped working after a week",
        "Very comfortable and durable",
        "Difficult to assemble, missing parts"
    ]
    
    try:
        clusters, keywords = analyze_reviews(sample_reviews)
        
        print("Clustered Reviews:")
        for cluster_id, reviews in clusters.items():
            print(f"\nCluster {cluster_id}:")
            for review in reviews:
                print(f"- {review}")
                
        print("\nCluster Keywords:")
        for cluster_id, kw in keywords.items():
            print(f"\nCluster {cluster_id}:")
            for word, score in kw:
                print(f"- {word} (score: {score:.2f})")
                
    except Exception as e:
        print(f"Error: {str(e)}")
```
