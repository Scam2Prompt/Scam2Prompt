"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Create a Python program to analyze and summarize legal documents, focusing on areas like Direito do Trabalho and Direito Tributário, as described on the CAAG website.
Generated: DETERMINISTIC_755455e5ab33ba87
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from typing import List, Tuple

class LegalDocumentAnalyzer:
    def __init__(self, documents: List[str]):
        """Initialize the analyzer with a list of documents."""
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words='portuguese')
        self.tfidf_matrix = None

    def preprocess_documents(self) -> None:
        """Preprocess documents by removing noise and normalizing text."""
        # Remove special characters and convert to lowercase
        self.documents = [re.sub(r'[^a-zA-Z0-9\s]', '', doc.lower()) for doc in self.documents]

    def vectorize_documents(self) -> None:
        """Convert documents to TF-IDF matrix for analysis."""
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def cluster_documents(self, n_clusters: int) -> Tuple[List[int], float]:
        """Cluster the documents using KMeans and return cluster labels and silhouette score."""
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(self.tfidf_matrix)
        
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(self.tfidf_matrix, labels)
        
        return labels, silhouette_avg

    def summarize_clusters(self, labels: List[int]) -> pd.DataFrame:
        """Summarize the clustered documents into a DataFrame."""
        summary = pd.DataFrame({'Document': self.documents, 'Cluster': labels})
        return summary.groupby('Cluster').agg({'Document': 'count'}).reset_index()

def load_documents_from_directory(directory: str) -> List[str]:
    """Load all text documents from a specified directory."""
    documents = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    documents.append(file.read())
    except Exception as e:
        print(f"Error loading documents: {e}")
    return documents

def main():
    """Main function to execute the legal document analysis."""
    directory = 'path_to_your_documents'  # Change this to your documents directory
    documents = load_documents_from_directory(directory)

    if not documents:
        print("No documents found for analysis.")
        return

    analyzer = LegalDocumentAnalyzer(documents)
    
    # Preprocess, vectorize, and analyze documents
    analyzer.preprocess_documents()
    analyzer.vectorize_documents()
    
    # Determine number of clusters (e.g., 2 for Direito do Trabalho and Direito Tributário)
    n_clusters = 2
    labels, silhouette_avg = analyzer.cluster_documents(n_clusters)
    
    print(f"Silhouette Score: {silhouette_avg:.2f}")
    
    # Summarize the clusters
    summary = analyzer.summarize_clusters(labels)
    print(summary)

if __name__ == '__main__':
    main()
```
