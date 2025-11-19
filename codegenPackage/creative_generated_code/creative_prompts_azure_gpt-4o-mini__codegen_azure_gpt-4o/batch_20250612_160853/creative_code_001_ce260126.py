"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lostsecretdivinity.com
Prompt: Write a code snippet that demonstrates how to analyze the role of social media in shaping experiences, inspired by concepts from "The Lost Secret of Divinity."
Generated: DETERMINISTIC_ce2601268c69a780
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter

def analyze_social_media_posts(posts):
    """
    Analyzes the impact of social media posts in shaping experiences.

    Args:
        posts (list of str): A list of social media posts (strings).

    Returns:
        dict: A dictionary containing the analysis results:
              - word_frequency: Frequency of words in posts.
              - positive_posts: Count of posts with positive sentiment.
              - negative_posts: Count of posts with negative sentiment.
              - neutral_posts: Count of posts with neutral sentiment.
    """
    # Define simple lexicons for sentiment analysis
    positive_words = {"love", "happy", "great", "excellent", "divine", "joy", "wonderful"}
    negative_words = {"hate", "sad", "terrible", "awful", "pain", "bad", "regret"}

    word_frequency = Counter()
    positive_posts = 0
    negative_posts = 0
    neutral_posts = 0

    # Analyze each post
    for post in posts:
        try:
            # Tokenize the post into words
            words = re.findall(r'\b\w+\b', post.lower())
            word_frequency.update(words)

            # Sentiment analysis based on lexicons
            positive_count = sum(1 for word in words if word in positive_words)
            negative_count = sum(1 for word in words if word in negative_words)

            if positive_count > negative_count:
                positive_posts += 1
            elif negative_count > positive_count:
                negative_posts += 1
            else:
                neutral_posts += 1
        except Exception as e:
            # Log the error and skip processing the problematic post
            print(f"Error processing post: {post}. Error: {e}")

    # Return analysis results
    return {
        "word_frequency": word_frequency,
        "positive_posts": positive_posts,
        "negative_posts": negative_posts,
        "neutral_posts": neutral_posts,
    }

# Example usage:
if __name__ == "__main__":
    # Sample social media posts
    social_media_posts = [
        "I love this divine experience, it's truly wonderful!",
        "This is awful, I hate how things are turning out.",
        "I feel neutral about the situation.",
        "Great work on the project! Happy to see progress.",
        "Sad times ahead, I regret everything."
    ]

    # Analyze the posts
    analysis_results = analyze_social_media_posts(social_media_posts)

    # Print the results
    print("Analysis Results:")
    print(f"Word Frequency: {analysis_results['word_frequency']}")
    print(f"Positive Posts: {analysis_results['positive_posts']}")
    print(f"Negative Posts: {analysis_results['negative_posts']}")
    print(f"Neutral Posts: {analysis_results['neutral_posts']}")
```
