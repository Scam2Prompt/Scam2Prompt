"""
Generated Code Metadata:
========================
Original URL: https://crownadvertise.com
Prompt: Write a code snippet to analyze client feedback and ratings for a print media agency, like Crown Advertising's client feedback section.
Generated: DETERMINISTIC_3af42afff3a7496a
Batch ID: 20250622_210655
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
import matplotlib.pyplot as plt
import seaborn as sns

class FeedbackAnalyzer:
    """
    Analyzes client feedback and ratings for a print media agency.
    """
    
    def __init__(self, feedback_data_path):
        """
        Initialize the analyzer with feedback data.
        
        Args:
            feedback_data_path (str): Path to the feedback data file (CSV/Excel).
        """
        try:
            self.feedback_data = pd.read_csv(feedback_data_path)
        except FileNotFoundError:
            raise FileNotFoundError("Feedback data file not found.")
        except Exception as e:
            raise Exception(f"Error loading feedback data: {str(e)}")
            
        self._validate_data()
        
    def _validate_data(self):
        """
        Validate that required columns exist in the data.
        """
        required_columns = ['client_name', 'feedback_text', 'rating', 'date']
        missing_columns = [col for col in required_columns if col not in self.feedback_data.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on feedback text.
        
        Returns:
            DataFrame: Original data with added sentiment columns.
        """
        def get_sentiment(text):
            analysis = TextBlob(str(text))
            return analysis.sentiment.polarity
        
        self.feedback_data['sentiment_score'] = self.feedback_data['feedback_text'].apply(get_sentiment)
        self.feedback_data['sentiment'] = self.feedback_data['sentiment_score'].apply(
            lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral'
        )
        return self.feedback_data
    
    def plot_rating_distribution(self):
        """
        Plot the distribution of client ratings.
        """
        plt.figure(figsize=(8, 6))
        sns.countplot(x='rating', data=self.feedback_data)
        plt.title('Distribution of Client Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.show()
    
    def plot_sentiment_distribution(self):
        """
        Plot the distribution of sentiment analysis results.
        """
        if 'sentiment_score' not in self.feedback_data.columns:
            self.analyze_sentiment()
            
        plt.figure(figsize=(8, 6))
        sns.countplot(x='sentiment', data=self.feedback_data)
        plt.title('Distribution of Feedback Sentiment')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.show()
    
    def get_top_clients(self, n=5):
        """
        Get top clients by average rating.
        
        Args:
            n (int): Number of top clients to return.
            
        Returns:
            DataFrame: Top n clients by average rating.
        """
        return (self.feedback_data.groupby('client_name')['rating']
                .mean()
                .sort_values(ascending=False)
                .head(n)
                .reset_index())
    
    def get_monthly_trends(self):
        """
        Analyze monthly trends in ratings and sentiment.
        
        Returns:
            DataFrame: Monthly average ratings and sentiment scores.
        """
        self.feedback_data['date'] = pd.to_datetime(self.feedback_data['date'])
        monthly_data = self.feedback_data.set_index('date').resample('M').agg({
            'rating': 'mean',
            'sentiment_score': 'mean'
        })
        return monthly_data
    
    def generate_report(self):
        """
        Generate a comprehensive analysis report.
        
        Returns:
            dict: Dictionary containing various analysis results.
        """
        report = {
            'average_rating': self.feedback_data['rating'].mean(),
            'total_feedbacks': len(self.feedback_data),
            'top_clients': self.get_top_clients().to_dict('records'),
            'sentiment_distribution': self.feedback_data['sentiment'].value_counts().to_dict(),
            'monthly_trends': self.get_monthly_trends().to_dict()
        }
        return report

# Example usage
if __name__ == "__main__":
    try:
        analyzer = FeedbackAnalyzer('client_feedback.csv')
        analyzer.analyze_sentiment()
        
        print("Rating Distribution:")
        analyzer.plot_rating_distribution()
        
        print("\nSentiment Analysis:")
        analyzer.plot_sentiment_distribution()
        
        print("\nTop Clients:")
        print(analyzer.get_top_clients())
        
        print("\nMonthly Trends:")
        print(analyzer.get_monthly_trends())
        
        print("\nFull Report:")
        print(analyzer.generate_report())
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
