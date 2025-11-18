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
  "https://www.reddit.com/r/AmItheAsshole/top.json": {
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
import json
import time
from typing import List, Dict, Any

# Constants
BASE_URL = "https://www.reddit.com/r/AmItheAsshole/top.json"
HEADERS = {"User-Agent": "AITA-Bias-Analyzer/1.0"}
MAX_RETRIES = 3
DEFAULT_POST_LIMIT = 100  # Maximum number of posts to fetch per request

def fetch_reddit_data(limit: int = DEFAULT_POST_LIMIT) -> List[Dict[str, Any]]:
    """
    Fetch top posts from Reddit's AITA subreddit.
    
    :param limit: Number of posts to fetch (max 100 per call).
    :return: List of posts with relevant data.
    """
    url = f"{BASE_URL}?limit={limit}"
    retries = 0

    while retries < MAX_RETRIES:
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            return data.get("data", {}).get("children", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            retries += 1
            time.sleep(2)  # Backoff in case of failure
    raise Exception("Failed to fetch data from Reddit after multiple retries.")

def extract_post_data(posts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Extract relevant information from Reddit posts.
    
    :param posts: List of raw post data from Reddit API.
    :return: List of structured post information.
    """
    extracted_data = []
    for post in posts:
        post_info = post.get("data", {})
        extracted_data.append({
            "title": post_info.get("title", ""),
            "score": post_info.get("score", 0),
            "upvote_ratio": post_info.get("upvote_ratio", 0.0),
            "comments": post_info.get("num_comments", 0),
            "id": post_info.get("id", ""),
            "author": post_info.get("author", ""),
        })
    return extracted_data

def analyze_bias(posts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze Reddit AITA data for any biases in post metrics.
    
    :param posts: List of extracted post data.
    :return: Analysis results as a dictionary.
    """
    if not posts:
        return {"error": "No posts to analyze."}

    total_posts = len(posts)
    total_score = sum(post["score"] for post in posts)
    total_comments = sum(post["comments"] for post in posts)

    # Calculate averages
    avg_score = total_score / total_posts
    avg_comments = total_comments / total_posts

    # Identify posts with extreme metrics
    max_score_post = max(posts, key=lambda x: x["score"], default=None)
    max_comments_post = max(posts, key=lambda x: x["comments"], default=None)

    return {
        "total_posts": total_posts,
        "avg_score": avg_score,
        "avg_comments": avg_comments,
        "max_score_post": max_score_post,
        "max_comments_post": max_comments_post,
    }

def main():
    """
    Main function to automate the analysis of Reddit AITA benchmarks.
    """
    try:
        print("Fetching Reddit data...")
        posts = fetch_reddit_data(limit=DEFAULT_POST_LIMIT)
        print(f"Fetched {len(posts)} posts.")

        print("Extracting post data...")
        extracted_posts = extract_post_data(posts)
        print(f"Extracted data from {len(extracted_posts)} posts.")

        print("Performing bias analysis...")
        analysis_results = analyze_bias(extracted_posts)

        # Display analysis results
        print(json.dumps(analysis_results, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
