"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Create a Python script to analyze customer reviews and feedback for Marant's "Exfoliadora de Calabaza" product, focusing on its effectiveness in reducing oxidative processes and free radicals.
Generated: DETERMINISTIC_62d9a0d6f1fba033
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from textblob import TextBlob
import pandas as pd

# Function to preprocess customer reviews
def preprocess_review(review):
    """
    Clean and preprocess the customer review text.
    Removes special characters, numbers, and converts to lowercase.
    """
    try:
        # Remove non-alphabetic characters
        review = re.sub(r'[^a-zA-Z\s]', '', review)
        # Convert text to lowercase
        review = review.lower()
        return review
    except Exception as e:
        print(f"Error preprocessing review: {e}")
        return None

# Function to analyze sentiment of the reviews
def analyze_sentiment(review):
    """
    Analyze sentiment of a review using TextBlob.
    Returns 'Positive', 'Neutral', or 'Negative' sentiment.
    """
    try:
        blob = TextBlob(review)
        sentiment_score = blob.sentiment.polarity
        # Define sentiment categories based on polarity score
        if sentiment_score > 0.3:
            return 'Positive'
        elif sentiment_score < -0.3:
            return 'Negative'
        else:
            return 'Neutral'
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None

# Function to extract key mentions about product effectiveness
def extract_effectiveness_mentions(review):
    """
    Check if the review mentions the product's effectiveness in reducing 
    oxidative processes or free radicals.
    Returns True if mentions are found, False otherwise.
    """
    try:
        keywords = ['oxidative', 'free radicals', 'effective', 'antioxidant']
        for keyword in keywords:
            if keyword in review:
                return True
        return False
    except Exception as e:
        print(f"Error extracting effectiveness mentions: {e}")
        return False

# Main function to analyze customer reviews
def analyze_customer_feedback(reviews):
    """
    Analyze a list of customer reviews for sentiment and effectiveness mentions.
    Returns a summary DataFrame with sentiment and effectiveness metrics.
    """
    try:
        # Initialize an empty list to store analysis results
        analysis_results = []
        for review in reviews:
            # Preprocess the review text
            cleaned_review = preprocess_review(review)
            if cleaned_review:
                # Analyze sentiment
                sentiment = analyze_sentiment(cleaned_review)
                # Check for effectiveness mentions
                effectiveness = extract_effectiveness_mentions(cleaned_review)
                # Append results to the list
                analysis_results.append({
                    'Original Review': review,
                    'Cleaned Review': cleaned_review,
                    'Sentiment': sentiment,
                    'Mentions Effectiveness': effectiveness
                })
        
        # Convert analysis results into a DataFrame for better readability
        result_df = pd.DataFrame(analysis_results)
        return result_df
    except Exception as e:
        print(f"Error analyzing customer feedback: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample customer reviews
    sample_reviews = [
        "I love this product! It's so effective at reducing oxidative stress.",
        "Not sure if it works for free radicals, but it smells great!",
        "This exfoliator is useless, it doesn't do anything for oxidative processes.",
        "Very effective antioxidant properties, I noticed a huge difference!",
        "Just an average product, nothing special."
    ]
    
    # Analyze the reviews
    feedback_summary = analyze_customer_feedback(sample_reviews)
    
    # Display the results
    if feedback_summary is not None:
        print("Customer Feedback Analysis:")
        print(feedback_summary)
```
