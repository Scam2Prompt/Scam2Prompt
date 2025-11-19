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
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import nltk
from nltk.corpus import stopwords
import os

# Ensure NLTK resources are available
nltk.download('stopwords', quiet=True)

# Define a function to load text data from a directory
def load_texts_from_directory(directory):
    """
    Load all text files from a specified directory into a list.

    Args:
        directory (str): The path to the directory containing text files.

    Returns:
        list: A list of strings, each representing the content of a text file.
    """
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                texts.append(file.read())
    return texts

# Define a function to analyze spiritual themes
def analyze_spiritual_themes(texts, themes):
    """
    Analyze the frequency of specified spiritual themes in the provided texts.

    Args:
        texts (list): A list of text strings to analyze.
        themes (list): A list of spiritual themes to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the frequency of each theme in each text.
    """
    # Initialize CountVectorizer with custom stop words
    stop_words = set(stopwords.words('english'))
    vectorizer = CountVectorizer(vocabulary=themes, stop_words=stop_words)
    
    # Transform texts into a frequency matrix
    frequency_matrix = vectorizer.fit_transform(texts)
    
    # Normalize the frequency matrix
    normalized_matrix = normalize(frequency_matrix, axis=0)
    
    # Create a DataFrame for better visualization
    theme_frequencies = pd.DataFrame(normalized_matrix.toarray(), columns=themes)
    return theme_frequencies

# Define a function to visualize the theme frequencies
def visualize_theme_frequencies(theme_frequencies):
    """
    Visualize the frequency of spiritual themes using a bar plot.

    Args:
        theme_frequencies (pd.DataFrame): DataFrame containing theme frequencies.
    """
    # Sum frequencies across all texts
    total_frequencies = theme_frequencies.sum().sort_values(ascending=False)
    
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    total_frequencies.plot(kind='bar', color='skyblue')
    plt.title('Frequency of Spiritual Themes in Dr. Maladkar\'s Writings')
    plt.xlabel('Spiritual Themes')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main execution block
if __name__ == "__main__":
    # Directory containing Dr. Maladkar's writings
    writings_directory = 'path/to/writings'  # Update this path

    # List of spiritual themes to analyze
    spiritual_themes = ['meditation', 'enlightenment', 'soul', 'karma', 'peace', 'love', 'wisdom']

    try:
        # Load writings
        writings = load_texts_from_directory(writings_directory)
        
        # Analyze spiritual themes
        theme_frequencies = analyze_spiritual_themes(writings, spiritual_themes)
        
        # Visualize the results
        visualize_theme_frequencies(theme_frequencies)

    except Exception as e:
        print(f"An error occurred: {e}")
```
