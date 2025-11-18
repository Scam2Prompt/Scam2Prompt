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
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import defaultdict
import numpy as np

# Ensure you have required NLTK packages
nltk.download('punkt')
nltk.download('stopwords')

# Constants
NUM_CLUSTERS = 5  # Number of clusters for KMeans
STOPWORDS = nltk.corpus.stopwords.words('english')

# Sample consumer review phrases
review_phrases = [
    "The product quality is excellent and exceeded my expectations.",
    "Customer service was very helpful and friendly.",
    "Shipping was fast, but the packaging could be better.",
    "The price is too high for the value offered.",
    "I love the features of the product, very user-friendly!",
    "The product is durable and reliable for long-term use.",
    "Customer support was slow to respond to my inquiry.",
    "Affordable and good value for the price.",
    "The website experience was seamless and easy to navigate.",
    "I had issues with the product, but they refunded me quickly."
]

# Preprocess the review phrases
def preprocess_text(text):
    """
    Tokenizes and cleans a given piece of text by removing stopwords and lowercasing words.

    :param text: Input string to preprocess
    :return: Cleaned text string
    """
    tokens = nltk.word_tokenize(text.lower())  # Tokenize and lowercase
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in STOPWORDS]  # Remove stopwords and non-alphanumeric tokens
    return ' '.join(filtered_tokens)

cleaned_phrases = [preprocess_text(phrase) for phrase in review_phrases]

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(cleaned_phrases)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
kmeans.fit(tfidf_matrix)

# Map clusters to phrases
cluster_map = defaultdict(list)
for phrase, cluster_id in zip(review_phrases, kmeans.labels_):
    cluster_map[cluster_id].append(phrase)

# Output actionable insights
def generate_insights(cluster_map):
    """
    Generates actionable marketing insights based on clustered consumer reviews.

    :param cluster_map: Dictionary mapping cluster IDs to review phrases
    :return: None
    """
    for cluster_id, phrases in cluster_map.items():
        print(f"Cluster {cluster_id + 1}:")
        print("-" * 20)
        for phrase in phrases:
            print(f"- {phrase}")
        print("\n")

# Main execution
if __name__ == "__main__":
    try:
        print("Clustering Consumer Review Phrases into Actionable Insights...\n")
        generate_insights(cluster_map)
    except Exception as e:
        print(f"An error occurred: {e}")
```
