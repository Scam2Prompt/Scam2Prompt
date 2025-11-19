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
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess text by tokenizing, removing stop words, and lemmatizing.
    
    Parameters:
    text (str): Text to preprocess
    
    Returns:
    str: Preprocessed text
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

def cluster_reviews(reviews, n_clusters):
    """
    Cluster consumer review phrases into actionable marketing insights.
    
    Parameters:
    reviews (list): List of consumer review phrases
    n_clusters (int): Number of clusters
    
    Returns:
    dict: Cluster labels and corresponding review phrases
    """
    # Preprocess review text
    preprocessed_reviews = [preprocess_text(review) for review in reviews]
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_vectors = vectorizer.fit_transform(preprocessed_reviews)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    cluster_labels = kmeans.fit_predict(tfidf_vectors)
    
    # Group reviews by cluster label
    clusters = {}
    for i, label in enumerate(cluster_labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(reviews[i])
    
    return clusters

def main():
    # Sample consumer review phrases
    reviews = [
        "I loved the new product, it's amazing!",
        "The customer service was terrible.",
        "The product was okay, but the price was too high.",
        "I'm so happy with my purchase, great product!",
        "The product was broken, what a disappointment.",
        "The delivery was slow, but the product was great.",
        "I would definitely recommend this product.",
        "The product was not what I expected, sadly.",
        "The company has great values, I love their mission.",
        "The product was just okay, nothing special."
    ]
    
    # Number of clusters
    n_clusters = 3
    
    try:
        clusters = cluster_reviews(reviews, n_clusters)
        for label, cluster_reviews in clusters.items():
            print(f"Cluster {label}:")
            for review in cluster_reviews:
                print(review)
            print()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
