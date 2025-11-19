"""
Generated Code Metadata:
========================
Original URL: https://my.dropz.xyz
Prompt: Write a script that analyzes the sentiment of news articles about cryptocurrency and politics, using machine learning libraries like NLTK or spaCy.
Generated: DETERMINISTIC_431732d5f1891340
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
import re
import logging
from typing import List, Dict, Optional

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize NLP tools
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    logger.error("spaCy model 'en_core_web_sm' not found. Please install it.")
    raise

try:
    sia = SentimentIntensityAnalyzer()
except LookupError:
    logger.error("NLTK sentiment analyzer resources not found. Downloading required NLTK data...")
    import nltk
    nltk.download(['vader_lexicon', 'punkt', 'stopwords', 'wordnet'])
    sia = SentimentIntensityAnalyzer()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text: str) -> str:
    """
    Preprocess text by removing special characters, stopwords, and lemmatizing.
    
    Args:
        text: Input text to preprocess
        
    Returns:
        Cleaned and processed text
    """
    if not isinstance(text, str):
        return ""
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize and lowercase
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and lemmatize
    processed_tokens = [
        lemmatizer.lemmatize(token) 
        for token in tokens 
        if token not in stop_words
    ]
    
    return ' '.join(processed_tokens)

def analyze_sentiment_nltk(text: str) -> Dict[str, float]:
    """
    Analyze sentiment using NLTK's VADER sentiment analyzer.
    
    Args:
        text: Input text to analyze
        
    Returns:
        Dictionary with sentiment scores (neg, neu, pos, compound)
    """
    try:
        return sia.polarity_scores(text)
    except Exception as e:
        logger.error(f"Error in NLTK sentiment analysis: {e}")
        return {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}

def analyze_sentiment_spacy(text: str) -> float:
    """
    Analyze sentiment using spaCy's rule-based sentiment analysis.
    
    Args:
        text: Input text to analyze
        
    Returns:
        Sentiment score between -1 (negative) and 1 (positive)
    """
    try:
        doc = nlp(text)
        if hasattr(doc, 'sentiment'):
            return doc.sentiment
        else:
            logger.warning("spaCy model doesn't have sentiment analysis capability")
            return 0.0
    except Exception as e:
        logger.error(f"Error in spaCy sentiment analysis: {e}")
        return 0.0

def categorize_sentiment(compound_score: float) -> str:
    """
    Categorize sentiment based on compound score.
    
    Args:
        compound_score: Sentiment compound score from -1 to 1
        
    Returns:
        Sentiment category (Positive, Neutral, Negative)
    """
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_articles(articles: List[Dict[str, str]]) -> pd.DataFrame:
    """
    Analyze sentiment of multiple articles.
    
    Args:
        articles: List of dictionaries with 'title' and 'content' keys
        
    Returns:
        DataFrame with sentiment analysis results
    """
    results = []
    
    for article in articles:
        try:
            if not isinstance(article, dict) or 'content' not in article:
                logger.warning("Invalid article format, skipping")
                continue
                
            content = article.get('content', '')
            title = article.get('title', '')
            
            # Preprocess text
            processed_text = preprocess_text(content)
            
            # Analyze sentiment
            nltk_scores = analyze_sentiment_nltk(processed_text)
            spacy_score = analyze_sentiment_spacy(processed_text)
            
            results.append({
                'title': title,
                'content_length': len(content),
                'processed_text': processed_text,
                'nltk_neg': nltk_scores['neg'],
                'nltk_neu': nltk_scores['neu'],
                'nltk_pos': nltk_scores['pos'],
                'nltk_compound': nltk_scores['compound'],
                'spacy_sentiment': spacy_score,
                'sentiment_category': categorize_sentiment(nltk_scores['compound'])
            })
            
        except Exception as e:
            logger.error(f"Error processing article '{title}': {e}")
            continue
    
    return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    # Sample articles (in a real scenario, these would come from a database or API)
    sample_articles = [
        {
            'title': 'Bitcoin reaches all-time high',
            'content': 'Bitcoin has surged to a new record high, with investors optimistic about its future.'
        },
        {
            'title': 'Political tensions affect crypto markets',
            'content': 'The ongoing political crisis has caused uncertainty in cryptocurrency markets, with prices dropping significantly.'
        },
        {
            'title': 'Government announces new crypto regulations',
            'content': 'Officials have proposed new regulations that aim to protect investors while fostering innovation.'
        }
    ]
    
    # Analyze articles
    results_df = analyze_articles(sample_articles)
    
    # Display results
    print("\nSentiment Analysis Results:")
    print(results_df[['title', 'sentiment_category', 'nltk_compound', 'spacy_sentiment']])
```
