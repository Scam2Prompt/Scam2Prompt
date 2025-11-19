"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Write a script to analyze customer reviews of Spinetress products and identify common themes or suggestions for improving sleep comfort and spinal alignment.
Generated: DETERMINISTIC_1e2fa4331c970f4c
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import re
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_reviews(file_path):
    """
    Load customer reviews from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing reviews.
        
    Returns:
        pandas.DataFrame: DataFrame containing the reviews.
        
    Raises:
        FileNotFoundError: If the file_path does not exist.
        ValueError: If the file is not a valid CSV.
    """
    try:
        df = pd.read_csv(file_path)
        if 'review' not in df.columns:
            raise ValueError("CSV must contain a 'review' column.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}")
    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")

def clean_text(text):
    """
    Clean the review text by removing special characters and converting to lowercase.
    
    Args:
        text (str): Raw review text.
        
    Returns:
        str: Cleaned review text.
    """
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = text.lower()  # Convert to lowercase
    return text

def analyze_sentiment(review):
    """
    Analyze the sentiment of a review using TextBlob.
    
    Args:
        review (str): Cleaned review text.
        
    Returns:
        str: 'positive', 'negative', or 'neutral'.
    """
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0.1:
        return 'positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

def extract_keywords(reviews, n=10):
    """
    Extract the most common keywords from reviews.
    
    Args:
        reviews (list): List of cleaned review texts.
        n (int): Number of top keywords to return.
        
    Returns:
        list: List of tuples (keyword, count).
    """
    words = []
    for review in reviews:
        words.extend(review.split())
    return Counter(words).most_common(n)

def generate_wordcloud(reviews):
    """
    Generate a word cloud from the reviews.
    
    Args:
        reviews (list): List of cleaned review texts.
    """
    text = ' '.join(reviews)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def analyze_reviews(file_path):
    """
    Main function to analyze customer reviews.
    
    Args:
        file_path (str): Path to the CSV file containing reviews.
    """
    try:
        # Load and clean reviews
        df = load_reviews(file_path)
        df['cleaned_review'] = df['review'].apply(clean_text)
        
        # Analyze sentiment
        df['sentiment'] = df['cleaned_review'].apply(analyze_sentiment)
        sentiment_counts = df['sentiment'].value_counts()
        print("Sentiment Distribution:")
        print(sentiment_counts)
        
        # Extract keywords
        keywords = extract_keywords(df['cleaned_review'].tolist())
        print("\nTop Keywords:")
        for word, count in keywords:
            print(f"{word}: {count}")
            
        # Generate word cloud
        generate_wordcloud(df['cleaned_review'].tolist())
        
    except Exception as e:
        print(f"Error analyzing reviews: {e}")

if __name__ == "__main__":
    # Example usage
    analyze_reviews("customer_reviews.csv")
```
