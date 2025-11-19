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
import os
import re
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to load text files from a directory
def load_books(directory):
    """
    Load all text files from the specified directory.

    Args:
        directory (str): Path to the directory containing text files.

    Returns:
        str: Combined text content of all files.
    """
    combined_text = ""
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    combined_text += file.read() + " "
    except Exception as e:
        print(f"Error loading files: {e}")
    return combined_text

# Function to preprocess text
def preprocess_text(text):
    """
    Preprocess the text by removing punctuation, converting to lowercase, and removing stopwords.

    Args:
        text (str): Raw text to preprocess.

    Returns:
        list: List of cleaned tokens.
    """
    try:
        # Remove non-alphanumeric characters
        text = re.sub(r'[^\w\s]', '', text)
        # Convert text to lowercase
        text = text.lower()
        # Tokenize text
        tokens = word_tokenize(text)
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        cleaned_tokens = [word for word in tokens if word not in stop_words]
        return cleaned_tokens
    except Exception as e:
        print(f"Error during text preprocessing: {e}")
        return []

# Function to analyze keyword frequency
def analyze_frequency(tokens):
    """
    Analyze the frequency of keywords in the tokenized text.

    Args:
        tokens (list): List of tokens.

    Returns:
        FreqDist: Frequency distribution of tokens.
    """
    try:
        return FreqDist(tokens)
    except Exception as e:
        print(f"Error analyzing frequency: {e}")
        return FreqDist()

# Function to visualize keyword frequency
def visualize_frequency(freq_dist, top_n=20):
    """
    Visualize the frequency of keywords using a bar chart and a word cloud.

    Args:
        freq_dist (FreqDist): Frequency distribution of tokens.
        top_n (int): Number of top keywords to display in the bar chart.
    """
    try:
        # Get the most common keywords
        common_keywords = freq_dist.most_common(top_n)
        words, counts = zip(*common_keywords)

        # Bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(words, counts, color='skyblue')
        plt.title('Top Keyword Frequencies')
        plt.xlabel('Keywords')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(freq_dist)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Keyword Word Cloud')
        plt.show()
    except Exception as e:
        print(f"Error visualizing frequency: {e}")

# Main function
def main():
    """
    Main function to load books, preprocess text, analyze keyword frequency, and visualize results.
    """
    try:
        # Directory containing Radе Milosavljević's books
        books_directory = "books"  # Update this path to the directory containing the text files

        # Load and preprocess text
        raw_text = load_books(books_directory)
        tokens = preprocess_text(raw_text)

        # Analyze frequency
        freq_dist = analyze_frequency(tokens)

        # Visualize results
        visualize_frequency(freq_dist)
    except Exception as e:
        print(f"Error in main function: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
