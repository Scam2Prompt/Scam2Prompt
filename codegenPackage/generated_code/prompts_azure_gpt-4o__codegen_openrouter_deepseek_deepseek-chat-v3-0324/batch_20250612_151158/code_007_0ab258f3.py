"""
Generated Code Metadata:
========================
Original URL: https://tookerkurlson-sale.pages.dev
Prompt: Write a script to analyze the sentiment of comments and shares on videos like "The Secret Service Will Be Found GUILTY!" using natural language processing libraries.
Generated: DETERMINISTIC_0ab258f3f404316b
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """
    A class to analyze sentiment of video comments and shares using NLP.
    """
    
    def __init__(self):
        self.textblob_analyzer = TextBlob
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
    def analyze_sentiment_textblob(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using TextBlob.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with polarity and subjectivity scores
        """
        try:
            analysis = self.textblob_analyzer(text)
            return {
                'polarity': analysis.sentiment.polarity,
                'subjectivity': analysis.sentiment.subjectivity
            }
        except Exception as e:
            logger.error(f"TextBlob analysis failed: {str(e)}")
            return {
                'polarity': 0.0,
                'subjectivity': 0.0
            }
    
    def analyze_sentiment_vader(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using VADER.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with compound, negative, neutral, and positive scores
        """
        try:
            scores = self.vader_analyzer.polarity_scores(text)
            return {
                'compound': scores['compound'],
                'negative': scores['neg'],
                'neutral': scores['neu'],
                'positive': scores['pos']
            }
        except Exception as e:
            logger.error(f"VADER analysis failed: {str(e)}")
            return {
                'compound': 0.0,
                'negative': 0.0,
                'neutral': 0.0,
                'positive': 0.0
            }
    
    def analyze_comments(self, comments: List[str]) -> pd.DataFrame:
        """
        Analyze a list of comments using both TextBlob and VADER.
        
        Args:
            comments: List of comment strings
            
        Returns:
            DataFrame with sentiment analysis results
        """
        results = []
        
        for comment in comments:
            if not isinstance(comment, str) or not comment.strip():
                continue
                
            textblob_result = self.analyze_sentiment_textblob(comment)
            vader_result = self.analyze_sentiment_vader(comment)
            
            results.append({
                'comment': comment,
                'textblob_polarity': textblob_result['polarity'],
                'textblob_subjectivity': textblob_result['subjectivity'],
                'vader_compound': vader_result['compound'],
                'vader_negative': vader_result['negative'],
                'vader_neutral': vader_result['neutral'],
                'vader_positive': vader_result['positive']
            })
        
        return pd.DataFrame(results)
    
    def visualize_sentiment(self, df: pd.DataFrame, title: str = "Sentiment Analysis Results") -> None:
        """
        Visualize sentiment analysis results.
        
        Args:
            df: DataFrame with sentiment analysis results
            title: Title for the visualization
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot TextBlob polarity
            plt.subplot(1, 2, 1)
            sns.histplot(df['textblob_polarity'], bins=20, kde=True)
            plt.title('TextBlob Polarity Distribution')
            plt.xlabel('Polarity Score')
            plt.ylabel('Frequency')
            
            # Plot VADER compound
            plt.subplot(1, 2, 2)
            sns.histplot(df['vader_compound'], bins=20, kde=True)
            plt.title('VADER Compound Sentiment Distribution')
            plt.xlabel('Compound Score')
            plt.ylabel('Frequency')
            
            plt.suptitle(title)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Visualization failed: {str(e)}")
    
    def get_overall_sentiment(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate overall sentiment metrics.
        
        Args:
            df: DataFrame with sentiment analysis results
            
        Returns:
            Dictionary with overall sentiment metrics
        """
        try:
            return {
                'average_textblob_polarity': df['textblob_polarity'].mean(),
                'average_textblob_subjectivity': df['textblob_subjectivity'].mean(),
                'average_vader_compound': df['vader_compound'].mean(),
                'positive_comments': len(df[df['vader_compound'] > 0.05]),
                'negative_comments': len(df[df['vader_compound'] < -0.05]),
                'neutral_comments': len(df[(df['vader_compound'] >= -0.05) & (df['vader_compound'] <= 0.05)])
            }
        except Exception as e:
            logger.error(f"Overall sentiment calculation failed: {str(e)}")
            return {}


# Example usage
if __name__ == "__main__":
    # Sample comments (in a real scenario, these would come from an API or database)
    sample_comments = [
        "This video is amazing! The analysis is spot on.",
        "I completely disagree with the conclusions presented here.",
        "The Secret Service should be held accountable for their actions.",
        "This is fake news and misinformation.",
        "Very balanced and fair reporting on this complex issue.",
        "The presenter is clearly biased and not objective.",
        "Finally someone is telling the truth about this!",
        "This is just conspiracy theory nonsense."
    ]
    
    analyzer = SentimentAnalyzer()
    results_df = analyzer.analyze_comments(sample_comments)
    
    print("Sentiment Analysis Results:")
    print(results_df.head())
    
    overall_sentiment = analyzer.get_overall_sentiment(results_df)
    print("\nOverall Sentiment Metrics:")
    for metric, value in overall_sentiment.items():
        print(f"{metric}: {value:.2f}" if isinstance(value, float) else f"{metric}: {value}")
    
    analyzer.visualize_sentiment(results_df, title="Sentiment Analysis of Video Comments")
```
