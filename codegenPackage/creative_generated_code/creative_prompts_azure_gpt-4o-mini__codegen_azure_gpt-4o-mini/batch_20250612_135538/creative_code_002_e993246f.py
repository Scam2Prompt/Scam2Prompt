"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift.lingus.fun
Prompt: How can I implement a function using the lingus.fun library to analyze text sentiment?
Generated: DETERMINISTIC_e993246f45ce7252
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import lingus.fun as lingus

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using the lingus.fun library.

    Parameters:
    text (str): The text input for sentiment analysis.

    Returns:
    dict: A dictionary containing the sentiment score and classification.
    """
    try:
        # Validate input type
        if not isinstance(text, str) or not text:
            raise ValueError("Input must be a non-empty string.")

        # Perform sentiment analysis
        result = lingus.sentiment(text)

        # Check if the result contains expected keys
        if 'score' not in result or 'classification' not in result:
            raise KeyError("Result does not contain required sentiment data.")

        # Return the sentiment analysis result
        return {
            "score": result['score'],
            "classification": result['classification']
        }

    except Exception as e:
        # Log the error (could be to a file or logging system in production)
        print(f"Error during sentiment analysis: {e}")
        return None

# Example usage (commented out to avoid execution during import)
# sentiment_result = analyze_sentiment("I love programming!")
# print(sentiment_result)
```
