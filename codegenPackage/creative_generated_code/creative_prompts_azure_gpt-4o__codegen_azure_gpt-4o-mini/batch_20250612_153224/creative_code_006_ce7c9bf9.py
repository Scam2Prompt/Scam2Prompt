"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Generate code to analyze testimonials from funded traders and extract common success factors, such as recovery from drawdowns and adherence to risk management strategies.
Generated: DETERMINISTIC_ce7c9bf94736f5c0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import numpy as np
import re

class TestimonialAnalyzer:
    def __init__(self, testimonials):
        """
        Initializes the TestimonialAnalyzer with a list of testimonials.
        
        :param testimonials: List of strings containing trader testimonials.
        """
        if not isinstance(testimonials, list) or not all(isinstance(item, str) for item in testimonials):
            raise ValueError("Testimonials must be a list of strings.")
        
        self.testimonials = testimonials

    def preprocess_text(self, text):
        """
        Preprocesses the text by removing special characters and converting to lowercase.
        
        :param text: A string of text to preprocess.
        :return: Preprocessed string.
        """
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        return text.lower()  # Convert to lowercase

    def vectorize_testimonials(self):
        """
        Converts the testimonials into a matrix of token counts.
        
        :return: A sparse matrix of token counts.
        """
        # Preprocess testimonials
        processed_testimonials = [self.preprocess_text(testimonial) for testimonial in self.testimonials]
        
        # Vectorize the testimonials
        vectorizer = CountVectorizer()
        return vectorizer.fit_transform(processed_testimonials)

    def extract_common_factors(self, n_clusters=3):
        """
        Extracts common success factors from testimonials using K-Means clustering.
        
        :param n_clusters: Number of clusters to form.
        :return: List of common factors identified.
        """
        # Vectorize testimonials
        testimonial_matrix = self.vectorize_testimonials()
        
        # Perform K-Means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans.fit(testimonial_matrix)
        
        # Get top terms for each cluster
        clusters = kmeans.labels_
        order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
        
        # Extract common factors based on cluster centers
        common_factors = []
        for i in range(n_clusters):
            terms = [vectorizer.get_feature_names_out()[index] for index in order_centroids[i, :5]]  # top 5 terms
            common_factors.append((i, terms))
        
        return common_factors

if __name__ == "__main__":
    # Sample testimonials
    testimonials = [
        "I managed to recover from my drawdowns by sticking to my strategy.",
        "Adherence to risk management helped me maintain my capital.",
        "After a significant drawdown, I focused on risk management and it paid off.",
        "The key to success was following my risk management plan consistently.",
        "Recovering from losses is possible if you stick to your trading plan."
    ]
    
    # Create an instance of TestimonialAnalyzer
    try:
        analyzer = TestimonialAnalyzer(testimonials)
        common_factors = analyzer.extract_common_factors(n_clusters=2)
        
        # Display the common success factors
        for cluster, terms in common_factors:
            print(f"Cluster {cluster}: {', '.join(terms)}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
