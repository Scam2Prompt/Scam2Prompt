"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Write a Python script to analyze social media engagement metrics for a marketing campaign, referencing strategies discussed in the "Mengenal Sosial Media Marketing" article on Azuharu.net.
Generated: DETERMINISTIC_7a88abfa51ea443c
Batch ID: 20250612_151947
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

class SocialMediaEngagementAnalyzer:
    """
    A class to analyze social media engagement metrics for marketing campaigns.
    """
    
    def __init__(self, data_file):
        """
        Initializes the analyzer with the given data file.

        Parameters:
        data_file (str): The path to the CSV file containing engagement metrics.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the engagement metrics data from a CSV file into a DataFrame.
        
        Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise

    def analyze_engagement(self):
        """
        Analyzes engagement metrics by calculating summary statistics.
        
        Returns:
        dict: A dictionary containing average likes, shares, and comments.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data before analysis.")
        
        # Calculate average metrics
        avg_likes = self.data['likes'].mean()
        avg_shares = self.data['shares'].mean()
        avg_comments = self.data['comments'].mean()
        
        return {
            'Average Likes': avg_likes,
            'Average Shares': avg_shares,
            'Average Comments': avg_comments
        }

    def plot_engagement(self):
        """
        Plots the engagement metrics over time.

        Raises:
        ValueError: If data is not loaded or expected columns are missing.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data before plotting.")
        
        if not all(col in self.data.columns for col in ['date', 'likes', 'shares', 'comments']):
            raise ValueError("Data must contain 'date', 'likes', 'shares', and 'comments' columns.")
        
        # Convert date column to datetime
        self.data['date'] = pd.to_datetime(self.data['date'])
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['date'], self.data['likes'], label='Likes', marker='o')
        plt.plot(self.data['date'], self.data['shares'], label='Shares', marker='o')
        plt.plot(self.data['date'], self.data['comments'], label='Comments', marker='o')
        
        plt.title('Social Media Engagement Metrics Over Time')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the social media engagement analysis.
    """
    # Path to the CSV file containing engagement metrics
    data_file_path = 'engagement_metrics.csv'
    
    analyzer = SocialMediaEngagementAnalyzer(data_file_path)
    
    try:
        analyzer.load_data()
        engagement_summary = analyzer.analyze_engagement()
        print("Engagement Summary:", engagement_summary)
        analyzer.plot_engagement()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
