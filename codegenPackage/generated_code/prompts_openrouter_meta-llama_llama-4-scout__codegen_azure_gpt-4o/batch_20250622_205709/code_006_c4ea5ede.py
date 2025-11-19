"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Write a script to analyze customer reviews and ratings, like those found on Acessanet's Google Play and App Store pages, and generate insights on common themes and areas for improvement.
Generated: DETERMINISTIC_c4ea5ede8bc00f06
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import string
from collections import Counter
from typing import List, Dict, Tuple
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text: str) -> List[str]:
    """
    Preprocesses the input text by removing punctuation, converting to lowercase,
    and tokenizing the text into words.
    
    Args:
        text (str): The raw text to preprocess.
    
    Returns:
        List[str]: A list of cleaned and tokenized words.
    """
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

def analyze_reviews(reviews: List[Dict[str, str]]) -> Dict[str, any]:
    """
    Analyzes customer reviews to extract common themes and areas for improvement.
    
    Args:
        reviews (List[Dict[str, str]]): A list of dictionaries containing customer reviews.
                                        Each dictionary should have 'review' and 'rating' keys.
    
    Returns:
        Dict[str, any]: Insights including common themes and average rating.
    """
    all_words = []
    ratings = []
    for review in reviews:
        try:
            # Extract and preprocess review text
            review_text = review.get('review', '')
            tokens = preprocess_text(review_text)
            all_words.extend(tokens)
            
            # Extract rating
            rating = review.get('rating', None)
            if rating is not None:
                ratings.append(float(rating))
        except Exception as e:
            print(f"Error processing review: {e}")
    
    # Calculate average rating
    average_rating = sum(ratings) / len(ratings) if ratings else 0
    
    # Identify common themes (most frequent words)
    word_counts = Counter(all_words)
    common_themes = word_counts.most_common(10)
    
    return {
        "average_rating": average_rating,
        "common_themes": common_themes
    }

def main():
    """
    Main function to demonstrate the review analysis script.
    """
    # Example reviews (replace with actual data from Google Play or App Store)
    reviews = [
        {"review": "Great app! Very user-friendly and intuitive.", "rating": 5},
        {"review": "The app crashes frequently. Needs improvement.", "rating": 2},
        {"review": "Excellent features, but the UI could be better.", "rating": 4},
        {"review": "Terrible experience. The app is slow and buggy.", "rating": 1},
        {"review": "I love this app! It has everything I need.", "rating": 5},
    ]
    
    # Analyze reviews
    insights = analyze_reviews(reviews)
    
    # Display insights
    print("Average Rating:", insights["average_rating"])
    print("Common Themes:")
    for theme, count in insights["common_themes"]:
        print(f"{theme}: {count}")

if __name__ == "__main__":
    main()
```
