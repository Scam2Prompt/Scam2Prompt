"""
Generated Code Metadata:
========================
Original URL: https://kristoslounge.com
Prompt: Create a sample social media post using Python's Natural Language Processing (NLP) libraries to promote Kristos Lounge's upcoming events.
Generated: DETERMINISTIC_423567207bdf1453
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure that the necessary NLTK resources are downloaded
nltk.download('vader_lexicon')

def generate_event_post(event_name, event_date, event_time, event_details):
    """
    Generate a promotional social media post for an event.

    Parameters:
    event_name (str): The name of the event.
    event_date (str): The date of the event.
    event_time (str): The time of the event.
    event_details (str): Additional details about the event.

    Returns:
    str: A formatted promotional post.
    """
    # Create a list of engaging phrases
    engaging_phrases = [
        "Join us for an unforgettable experience!",
        "Don't miss out on this amazing event!",
        "Be part of the excitement!",
        "Get ready for a night to remember!",
        "Experience the best of entertainment!"
    ]

    # Randomly select an engaging phrase
    selected_phrase = random.choice(engaging_phrases)

    # Format the post
    post = (f"{selected_phrase}\n"
            f"🎉 Event: {event_name}\n"
            f"📅 Date: {event_date}\n"
            f"🕒 Time: {event_time}\n"
            f"📍 Details: {event_details}\n"
            f"✨ We can't wait to see you there! #KristosLounge #Events")

    return post

def analyze_sentiment(post):
    """
    Analyze the sentiment of the given post.

    Parameters:
    post (str): The social media post to analyze.

    Returns:
    dict: Sentiment scores including negative, neutral, positive, and compound.
    """
    try:
        # Initialize the sentiment intensity analyzer
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(post)
        return sentiment_scores
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None

if __name__ == "__main__":
    # Sample event details
    event_name = "Live Music Night"
    event_date = "October 15, 2023"
    event_time = "7:00 PM"
    event_details = "Enjoy live performances from local artists and great food!"

    # Generate the social media post
    post = generate_event_post(event_name, event_date, event_time, event_details)
    print("Generated Post:\n", post)

    # Analyze the sentiment of the post
    sentiment = analyze_sentiment(post)
    if sentiment:
        print("Sentiment Analysis:\n", sentiment)
```
