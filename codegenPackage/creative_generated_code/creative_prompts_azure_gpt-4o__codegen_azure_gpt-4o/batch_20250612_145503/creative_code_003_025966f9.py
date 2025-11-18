"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: Provide an example of a Python-based AI project for beginners, aligning with the "Inteligencia artificial basico" content from https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_025966f96428d7bf
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simple Python AI Project: Sentiment Analysis using Natural Language Toolkit (NLTK)

This script performs basic sentiment analysis on user-provided text to determine
if it has a positive, negative, or neutral sentiment.

Dependencies:
- nltk: Install via `pip install nltk`

Author: Beginner AI Project
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sys

# Ensure NLTK data is downloaded
try:
    nltk.download('vader_lexicon', quiet=True)  # Lexicon for sentiment analysis
except Exception as e:
    print(f"Error downloading NLTK data: {e}")
    sys.exit(1)

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using NLTK's SentimentIntensityAnalyzer.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        str: The sentiment of the text (Positive, Negative, or Neutral).
    """
    # Initialize sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(text)

    # Determine sentiment category
    if sentiment_scores['compound'] > 0.05:
        return "Positive"
    elif sentiment_scores['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    """
    Main function to run the sentiment analysis program.
    """
    print("Welcome to the Sentiment Analysis Tool!")
    print("Type your text below to analyze its sentiment, or type 'exit' to quit.\n")

    while True:
        try:
            # Get input from the user
            user_input = input("Enter text: ").strip()

            # Exit condition
            if user_input.lower() == 'exit':
                print("Thank you for using the Sentiment Analysis Tool. Goodbye!")
                break

            # Check if input is empty
            if not user_input:
                print("No input provided. Please enter some text.")
                continue

            # Perform sentiment analysis
            sentiment = analyze_sentiment(user_input)
            print(f"Sentiment: {sentiment}\n")

        except KeyboardInterrupt:
            # Handle user interrupt gracefully
            print("\nProgram interrupted. Exiting.")
            break
        except Exception as e:
            # Catch and log unexpected errors
            print(f"An error occurred: {e}. Please try again.\n")

if __name__ == "__main__":
    main()
```
