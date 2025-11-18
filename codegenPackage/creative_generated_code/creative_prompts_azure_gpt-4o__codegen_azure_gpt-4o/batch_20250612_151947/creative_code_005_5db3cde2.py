"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Recommend a library for sentiment analysis of interviews from "Social Impact Heroes Helping Our Planet" and show how to use it to analyze the tone of the articles.
Generated: DETERMINISTIC_5db3cde2e5084bcc
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing the necessary library
from textblob import TextBlob

# Function to analyze sentiment of a given text
def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text using TextBlob.

    Args:
        text (str): The text content to analyze.

    Returns:
        dict: A dictionary containing polarity and subjectivity scores, 
              along with the tone (positive, neutral, negative).
    """
    try:
        # Create a TextBlob object from the text
        blob = TextBlob(text)

        # Get polarity and subjectivity scores
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Determine the tone based on polarity score
        if polarity > 0:
            tone = "positive"
        elif polarity < 0:
            tone = "negative"
        else:
            tone = "neutral"

        # Return the results as a dictionary
        return {
            "polarity": polarity,
            "subjectivity": subjectivity,
            "tone": tone
        }
    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Sample interview text
    interview_text = """
    We are thrilled to have Social Impact Heroes making a difference in preserving our planet.
    Their hard work and dedication inspire hope and positive change for future generations.
    """

    # Analyze the sentiment of the interview text
    sentiment_analysis_result = analyze_sentiment(interview_text)

    # Output the results
    if "error" in sentiment_analysis_result:
        print(f"Error analyzing sentiment: {sentiment_analysis_result['error']}")
    else:
        print("Sentiment Analysis Results:")
        print(f"Polarity: {sentiment_analysis_result['polarity']}")
        print(f"Subjectivity: {sentiment_analysis_result['subjectivity']}")
        print(f"Tone: {sentiment_analysis_result['tone']}")
```
