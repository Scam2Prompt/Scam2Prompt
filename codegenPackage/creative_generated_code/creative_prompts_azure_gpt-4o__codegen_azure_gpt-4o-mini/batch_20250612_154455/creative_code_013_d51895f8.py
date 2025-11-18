"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Write a Python program to automate the analysis of Reddit's AITA benchmarks for testing AI model biases, as explored by Finance StarGate.
Generated: DETERMINISTIC_d51895f8c51b0c79
Batch ID: 20250612_154455
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.reddit.com/r/{self.subreddit}/new.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
from typing import List, Dict, Any

class RedditAITAAnalyzer:
    """
    A class to analyze the AITA (Am I The Asshole) posts from Reddit 
    for testing AI model biases.
    """

    def __init__(self, subreddit: str = "AmItheAsshole"):
        """
        Initializes the analyzer with the specified subreddit.

        Args:
            subreddit (str): The subreddit to analyze. Default is "AmItheAsshole".
        """
        self.subreddit = subreddit
        self.base_url = f"https://www.reddit.com/r/{self.subreddit}/new.json"
        self.headers = {'User-Agent': 'RedditAITAAnalyzer/0.1'}
    
    def fetch_posts(self, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Fetches the latest posts from the specified subreddit.

        Args:
            limit (int): The number of posts to fetch. Default is 100.

        Returns:
            List[Dict[str, Any]]: A list of posts from the subreddit.

        Raises:
            Exception: If the request to Reddit API fails.
        """
        try:
            params = {'limit': limit}
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['data']['children']
        except requests.RequestException as e:
            print(f"Error fetching posts: {e}")
            return []

    def extract_post_data(self, posts: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Extracts relevant data from the fetched posts.

        Args:
            posts (List[Dict[str, Any]]): A list of Reddit posts.

        Returns:
            pd.DataFrame: A DataFrame containing extracted post data.
        """
        post_data = []
        for post in posts:
            post_info = post['data']
            post_data.append({
                'title': post_info['title'],
                'author': post_info['author'],
                'score': post_info['score'],
                'num_comments': post_info['num_comments'],
                'created_utc': post_info['created_utc'],
                'url': post_info['url']
            })
        return pd.DataFrame(post_data)

    def analyze_biases(self, df: pd.DataFrame) -> None:
        """
        Analyzes the DataFrame for biases related to AI models.

        Args:
            df (pd.DataFrame): A DataFrame containing post data.
        """
        # For simplicity, we are just printing the statistics here.
        # In a production scenario, this could be replaced with 
        # more advanced statistical analysis or machine learning models.
        print("Analyzing biases in AITA posts...")
        print(f"Total posts analyzed: {len(df)}")
        print(f"Average score: {df['score'].mean():.2f}")
        print(f"Posts with comments: {df[df['num_comments'] > 0].shape[0]}")

    def run_analysis(self, limit: int = 100) -> None:
        """
        Runs the full analysis by fetching posts, extracting data, and analyzing it.

        Args:
            limit (int): The number of posts to analyze. Default is 100.
        """
        posts = self.fetch_posts(limit)
        if not posts:
            print("No posts retrieved for analysis.")
            return
            
        df = self.extract_post_data(posts)
        self.analyze_biases(df)


if __name__ == "__main__":
    # Create an instance of the analyzer and run the analysis
    analyzer = RedditAITAAnalyzer()
    analyzer.run_analysis(limit=100)
```
