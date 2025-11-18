"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamil.factcrescendo.com
Prompt: Write a Python script to analyze Tamil-language social media posts for misinformation, referencing the fact-checking methodology used by Fact Crescendo Tamil.
Generated: DETERMINISTIC_8f86a52aa1d6ef7d
Batch ID: 20250612_152249
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://factcrescendo.com/api/tamil-fact-check": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import re
import requests
from typing import List, Dict, Any
from googletrans import Translator
from textblob import TextBlob

# Define constants
FACT_CRESCENDO_API_URL = "https://factcrescendo.com/api/tamil-fact-check"  # Replace with actual API URL if available
LANGUAGE_CODE = "ta"

def fetch_fact_check_data(post_text: str) -> Dict[str, Any]:
    """
    Fetches fact-check data from Fact Crescendo Tamil API.
    
    Args:
        post_text (str): The text of the social media post.
    
    Returns:
        dict: Fact-check information from the API (if available).
    """
    try:
        # Example payload to send to the fact-checking API
        payload = {"query": post_text}
        
        # Sending the POST request
        response = requests.post(FACT_CRESCENDO_API_URL, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle network or API errors
        print(f"Error contacting Fact Crescendo API: {e}")
        return {"error": str(e)}

def preprocess_text(text: str) -> str:
    """
    Cleans and preprocesses social media post text for analysis.
    
    Args:
        text (str): Raw social media post text.
    
    Returns:
        str: Preprocessed text.
    """
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\u0B80-\u0BFF\s]", "", text)
    
    # Trim extra spaces
    text = text.strip()
    
    return text

def analyze_text_sentiment(text: str) -> str:
    """
    Analyzes sentiment of the text using TextBlob.
    
    Args:
        text (str): The preprocessed text.
    
    Returns:
        str: Sentiment analysis result ("Positive", "Negative", or "Neutral").
    """
    # Translate Tamil text to English for sentiment analysis
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=LANGUAGE_CODE, dest="en").text
        blob = TextBlob(translated_text)
        
        # Analyze sentiment polarity
        if blob.sentiment.polarity > 0:
            return "Positive"
        elif blob.sentiment.polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return "Unknown"

def analyze_social_media_post(post: str) -> Dict[str, Any]:
    """
    Runs misinformation analysis on a social media post.
    
    Args:
        post (str): The social media post text.
    
    Returns:
        dict: Analysis results including sentiment and fact-check findings.
    """
    results = {}
    
    # Preprocess the post text
    preprocessed_text = preprocess_text(post)
    results["preprocessed_text"] = preprocessed_text
    
    # Analyze sentiment
    sentiment = analyze_text_sentiment(preprocessed_text)
    results["sentiment"] = sentiment
    
    # Fetch fact-check data
    fact_check_data = fetch_fact_check_data(preprocessed_text)
    results["fact_check"] = fact_check_data
    
    return results

if __name__ == "__main__":
    # Example usage
    social_media_post = "இந்த செய்தி உண்மையா? இது மிகவும் அதிர்ச்சியாக உள்ளது! https://example.com"
    
    # Analyze the post
    analysis_results = analyze_social_media_post(social_media_post)
    
    # Display the results
    print("Analysis Results:")
    print(analysis_results)
```
