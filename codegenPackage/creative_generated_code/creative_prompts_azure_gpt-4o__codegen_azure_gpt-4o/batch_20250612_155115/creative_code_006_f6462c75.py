"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Write code to perform sentiment analysis on financial news articles to assess market trends, inspired by the "Stay Informed" advice on Investolazlo.
Generated: DETERMINISTIC_f6462c75e820c339
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Function to clean and preprocess the text data
def clean_text(text):
    """
    Cleans the input text by removing special characters, numbers, and stopwords.
    Returns the cleaned text.
    """
    if not isinstance(text, str):
        return ""
    
    # Lowercase the text
    text = text.lower()
    
    # Remove non-alphanumeric characters
    text = re.sub(r'\W+', ' ', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in ENGLISH_STOP_WORDS]
    
    return ' '.join(filtered_words)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using TextBlob.
    Returns a sentiment score and polarity label (Positive, Neutral, Negative).
    """
    cleaned_text = clean_text(text)
    analysis = TextBlob(cleaned_text)
    sentiment_score = analysis.sentiment.polarity
    
    # Assign polarity labels based on sentiment score
    if sentiment_score > 0.2:
        sentiment_label = "Positive"
    elif sentiment_score < -0.2:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    return sentiment_score, sentiment_label

# Main function to process a dataset of financial news articles
def process_financial_news(file_path):
    """
    Reads a dataset of financial news articles from a CSV file, performs sentiment analysis,
    and assesses market trends based on sentiment polarity.
    Outputs the results into a new CSV file.
    """
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        
        # Ensure the file contains a 'content' column
        if 'content' not in df.columns:
            raise ValueError("The CSV file must contain a 'content' column with article text.")
        
        # Perform sentiment analysis on each article
        df['cleaned_content'] = df['content'].apply(clean_text)
        df['sentiment_score'], df['sentiment_label'] = zip(
            *df['content'].apply(analyze_sentiment)
        )
        
        # Save results to output CSV file
        output_file = "financial_news_sentiment_analysis.csv"
        df.to_csv(output_file, index=False)
        print(f"Sentiment analysis completed. Results saved to {output_file}")
    
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The input file is empty or invalid.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'financial_news.csv' with the path to your dataset
    process_financial_news('financial_news.csv')
```
