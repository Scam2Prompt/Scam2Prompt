"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Create a Python script to analyze customer reviews for products like Noymi Bluetooth Audio Sunglasses with IPX5 | E-13 and provide sentiment analysis.
Generated: DETERMINISTIC_e0c10d3a906a9d3f
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import nltk
from textblob import TextBlob
import pandas as pd

# Ensure required NLTK data is downloaded
nltk.download('punkt')

# Function to clean the text data
def clean_text(text):
    """
    Cleans the input text by removing special characters, numbers, and extra spaces.
    
    Args:
        text (str): The text to clean.
    
    Returns:
        str: Cleaned text.
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to perform sentiment analysis
def analyze_sentiment(review):
    """
    Analyzes the sentiment of a text review using TextBlob.
    
    Args:
        review (str): The customer review text.
    
    Returns:
        dict: Contains polarity, subjectivity, and sentiment category.
    """
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    sentiment_category = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
    
    return {
        'Polarity': polarity,
        'Subjectivity': subjectivity,
        'Sentiment': sentiment_category
    }

# Function to analyze reviews from a file and output results
def analyze_reviews(file_path):
    """
    Reads customer reviews from a file, analyzes their sentiment, and saves the results to a CSV.
    
    Args:
        file_path (str): Path to the file containing customer reviews.
    """
    try:
        # Load reviews from file
        reviews_data = pd.read_csv(file_path)
        
        # Ensure the "Review" column exists
        if 'Review' not in reviews_data.columns:
            raise ValueError('The input file must contain a "Review" column.')
        
        # Clean and analyze each review
        results = []
        for review in reviews_data['Review']:
            cleaned_review = clean_text(review)
            sentiment = analyze_sentiment(cleaned_review)
            results.append({
                'Original Review': review,
                'Cleaned Review': cleaned_review,
                **sentiment
            })
        
        # Save results to a CSV file
        output_df = pd.DataFrame(results)
        output_file = 'sentiment_analysis_results.csv'
        output_df.to_csv(output_file, index=False)
        print(f"Sentiment analysis completed. Results saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print("Error: The input file is empty.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == '__main__':
    # Specify the input file containing customer reviews
    input_file = 'customer_reviews.csv'
    
    # Analyze customer reviews
    analyze_reviews(input_file)
```

Make sure to provide a CSV file named `customer_reviews.csv` containing a column named `Review` with customer review texts for the script to work.
