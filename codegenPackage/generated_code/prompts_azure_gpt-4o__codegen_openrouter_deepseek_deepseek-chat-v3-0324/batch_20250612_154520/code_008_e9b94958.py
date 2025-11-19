"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Develop a Python program to analyze participant feedback for Anatolian folk dance courses, focusing on metrics like enjoyment and physical improvement, inspired by danceanatolia.com.
Generated: DETERMINISTIC_e9b94958bb14ba6d
Batch ID: 20250612_154520
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
import matplotlib.pyplot as plt
from textblob import TextBlob
import seaborn as sns
from typing import List, Dict, Tuple, Optional

class FeedbackAnalyzer:
    """
    A class to analyze participant feedback for Anatolian folk dance courses.
    Focuses on metrics like enjoyment and physical improvement.
    """
    
    def __init__(self, feedback_data: pd.DataFrame):
        """
        Initialize the analyzer with feedback data.
        
        Args:
            feedback_data (pd.DataFrame): DataFrame containing feedback data with columns:
                - 'participant_id': Unique identifier for each participant
                - 'feedback_text': Textual feedback from participants
                - 'enjoyment_rating': Numeric rating (1-5) for enjoyment
                - 'physical_improvement_rating': Numeric rating (1-5) for physical improvement
                - 'course_name': Name of the dance course
        """
        self.data = feedback_data.copy()
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate the input data structure and content."""
        required_columns = {
            'participant_id', 
            'feedback_text', 
            'enjoyment_rating', 
            'physical_improvement_rating',
            'course_name'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values")
            
        if not all(self.data['enjoyment_rating'].between(1, 5)):
            raise ValueError("Enjoyment ratings must be between 1 and 5")
            
        if not all(self.data['physical_improvement_rating'].between(1, 5)):
            raise ValueError("Physical improvement ratings must be between 1 and 5")
    
    def calculate_sentiment_scores(self) -> pd.DataFrame:
        """
        Calculate sentiment polarity scores for feedback text.
        
        Returns:
            pd.DataFrame: Original DataFrame with added 'sentiment_score' column
        """
        self.data['sentiment_score'] = self.data['feedback_text'].apply(
            lambda text: TextBlob(str(text)).sentiment.polarity
        )
        return self.data
    
    def get_average_ratings(self) -> pd.DataFrame:
        """
        Calculate average ratings by course.
        
        Returns:
            pd.DataFrame: Average ratings grouped by course_name
        """
        return self.data.groupby('course_name').agg({
            'enjoyment_rating': 'mean',
            'physical_improvement_rating': 'mean',
            'sentiment_score': 'mean'
        }).round(2)
    
    def plot_rating_distributions(self) -> plt.Figure:
        """
        Create distribution plots for enjoyment and physical improvement ratings.
        
        Returns:
            plt.Figure: Matplotlib figure object
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        sns.histplot(
            data=self.data, 
            x='enjoyment_rating', 
            bins=5, 
            kde=True, 
            ax=ax1
        )
        ax1.set_title('Enjoyment Rating Distribution')
        ax1.set_xlabel('Rating (1-5)')
        
        sns.histplot(
            data=self.data, 
            x='physical_improvement_rating', 
            bins=5, 
            kde=True, 
            ax=ax2
        )
        ax2.set_title('Physical Improvement Rating Distribution')
        ax2.set_xlabel('Rating (1-5)')
        
        plt.tight_layout()
        return fig
    
    def plot_sentiment_vs_ratings(self) -> plt.Figure:
        """
        Create scatter plots of sentiment vs ratings.
        
        Returns:
            plt.Figure: Matplotlib figure object
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        sns.scatterplot(
            data=self.data,
            x='sentiment_score',
            y='enjoyment_rating',
            hue='course_name',
            ax=ax1
        )
        ax1.set_title('Sentiment vs Enjoyment Rating')
        ax1.set_xlabel('Sentiment Score')
        ax1.set_ylabel('Enjoyment Rating')
        
        sns.scatterplot(
            data=self.data,
            x='sentiment_score',
            y='physical_improvement_rating',
            hue='course_name',
            ax=ax2
        )
        ax2.set_title('Sentiment vs Physical Improvement Rating')
        ax2.set_xlabel('Sentiment Score')
        ax2.set_ylabel('Physical Improvement Rating')
        
        plt.tight_layout()
        return fig
    
    def generate_report(self) -> Dict[str, Dict[str, float]]:
        """
        Generate a comprehensive report of feedback analysis.
        
        Returns:
            Dict: Dictionary containing analysis results
        """
        self.calculate_sentiment_scores()
        avg_ratings = self.get_average_ratings()
        
        report = {
            'overall': {
                'average_enjoyment': self.data['enjoyment_rating'].mean(),
                'average_physical_improvement': self.data['physical_improvement_rating'].mean(),
                'average_sentiment': self.data['sentiment_score'].mean()
            },
            'by_course': avg_ratings.to_dict('index')
        }
        
        return report


def load_sample_data() -> pd.DataFrame:
    """Generate sample data for demonstration purposes."""
    data = {
        'participant_id': range(1, 101),
        'feedback_text': [
            "I loved the course! Improved my dancing skills significantly." if i % 3 == 0 else
            "It was okay, but could be better organized." if i % 3 == 1 else
            "Not what I expected, but still learned some moves." 
            for i in range(100)
        ],
        'enjoyment_rating': np.random.randint(1, 6, size=100),
        'physical_improvement_rating': np.random.randint(1, 6, size=100),
        'course_name': ['Course A'] * 50 + ['Course B'] * 50
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    # Example usage
    try:
        # Load sample data (replace with actual data loading in production)
        feedback_data = load_sample_data()
        
        # Initialize analyzer
        analyzer = FeedbackAnalyzer(feedback_data)
        
        # Calculate sentiment scores
        analyzer.calculate_sentiment_scores()
        
        # Generate and print report
        report = analyzer.generate_report()
        print("Feedback Analysis Report:")
        print("=" * 50)
        print(f"Overall Average Enjoyment: {report['overall']['average_enjoyment']:.2f}")
        print(f"Overall Average Physical Improvement: {report['overall']['average_physical_improvement']:.2f}")
        print(f"Overall Average Sentiment: {report['overall']['average_sentiment']:.2f}")
        print("\nBy Course:")
        for course, metrics in report['by_course'].items():
            print(f"\n{course}:")
            print(f"  Enjoyment: {metrics['enjoyment_rating']:.2f}")
            print(f"  Physical Improvement: {metrics['physical_improvement_rating']:.2f}")
            print(f"  Sentiment: {metrics['sentiment_score']:.2f}")
        
        # Generate plots
        dist_fig = analyzer.plot_rating_distributions()
        sentiment_fig = analyzer.plot_sentiment_vs_ratings()
        
        # Save plots (in production, you might display them or save to files)
        dist_fig.savefig('rating_distributions.png')
        sentiment_fig.savefig('sentiment_vs_ratings.png')
        
    except Exception as e:
        print(f"Error occurred during analysis: {str(e)}")
```
