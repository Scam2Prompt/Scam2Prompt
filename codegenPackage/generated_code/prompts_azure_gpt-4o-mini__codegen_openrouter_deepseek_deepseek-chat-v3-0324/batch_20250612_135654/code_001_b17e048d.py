"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Write a Python script that utilizes the principles of SQ (somatic intelligence) to analyze user feedback on personal coaching sessions.
Generated: DETERMINISTIC_b17e048d4258a462
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import re
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import numpy as np
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class SQFeedbackAnalyzer:
    """
    A class to analyze user feedback using Somatic Intelligence (SQ) principles.
    """
    
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
        self.sq_keywords = {
            'body_awareness': ['body', 'posture', 'breath', 'movement', 'physical'],
            'emotional': ['feel', 'emotion', 'emotional', 'mood', 'affect'],
            'cognitive': ['think', 'thought', 'mind', 'cognitive', 'mental'],
            'relational': ['connect', 'relationship', 'interact', 'social', 'others']
        }
    
    def _preprocess_text(self, text: str) -> str:
        """
        Preprocess text by removing special characters, lowercasing, and tokenizing.
        """
        text = re.sub(r'[^\w\s]', '', text.lower())
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in self.stop_words]
        return ' '.join(tokens)
    
    def _analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of the text using VADER.
        """
        return self.sia.polarity_scores(text)
    
    def _extract_sq_dimensions(self, text: str) -> Dict[str, int]:
        """
        Extract mentions of SQ dimensions in the text.
        """
        dimension_counts = defaultdict(int)
        preprocessed_text = self._preprocess_text(text)
        
        for dimension, keywords in self.sq_keywords.items():
            for keyword in keywords:
                if keyword in preprocessed_text:
                    dimension_counts[dimension] += 1
        
        return dict(dimension_counts)
    
    def _calculate_sq_score(self, sentiment: Dict[str, float], dimensions: Dict[str, int]) -> float:
        """
        Calculate an overall SQ score based on sentiment and dimension mentions.
        """
        if not dimensions:
            return 0.0
        
        # Weight positive sentiment more heavily
        sentiment_weight = 0.7 * sentiment['pos'] - 0.3 * sentiment['neg']
        
        # Normalize dimension counts
        total_dimensions = sum(dimensions.values())
        if total_dimensions == 0:
            return 0.0
        
        dimension_score = sum(dimensions.values()) / total_dimensions
        
        # Combine scores (70% sentiment, 30% dimensions)
        return 0.7 * sentiment_weight + 0.3 * dimension_score
    
    def analyze_feedback(self, feedback_text: str) -> Dict:
        """
        Analyze user feedback and return comprehensive SQ analysis.
        """
        if not feedback_text or not isinstance(feedback_text, str):
            raise ValueError("Feedback text must be a non-empty string")
        
        sentiment = self._analyze_sentiment(feedback_text)
        dimensions = self._extract_sq_dimensions(feedback_text)
        sq_score = self._calculate_sq_score(sentiment, dimensions)
        
        return {
            'sentiment': sentiment,
            'sq_dimensions': dimensions,
            'sq_score': round(sq_score, 2),
            'feedback_length': len(feedback_text),
            'word_count': len(word_tokenize(feedback_text))
        }
    
    def analyze_multiple_feedbacks(self, feedbacks: List[str]) -> Dict:
        """
        Analyze multiple feedback texts and return aggregated results.
        """
        if not feedbacks or not isinstance(feedbacks, list):
            raise ValueError("Feedbacks must be a non-empty list")
        
        results = []
        for feedback in feedbacks:
            try:
                results.append(self.analyze_feedback(feedback))
            except ValueError as e:
                print(f"Skipping invalid feedback: {e}")
                continue
        
        if not results:
            return {}
        
        # Calculate averages
        avg_sq_score = np.mean([r['sq_score'] for r in results])
        avg_sentiment = {
            'pos': np.mean([r['sentiment']['pos'] for r in results]),
            'neg': np.mean([r['sentiment']['neg'] for r in results]),
            'neu': np.mean([r['sentiment']['neu'] for r in results]),
            'compound': np.mean([r['sentiment']['compound'] for r in results])
        }
        
        # Sum dimension counts
        total_dimensions = defaultdict(int)
        for r in results:
            for dim, count in r['sq_dimensions'].items():
                total_dimensions[dim] += count
        
        return {
            'average_sq_score': round(avg_sq_score, 2),
            'average_sentiment': avg_sentiment,
            'total_dimension_mentions': dict(total_dimensions),
            'total_feedbacks_analyzed': len(results),
            'individual_results': results
        }

def main():
    """
    Example usage of the SQFeedbackAnalyzer.
    """
    analyzer = SQFeedbackAnalyzer()
    
    # Example feedbacks
    feedbacks = [
        "The session helped me become more aware of my body posture and breathing. I feel more relaxed now.",
        "I didn't connect well with the coach. The exercises felt forced and uncomfortable.",
        "Great insights into how my emotions affect my physical state. Will definitely come back!",
        "The cognitive exercises were too challenging. I felt frustrated during most of the session."
    ]
    
    # Analyze single feedback
    print("Analyzing single feedback:")
    result = analyzer.analyze_feedback(feedbacks[0])
    print(json.dumps(result, indent=2))
    
    # Analyze multiple feedbacks
    print("\nAnalyzing multiple feedbacks:")
    aggregated = analyzer.analyze_multiple_feedbacks(feedbacks)
    print(json.dumps(aggregated, indent=2))

if __name__ == "__main__":
    main()
```
