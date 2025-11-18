"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Suggest an open-source library for analyzing refugee stories and media advocacy tactics, as discussed in Jusoor International's panel talk.
Generated: DETERMINISTIC_742bb408afda2f9e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script suggests an open-source Python library for analyzing refugee stories 
and media advocacy tactics. It provides an example of using the Natural Language Toolkit (NLTK)
to analyze text data. NLTK is a widely-used library for text mining and natural language processing (NLP).
"""

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
import os

# Function to download NLTK resources
def setup_nltk():
    """
    Ensures necessary NLTK resources are downloaded.
    This is a one-time setup and downloads essential components for text processing.
    """
    try:
        nltk.download('punkt')  # Tokenizer data
        nltk.download('vader_lexicon')  # Sentiment analysis lexicon
    except Exception as e:
        print(f"Error downloading NLTK resources: {e}")

# Function to analyze text data
def analyze_text(text):
    """
    Analyzes the given text for word frequency and sentiment.

    Args:
        text (str): The refugee story or media advocacy text to be analyzed.

    Returns:
        dict: Contains word frequency and sentiment analysis results.
    """
    try:
        # Tokenize the text into words
        tokens = word_tokenize(text)
        
        # Calculate word frequency
        freq_dist = FreqDist(tokens)
        most_common_words = freq_dist.most_common(10)

        # Sentiment analysis
        sentiment_analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = sentiment_analyzer.polarity_scores(text)

        # Return analysis results
        return {
            "Word Frequency": most_common_words,
            "Sentiment Scores": sentiment_scores
        }
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return None

# Main function
def main():
    """
    Main entry point of the script. Demonstrates text analysis on 
    sample refugee stories or media advocacy text.
    """
    # Sample text (Replace with actual refugee stories or media advocacy text)
    sample_text = """
    Refugee stories are a powerful tool in media advocacy. They highlight the struggles, 
    resilience, and humanity of displaced individuals. Advocacy campaigns using these stories 
    help raise awareness and drive policy change to support refugees.
    """

    # Set up NLTK resources
    setup_nltk()

    # Analyze the sample text
    results = analyze_text(sample_text)

    # Display the results
    if results:
        print("Analysis Results:")
        print("Most Common Words:")
        for word, count in results["Word Frequency"]:
            print(f"{word}: {count}")
        
        print("\nSentiment Scores:")
        for key, score in results["Sentiment Scores"].items():
            print(f"{key}: {score}")

if __name__ == "__main__":
    main()
```
