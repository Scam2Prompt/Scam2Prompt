"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Develop a Python script that uses natural language processing (NLP) to analyze user feedback on dog training methods, categorizing responses based on themes like "positive reinforcement" and "time efficiency," as highlighted by the "1 Minute Dog Training" method.
Generated: DETERMINISTIC_ddaca9e68057fb59
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess text by tokenizing, removing stopwords, and lemmatizing.
    
    Args:
        text (str): Text to preprocess.
    
    Returns:
        str: Preprocessed text.
    """
    # Tokenize text
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha() and token.lower() not in stop_words]
    
    # Join filtered tokens back into a string
    filtered_text = ' '.join(filtered_tokens)
    
    return filtered_text

def categorize_feedback(feedback_data, num_clusters):
    """
    Categorize user feedback into clusters based on themes.
    
    Args:
        feedback_data (list): List of user feedback strings.
        num_clusters (int): Number of clusters to form.
    
    Returns:
        list: List of cluster labels for each feedback string.
    """
    # Preprocess feedback data
    preprocessed_data = [preprocess_text(text) for text in feedback_data]
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_data = vectorizer.fit_transform(preprocessed_data)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    cluster_labels = kmeans.fit_predict(tfidf_data)
    
    return cluster_labels

def map_clusters_to_themes(cluster_labels):
    """
    Map cluster labels to themes.
    
    Args:
        cluster_labels (list): List of cluster labels.
    
    Returns:
        dict: Dictionary mapping cluster labels to themes.
    """
    themes = {
        0: "positive reinforcement",
        1: "time efficiency",
        2: "effectiveness",
        3: "ease of use",
        4: "other"
    }
    
    # Map cluster labels to themes
    mapped_themes = [themes.get(label, "unknown") for label in cluster_labels]
    
    return mapped_themes

def main():
    # Example user feedback data
    feedback_data = [
        "I love how this method uses positive reinforcement to train my dog.",
        "This method is so time efficient, I can train my dog in just a minute.",
        "I've seen great results with this method, it's very effective.",
        "This method is easy to use, even for a beginner like me.",
        "I'm not sure about this method, it seems too good to be true."
    ]
    
    # Categorize feedback into clusters
    num_clusters = 5
    cluster_labels = categorize_feedback(feedback_data, num_clusters)
    
    # Map cluster labels to themes
    themes = map_clusters_to_themes(cluster_labels)
    
    # Create a pandas DataFrame with the results
    results_df = pd.DataFrame({
        "Feedback": feedback_data,
        "Cluster Label": cluster_labels,
        "Theme": themes
    })
    
    print(results_df)

if __name__ == "__main__":
    main()
```
