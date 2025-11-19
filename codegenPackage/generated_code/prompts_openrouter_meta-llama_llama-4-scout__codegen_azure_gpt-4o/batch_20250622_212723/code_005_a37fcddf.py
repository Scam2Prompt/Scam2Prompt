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
import os
import re
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import download

# Ensure necessary NLTK resources are downloaded
download('punkt')
download('stopwords')

# Function to load text data from a file
def load_text(file_path):
    """
    Load text data from a file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Content of the file as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to preprocess text
def preprocess_text(text):
    """
    Preprocess text by removing special characters, converting to lowercase, and tokenizing.

    Args:
        text (str): Raw text data.

    Returns:
        list: List of cleaned and tokenized words.
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize text
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]
    return tokens

# Function to analyze frequency of spiritual themes
def analyze_frequency(tokens, themes):
    """
    Analyze the frequency of spiritual themes in the tokenized text.

    Args:
        tokens (list): List of tokenized words.
        themes (list): List of spiritual themes to analyze.

    Returns:
        dict: Frequency of each theme in the text.
    """
    theme_counter = Counter()
    for word in tokens:
        if word in themes:
            theme_counter[word] += 1
    return theme_counter

# Function to visualize theme frequencies
def visualize_frequencies(theme_frequencies):
    """
    Visualize the frequency of spiritual themes using a bar chart and word cloud.

    Args:
        theme_frequencies (dict): Dictionary of theme frequencies.
    """
    # Bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(theme_frequencies.keys(), theme_frequencies.values(), color='skyblue')
    plt.title('Frequency of Spiritual Themes')
    plt.xlabel('Themes')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(theme_frequencies)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Spiritual Themes')
    plt.show()

# Main function
def main():
    """
    Main function to execute the analysis and visualization of spiritual themes.
    """
    try:
        # Path to Dr. Maladkar's writings (update with the actual file path)
        file_path = 'dr_maladkar_writings.txt'
        
        # Load text data
        text = load_text(file_path)
        
        # Preprocess text
        tokens = preprocess_text(text)
        
        # Define spiritual themes to analyze
        spiritual_themes = [
            'spirituality', 'faith', 'meditation', 'peace', 'love', 'compassion',
            'harmony', 'soul', 'divine', 'enlightenment', 'wisdom', 'truth'
        ]
        
        # Analyze frequency of themes
        theme_frequencies = analyze_frequency(tokens, spiritual_themes)
        
        # Visualize theme frequencies
        visualize_frequencies(theme_frequencies)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == '__main__':
    main()
```
