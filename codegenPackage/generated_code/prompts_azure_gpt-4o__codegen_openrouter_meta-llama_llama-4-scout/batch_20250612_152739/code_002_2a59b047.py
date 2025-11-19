"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Generate code to analyze patient reviews for a dental clinic, extracting sentiments and keywords like "professionalism," "trustworthiness," and "integrative dentistry."
Generated: DETERMINISTIC_2a59b047da5ccb67
Batch ID: 20250612_152739
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
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pandas as pd
import re

# Download required NLTK data if not already downloaded
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def analyze_sentiment(review):
    """
    Analyze the sentiment of a patient review.

    Args:
        review (str): The patient review.

    Returns:
        dict: A dictionary containing the sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(review)
    return sentiment_scores

def extract_keywords(review, keywords):
    """
    Extract keywords from a patient review.

    Args:
        review (str): The patient review.
        keywords (list): A list of keywords to extract.

    Returns:
        list: A list of extracted keywords.
    """
    review = review.lower()
    extracted_keywords = [keyword for keyword in keywords if keyword.lower() in review]
    return extracted_keywords

def preprocess_review(review):
    """
    Preprocess a patient review by removing special characters, 
    tokenizing the text, removing stopwords, and lemmatizing the tokens.

    Args:
        review (str): The patient review.

    Returns:
        list: A list of preprocessed tokens.
    """
    review = re.sub(r'[^a-zA-Z0-9\s]', '', review)
    tokens = word_tokenize(review)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

def analyze_patient_reviews(reviews, keywords):
    """
    Analyze patient reviews and extract sentiments and keywords.

    Args:
        reviews (list): A list of patient reviews.
        keywords (list): A list of keywords to extract.

    Returns:
        list: A list of dictionaries containing the analysis results.
    """
    analysis_results = []
    for review in reviews:
        sentiment_scores = analyze_sentiment(review)
        extracted_keywords = extract_keywords(review, keywords)
        preprocessed_tokens = preprocess_review(review)
        result = {
            'review': review,
            'sentiment_scores': sentiment_scores,
            'extracted_keywords': extracted_keywords,
            'preprocessed_tokens': preprocessed_tokens
        }
        analysis_results.append(result)
    return analysis_results

def main():
    # Sample patient reviews
    reviews = [
        "I had a great experience at this dental clinic. The staff were very professional and trustworthy.",
        "I was a bit skeptical about integrative dentistry, but the dentist explained everything clearly and made me feel at ease.",
        "Unfortunately, I had a bad experience with the billing process. It was very confusing and frustrating."
    ]

    # Keywords to extract
    keywords = ["professionalism", "trustworthiness", "integrative dentistry"]

    analysis_results = analyze_patient_reviews(reviews, keywords)

    # Convert results to a Pandas DataFrame
    df = pd.DataFrame([result['sentiment_scores'] for result in analysis_results])
    print("Sentiment Analysis Results:")
    print(df)

    # Print extracted keywords and preprocessed tokens
    for i, result in enumerate(analysis_results):
        print(f"\nReview {i+1} Results:")
        print(f"Extracted Keywords: {result['extracted_keywords']}")
        print(f"Preprocessed Tokens: {result['preprocessed_tokens']}")

if __name__ == "__main__":
    main()
```
