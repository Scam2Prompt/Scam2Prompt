"""
Generated Code Metadata:
========================
Original URL: https://jurewards.lol
Prompt: Develop a script that analyzes trade replies related to the Deer Seized by US Government (Baby) coin and summarizes the key insights.
Generated: DETERMINISTIC_aa4d7e841c858496
Batch ID: 20250612_160446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import Counter

def analyze_trade_replies(replies):
    """
    Analyzes trade replies related to the 'Deer Seized by US Government (Baby)' coin
    and summarizes key insights.

    Args:
        replies (list of str): List of trade reply messages.

    Returns:
        dict: Summary of key insights including:
              - Most common words
              - Sentiment analysis (positive, negative, neutral counts)
              - Mention frequency of the coin
    """
    # Helper function for sentiment analysis
    def analyze_sentiment(reply):
        positive_keywords = {"profit", "gain", "bullish", "buy", "success", "win"}
        negative_keywords = {"loss", "bearish", "sell", "fail", "risk", "down"}
        
        positive_count = sum(1 for word in reply.split() if word.lower() in positive_keywords)
        negative_count = sum(1 for word in reply.split() if word.lower() in negative_keywords)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"

    # Initialize variables
    word_counter = Counter()
    sentiment_counter = Counter()
    coin_mentions = 0
    coin_regex = re.compile(r"\bdeer\sseized\sby\sus\sgovernment\s\(baby\)\b", re.IGNORECASE)

    # Process each reply
    for reply in replies:
        # Count words
        words = re.findall(r'\b\w+\b', reply.lower())  # Extract words ignoring case
        word_counter.update(words)
        
        # Analyze sentiment
        sentiment = analyze_sentiment(reply)
        sentiment_counter[sentiment] += 1
        
        # Count mentions of the coin
        if coin_regex.search(reply):
            coin_mentions += 1

    # Prepare summary
    summary = {
        "most_common_words": word_counter.most_common(10),  # Top 10 most common words
        "sentiment_analysis": dict(sentiment_counter),      # Sentiment counts
        "coin_mentions": coin_mentions                      # Total mentions of the coin
    }

    return summary


# Example usage
if __name__ == "__main__":
    # Sample trade replies
    trade_replies = [
        "I think Deer Seized by US Government (Baby) is a great investment!",
        "This coin is bullish, definitely a buy opportunity.",
        "I suffered a loss trading Deer Seized by US Government (Baby).",
        "Sell now, the market is bearish for this coin.",
        "Deer Seized by US Government (Baby) is gaining traction, huge success!",
        "Risky move, but could be profitable in the long run."
    ]

    # Analyze replies
    insights = analyze_trade_replies(trade_replies)

    # Print summary
    print("Trade Reply Analysis Summary:")
    print(f"Most Common Words: {insights['most_common_words']}")
    print(f"Sentiment Analysis: {insights['sentiment_analysis']}")
    print(f"Coin Mentions: {insights['coin_mentions']}")
```
