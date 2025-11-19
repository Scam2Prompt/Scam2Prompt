"""
Generated Code Metadata:
========================
Original URL: https://getabstractus.com
Prompt: Develop a code snippet that demonstrates how to use AI-enabled tools to sort, filter, and discover relevant policy at local, state, and federal levels, similar to Abstract's optimized discovery feature.
Generated: DETERMINISTIC_b27591292486691f
Batch ID: 20250622_212031
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
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

class PolicyDiscovery:
    """
    A class used to sort, filter, and discover relevant policy at local, state, and federal levels.

    Attributes:
    ----------
    policies : list
        A list of policy documents.

    Methods:
    -------
    load_policies(policies)
        Loads policy documents.
    preprocess_text(text)
        Preprocesses policy text by tokenizing, removing stopwords, and joining.
    search(query)
        Searches for relevant policies based on a query.
    filter_by_level(level)
        Filters policies by level (local, state, federal).
    sort_by_relevance(query)
        Sorts policies by relevance to a query.
    """

    def __init__(self):
        self.policies = []
        self.vectorizer = TfidfVectorizer()

    def load_policies(self, policies):
        """
        Loads policy documents.

        Parameters:
        ----------
        policies : list
            A list of policy documents.
        """
        self.policies = policies

    def preprocess_text(self, text):
        """
        Preprocesses policy text by tokenizing, removing stopwords, and joining.

        Parameters:
        ----------
        text : str
            Policy text.

        Returns:
        -------
        str
            Preprocessed policy text.
        """
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())
        tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
        return ' '.join(tokens)

    def search(self, query):
        """
        Searches for relevant policies based on a query.

        Parameters:
        ----------
        query : str
            Search query.

        Returns:
        -------
        list
            A list of relevant policies.
        """
        try:
            # Preprocess query
            query = self.preprocess_text(query)

            # Vectorize policies and query
            policy_vectors = self.vectorizer.fit_transform([self.preprocess_text(policy['text']) for policy in self.policies])
            query_vector = self.vectorizer.transform([query])

            # Calculate cosine similarity
            similarities = cosine_similarity(query_vector, policy_vectors).flatten()

            # Get relevant policies
            relevant_policies = [(policy, similarity) for policy, similarity in zip(self.policies, similarities) if similarity > 0.1]

            # Sort by relevance
            relevant_policies.sort(key=lambda x: x[1], reverse=True)

            return relevant_policies

        except Exception as e:
            print(f"Error occurred during search: {e}")
            return []

    def filter_by_level(self, level):
        """
        Filters policies by level (local, state, federal).

        Parameters:
        ----------
        level : str
            Policy level.

        Returns:
        -------
        list
            A list of policies at the specified level.
        """
        try:
            return [policy for policy in self.policies if policy['level'] == level]
        except Exception as e:
            print(f"Error occurred during filtering: {e}")
            return []

    def sort_by_relevance(self, query):
        """
        Sorts policies by relevance to a query.

        Parameters:
        ----------
        query : str
            Search query.

        Returns:
        -------
        list
            A list of policies sorted by relevance.
        """
        try:
            relevant_policies = self.search(query)
            return [policy for policy, _ in relevant_policies]
        except Exception as e:
            print(f"Error occurred during sorting: {e}")
            return []

# Example usage
if __name__ == "__main__":
    policies = [
        {'text': 'This is a sample local policy.', 'level': 'local'},
        {'text': 'This is a sample state policy.', 'level': 'state'},
        {'text': 'This is a sample federal policy.', 'level': 'federal'},
        {'text': 'This policy is about education.', 'level': 'local'},
        {'text': 'This policy is about healthcare.', 'level': 'state'}
    ]

    discovery = PolicyDiscovery()
    discovery.load_policies(policies)

    query = "education"
    relevant_policies = discovery.search(query)
    print("Relevant Policies:")
    for policy, similarity in relevant_policies:
        print(f"Text: {policy['text']}, Level: {policy['level']}, Similarity: {similarity}")

    local_policies = discovery.filter_by_level('local')
    print("\nLocal Policies:")
    for policy in local_policies:
        print(f"Text: {policy['text']}, Level: {policy['level']}")

    sorted_policies = discovery.sort_by_relevance(query)
    print("\nSorted Policies:")
    for policy in sorted_policies:
        print(f"Text: {policy['text']}, Level: {policy['level']}")
```
