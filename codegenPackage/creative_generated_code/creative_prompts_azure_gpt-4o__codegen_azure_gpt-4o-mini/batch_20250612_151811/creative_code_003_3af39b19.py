"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Develop a function using a natural language processing library to identify key themes in SRH Life Foundation blog posts, such as "naturopathic centers" or "moisture-wicking fabric."
Generated: DETERMINISTIC_3af39b199277fd4e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Set up logging
logging.basicConfig(level=logging.INFO)

class ThemeExtractor:
    def __init__(self, num_clusters=5):
        """
        Initialize the ThemeExtractor with the number of clusters to form.
        
        :param num_clusters: The number of themes to extract from the text
        """
        self.num_clusters = num_clusters
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.kmeans = KMeans(n_clusters=num_clusters, random_state=0)

    def preprocess_text(self, text):
        """
        Preprocess the text by tokenizing and removing stopwords.
        
        :param text: The raw text to preprocess
        :return: A list of tokens
        """
        tokens = word_tokenize(text)
        filtered_tokens = [word for word in tokens if word.isalnum() and word.lower() not in stopwords.words('english')]
        return ' '.join(filtered_tokens)

    def extract_themes(self, documents):
        """
        Extract key themes from a list of documents using KMeans clustering.
        
        :param documents: A list of blog post contents (strings)
        :return: A list of identified themes (strings)
        """
        try:
            # Preprocess each document
            preprocessed_docs = [self.preprocess_text(doc) for doc in documents]
            # Vectorize the documents
            tfidf_matrix = self.vectorizer.fit_transform(preprocessed_docs)
            # Fit the KMeans model
            self.kmeans.fit(tfidf_matrix)
            # Extract key themes (as cluster centers)
            themes = self.vectorizer.inverse_transform(self.kmeans.cluster_centers_)
            return [' '.join(theme) for theme in themes]
        except Exception as e:
            logging.error("An error occurred while extracting themes: %s", e)
            return []

# Example usage (ensure to replace with actual blog post content):
if __name__ == "__main__":
    blog_posts = [
        "Naturopathic centers offer holistic health solutions.",
        "Moisture-wicking fabric is essential for athletic wear.",
        "The benefits of natural medicine are profound.",
        "Choosing the right moisture-wicking apparel can enhance performance.",
    ]
    
    theme_extractor = ThemeExtractor(num_clusters=2)
    themes = theme_extractor.extract_themes(blog_posts)
    logging.info("Identified themes: %s", themes)
```
