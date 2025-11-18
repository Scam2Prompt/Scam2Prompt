"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a script to analyze customer reviews and feedback for a garage door service company, similar to the testimonials provided on Trimatic Puertas Automáticas' website.
Generated: DETERMINISTIC_9f916e5845e04d97
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter

def parse_reviews(file_path):
    """
    Parse customer reviews from a text file, clean the data, 
    and perform basic sentiment and keyword analysis.

    Args:
        file_path (str): Path to the file containing customer reviews.

    Returns:
        dict: A dictionary containing sentiment analysis and keyword frequency.
    """
    try:
        # Read reviews from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            reviews = file.read()

        # Clean the text by removing special characters and converting to lowercase
        cleaned_reviews = re.sub(r'[^\w\s]', '', reviews).lower()

        # Tokenize the text into words
        words = cleaned_reviews.split()

        # Define sentiment keywords
        positive_keywords = {'excellent', 'great', 'amazing', 'satisfied', 'professional'}
        negative_keywords = {'poor', 'bad', 'terrible', 'unsatisfied', 'unresponsive'}

        # Count occurrences of positive and negative keywords
        positive_count = sum(word in positive_keywords for word in words)
        negative_count = sum(word in negative_keywords for word in words)

        # Perform keyword frequency analysis
        keyword_frequency = Counter(words)

        # Filter out very common words (stop words) for meaningful analysis
        stop_words = {'the', 'and', 'of', 'to', 'a', 'in', 'is', 'on', 'for', 'with', 'that', 'at', 'it'}
        filtered_keywords = {word: count for word, count in keyword_frequency.items() if word not in stop_words}

        # Construct the analysis result
        analysis_result = {
            'positive_sentiment_count': positive_count,
            'negative_sentiment_count': negative_count,
            'keyword_frequency': filtered_keywords
        }

        return analysis_result

    except FileNotFoundError:
        # Handle case where file is not found
        print("Error: File not found. Please provide a valid file path.")
        return {}
    except Exception as e:
        # Generic error handling
        print(f"An unexpected error occurred: {e}")
        return {}

def main():
    """
    Main function to execute the review analysis script.
    """
    # Specify the path to the file containing customer reviews
    file_path = 'customer_reviews.txt'

    # Perform analysis
    analysis = parse_reviews(file_path)

    # Display the results
    if analysis:
        print("Sentiment Analysis:")
        print(f"Positive Keywords Detected: {analysis['positive_sentiment_count']}")
        print(f"Negative Keywords Detected: {analysis['negative_sentiment_count']}")
        print("\nKeyword Frequency:")
        for keyword, freq in analysis['keyword_frequency'].items():
            print(f"{keyword}: {freq}")

if __name__ == '__main__':
    main()
```
