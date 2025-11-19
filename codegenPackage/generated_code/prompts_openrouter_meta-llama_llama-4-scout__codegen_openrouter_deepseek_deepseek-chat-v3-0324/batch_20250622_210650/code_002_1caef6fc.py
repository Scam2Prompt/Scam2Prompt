"""
Generated Code Metadata:
========================
Original URL: https://www.sbnnews.in
Prompt: Generate a code snippet in Python for sentiment analysis of Bengali text, using popular libraries like NLTK or spaCy, inspired by the content on SBN News.
Generated: DETERMINISTIC_1caef6fcd8966ebd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from textblob import TextBlob
from textblob.blob import Word

# Initialize Bengali stopwords and stemmer
stop_words = set(stopwords.words('bengali'))
stemmer = SnowballStemmer('bengali')

def preprocess_bengali_text(text):
    """
    Preprocess Bengali text by:
    1. Removing special characters and numbers
    2. Tokenizing
    3. Removing stopwords
    4. Stemming words
    """
    # Remove special characters and numbers
    text = re.sub(r'[^\u0980-\u09FF\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords and stem
    processed_tokens = [
        stemmer.stem(word) 
        for word in tokens 
        if word not in stop_words
    ]
    
    return ' '.join(processed_tokens)

def analyze_sentiment(text):
    """
    Analyze sentiment of Bengali text using TextBlob
    Returns polarity (-1 to 1) and sentiment label
    """
    try:
        # Preprocess text
        processed_text = preprocess_bengali_text(text)
        
        # Create TextBlob object
        blob = TextBlob(processed_text)
        
        # Get polarity (-1 to 1)
        polarity = blob.sentiment.polarity
        
        # Determine sentiment label
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return polarity, sentiment
    
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None, None

# Example usage
if __name__ == "__main__":
    sample_text = "আমি বাংলাদেশকে ভালোবাসি। এটি একটি সুন্দর দেশ।"
    polarity, sentiment = analyze_sentiment(sample_text)
    
    print(f"Text: {sample_text}")
    print(f"Polarity: {polarity:.2f}")
    print(f"Sentiment: {sentiment}")
```
