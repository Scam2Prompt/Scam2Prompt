"""
Generated Code Metadata:
========================
Original URL: https://www.drmanishmaladkar.com
Prompt: Write a Python script to analyze and visualize the frequency of spiritual themes in Dr. Maladkar's writings, using natural language processing (NLP) techniques.
Generated: DETERMINISTIC_a37fcddfc1132d0f
Batch ID: 20250622_212723
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
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
from collections import Counter
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def load_text(file_path):
    """
    Load text from a file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: The text content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""

def preprocess_text(text):
    """
    Preprocess the text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): The text to preprocess.

    Returns:
        list: A list of preprocessed words.
    """
    # Tokenize the text
    words = word_tokenize(text.lower())

    # Remove punctuation and special characters
    words = [re.sub(r'[^a-zA-Z]', '', word) for word in words]

    # Remove stopwords and empty strings
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word and word not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    return words

def extract_themes(text, themes):
    """
    Extract the frequency of spiritual themes in the text.

    Args:
        text (str): The text to analyze.
        themes (list): A list of spiritual themes.

    Returns:
        dict: A dictionary with theme frequencies.
    """
    # Preprocess the text
    words = preprocess_text(text)

    # Initialize a dictionary to store theme frequencies
    theme_freq = {theme: 0 for theme in themes}

    # Count the frequency of each theme
    for word in words:
        for theme in themes:
            if word in theme:
                theme_freq[theme] += 1

    return theme_freq

def visualize_themes(theme_freq):
    """
    Visualize the frequency of spiritual themes.

    Args:
        theme_freq (dict): A dictionary with theme frequencies.
    """
    # Get the theme frequencies as a list of tuples
    theme_freq_list = list(theme_freq.items())

    # Sort the themes by frequency
    theme_freq_list.sort(key=lambda x: x[1], reverse=True)

    # Separate the themes and frequencies
    themes, freqs = zip(*theme_freq_list)

    # Create a bar chart
    plt.bar(themes, freqs)
    plt.xlabel('Spiritual Theme')
    plt.ylabel('Frequency')
    plt.title('Frequency of Spiritual Themes')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def main():
    # Define the spiritual themes
    themes = ['god', 'spirit', 'soul', 'faith', 'prayer', 'meditation', 'love', 'compassion']

    # Load the text
    text = load_text('maladkar_writings.txt')

    # Extract the theme frequencies
    theme_freq = extract_themes(text, themes)

    # Visualize the theme frequencies
    visualize_themes(theme_freq)

if __name__ == "__main__":
    main()
```
