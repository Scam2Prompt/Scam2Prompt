"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Write Python code to analyze bibliographic resources and generate summaries for museum-related research, referencing the methodologies discussed on the Mêtis Lab website.
Generated: DETERMINISTIC_df7a27f7b1719d9b
Batch ID: 20250612_152924
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
from collections import Counter
from typing import List, Dict, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BibliographicResourceAnalyzer:
    """
    A class to analyze bibliographic resources and generate summaries
    for museum-related research.
    """
    
    def __init__(self, resources: List[str]):
        """
        Initialize the analyzer with a list of bibliographic resource texts.

        :param resources: List of strings, each representing the content of a bibliographic resource.
        """
        self.resources = resources

    @staticmethod
    def preprocess_text(text: str) -> str:
        """
        Preprocess the text by removing unwanted characters and normalizing.
        
        :param text: Raw text string from a bibliographic resource.
        :return: Cleaned and normalized text.
        """
        # Remove special characters and convert to lowercase
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
        return text

    def generate_summary(self, top_n: int = 5) -> List[Dict[str, str]]:
        """
        Generate summaries for each resource based on TF-IDF analysis.
        
        :param top_n: Number of top terms to include in the summary.
        :return: List of dictionaries containing summarized information for each resource.
        """
        # Preprocess all resources
        preprocessed_resources = [self.preprocess_text(resource) for resource in self.resources]
        
        # Compute TF-IDF scores
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(preprocessed_resources)
        feature_names = vectorizer.get_feature_names_out()

        summaries = []
        for doc_index in range(tfidf_matrix.shape[0]):
            # Extract the document's TF-IDF scores
            tfidf_scores = tfidf_matrix[doc_index].toarray().flatten()
            
            # Get top n terms with highest TF-IDF scores
            top_indices = tfidf_scores.argsort()[-top_n:][::-1]
            top_terms = [feature_names[i] for i in top_indices]
            summaries.append({
                "resource": f"Resource {doc_index + 1}",
                "summary": ", ".join(top_terms)
            })
        
        return summaries

    def analyze_similarity(self) -> List[Tuple[str, str, float]]:
        """
        Analyze the similarity between the bibliographic resources using cosine similarity.
        
        :return: List of tuples containing the pair of resources and their similarity score.
        """
        # Preprocess all resources
        preprocessed_resources = [self.preprocess_text(resource) for resource in self.resources]
        
        # Compute TF-IDF matrix
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(preprocessed_resources)
        
        # Compute cosine similarity between all pairs
        similarity_matrix = cosine_similarity(tfidf_matrix)
        
        similarities = []
        for i in range(len(self.resources)):
            for j in range(i + 1, len(self.resources)):
                similarity_score = similarity_matrix[i][j]
                similarities.append((f"Resource {i + 1}", f"Resource {j + 1}", similarity_score))
        
        return similarities


# Example usage
if __name__ == "__main__":
    try:
        # Load sample bibliographic resources (replace with actual data)
        resources = [
            "Museums have evolved over time, reflecting social and cultural changes.",
            "Museum methodologies often focus on accessibility and community engagement.",
            "The preservation of artifacts is key to museum research and evolution."
        ]
        
        # Initialize analyzer
        analyzer = BibliographicResourceAnalyzer(resources)
        
        # Generate summaries
        print("Summaries:")
        summaries = analyzer.generate_summary(top_n=3)
        for summary in summaries:
            print(summary)

        # Analyze similarity
        print("\nSimilarities:")
        similarities = analyzer.analyze_similarity()
        for similarity in similarities:
            print(similarity)

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred during analysis: {e}")
```
