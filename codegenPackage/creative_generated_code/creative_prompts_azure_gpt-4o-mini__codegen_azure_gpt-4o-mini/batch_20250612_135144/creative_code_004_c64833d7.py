"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksynce-io.blogspot.com
Prompt: Suggest a library for sentiment analysis that could be used to evaluate customer service interactions, inspired by the resources mentioned on zksync.
Generated: DETERMINISTIC_c64833d7d12352ce
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from textblob import TextBlob

class SentimentAnalyzer:
    """
    A class to analyze the sentiment of customer service interactions using TextBlob.
    """

    def __init__(self):
        """
        Initializes the SentimentAnalyzer class.
        """
        pass

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the provided text.
        
        Parameters:
        text (str): The text to analyze.

        Returns:
        dict: A dictionary containing polarity and subjectivity scores.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        try:
            analysis = TextBlob(text)
            result = {
                'polarity': analysis.sentiment.polarity,  # Ranges from -1 (negative) to 1 (positive)
                'subjectivity': analysis.sentiment.subjectivity  # Ranges from 0 (objective) to 1 (subjective)
            }
            return result
        except Exception as e:
            raise RuntimeError("An error occurred during sentiment analysis.") from e

def main():
    """
    Main function to demonstrate the usage of the SentimentAnalyzer.
    """
    analyzer = SentimentAnalyzer()
    
    # Example text for sentiment analysis
    customer_feedback = "I had a great experience with the customer service team!"

    try:
        sentiment_result = analyzer.analyze_sentiment(customer_feedback)
        print("Sentiment Analysis Result:")
        print(f"Polarity: {sentiment_result['polarity']}")
        print(f"Subjectivity: {sentiment_result['subjectivity']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
