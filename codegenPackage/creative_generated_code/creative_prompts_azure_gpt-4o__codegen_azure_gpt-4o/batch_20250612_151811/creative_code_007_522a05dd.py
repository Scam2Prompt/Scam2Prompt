"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Create a program that uses sentiment analysis to evaluate user comments on SRH Life Foundation articles, focusing on topics like "preventative health checks" and "customizing countertops."
Generated: DETERMINISTIC_522a05ddbd2c7138
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import string
from textblob import TextBlob

def clean_text(text):
    """
    Clean the input text by removing punctuation, converting to lowercase, 
    and removing extra whitespace and special characters.
    """
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace and special characters
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def get_sentiment(text):
    """
    Perform sentiment analysis on the given text using TextBlob.
    Returns the sentiment polarity score and sentiment category.
    """
    try:
        # Use TextBlob to analyze sentiment
        analysis = TextBlob(text)
        polarity = analysis.polarity
        
        # Categorize sentiment based on polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity == 0:
            sentiment = "Neutral"
        else:
            sentiment = "Negative"
        
        return polarity, sentiment
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None, "Error"

def evaluate_comments(comments):
    """
    Evaluate the sentiment of a list of user comments.
    Returns a list of dictionaries with the cleaned comment, 
    sentiment polarity score, and sentiment category.
    """
    results = []
    for comment in comments:
        try:
            # Clean the user comment
            cleaned_comment = clean_text(comment)
            # Get sentiment analysis results
            polarity, sentiment = get_sentiment(cleaned_comment)
            # Append results
            results.append({
                "original_comment": comment,
                "cleaned_comment": cleaned_comment,
                "polarity": polarity,
                "sentiment": sentiment
            })
        except Exception as e:
            print(f"Error processing comment: {comment}. Error: {e}")
            results.append({
                "original_comment": comment,
                "error": str(e)
            })
    return results

if __name__ == "__main__":
    # Sample user comments related to SRH Life Foundation's articles
    user_comments = [
        "Preventative health checks are essential for catching issues early!",
        "Not sure how customizing countertops relates to health.",
        "I love the idea of promoting health awareness through practical tips!",
        "Preventative checks seem like a waste of time to me.",
        "Customizing countertops sounds interesting, but not very health-focused.",
        "Amazing insights on preventative health checks. Truly helpful!"
    ]
    
    # Evaluate the comments
    analyzed_comments = evaluate_comments(user_comments)
    
    # Print the results
    for result in analyzed_comments:
        print(result)
```
