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
import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestorSentimentAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the InvestorSentimentAnalyzer with a data file.

        :param data_file: Path to the CSV file containing investment data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads investment data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error("The specified file was not found.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The file is empty.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def analyze_sentiment(self):
        """
        Analyzes the sentiment of the investment-related text data.
        Adds a 'sentiment' column to the DataFrame.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data first.")
            return

        try:
            self.data['sentiment'] = self.data['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
            logging.info("Sentiment analysis completed.")
        except KeyError:
            logging.error("The 'text' column is missing from the data.")
            raise
        except Exception as e:
            logging.error(f"An error occurred during sentiment analysis: {e}")
            raise

    def visualize_sentiment(self):
        """
        Visualizes the sentiment analysis results using a histogram.
        """
        if self.data is None or 'sentiment' not in self.data.columns:
            logging.error("Sentiment data not available for visualization.")
            return

        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['sentiment'], bins=30, kde=True)
        plt.title('Sentiment Analysis of Investor Text Data')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.axvline(0, color='red', linestyle='--', label='Neutral')
        plt.legend()
        plt.show()
        logging.info("Sentiment visualization displayed.")

    def summarize_investment_decisions(self):
        """
        Summarizes the investment decisions based on sentiment scores.
        """
        if self.data is None or 'sentiment' not in self.data.columns:
            logging.error("Sentiment data not available for summarization.")
            return

        summary = {
            'positive': self.data[self.data['sentiment'] > 0].shape[0],
            'neutral': self.data[self.data['sentiment'] == 0].shape[0],
            'negative': self.data[self.data['sentiment'] < 0].shape[0],
        }
        logging.info(f"Investment decision summary: {summary}")
        return summary

if __name__ == "__main__":
    # Example usage
    analyzer = InvestorSentimentAnalyzer('investment_data.csv')
    analyzer.load_data()
    analyzer.analyze_sentiment()
    analyzer.visualize_sentiment()
    summary = analyzer.summarize_investment_decisions()
    print(summary)
```

Make sure to have the required libraries installed before running the code:
```bash
pip install pandas numpy textblob matplotlib seaborn
```
