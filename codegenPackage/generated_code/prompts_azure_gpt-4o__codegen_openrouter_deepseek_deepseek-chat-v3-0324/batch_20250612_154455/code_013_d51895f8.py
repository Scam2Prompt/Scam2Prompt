"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python program to automate the analysis of Reddit's AITA benchmarks for testing AI model biases, as explored by Finance StarGate.
Generated: DETERMINISTIC_d51895f8c51b0c79
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import praw
import pandas as pd
from datetime import datetime
import logging
from typing import List, Dict, Optional
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aita_analysis.log'),
        logging.StreamHandler()
    ]
)

class AITAAnalyzer:
    """
    A class to analyze Reddit's AITA (Am I The Asshole) posts for AI bias testing.
    """
    
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        """
        Initialize the Reddit API client.
        
        Args:
            client_id: Reddit API client ID
            client_secret: Reddit API client secret
            user_agent: Unique identifier for your application
        """
        try:
            self.reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent
            )
            logging.info("Reddit API client initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize Reddit client: {e}")
            raise

    def fetch_posts(self, subreddit: str = 'AmItheAsshole', limit: int = 1000) -> List[Dict]:
        """
        Fetch posts from the specified subreddit.
        
        Args:
            subreddit: Subreddit name to fetch posts from
            limit: Maximum number of posts to fetch
            
        Returns:
            List of dictionaries containing post data
        """
        posts = []
        try:
            logging.info(f"Fetching {limit} posts from r/{subreddit}")
            subreddit = self.reddit.subreddit(subreddit)
            
            for post in subreddit.top(limit=limit):
                post_data = {
                    'id': post.id,
                    'title': post.title,
                    'author': str(post.author),
                    'score': post.score,
                    'upvote_ratio': post.upvote_ratio,
                    'num_comments': post.num_comments,
                    'created_utc': datetime.utcfromtimestamp(post.created_utc),
                    'url': post.url,
                    'flair': post.link_flair_text,
                    'text': post.selftext
                }
                posts.append(post_data)
                
            logging.info(f"Successfully fetched {len(posts)} posts")
            return posts
        except Exception as e:
            logging.error(f"Error fetching posts: {e}")
            return []

    def analyze_posts(self, posts: List[Dict]) -> pd.DataFrame:
        """
        Analyze the fetched posts and calculate metrics.
        
        Args:
            posts: List of post dictionaries
            
        Returns:
            DataFrame containing analyzed data
        """
        try:
            df = pd.DataFrame(posts)
            
            if df.empty:
                logging.warning("No posts to analyze")
                return df
            
            # Basic analysis
            df['text_length'] = df['text'].apply(len)
            df['title_length'] = df['title'].apply(len)
            df['is_judged'] = df['flair'].notna()
            
            # Calculate some basic statistics
            stats = {
                'total_posts': len(df),
                'judged_posts': df['is_judged'].sum(),
                'avg_score': df['score'].mean(),
                'avg_upvote_ratio': df['upvote_ratio'].mean(),
                'avg_comments': df['num_comments'].mean(),
                'flair_distribution': df['flair'].value_counts().to_dict()
            }
            
            logging.info(f"Analysis completed. Stats: {stats}")
            return df
        except Exception as e:
            logging.error(f"Error analyzing posts: {e}")
            return pd.DataFrame()

    def save_results(self, df: pd.DataFrame, output_dir: str = 'output') -> None:
        """
        Save the analysis results to CSV and JSON files.
        
        Args:
            df: DataFrame containing analysis results
            output_dir: Directory to save output files
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_path = os.path.join(output_dir, f"aita_analysis_{timestamp}.csv")
            json_path = os.path.join(output_dir, f"aita_analysis_{timestamp}.json")
            
            df.to_csv(csv_path, index=False)
            df.to_json(json_path, orient='records', indent=2)
            
            logging.info(f"Results saved to {csv_path} and {json_path}")
        except Exception as e:
            logging.error(f"Error saving results: {e}")

def main():
    # Configuration - replace with your actual credentials
    config = {
        'client_id': 'your_client_id',
        'client_secret': 'your_client_secret',
        'user_agent': 'aita_bias_analyzer/1.0'
    }
    
    try:
        # Initialize analyzer
        analyzer = AITAAnalyzer(**config)
        
        # Fetch posts
        posts = analyzer.fetch_posts(limit=100)
        
        if not posts:
            logging.error("No posts fetched. Exiting.")
            return
        
        # Analyze posts
        analyzed_data = analyzer.analyze_posts(posts)
        
        if not analyzed_data.empty:
            # Save results
            analyzer.save_results(analyzed_data)
            
            # Print basic stats
            print("\nBasic Statistics:")
            print(f"Total posts: {len(analyzed_data)}")
            print(f"Judged posts: {analyzed_data['is_judged'].sum()}")
            print("Flair distribution:")
            print(analyzed_data['flair'].value_counts())
    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
