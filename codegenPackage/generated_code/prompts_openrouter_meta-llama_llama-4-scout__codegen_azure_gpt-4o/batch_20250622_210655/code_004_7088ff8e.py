"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Write a Python script to analyze customer reviews of skincare products and determine the most highly-rated products based on their scientific features.
Generated: DETERMINISTIC_7088ff8ecfbf75f0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from textblob import TextBlob
import re

# Function to clean text data
def clean_text(text):
    """
    Cleans the input text by removing special characters, numbers, and extra spaces.
    Args:
        text (str): The text to be cleaned.
    Returns:
        str: The cleaned text.
    """
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip().lower()

# Function to calculate sentiment score
def calculate_sentiment(text):
    """
    Calculates the sentiment polarity of the given text using TextBlob.
    Args:
        text (str): The text to analyze.
    Returns:
        float: Sentiment polarity score (-1 to 1).
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Function to analyze reviews and determine highly-rated products
def analyze_reviews(data):
    """
    Analyzes customer reviews to determine the most highly-rated skincare products.
    Args:
        data (pd.DataFrame): DataFrame containing product reviews and features.
    Returns:
        pd.DataFrame: DataFrame with products ranked by average sentiment score.
    """
    try:
        # Clean review text
        data['cleaned_review'] = data['review'].apply(clean_text)
        
        # Calculate sentiment score for each review
        data['sentiment_score'] = data['cleaned_review'].apply(calculate_sentiment)
        
        # Group by product and calculate average sentiment score
        product_scores = data.groupby('product_name')['sentiment_score'].mean().reset_index()
        product_scores.rename(columns={'sentiment_score': 'average_sentiment_score'}, inplace=True)
        
        # Sort products by average sentiment score in descending order
        ranked_products = product_scores.sort_values(by='average_sentiment_score', ascending=False)
        
        return ranked_products
    except Exception as e:
        print(f"Error occurred during analysis: {e}")
        return pd.DataFrame()

# Main function to execute the script
def main():
    """
    Main function to load data, analyze reviews, and display results.
    """
    try:
        # Load customer reviews data (replace 'reviews.csv' with your actual file path)
        data = pd.read_csv('reviews.csv')
        
        # Ensure required columns exist
        if 'product_name' not in data.columns or 'review' not in data.columns:
            raise ValueError("Input data must contain 'product_name' and 'review' columns.")
        
        # Analyze reviews
        ranked_products = analyze_reviews(data)
        
        # Display top 10 highly-rated products
        print("Top 10 Highly-Rated Skincare Products:")
        print(ranked_products.head(10))
    except FileNotFoundError:
        print("Error: The file 'reviews.csv' was not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
