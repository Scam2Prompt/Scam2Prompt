"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Create a script to automate the collection and analysis of feedback from experiential learning events, incorporating features for sentiment analysis and actionable insights, as emphasized by Virtual5.
Generated: DETERMINISTIC_ec300c57b6577261
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import pandas as pd
from textblob import TextBlob
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from typing import List, Dict, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('feedback_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FeedbackAnalyzer:
    """Automates collection and analysis of experiential learning feedback."""
    
    def __init__(self, data_dir: str = 'data'):
        """Initialize the analyzer with data directory."""
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.feedback_data = []
        self.insights = defaultdict(list)
        
    def load_feedback(self, file_path: str) -> None:
        """Load feedback data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.feedback_data.extend(data)
                    logger.info(f"Loaded {len(data)} feedback entries from {file_path}")
                else:
                    logger.warning(f"Invalid data format in {file_path}. Expected list.")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in file: {file_path}")
        except Exception as e:
            logger.error(f"Error loading feedback: {str(e)}")
    
    def collect_feedback(self, feedback: Dict) -> None:
        """Collect individual feedback entry."""
        try:
            required_fields = ['event_id', 'participant_id', 'feedback_text', 'timestamp']
            if all(field in feedback for field in required_fields):
                feedback['timestamp'] = datetime.now().isoformat()
                self.feedback_data.append(feedback)
                logger.info(f"Collected feedback from participant {feedback['participant_id']}")
            else:
                logger.warning("Feedback missing required fields")
        except Exception as e:
            logger.error(f"Error collecting feedback: {str(e)}")
    
    def analyze_sentiment(self, text: str) -> Tuple[float, float]:
        """Perform sentiment analysis on feedback text."""
        try:
            analysis = TextBlob(text)
            return analysis.sentiment.polarity, analysis.sentiment.subjectivity
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {str(e)}")
            return 0.0, 0.0
    
    def generate_insights(self) -> None:
        """Generate actionable insights from feedback data."""
        if not self.feedback_data:
            logger.warning("No feedback data to analyze")
            return
        
        df = pd.DataFrame(self.feedback_data)
        
        # Sentiment analysis
        df[['polarity', 'subjectivity']] = df['feedback_text'].apply(
            lambda x: pd.Series(self.analyze_sentiment(x))
        )
        
        # Categorize sentiment
        df['sentiment'] = df['polarity'].apply(
            lambda x: 'positive' if x > 0.1 else 'negative' if x < -0.1 else 'neutral'
        )
        
        # Group by event and sentiment
        event_sentiment = df.groupby(['event_id', 'sentiment']).size().unstack(fill_value=0)
        
        # Calculate sentiment percentages
        event_sentiment_pct = event_sentiment.div(event_sentiment.sum(axis=1), axis=0) * 100
        
        # Store insights
        self.insights['sentiment_distribution'] = event_sentiment_pct.to_dict()
        
        # Identify common themes (simplified)
        positive_feedback = ' '.join(df[df['sentiment'] == 'positive']['feedback_text'])
        negative_feedback = ' '.join(df[df['sentiment'] == 'negative']['feedback_text'])
        
        self.insights['common_positive_themes'] = self._extract_keywords(positive_feedback)
        self.insights['common_negative_themes'] = self._extract_keywords(negative_feedback)
        
        logger.info("Generated insights from feedback data")
    
    def _extract_keywords(self, text: str, top_n: int = 5) -> List[str]:
        """Extract top keywords from text (simplified version)."""
        try:
            blob = TextBlob(text)
            words = [word.lower() for word in blob.words if len(word) > 3]
            freq = defaultdict(int)
            for word in words:
                freq[word] += 1
            return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
        except Exception as e:
            logger.error(f"Error extracting keywords: {str(e)}")
            return []
    
    def visualize_insights(self, output_dir: str = 'visualizations') -> None:
        """Generate visualizations of insights."""
        os.makedirs(output_dir, exist_ok=True)
        
        if not self.insights:
            logger.warning("No insights to visualize")
            return
        
        try:
            # Sentiment distribution visualization
            sentiment_df = pd.DataFrame(self.insights['sentiment_distribution'])
            ax = sentiment_df.plot(kind='bar', stacked=True, figsize=(10, 6))
            plt.title('Sentiment Distribution by Event')
            plt.ylabel('Percentage')
            plt.xlabel('Event ID')
            plt.legend(title='Sentiment')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'sentiment_distribution.png'))
            plt.close()
            
            # Positive themes word cloud (placeholder)
            if self.insights['common_positive_themes']:
                words, counts = zip(*self.insights['common_positive_themes'])
                plt.figure(figsize=(10, 6))
                sns.barplot(x=list(counts), y=list(words))
                plt.title('Top Positive Feedback Themes')
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, 'positive_themes.png'))
                plt.close()
            
            # Negative themes word cloud (placeholder)
            if self.insights['common_negative_themes']:
                words, counts = zip(*self.insights['common_negative_themes'])
                plt.figure(figsize=(10, 6))
                sns.barplot(x=list(counts), y=list(words))
                plt.title('Top Negative Feedback Themes')
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, 'negative_themes.png'))
                plt.close()
            
            logger.info(f"Visualizations saved to {output_dir}")
        except Exception as e:
            logger.error(f"Error generating visualizations: {str(e)}")
    
    def save_insights(self, file_path: str = 'insights.json') -> None:
        """Save insights to JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.insights, f, indent=2)
            logger.info(f"Insights saved to {file_path}")
        except Exception as e:
            logger.error(f"Error saving insights: {str(e)}")
    
    def run_analysis(self, feedback_files: Optional[List[str]] = None) -> None:
        """Run complete analysis pipeline."""
        try:
            # Load feedback if files provided
            if feedback_files:
                for file in feedback_files:
                    self.load_feedback(file)
            
            # Generate insights
            self.generate_insights()
            
            # Visualize and save results
            self.visualize_insights()
            self.save_insights()
            
            logger.info("Analysis completed successfully")
        except Exception as e:
            logger.error(f"Error in analysis pipeline: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = FeedbackAnalyzer()
    
    # Example feedback data
    example_feedback = [
        {
            "event_id": "event_001",
            "participant_id": "user_123",
            "feedback_text": "The workshop was incredibly helpful and engaging!"
        },
        {
            "event_id": "event_001",
            "participant_id": "user_456",
            "feedback_text": "I didn't like the pace, it was too fast for me."
        },
        {
            "event_id": "event_002",
            "participant_id": "user_789",
            "feedback_text": "Excellent content and knowledgeable instructors."
        }
    ]
    
    # Collect feedback
    for feedback in example_feedback:
        analyzer.collect_feedback(feedback)
    
    # Run analysis
    analyzer.run_analysis()
```
