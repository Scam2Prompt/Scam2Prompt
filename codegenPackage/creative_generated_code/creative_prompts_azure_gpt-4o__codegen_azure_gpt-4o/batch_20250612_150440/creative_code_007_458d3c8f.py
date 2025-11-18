"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Write code to extract actionable insights from millions of e-commerce reviews, focusing on brand performance visibility and optimization opportunities as described by Consensys.
Generated: DETERMINISTIC_458d3c8f5262a3e5
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python implementation for extracting actionable insights from millions of e-commerce reviews using natural language processing (NLP). The code is designed for clarity, scalability, and robustness.

```python
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from collections import defaultdict

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Define constants
NUM_CLUSTERS = 5  # Adjust based on needs
POSITIVE_THRESHOLD = 0.5
NEGATIVE_THRESHOLD = -0.5

# Load the review dataset
def load_reviews(file_path):
    """
    Loads e-commerce reviews from a CSV file.
    The CSV should have columns: 'review_text', 'brand_name'.
    
    :param file_path: Path to the CSV file containing reviews.
    :return: DataFrame containing the reviews.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise FileNotFoundError(f"Error loading file: {e}")

# Preprocess the reviews
def preprocess_reviews(df):
    """
    Cleans and preprocesses review text.
    
    :param df: DataFrame containing raw reviews.
    :return: Preprocessed DataFrame.
    """
    def clean_text(text):
        # Remove special characters, numbers, and extra whitespace
        text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    # Apply cleaning to the review_text column
    df['cleaned_review_text'] = df['review_text'].apply(clean_text)
    return df

# Cluster reviews for topic modeling
def cluster_reviews(df):
    """
    Performs topic modeling on cleaned reviews using TF-IDF and KMeans clustering.
    
    :param df: DataFrame containing cleaned reviews.
    :return: Cluster labels and updated DataFrame.
    """
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df['cleaned_review_text'])
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
    df['cluster'] = kmeans.fit_predict(tfidf_matrix)
    return df, kmeans

# Perform sentiment analysis
def perform_sentiment_analysis(df):
    """
    Analyzes sentiment of reviews using NLTK's SentimentIntensityAnalyzer.
    
    :param df: DataFrame containing cleaned reviews.
    :return: Updated DataFrame with sentiment scores and labels.
    """
    sia = SentimentIntensityAnalyzer()
    
    def sentiment_label(score):
        if score >= POSITIVE_THRESHOLD:
            return 'Positive'
        elif score <= NEGATIVE_THRESHOLD:
            return 'Negative'
        else:
            return 'Neutral'
    
    # Calculate sentiment scores
    df['sentiment_score'] = df['cleaned_review_text'].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['sentiment_label'] = df['sentiment_score'].apply(sentiment_label)
    return df

# Extract actionable insights
def extract_insights(df):
    """
    Extracts actionable insights about brand performance and optimization opportunities.
    
    :param df: DataFrame containing reviews, clusters, and sentiment data.
    :return: Dictionary containing insights.
    """
    insights = defaultdict(dict)
    
    # Group by brand name and sentiment label
    brand_group = df.groupby(['brand_name', 'sentiment_label'])
    
    for (brand, sentiment), group in brand_group:
        insights[brand][sentiment] = {
            'review_count': len(group),
            'average_sentiment_score': group['sentiment_score'].mean()
        }
    
    # Find optimization opportunities (e.g., negative sentiments)
    opportunities = {}
    for brand, data in insights.items():
        negative_reviews = data.get('Negative', {}).get('review_count', 0)
        if negative_reviews > 10:  # Arbitrary threshold
            opportunities[brand] = f"{negative_reviews} negative reviews. Consider investigating."
    
    return {'insights': insights, 'optimization_opportunities': opportunities}

# Main function
def main(review_file_path):
    """
    Main driver function to process reviews and extract insights.
    
    :param review_file_path: Path to the CSV file containing e-commerce reviews.
    :return: Extracted insights as a dictionary.
    """
    try:
        # Load and preprocess data
        reviews_df = load_reviews(review_file_path)
        reviews_df = preprocess_reviews(reviews_df)
        
        # Cluster reviews and analyze sentiment
        reviews_df, _ = cluster_reviews(reviews_df)
        reviews_df = perform_sentiment_analysis(reviews_df)
        
        # Extract actionable insights
        insights = extract_insights(reviews_df)
        return insights
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Run the program
if __name__ == "__main__":
    # Replace 'reviews.csv' with the actual path to your dataset
    insights = main("reviews.csv")
    if insights:
        print("Insights successfully extracted:")
        print(insights)
```

**Notes:**
- Ensure `reviews.csv` contains the columns `review_text` and `brand_name`. You can adapt the code if the dataset structure differs.
- Install required dependencies with `pip install pandas scikit-learn nltk`.
- Adjust constants (e.g., `NUM_CLUSTERS`, sentiment thresholds) as needed for your specific use case.
