"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurewards.lol
Prompt: Develop a script that analyzes trade replies related to the Deer Seized by US Government (Baby) coin and summarizes the key insights.
Generated: DETERMINISTIC_aa4d7e841c858496
Batch ID: 20250612_160446
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

def analyze_trade_replies(replies):
    """
    Analyzes trade replies related to the Deer Seized by US Government (Baby) coin
    and summarizes key insights.

    Args:
        replies (list of str): A list of trade reply strings.

    Returns:
        dict: A summary containing:
              - 'top_mentions': Most frequently mentioned words (excluding stopwords).
              - 'sentiment_analysis': Distribution of positive, negative, and neutral replies.
              - 'total_replies': Total number of replies analyzed.
    """
    # Define a basic list of stopwords
    stopwords = {"the", "is", "by", "and", "a", "an", "to", "of", "on", "in", "for", "with", "baby", 
                 "us", "coin", "government", "deer", "seized"}
    
    # Sentiment keywords
    positive_keywords = {"great", "profit", "bullish", "good", "buy"}
    negative_keywords = {"loss", "bearish", "bad", "sell"}
    
    # Initialize counters
    word_counter = Counter()
    sentiment_counter = {"positive": 0, "negative": 0, "neutral": 0}
    
    # Process each reply
    for reply in replies:
        # Normalize text to lowercase and remove non-alphanumeric characters
        cleaned_reply = re.sub(r"[^\w\s]", "", reply.lower())
        words = cleaned_reply.split()
        
        # Count words excluding stopwords
        for word in words:
            if word not in stopwords:
                word_counter[word] += 1
        
        # Sentiment analysis
        positive_count = sum(word in positive_keywords for word in words)
        negative_count = sum(word in negative_keywords for word in words)
        
        if positive_count > negative_count:
            sentiment_counter["positive"] += 1
        elif negative_count > positive_count:
            sentiment_counter["negative"] += 1
        else:
            sentiment_counter["neutral"] += 1
    
    # Prepare summary
    summary = {
        "top_mentions": word_counter.most_common(5),  # Top 5 mentioned words
        "sentiment_analysis": sentiment_counter,
        "total_replies": len(replies)
    }
    
    return summary


# Example usage
if __name__ == "__main__":
    # Sample trade replies
    trade_replies = [
        "Wow, the Baby coin is such a great investment!",
        "I can't believe the bearish trend today. Sell now!",
        "Good profits on Baby coin. Bullish signs ahead!",
        "This is a bad move by the government...",
        "Neutral thoughts about today's market. No significant changes."
    ]
    
    try:
        # Analyze trade replies
        insights = analyze_trade_replies(trade_replies)
        
        # Output results
        print("Trade Replies Analysis:")
        print(f"Top Mentions: {insights['top_mentions']}")
        print(f"Sentiment Analysis: {insights['sentiment_analysis']}")
        print(f"Total Replies: {insights['total_replies']}")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
