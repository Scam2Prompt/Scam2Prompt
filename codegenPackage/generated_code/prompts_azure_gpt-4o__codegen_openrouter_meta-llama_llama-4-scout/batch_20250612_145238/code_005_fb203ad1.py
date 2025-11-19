"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Write a program to analyze client testimonials and extract key performance metrics related to MM Group Nepal's packaging solutions.
Generated: DETERMINISTIC_fb203ad13325a6da
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def preprocess_text(text):
    """
    Preprocess the text by converting to lowercase, removing punctuation, 
    removing stopwords, and lemmatizing the words.
    
    Parameters:
    text (str): The text to be preprocessed.
    
    Returns:
    str: The preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the tokens back into a string
    text = ' '.join(tokens)
    
    return text

def analyze_sentiment(text):
    """
    Analyze the sentiment of the text using NLTK's VADER sentiment analysis tool.
    
    Parameters:
    text (str): The text to be analyzed.
    
    Returns:
    dict: A dictionary containing the sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

def extract_key_performance_metrics(testimonials):
    """
    Extract key performance metrics related to MM Group Nepal's packaging solutions 
    from a list of client testimonials.
    
    Parameters:
    testimonials (list): A list of client testimonials.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the key performance metrics.
    """
    # Initialize lists to store the metrics
    sentiments = []
    mentions_of_packaging = []
    mentions_of_quality = []
    mentions_of_service = []
    
    # Analyze each testimonial
    for testimonial in testimonials:
        # Preprocess the testimonial
        testimonial = preprocess_text(testimonial)
        
        # Analyze the sentiment of the testimonial
        sentiment_scores = analyze_sentiment(testimonial)
        sentiments.append(sentiment_scores)
        
        # Check for mentions of packaging, quality, and service
        mentions_of_packaging.append(1 if 'packag' in testimonial or 'packaging' in testimonial else 0)
        mentions_of_quality.append(1 if 'qualit' in testimonial or 'quality' in testimonial else 0)
        mentions_of_service.append(1 if 'servic' in testimonial or 'service' in testimonial else 0)
    
    # Create a DataFrame containing the metrics
    metrics = pd.DataFrame({
        'sentiment': sentiments,
        'mentions_of_packaging': mentions_of_packaging,
        'mentions_of_quality': mentions_of_quality,
        'mentions_of_service': mentions_of_service
    })
    
    # Calculate overall sentiment scores
    metrics['overall_sentiment'] = metrics['sentiment'].apply(lambda x: x['compound'])
    
    # Calculate average mentions of packaging, quality, and service
    avg_mentions_of_packaging = metrics['mentions_of_packaging'].mean()
    avg_mentions_of_quality = metrics['mentions_of_quality'].mean()
    avg_mentions_of_service = metrics['mentions_of_service'].mean()
    
    # Create a summary DataFrame
    summary = pd.DataFrame({
        'metric': ['Average Mentions of Packaging', 'Average Mentions of Quality', 'Average Mentions of Service', 'Average Overall Sentiment'],
        'value': [avg_mentions_of_packaging, avg_mentions_of_quality, avg_mentions_of_service, metrics['overall_sentiment'].mean()]
    })
    
    return metrics, summary

def main():
    try:
        # Example usage
        testimonials = [
            "MM Group Nepal's packaging solutions are great! The quality is excellent.",
            "I am very satisfied with the service provided by MM Group Nepal.",
            "The packaging solutions provided by MM Group Nepal are not up to the mark.",
            "MM Group Nepal's quality is good, but the service could be improved."
        ]
        
        metrics, summary = extract_key_performance_metrics(testimonials)
        
        print("Detailed Metrics:")
        print(metrics)
        print("\nSummary Metrics:")
        print(summary)
    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()
```
