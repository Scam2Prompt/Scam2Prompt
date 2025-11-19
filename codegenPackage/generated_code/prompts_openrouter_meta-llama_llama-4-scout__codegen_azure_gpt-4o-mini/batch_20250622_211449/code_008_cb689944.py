"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Create a natural language processing (NLP) tool to analyze and summarize the Morpho Foundation's project reports, extracting key insights and themes.
Generated: DETERMINISTIC_cb689944382ee823
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk import download

# Ensure necessary NLTK resources are downloaded
download('punkt')
download('stopwords')

# Configure logging
logging.basicConfig(level=logging.INFO)

class NLPAnalyzer:
    def __init__(self, reports: List[str]):
        """
        Initialize the NLPAnalyzer with project reports.

        :param reports: A list of project report texts.
        """
        self.reports = reports
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.kmeans = None

    def preprocess_reports(self) -> List[str]:
        """
        Preprocess the reports by tokenizing sentences and removing stopwords.

        :return: A list of preprocessed report texts.
        """
        stop_words = set(stopwords.words('english'))
        preprocessed_reports = []

        for report in self.reports:
            sentences = sent_tokenize(report)
            filtered_sentences = [
                sentence for sentence in sentences if sentence.lower() not in stop_words
            ]
            preprocessed_reports.append(' '.join(filtered_sentences))

        return preprocessed_reports

    def extract_key_insights(self, n_clusters: int = 5) -> Dict[str, List[str]]:
        """
        Extract key insights from the reports using KMeans clustering.

        :param n_clusters: The number of clusters to form.
        :return: A dictionary with cluster labels and their corresponding report summaries.
        """
        try:
            preprocessed_reports = self.preprocess_reports()
            tfidf_matrix = self.vectorizer.fit_transform(preprocessed_reports)

            # Fit KMeans clustering
            self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            self.kmeans.fit(tfidf_matrix)

            # Organize insights by cluster
            insights = {f'Cluster {i}': [] for i in range(n_clusters)}
            for idx, label in enumerate(self.kmeans.labels_):
                insights[f'Cluster {label}'].append(preprocessed_reports[idx])

            return insights

        except Exception as e:
            logging.error(f"Error during key insights extraction: {e}")
            return {}

def load_reports_from_json(file_path: str) -> List[str]:
    """
    Load project reports from a JSON file.

    :param file_path: Path to the JSON file containing reports.
    :return: A list of report texts.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('reports', [])
    except Exception as e:
        logging.error(f"Error loading reports from JSON: {e}")
        return []

def main():
    # Path to the JSON file containing project reports
    json_file_path = 'morpho_foundation_reports.json'

    # Load reports
    reports = load_reports_from_json(json_file_path)

    if not reports:
        logging.warning("No reports found to analyze.")
        return

    # Initialize the NLP Analyzer
    analyzer = NLPAnalyzer(reports)

    # Extract key insights
    insights = analyzer.extract_key_insights(n_clusters=5)

    # Output the insights
    for cluster, summaries in insights.items():
        print(f"{cluster}:")
        for summary in summaries:
            print(f" - {summary[:100]}...")  # Print the first 100 characters of each summary
        print()

if __name__ == "__main__":
    main()
```
