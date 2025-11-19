"""
Generated Code Metadata:
========================
Original URL: https://immediate-byte.com
Prompt: Develop a Python program to analyze the emotional and behavioral aspects influencing investors' decision-making processes, using investment psychology principles and sentiment analysis techniques.
Generated: DETERMINISTIC_1671d61a9f131fe5
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
import numpy as np
import pandas as pd
from textblob import TextBlob
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('investor_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class InvestorSentimentAnalyzer:
    """
    A class to analyze investor sentiment and behavioral aspects using text analysis.
    """
    
    def __init__(self):
        self.lexicon = self._load_lexicon()
        self.stopwords = self._load_stopwords()
        
    def _load_lexicon(self) -> Dict[str, float]:
        """
        Load sentiment lexicon from a predefined file.
        Returns a dictionary of words with their sentiment scores.
        """
        try:
            # In a real scenario, this would load from a file or database
            lexicon = {
                'profit': 0.8,
                'gain': 0.7,
                'loss': -0.8,
                'risk': -0.5,
                'bullish': 0.9,
                'bearish': -0.9,
                'stable': 0.3,
                'volatile': -0.6
            }
            return lexicon
        except Exception as e:
            logger.error(f"Failed to load lexicon: {e}")
            raise

    def _load_stopwords(self) -> List[str]:
        """
        Load stopwords to filter out from analysis.
        """
        try:
            # In a real scenario, this would load from a file
            stopwords = ['the', 'and', 'is', 'in', 'it', 'this', 'that']
            return stopwords
        except Exception as e:
            logger.error(f"Failed to load stopwords: {e}")
            raise

    def clean_text(self, text: str) -> str:
        """
        Clean and preprocess text for analysis.
        """
        try:
            text = text.lower()
            text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
            text = ' '.join([word for word in text.split() if word not in self.stopwords])
            return text
        except Exception as e:
            logger.error(f"Text cleaning failed: {e}")
            raise

    def calculate_sentiment(self, text: str) -> float:
        """
        Calculate sentiment score for a given text using lexicon-based approach.
        """
        try:
            cleaned_text = self.clean_text(text)
            words = cleaned_text.split()
            sentiment = 0.0
            valid_words = 0
            
            for word in words:
                if word in self.lexicon:
                    sentiment += self.lexicon[word]
                    valid_words += 1
            
            return sentiment / valid_words if valid_words > 0 else 0.0
        except Exception as e:
            logger.error(f"Sentiment calculation failed: {e}")
            raise

    def analyze_textblob_sentiment(self, text: str) -> Tuple[float, float]:
        """
        Analyze sentiment using TextBlob (polarity and subjectivity).
        """
        try:
            analysis = TextBlob(text)
            return analysis.sentiment.polarity, analysis.sentiment.subjectivity
        except Exception as e:
            logger.error(f"TextBlob analysis failed: {e}")
            raise

    def behavioral_analysis(self, investment_data: List[Dict]) -> Dict[str, Dict]:
        """
        Perform behavioral analysis on investment decisions.
        """
        try:
            results = defaultdict(dict)
            
            for record in investment_data:
                text = record.get('comment', '') or record.get('description', '')
                if not text:
                    continue
                
                # Get sentiment scores
                lexicon_score = self.calculate_sentiment(text)
                polarity, subjectivity = self.analyze_textblob_sentiment(text)
                
                # Behavioral indicators
                results[record.get('id', 'unknown')] = {
                    'lexicon_score': lexicon_score,
                    'polarity': polarity,
                    'subjectivity': subjectivity,
                    'confidence': abs(polarity) * (1 - subjectivity),
                    'risk_tolerance': self._assess_risk_tolerance(polarity, lexicon_score),
                    'decision_making': self._assess_decision_making(subjectivity)
                }
            
            return dict(results)
        except Exception as e:
            logger.error(f"Behavioral analysis failed: {e}")
            raise

    def _assess_risk_tolerance(self, polarity: float, lexicon_score: float) -> str:
        """
        Assess risk tolerance based on sentiment scores.
        """
        try:
            combined_score = (polarity + lexicon_score) / 2
            if combined_score > 0.5:
                return "High risk tolerance"
            elif combined_score > 0:
                return "Moderate risk tolerance"
            else:
                return "Low risk tolerance"
        except Exception as e:
            logger.error(f"Risk tolerance assessment failed: {e}")
            raise

    def _assess_decision_making(self, subjectivity: float) -> str:
        """
        Assess decision-making style based on subjectivity.
        """
        try:
            if subjectivity > 0.6:
                return "Emotional decision-making"
            elif subjectivity > 0.3:
                return "Balanced decision-making"
            else:
                return "Rational decision-making"
        except Exception as e:
            logger.error(f"Decision-making assessment failed: {e}")
            raise

    def visualize_results(self, analysis_results: Dict[str, Dict], output_path: str = None):
        """
        Visualize the analysis results.
        """
        try:
            df = pd.DataFrame.from_dict(analysis_results, orient='index')
            
            plt.figure(figsize=(12, 8))
            
            # Plot sentiment distribution
            plt.subplot(2, 2, 1)
            sns.histplot(df['polarity'], kde=True)
            plt.title('Sentiment Polarity Distribution')
            
            # Plot subjectivity distribution
            plt.subplot(2, 2, 2)
            sns.histplot(df['subjectivity'], kde=True)
            plt.title('Subjectivity Distribution')
            
            # Plot risk tolerance
            plt.subplot(2, 2, 3)
            sns.countplot(y='risk_tolerance', data=df)
            plt.title('Risk Tolerance Analysis')
            
            # Plot decision making
            plt.subplot(2, 2, 4)
            sns.countplot(y='decision_making', data=df)
            plt.title('Decision Making Style')
            
            plt.tight_layout()
            
            if output_path:
                plt.savefig(output_path)
                logger.info(f"Visualization saved to {output_path}")
            else:
                plt.show()
        except Exception as e:
            logger.error(f"Visualization failed: {e}")
            raise

def load_sample_data() -> List[Dict]:
    """
    Load sample investment data for demonstration.
    """
    sample_data = [
        {
            "id": 1,
            "comment": "I'm very bullish on this stock. The fundamentals are strong and growth potential is excellent.",
            "timestamp": "2023-01-15"
        },
        {
            "id": 2,
            "comment": "The market seems too volatile right now. I'm concerned about potential losses.",
            "timestamp": "2023-01-16"
        },
        {
            "id": 3,
            "comment": "This is a stable investment with moderate returns. Not exciting but safe.",
            "timestamp": "2023-01-17"
        },
        {
            "id": 4,
            "comment": "I feel uncertain about this investment. The risk might outweigh the potential gains.",
            "timestamp": "2023-01-18"
        }
    ]
    return sample_data

def main():
    try:
        # Initialize analyzer
        analyzer = InvestorSentimentAnalyzer()
        
        # Load data (in production, this would come from a database/API)
        investment_data = load_sample_data()
        
        # Perform analysis
        analysis_results = analyzer.behavioral_analysis(investment_data)
        
        # Save results to JSON
        with open('analysis_results.json', 'w') as f:
            json.dump(analysis_results, f, indent=2)
        
        # Visualize results
        analyzer.visualize_results(analysis_results, 'analysis_visualization.png')
        
        logger.info("Analysis completed successfully")
        
    except Exception as e:
        logger.error(f"Program failed: {e}")
        raise

if __name__ == "__main__":
    main()
```
