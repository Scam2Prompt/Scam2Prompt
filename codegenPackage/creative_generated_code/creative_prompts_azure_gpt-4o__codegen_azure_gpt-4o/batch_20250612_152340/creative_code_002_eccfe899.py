"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Recommend a library for analyzing text descriptions of artists from the "Tree House Sessions" website and provide example code for sentiment analysis.
Generated: DETERMINISTIC_eccfe899099692ac
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from textblob import TextBlob  # Library for text processing and sentiment analysis

# Function to analyze the sentiment of text
def analyze_artist_sentiment(description):
    """
    Analyze the sentiment of a given text description.
    
    Parameters:
        description (str): The text description of the artist.
    
    Returns:
        dict: A dictionary containing polarity and subjectivity scores.
              Polarity is a measure of sentiment (-1.0 to 1.0).
              Subjectivity is a measure of opinion (0.0 to 1.0).
    """
    try:
        # Create a TextBlob object
        blob = TextBlob(description)
        
        # Extract sentiment metrics
        sentiment = {
            'polarity': blob.sentiment.polarity,     # Sentiment polarity (-1.0 to 1.0)
            'subjectivity': blob.sentiment.subjectivity  # Sentiment subjectivity (0.0 to 1.0)
        }
        return sentiment
    except Exception as e:
        # Handle any errors gracefully
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Sample text description
    sample_description = "The artist's performance was absolutely captivating and full of emotion."
    
    # Analyze sentiment
    sentiment_result = analyze_artist_sentiment(sample_description)
    
    # Output the results
    if 'error' in sentiment_result:
        print(f"Error occurred: {sentiment_result['error']}")
    else:
        print(f"Sentiment Analysis Results:")
        print(f"Polarity: {sentiment_result['polarity']}")
        print(f"Subjectivity: {sentiment_result['subjectivity']}")
```
