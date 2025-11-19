"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Generate a list of 10 popular categories for articles and trending posts using natural language processing techniques.
Generated: DETERMINISTIC_747faeada6bf73d1
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """Preprocess text by tokenizing, removing stopwords/punctuation, and lemmatizing."""
    # Tokenize
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

def extract_categories(articles, num_categories=10):
    """Extract popular categories from a list of articles."""
    all_words = []
    
    for article in articles:
        processed_words = preprocess_text(article)
        all_words.extend(processed_words)
    
    # Get most common words
    word_counts = Counter(all_words)
    most_common = word_counts.most_common(num_categories)
    
    # Return just the words, not counts
    return [word[0] for word in most_common]

# Example usage with sample articles
if __name__ == "__main__":
    sample_articles = [
        "Technology is advancing rapidly with new AI developments",
        "Health experts recommend regular exercise and balanced diet",
        "Financial markets show volatility amid economic uncertainty",
        "Travel destinations for summer vacations are trending",
        "Climate change impacts are becoming more severe",
        "Education systems adapt to remote learning technologies",
        "Sports events draw millions of viewers worldwide",
        "Entertainment industry releases blockbuster movies",
        "Politics dominate news cycles with election coverage",
        "Food trends shift towards plant-based alternatives",
        "Science discoveries reveal new insights about space",
        "Business strategies evolve in the digital age",
        "Fashion trends change with seasonal collections",
        "Parenting advice focuses on mental health awareness",
        "Gaming industry breaks revenue records annually"
    ]
    
    categories = extract_categories(sample_articles)
    print("Top 10 Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")
```
