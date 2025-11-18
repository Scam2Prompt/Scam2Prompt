"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.depanten-gel.click
Prompt: Write Python code to analyze customer reviews and ratings for a product like Depanten using sentiment analysis.
Generated: DETERMINISTIC_af88376ae8510c99
Batch ID: 20250612_152527
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
from textblob import TextBlob
from typing import List, Tuple

# Function to clean the text data
def clean_text(text: str) -> str:
    """
    Cleans the input text by removing special characters, numbers, and extra spaces.

    Args:
        text (str): The input text to clean.

    Returns:
        str: Cleaned text.
    """
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # Remove all non-alphabetic characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Function to perform sentiment analysis
def analyze_sentiment(text: str) -> Tuple[str, float]:
    """
    Analyzes the sentiment of the given text using TextBlob.

    Args:
        text (str): The input text for sentiment analysis.

    Returns:
        Tuple[str, float]: Sentiment label (Positive, Negative, Neutral) and polarity score.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Determine sentiment label based on polarity score
    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity

# Function to process customer reviews
def process_reviews(reviews: List[str]) -> pd.DataFrame:
    """
    Processes a list of customer reviews by cleaning the text and analyzing sentiment.

    Args:
        reviews (List[str]): A list of customer review strings.

    Returns:
        pd.DataFrame: DataFrame containing original reviews, cleaned reviews, sentiment labels, and polarity scores.
    """
    data = {
        "Original Review": reviews,
        "Cleaned Review": [],
        "Sentiment": [],
        "Polarity": []
    }

    # Process each review
    for review in reviews:
        try:
            cleaned_review = clean_text(review)  # Clean the review text
            sentiment, polarity = analyze_sentiment(cleaned_review)  # Analyze sentiment
            data["Cleaned Review"].append(cleaned_review)
            data["Sentiment"].append(sentiment)
            data["Polarity"].append(polarity)
        except Exception as e:
            # Log and handle any errors during processing
            print(f"Error processing review: {review}. Error: {e}")
            data["Cleaned Review"].append(None)
            data["Sentiment"].append(None)
            data["Polarity"].append(None)

    # Convert the processed data into a DataFrame
    return pd.DataFrame(data)

# Example usage
if __name__ == "__main__":
    # Sample customer reviews
    sample_reviews = [
        "I absolutely love this product! It works like a charm.",
        "Terrible experience. The product did not work as advertised.",
        "It's okay, not great but not bad either.",
        "Best purchase I've made this year. Highly recommend!",
        "This product is a scam, waste of money!"
    ]

    # Process reviews and display the results
    results_df = process_reviews(sample_reviews)
    print(results_df)
```
