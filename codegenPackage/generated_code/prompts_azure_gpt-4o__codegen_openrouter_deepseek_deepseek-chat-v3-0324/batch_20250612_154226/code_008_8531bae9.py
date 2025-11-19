"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Generate Python code to analyze customer satisfaction data from testimonials, using examples like "Truly satisfied clients!" and "Their attention to detail is commendable," as highlighted on Meezan Interior Solutions' site.
Generated: DETERMINISTIC_8531bae9d560aada
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import defaultdict
from typing import List, Dict, Tuple
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure required NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')

class TestimonialAnalyzer:
    """
    Analyzes customer testimonials for sentiment and key themes.
    """
    
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.positive_words = set(['satisfied', 'happy', 'excellent', 'great', 'commendable', 'wonderful'])
        self.negative_words = set(['unsatisfied', 'poor', 'bad', 'terrible', 'disappointed'])
    
    def preprocess_text(self, text: str) -> List[str]:
        """
        Preprocesses text by tokenizing, removing stopwords, and lemmatizing.
        """
        tokens = word_tokenize(text.lower())
        filtered_tokens = [
            self.lemmatizer.lemmatize(token) 
            for token in tokens 
            if token.isalpha() and token not in self.stop_words
        ]
        return filtered_tokens
    
    def analyze_sentiment(self, testimonial: str) -> Dict[str, float]:
        """
        Analyzes sentiment of a single testimonial.
        Returns a dictionary with sentiment scores.
        """
        return self.sia.polarity_scores(testimonial)
    
    def extract_key_themes(self, testimonials: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
        """
        Extracts and counts the most common themes from testimonials.
        """
        theme_counts = defaultdict(int)
        
        for testimonial in testimonials:
            tokens = self.preprocess_text(testimonial)
            for token in tokens:
                if token in self.positive_words or token in self.negative_words:
                    theme_counts[token] += 1
        
        return sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    def analyze_testimonials(self, testimonials: List[str]) -> Dict:
        """
        Comprehensive analysis of multiple testimonials.
        Returns sentiment statistics and key themes.
        """
        if not testimonials:
            raise ValueError("No testimonials provided for analysis.")
        
        results = {
            'sentiments': [],
            'average_scores': {
                'pos': 0,
                'neg': 0,
                'neu': 0,
                'compound': 0
            },
            'key_themes': []
        }
        
        total = len(testimonials)
        
        for testimonial in testimonials:
            sentiment = self.analyze_sentiment(testimonial)
            results['sentiments'].append(sentiment)
            
            for key in results['average_scores']:
                results['average_scores'][key] += sentiment[key] / total
        
        results['key_themes'] = self.extract_key_themes(testimonials)
        
        return results

# Example usage
if __name__ == "__main__":
    testimonials = [
        "Truly satisfied clients!",
        "Their attention to detail is commendable.",
        "The team delivered beyond our expectations.",
        "Very disappointed with the timeline.",
        "Excellent craftsmanship and professional service."
    ]
    
    analyzer = TestimonialAnalyzer()
    analysis_results = analyzer.analyze_testimonials(testimonials)
    
    print("Analysis Results:")
    print(f"Average Positive Score: {analysis_results['average_scores']['pos']:.2f}")
    print(f"Average Negative Score: {analysis_results['average_scores']['neg']:.2f}")
    print(f"Key Themes: {analysis_results['key_themes']}")
```
