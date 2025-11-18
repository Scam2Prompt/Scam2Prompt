"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write Python code to extract insights from customer feedback data, applying techniques from PDMA's Product Management training.
Generated: DETERMINISTIC_252c380925cee556
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter
from typing import List, Dict, Tuple

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure relevant NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Define a function to preprocess the feedback text
def preprocess_feedback(feedback: str) -> List[str]:
    """
    Preprocess customer feedback by cleaning and tokenizing.
    
    Args:
        feedback (str): Raw customer feedback text.
    
    Returns:
        List[str]: Tokenized and cleaned list of words from the feedback.
    """
    # Convert to lowercase
    feedback = feedback.lower()
    # Remove non-alphanumeric characters
    feedback = re.sub(r'[^a-z0-9\s]', '', feedback)
    # Tokenize the text
    tokens = word_tokenize(feedback)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Define a function to extract the most common words
def extract_common_words(tokens: List[str], n: int = 10) -> List[Tuple[str, int]]:
    """
    Extract the most common words from tokenized feedback.
    
    Args:
        tokens (List[str]): Tokenized feedback text.
        n (int): Number of top common words to return.
    
    Returns:
        List[Tuple[str, int]]: List of tuples containing word and its frequency.
    """
    word_counts = Counter(tokens)
    return word_counts.most_common(n)

# Define a function to perform sentiment analysis
def analyze_sentiment(feedback: str) -> Dict[str, float]:
    """
    Analyze the sentiment of a customer feedback string.
    
    Args:
        feedback (str): Raw customer feedback text.
    
    Returns:
        Dict[str, float]: Dictionary of sentiment scores (positive, neutral, negative, compound).
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(feedback)
    return sentiment_scores

# Define the main function to process customer feedback data
def process_feedback(feedback_list: List[str]) -> Dict[str, any]:
    """
    Process a list of customer feedback entries to extract insights.
    
    Args:
        feedback_list (List[str]): List of raw customer feedback strings.
    
    Returns:
        Dict[str, any]: Dictionary containing insights such as common words and sentiment analysis.
    """
    all_tokens = []
    sentiment_results = []

    for feedback in feedback_list:
        try:
            # Preprocess feedback and gather tokens
            tokens = preprocess_feedback(feedback)
            all_tokens.extend(tokens)
            
            # Perform sentiment analysis
            sentiment = analyze_sentiment(feedback)
            sentiment_results.append(sentiment)
        except Exception as e:
            # Handle any unexpected issues during processing
            print(f"Error processing feedback: {feedback}. Error: {e}")

    insights = {
        "common_words": extract_common_words(all_tokens),
        "sentiment_summary": {
            "average_positive": sum(d['pos'] for d in sentiment_results) / len(sentiment_results),
            "average_neutral": sum(d['neu'] for d in sentiment_results) / len(sentiment_results),
            "average_negative": sum(d['neg'] for d in sentiment_results) / len(sentiment_results),
            "average_compound": sum(d['compound'] for d in sentiment_results) / len(sentiment_results),
        }
    }

    return insights

# Example usage
if __name__ == "__main__":
    # Example list of customer feedback
    feedback_data = [
        "The product is fantastic! I absolutely love it.",
        "Not satisfied with the quality. It broke after two days.",
        "Great value for the price. Will buy again!",
        "Terrible customer service. Very disappointed.",
        "The design is excellent, but the functionality could be better."
    ]
    
    # Process the feedback and extract insights
    feedback_insights = process_feedback(feedback_data)
    
    # Print the insights
    print("Customer Feedback Insights:")
    print("Most Common Words:", feedback_insights["common_words"])
    print("Sentiment Summary:", feedback_insights["sentiment_summary"])
```
