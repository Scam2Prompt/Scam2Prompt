"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Create a code snippet to analyze customer testimonials for a business training course and provide insights on course effectiveness.
Generated: DETERMINISTIC_1031a283372e14db
Batch ID: 20250622_205751
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
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

def preprocess_text(text):
    """
    Preprocess text by converting to lowercase, removing punctuation, 
    lemmatizing words, and removing stopwords.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize words
    words = text.split()
    
    # Lemmatize words and remove stopwords
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return ' '.join(words)

def analyze_sentiment(text):
    """
    Analyze sentiment of the given text using VADER sentiment analysis.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_testimonials(testimonials):
    """
    Analyze customer testimonials and provide insights on course effectiveness.
    """
    # Initialize lists to store preprocessed testimonials and sentiments
    preprocessed_testimonials = []
    sentiments = []
    
    # Preprocess testimonials and analyze sentiments
    for testimonial in testimonials:
        preprocessed_testimonial = preprocess_text(testimonial)
        preprocessed_testimonials.append(preprocessed_testimonial)
        sentiment = analyze_sentiment(testimonial)
        sentiments.append(sentiment)
    
    # Count sentiment occurrences
    sentiment_counts = Counter(sentiments)
    
    # Calculate sentiment percentages
    total_testimonials = len(testimonials)
    sentiment_percentages = {
        sentiment: (count / total_testimonials) * 100
        for sentiment, count in sentiment_counts.items()
    }
    
    return {
        'preprocessed_testimonials': preprocessed_testimonials,
        'sentiment_counts': sentiment_counts,
        'sentiment_percentages': sentiment_percentages,
    }

def main():
    # Sample testimonials data
    data = {
        'Testimonial': [
            'This course was amazing! The instructor was knowledgeable and helpful.',
            'I was disappointed with the course. It did not meet my expectations.',
            'The course was okay. I learned some new things, but it was not engaging.',
            'I loved this course! The material was relevant and the instructor was great.',
            'The course was terrible. I would not recommend it to anyone.',
        ]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    try:
        # Analyze testimonials
        insights = analyze_testimonials(df['Testimonial'])
        
        # Print insights
        print('Preprocessed Testimonials:')
        for testimonial in insights['preprocessed_testimonials']:
            print(testimonial)
        
        print('\nSentiment Counts:')
        print(insights['sentiment_counts'])
        
        print('\nSentiment Percentages:')
        for sentiment, percentage in insights['sentiment_percentages'].items():
            print(f'{sentiment}: {percentage:.2f}%')
    
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
