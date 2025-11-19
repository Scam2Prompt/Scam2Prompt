"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Write a script to analyze and visualize the frequency of keywords in the titles of Mêtis' resources (e.g., articles, videos, podcasts) using natural language processing techniques.
Generated: DETERMINISTIC_312edebe2200b2c9
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
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def load_data(file_path):
    """
    Load resource titles from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the resource titles.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("The file does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file.")
        return None

def preprocess_text(text):
    """
    Preprocess a text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): The text to preprocess.

    Returns:
        list: A list of preprocessed tokens.
    """
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalpha() and token.lower() not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]

    return tokens

def analyze_keywords(titles, num_keywords):
    """
    Analyze the frequency of keywords in the titles.

    Args:
        titles (list): A list of resource titles.
        num_keywords (int): The number of top keywords to return.

    Returns:
        list: A list of tuples containing the top keywords and their frequencies.
    """
    # Preprocess the titles
    tokens = []
    for title in titles:
        tokens.extend(preprocess_text(title))

    # Count the frequency of each token
    token_freq = Counter(tokens)

    # Return the top keywords
    return token_freq.most_common(num_keywords)

def visualize_keywords(keywords):
    """
    Visualize the frequency of keywords using a bar chart.

    Args:
        keywords (list): A list of tuples containing the keywords and their frequencies.
    """
    # Extract the keywords and frequencies
    keywords, freqs = zip(*keywords)

    # Create a bar chart
    plt.bar(keywords, freqs)
    plt.xlabel('Keyword')
    plt.ylabel('Frequency')
    plt.title('Keyword Frequency')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def main():
    # Load the resource titles from a CSV file
    file_path = 'resource_titles.csv'  # Replace with your file path
    data = load_data(file_path)

    if data is not None:
        # Extract the titles from the DataFrame
        titles = data['title'].tolist()

        # Analyze the keywords
        num_keywords = 10
        keywords = analyze_keywords(titles, num_keywords)

        # Visualize the keywords
        visualize_keywords(keywords)

if __name__ == '__main__':
    main()
```
