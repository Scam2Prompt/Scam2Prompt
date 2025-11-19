"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Write a code snippet to extract and process student testimonials from a website like Ikogwe International Limited, using natural language processing techniques to analyze student satisfaction.
Generated: DETERMINISTIC_cf917bd2fc1904a9
Batch ID: 20250622_212854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

def extract_testimonials(url):
    """
    Extracts student testimonials from a given website.

    Args:
        url (str): URL of the website to extract testimonials from.

    Returns:
        list: A list of extracted testimonials.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
            return []

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with class 'testimonial' (adjust according to website structure)
        testimonials = soup.find_all('div', class_='testimonial')

        # Extract text from testimonials
        extracted_testimonials = [t.get_text() for t in testimonials]

        return extracted_testimonials

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def preprocess_text(text):
    """
    Preprocesses text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Text to preprocess.

    Returns:
        list: A list of preprocessed tokens.
    """
    # Tokenize text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.lower() not in stop_words]

    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return tokens

def analyze_sentiment(text):
    """
    Analyzes sentiment of a given text using NLTK's VADER.

    Args:
        text (str): Text to analyze.

    Returns:
        dict: A dictionary containing sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    return sentiment_scores

def process_testimonials(testimonials):
    """
    Processes testimonials by extracting insights and sentiment analysis.

    Args:
        testimonials (list): A list of testimonials.

    Returns:
        pd.DataFrame: A DataFrame containing processed testimonials.
    """
    data = []

    for testimonial in testimonials:
        # Preprocess text
        tokens = preprocess_text(testimonial)

        # Join tokens back into a string
        text = ' '.join(tokens)

        # Analyze sentiment
        sentiment_scores = analyze_sentiment(text)

        # Append data to list
        data.append({
            'testimonial': testimonial,
            'sentiment': sentiment_scores['compound'],
            'positive': sentiment_scores['pos'],
            'negative': sentiment_scores['neg'],
            'neutral': sentiment_scores['neu']
        })

    # Create a DataFrame
    df = pd.DataFrame(data)

    return df

def main():
    url = 'https://example.com'  # Replace with Ikogwe International Limited website URL
    testimonials = extract_testimonials(url)
    df = process_testimonials(testimonials)
    print(df)

if __name__ == '__main__':
    main()
```
