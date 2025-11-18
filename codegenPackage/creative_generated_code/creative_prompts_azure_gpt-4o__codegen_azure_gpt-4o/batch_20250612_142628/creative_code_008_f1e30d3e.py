"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.world
Prompt: Write code to analyze client feedback data using AI to identify trends in investment success, inspired by the testimonials provided on AIvest Securities Limited's website.
Generated: DETERMINISTIC_f1e30d3e63b0224c
Batch ID: 20250612_142628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from transformers import pipeline

# Function to clean feedback text
def clean_text(text):
    """
    Cleans text by removing special characters, numbers, and extra spaces.

    Args:
        text (str): Raw feedback text.

    Returns:
        str: Cleaned text.
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

# Function to analyze trends using AI
def analyze_feedback(feedback_list):
    """
    Analyzes client feedback data using AI technologies to detect trends.

    Args:
        feedback_list (list): List of client feedback strings.

    Returns:
        dict: Dictionary containing discovered clusters and sentiment analysis summary.
    """
    try:
        # Step 1: Clean the feedback
        cleaned_feedback = [clean_text(feedback) for feedback in feedback_list]

        # Step 2: Vectorize the feedback using CountVectorizer
        vectorizer = CountVectorizer(stop_words='english')
        feedback_vectors = vectorizer.fit_transform(cleaned_feedback)

        # Step 3: Use KMeans clustering to identify trends (client feedback clusters)
        kmeans = KMeans(n_clusters=3, random_state=42)  # Adjust n_clusters as needed
        cluster_labels = kmeans.fit_predict(feedback_vectors)

        # Calculate silhouette score to evaluate clustering quality
        silhouette_avg = silhouette_score(feedback_vectors, cluster_labels)

        # Step 4: Use AI for sentiment analysis
        sentiment_analyzer = pipeline("sentiment-analysis")
        sentiments = [sentiment_analyzer(feedback)[0] for feedback in feedback_list]

        # Summarize sentiment analysis results
        sentiment_summary = {
            "positive": sum(1 for sentiment in sentiments if sentiment['label'] == 'POSITIVE'),
            "negative": sum(1 for sentiment in sentiments if sentiment['label'] == 'NEGATIVE'),
            "neutral": len(feedback_list) - sum(1 for sentiment in sentiments if sentiment['label'] in ['POSITIVE', 'NEGATIVE'])
        }

        # Step 5: Organize clusters and sentiments into a result
        cluster_feedback = {i: [] for i in range(kmeans.n_clusters)}
        for feedback, label in zip(feedback_list, cluster_labels):
            cluster_feedback[label].append(feedback)

        result = {
            "clusters": cluster_feedback,
            "sentiment_summary": sentiment_summary,
            "silhouette_score": silhouette_avg,
        }

        return result

    except Exception as e:
        print(f"Error occurred during feedback analysis: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example client feedback data (replace with actual data)
    feedback_data = [
        "AIvest helped me achieve my investment goals quickly!",
        "I lost money in my initial investments, but their advisors guided me to success.",
        "The platform is intuitive and easy to use. Highly recommended!",
        "I wasn't satisfied with the returns initially, but now I'm seeing great progress.",
        "Their AI-based suggestions are spot-on and saved me a lot of time."
    ]

    # Analyze the feedback
    analysis_result = analyze_feedback(feedback_data)

    # Print the results
    if analysis_result:
        print("Clustered Feedback:")
        for cluster, feedbacks in analysis_result["clusters"].items():
            print(f"Cluster {cluster}: {feedbacks}")
        print("\nSentiment Summary:", analysis_result["sentiment_summary"])
        print("\nSilhouette Score:", analysis_result["silhouette_score"])
```
