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
# Import required libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess the text by tokenizing, removing stopwords, and lemmatizing.
    
    Args:
        text (str): The text to preprocess.
    
    Returns:
        list: A list of preprocessed words.
    """
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens

def get_categories(texts, num_categories):
    """
    Get the top categories from a list of texts.
    
    Args:
        texts (list): A list of texts.
        num_categories (int): The number of categories to return.
    
    Returns:
        list: A list of the top categories.
    """
    # Preprocess the texts
    preprocessed_texts = [preprocess_text(text) for text in texts]
    
    # Flatten the list of lists
    all_tokens = [token for text in preprocessed_texts for token in text]
    
    # Count the frequency of each token
    token_counts = Counter(all_tokens)
    
    # Get the top categories
    categories = token_counts.most_common(num_categories)
    
    return categories

def get_trending_posts(texts, num_posts):
    """
    Get the top trending posts from a list of texts.
    
    Args:
        texts (list): A list of texts.
        num_posts (int): The number of posts to return.
    
    Returns:
        list: A list of the top trending posts.
    """
    # Calculate the word count for each text
    word_counts = [len(preprocess_text(text)) for text in texts]
    
    # Get the top trending posts
    trending_posts = sorted(zip(texts, word_counts), key=lambda x: x[1], reverse=True)[:num_posts]
    
    return trending_posts

def main():
    # Sample texts
    texts = [
        "This is a sample article about machine learning and AI.",
        "Machine learning is a subset of artificial intelligence.",
        "Deep learning is a type of machine learning.",
        "Natural language processing is a key application of AI.",
        "Computer vision is another key application of AI.",
        "Robotics is a field that combines AI and machine learning.",
        "AI has many applications in healthcare and finance.",
        "Machine learning is used in many industries, including tech and finance.",
        "AI and machine learning are transforming the way we live and work.",
        "The future of AI and machine learning is exciting and full of possibilities."
    ]
    
    # Get the top categories
    categories = get_categories(texts, 10)
    print("Popular Categories:")
    for category, count in categories:
        print(f"{category}: {count}")
    
    # Get the top trending posts
    trending_posts = get_trending_posts(texts, 3)
    print("\nTrending Posts:")
    for post, word_count in trending_posts:
        print(f"Post: {post}")
        print(f"Word Count: {word_count}")
        print()

if __name__ == "__main__":
    main()
```
