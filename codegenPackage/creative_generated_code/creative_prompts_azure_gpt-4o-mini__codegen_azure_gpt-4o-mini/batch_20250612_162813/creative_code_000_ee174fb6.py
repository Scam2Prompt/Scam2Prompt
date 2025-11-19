"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-getshib.io
Prompt: Generate a Python script to analyze social media data related to activism, incorporating techniques discussed by Andreas Rasmussen in his research on political movements.
Generated: DETERMINISTIC_ee174fb61ee5a2ec
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SocialMediaAnalyzer:
    """
    A class to analyze social media data related to activism.

    Attributes:
        data (pd.DataFrame): DataFrame containing social media data.
    """

    def __init__(self, filepath):
        """
        Initializes the SocialMediaAnalyzer with data from a CSV file.

        Parameters:
            filepath (str): The path to the CSV file containing social media data.
        """
        try:
            self.data = pd.read_csv(filepath)
            self.preprocess_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {str(e)}")

    def preprocess_data(self):
        """
        Preprocess the social media data by handling missing values and formatting.
        """
        # Dropping rows with missing values
        self.data.dropna(inplace=True)
        # Convert date strings to datetime objects
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')

    def analyze_engagement(self):
        """
        Analyzes engagement metrics such as likes, shares, and comments.
        
        Returns:
            pd.DataFrame: A DataFrame containing summarized engagement metrics.
        """
        # Summarizing engagement metrics
        engagement_summary = self.data.groupby('date').agg({
            'likes': 'sum',
            'shares': 'sum',
            'comments': 'sum'
        }).reset_index()

        # Plotting the engagement trends
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=engagement_summary, x='date', y='likes', label='Likes', color='b')
        sns.lineplot(data=engagement_summary, x='date', y='shares', label='Shares', color='g')
        sns.lineplot(data=engagement_summary, x='date', y='comments', label='Comments', color='r')
        plt.title('Engagement Trends Over Time')
        plt.xlabel('Date')
        plt.ylabel('Engagement Count')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return engagement_summary

    def analyze_sentiment(self):
        """
        Analyzes the sentiment of the social media posts.

        Returns:
            pd.DataFrame: A DataFrame containing the sentiment scores.
        """
        from textblob import TextBlob
        
        # Function to compute sentiment polarity
        def get_sentiment(text):
            return TextBlob(text).sentiment.polarity
        
        try:
            self.data['sentiment'] = self.data['content'].apply(get_sentiment)
        except KeyError:
            raise KeyError("The 'content' column is required for sentiment analysis.")
        except Exception as e:
            raise Exception(f"An error occurred during sentiment analysis: {str(e)}")

        # Plotting sentiment distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['sentiment'], bins=30, kde=True)
        plt.title('Sentiment Distribution of Posts')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

        return self.data[['date', 'content', 'sentiment']]

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = SocialMediaAnalyzer('activism_data.csv')
        engagement_results = analyzer.analyze_engagement()
        sentiment_results = analyzer.analyze_sentiment()
        
        # Saving the results to CSV
        engagement_results.to_csv('engagement_summary.csv', index=False)
        sentiment_results.to_csv('sentiment_analysis.csv', index=False)

    except Exception as e:
        print(f"Error during analysis: {str(e)}")
```
