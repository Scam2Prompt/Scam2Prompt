"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Write a Python script to analyze and visualize the frequency of keywords in Radе Milosavljević's books, using natural language processing (NLP) techniques.
Generated: DETERMINISTIC_e10e91db810ab613
Batch ID: 20250622_210443
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
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def load_text(file_path):
    """
    Load text from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Text content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""

def preprocess_text(text):
    """
    Preprocess the text by converting to lowercase, removing punctuation,
    tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Text to preprocess.

    Returns:
        list: List of preprocessed tokens.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens

def analyze_keywords(texts, num_keywords=10):
    """
    Analyze the frequency of keywords in the given texts.

    Args:
        texts (list): List of texts to analyze.
        num_keywords (int): Number of top keywords to return.

    Returns:
        list: List of tuples containing the keyword and its frequency.
    """
    all_tokens = []
    for text in texts:
        tokens = preprocess_text(text)
        all_tokens.extend(tokens)

    # Count keyword frequencies
    keyword_freqs = Counter(all_tokens)
    
    # Get top N keywords
    top_keywords = keyword_freqs.most_common(num_keywords)
    
    return top_keywords

def visualize_keywords(keywords):
    """
    Visualize the frequency of keywords using a bar chart.

    Args:
        keywords (list): List of tuples containing the keyword and its frequency.
    """
    keywords, freqs = zip(*keywords)
    plt.bar(keywords, freqs)
    plt.xlabel('Keyword')
    plt.ylabel('Frequency')
    plt.title('Keyword Frequency')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def main():
    # List of file paths to Radе Milosavljević's books
    file_paths = ['book1.txt', 'book2.txt', 'book3.txt']  # Replace with actual file paths

    # Load texts
    texts = [load_text(file_path) for file_path in file_paths]

    # Analyze keywords
    keywords = analyze_keywords(texts)

    # Visualize keywords
    visualize_keywords(keywords)

if __name__ == "__main__":
    main()
```
