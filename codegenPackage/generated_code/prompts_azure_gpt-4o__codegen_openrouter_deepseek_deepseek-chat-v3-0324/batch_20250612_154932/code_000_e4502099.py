"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Write Python code to analyze social media content for patterns of misinformation using sentiment analysis and keyword extraction. Recommend libraries or APIs that can assist with this task.
Generated: DETERMINISTIC_e45020998e410acb
Batch ID: 20250612_154932
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
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import logging
from typing import List, Dict, Tuple, Optional

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

class MisinformationAnalyzer:
    """
    A class to analyze social media content for patterns of misinformation using
    sentiment analysis and keyword extraction.
    """
    
    def __init__(self, custom_stopwords: Optional[List[str]] = None):
        """
        Initialize the analyzer with optional custom stopwords.
        
        Args:
            custom_stopwords: List of additional stopwords to exclude from analysis
        """
        self.stop_words = set(stopwords.words('english'))
        if custom_stopwords:
            self.stop_words.update(custom_stopwords)
        self.vectorizer = TfidfVectorizer(max_features=100, stop_words=list(self.stop_words))
        
    def preprocess_text(self, text: str) -> str:
        """
        Clean and preprocess text for analysis.
        
        Args:
            text: Raw text to preprocess
            
        Returns:
            Cleaned text
        """
        try:
            # Remove URLs, mentions, and special characters
            text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
            text = re.sub(r'\@\w+|\#', '', text)
            text = re.sub(r'[^\w\s]', '', text)
            text = text.lower().strip()
            return text
        except Exception as e:
            logger.error(f"Error preprocessing text: {e}")
            return ""
    
    def analyze_sentiment(self, text: str) -> Tuple[float, float]:
        """
        Perform sentiment analysis on text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Tuple of (polarity, subjectivity) scores
        """
        try:
            analysis = TextBlob(text)
            return analysis.sentiment.polarity, analysis.sentiment.subjectivity
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {e}")
            return 0.0, 0.0
    
    def extract_keywords(self, texts: List[str]) -> Dict[str, float]:
        """
        Extract important keywords from a collection of texts.
        
        Args:
            texts: List of texts to analyze
            
        Returns:
            Dictionary of keywords and their TF-IDF scores
        """
        try:
            processed_texts = [self.preprocess_text(text) for text in texts]
            tfidf_matrix = self.vectorizer.fit_transform(processed_texts)
            feature_names = self.vectorizer.get_feature_names_out()
            tfidf_scores = tfidf_matrix.sum(axis=0).A1
            return dict(zip(feature_names, tfidf_scores))
        except Exception as e:
            logger.error(f"Error extracting keywords: {e}")
            return {}
    
    def analyze_content(self, content: List[str]) -> Dict:
        """
        Analyze social media content for misinformation patterns.
        
        Args:
            content: List of social media posts/texts
            
        Returns:
            Analysis results including sentiment and keywords
        """
        results = {
            'sentiments': [],
            'keywords': {},
            'average_polarity': 0.0,
            'average_subjectivity': 0.0
        }
        
        try:
            # Analyze sentiment for each post
            sentiments = []
            for text in content:
                polarity, subjectivity = self.analyze_sentiment(text)
                sentiments.append({
                    'text': text,
                    'polarity': polarity,
                    'subjectivity': subjectivity
                })
            
            # Calculate averages
            if sentiments:
                avg_polarity = sum(s['polarity'] for s in sentiments) / len(sentiments)
                avg_subjectivity = sum(s['subjectivity'] for s in sentiments) / len(sentiments)
                
                results['sentiments'] = sentiments
                results['average_polarity'] = avg_polarity
                results['average_subjectivity'] = avg_subjectivity
            
            # Extract keywords
            results['keywords'] = self.extract_keywords(content)
            
            return results
        except Exception as e:
            logger.error(f"Error analyzing content: {e}")
            return results

# Example usage
if __name__ == "__main__":
    # Sample social media content
    sample_content = [
        "The vaccine causes autism. Don't trust big pharma!",
        "Climate change is a hoax created by the government.",
        "5G towers are spreading coronavirus. Wake up people!",
        "The earth is flat and NASA is lying to us all.",
        "Bill Gates wants to microchip everyone with the vaccine."
    ]
    
    analyzer = MisinformationAnalyzer()
    analysis_results = analyzer.analyze_content(sample_content)
    
    # Print results
    print("Sentiment Analysis Results:")
    for sentiment in analysis_results['sentiments']:
        print(f"\nText: {sentiment['text']}")
        print(f"Polarity: {sentiment['polarity']:.2f}, Subjectivity: {sentiment['subjectivity']:.2f}")
    
    print(f"\nAverage Polarity: {analysis_results['average_polarity']:.2f}")
    print(f"Average Subjectivity: {analysis_results['average_subjectivity']:.2f}")
    
    print("\nTop Keywords:")
    for keyword, score in sorted(analysis_results['keywords'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{keyword}: {score:.2f}")
```
