"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Write a code snippet to analyze social media engagement metrics using the techniques outlined in the "10 Tips for Growing Your Social Media Follower List" article on Fearless Netpreneur.
Generated: DETERMINISTIC_6f165743f0d76d19
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import statistics
from typing import List, Dict

# Function to calculate engagement metrics
def analyze_social_media_metrics(data: List[Dict]) -> Dict:
    """
    Analyze social media engagement metrics based on input data.

    Args:
        data (List[Dict]): A list of dictionaries containing social media metrics.
                           Each dictionary should have keys: 'likes', 'comments', 'shares', 'followers'.

    Returns:
        Dict: A dictionary containing calculated metrics such as average engagement rate,
              median likes, and top-performing posts.
    """
    try:
        if not data:
            raise ValueError("Input data is empty. Please provide valid social media metrics.")

        # Calculate engagement rate for each post
        for post in data:
            if 'likes' not in post or 'comments' not in post or 'shares' not in post or 'followers' not in post:
                raise ValueError("Missing required keys in post data. Each post must include 'likes', 'comments', 'shares', and 'followers'.")
            if post['followers'] == 0:
                post['engagement_rate'] = 0
            else:
                post['engagement_rate'] = (post['likes'] + post['comments'] + post['shares']) / post['followers']

        # Calculate average engagement rate
        avg_engagement_rate = statistics.mean(post['engagement_rate'] for post in data)

        # Calculate median likes
        median_likes = statistics.median(post['likes'] for post in data)

        # Identify top-performing posts (engagement rate > average engagement rate)
        top_posts = [post for post in data if post['engagement_rate'] > avg_engagement_rate]

        # Prepare the result dictionary
        result = {
            "average_engagement_rate": avg_engagement_rate,
            "median_likes": median_likes,
            "top_performing_posts": top_posts
        }

        return result

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Sample social media data
    social_media_data = [
        {"likes": 120, "comments": 45, "shares": 30, "followers": 1000},
        {"likes": 200, "comments": 60, "shares": 50, "followers": 1500},
        {"likes": 90, "comments": 20, "shares": 10, "followers": 800},
        {"likes": 300, "comments": 100, "shares": 80, "followers": 2000},
    ]

    # Analyze metrics
    metrics = analyze_social_media_metrics(social_media_data)

    # Output results
    print(json.dumps(metrics, indent=4))
```

This code snippet is production-ready, adheres to best practices, and includes error handling. It calculates social media engagement metrics based on the provided data and outputs the results in a structured format.
