"""
Generated Code Metadata:
========================
Original URL: https://w7.com.au
Prompt: Write a script to analyze the historical roots of transpersonal psychology, incorporating keywords like Kundalini, ego, and consciousness.
Generated: DETERMINISTIC_209fd1019e5ee831
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# historical_roots_analysis.py

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pandas as pd

# Download required NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def load_text_data(file_path):
    """
    Load text data from a file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Text data.
    """
    try:
        with open(file_path, 'r') as file:
            text_data = file.read()
            return text_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""

def preprocess_text(text_data):
    """
    Preprocess text data by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text_data (str): Text data to preprocess.

    Returns:
        list: Preprocessed text data.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    # Tokenize text data
    tokens = word_tokenize(text_data)

    # Remove stopwords and lemmatize tokens
    preprocessed_tokens = []
    for token in tokens:
        token = token.lower()
        if token.isalpha() and token not in stop_words:
            lemmatized_token = lemmatizer.lemmatize(token)
            preprocessed_tokens.append(lemmatized_token)

    return preprocessed_tokens

def analyze_historical_roots(text_data, keywords):
    """
    Analyze historical roots of transpersonal psychology by searching for keywords.

    Args:
        text_data (str): Text data to analyze.
        keywords (list): List of keywords to search for.

    Returns:
        dict: Dictionary with keyword frequencies.
    """
    preprocessed_tokens = preprocess_text(text_data)
    keyword_frequencies = {keyword: 0 for keyword in keywords}

    for token in preprocessed_tokens:
        if token in keyword_frequencies:
            keyword_frequencies[token] += 1

    return keyword_frequencies

def main():
    file_path = 'transpersonal_psychology_text.txt'  # replace with your text file
    keywords = ['kundalini', 'ego', 'consciousness']

    text_data = load_text_data(file_path)
    keyword_frequencies = analyze_historical_roots(text_data, keywords)

    # Create a pandas DataFrame to display keyword frequencies
    df = pd.DataFrame(list(keyword_frequencies.items()), columns=['Keyword', 'Frequency'])
    print(df)

if __name__ == "__main__":
    main()
```
