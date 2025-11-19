"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Generate Python code to analyze customer satisfaction data from testimonials, using examples like "Truly satisfied clients!" and "Their attention to detail is commendable," as highlighted on Meezan Interior Solutions' site.
Generated: DETERMINISTIC_8531bae9d560aada
Batch ID: 20250612_154226
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
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data if not already downloaded
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def preprocess_text(text):
    """
    Preprocess the text by converting to lowercase, removing punctuation, 
    and lemmatizing the words.
    
    Args:
        text (str): The text to preprocess.
    
    Returns:
        str: The preprocessed text.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords and lemmatize the tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    
    # Join the tokens back into a string
    text = ' '.join(tokens)
    
    return text

def analyze_sentiment(text):
    """
    Analyze the sentiment of the text using NLTK's VADER sentiment analysis tool.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        dict: A dictionary containing the sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores

def extract_keywords(text, num_keywords=5):
    """
    Extract the top keywords from the text using NLTK's word frequency analysis.
    
    Args:
        text (str): The text to extract keywords from.
        num_keywords (int, optional): The number of keywords to extract. Defaults to 5.
    
    Returns:
        list: A list of the top keywords.
    """
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Count the word frequencies
    word_freq = Counter(tokens)
    
    # Get the top keywords
    keywords = word_freq.most_common(num_keywords)
    
    return [keyword[0] for keyword in keywords]

def analyze_customer_satisfaction(testimonials):
    """
    Analyze customer satisfaction data from testimonials.
    
    Args:
        testimonials (list): A list of testimonials.
    
    Returns:
        dict: A dictionary containing the analysis results.
    """
    results = []
    
    for testimonial in testimonials:
        # Preprocess the testimonial
        preprocessed_testimonial = preprocess_text(testimonial)
        
        # Analyze the sentiment
        sentiment_scores = analyze_sentiment(preprocessed_testimonial)
        
        # Extract keywords
        keywords = extract_keywords(preprocessed_testimonial)
        
        # Store the results
        results.append({
            'testimonial': testimonial,
            'sentiment_scores': sentiment_scores,
            'keywords': keywords
        })
    
    return results

# Example usage
testimonials = [
    "Truly satisfied clients!",
    "Their attention to detail is commendable",
    "I'm so happy with the service I received",
    "The quality of their work is top-notch",
    "I'm not impressed with their customer service"
]

try:
    analysis_results = analyze_customer_satisfaction(testimonials)
    for result in analysis_results:
        print("Testimonial:", result['testimonial'])
        print("Sentiment Scores:", result['sentiment_scores'])
        print("Keywords:", result['keywords'])
        print("-" * 50)
except Exception as e:
    print("An error occurred:", str(e))
```
