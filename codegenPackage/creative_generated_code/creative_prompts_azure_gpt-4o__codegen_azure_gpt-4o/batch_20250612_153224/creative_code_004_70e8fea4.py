"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npors.net
Prompt: Write code to analyze case studies from the Études Newsletter and extract design insights using natural language processing techniques.
Generated: DETERMINISTIC_70e8fea4fe3426a3
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
from typing import List, Dict
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import logging

# Ensure nltk data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load case studies from files
def load_case_studies(directory: str) -> List[str]:
    """
    Load case studies from text files in the specified directory.
    
    Parameters:
        directory (str): Path to the directory containing case study text files.
    
    Returns:
        List[str]: List of case study content as strings.
    """
    case_studies = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    case_studies.append(file.read())
        logging.info(f"Loaded {len(case_studies)} case studies from {directory}.")
    except Exception as e:
        logging.error(f"Error loading case studies: {e}")
    return case_studies

# Preprocess text
def preprocess_text(text: str) -> str:
    """
    Preprocess text by tokenizing, removing stopwords and non-alphanumeric characters.
    
    Parameters:
        text (str): Raw text input.
    
    Returns:
        str: Preprocessed text.
    """
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(filtered_tokens)

# Extract design insights using TF-IDF and clustering
def extract_design_insights(case_studies: List[str], num_clusters: int = 5) -> Dict[int, List[str]]:
    """
    Analyze case studies and extract design insights using TF-IDF and KMeans clustering.
    
    Parameters:
        case_studies (List[str]): List of case study content.
        num_clusters (int): Number of clusters to identify in the data.
    
    Returns:
        Dict[int, List[str]]: Dictionary where keys are cluster IDs and values are lists of design insights.
    """
    try:
        # Preprocess all case studies
        preprocessed_studies = [preprocess_text(study) for study in case_studies]
        
        # Compute TF-IDF matrix
        tfidf_vectorizer = TfidfVectorizer(max_features=1000)
        tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_studies)
        
        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(tfidf_matrix)
        
        # Group case studies by cluster and extract insights
        clusters = kmeans.labels_
        insights = {i: [] for i in range(num_clusters)}
        for idx, cluster_id in enumerate(clusters):
            insights[cluster_id].append(preprocessed_studies[idx])
        
        logging.info("Design insights successfully extracted.")
        return insights
    
    except Exception as e:
        logging.error(f"Error extracting design insights: {e}")
        return {}

# Main function
def main():
    """
    Main function to load case studies, analyze them, and extract design insights.
    """
    # Path to directory containing case study files
    case_study_directory = "path/to/etudes/case/studies"
    
    # Load case studies
    case_studies = load_case_studies(case_study_directory)
    
    if not case_studies:
        logging.error("No case studies found. Exiting.")
        return
    
    # Extract design insights
    insights = extract_design_insights(case_studies, num_clusters=5)
    
    # Print insights
    print("Design Insights:")
    for cluster_id, cluster_insights in insights.items():
        print(f"\nCluster {cluster_id}:")
        for insight in cluster_insights:
            print(f"- {insight[:100]}...")  # Print first 100 characters of each insight for brevity

# Entry point
if __name__ == "__main__":
    main()
```
