"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Write code to visualize the frequency of topics covered in SRH Life Foundation's blog categories, such as "Health," "Home and Lifestyle," and "Environmental."
Generated: DETERMINISTIC_6e452a40dd4f8955
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

def load_blog_data(file_path):
    """
    Load blog data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pandas.DataFrame: A DataFrame containing the blog data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file. Please check the file format.")
        return None

def preprocess_text(text):
    """
    Preprocess text by converting to lowercase and removing special characters.

    Parameters:
    text (str): The text to preprocess.

    Returns:
    str: The preprocessed text.
    """
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def extract_topics(data, category_column, text_column):
    """
    Extract topics from blog data.

    Parameters:
    data (pandas.DataFrame): The blog data.
    category_column (str): The column name for blog categories.
    text_column (str): The column name for blog text.

    Returns:
    dict: A dictionary with categories as keys and lists of topics as values.
    """
    topics = {}
    # Iterate over each row in the data
    for index, row in data.iterrows():
        category = row[category_column]
        text = row[text_column]
        # Preprocess text
        text = preprocess_text(text)
        # Split text into words
        words = text.split()
        # Add words to the list of topics for the category
        if category in topics:
            topics[category].extend(words)
        else:
            topics[category] = words
    return topics

def calculate_topic_frequencies(topics):
    """
    Calculate the frequency of topics in each category.

    Parameters:
    topics (dict): A dictionary with categories as keys and lists of topics as values.

    Returns:
    dict: A dictionary with categories as keys and dictionaries of topic frequencies as values.
    """
    topic_frequencies = {}
    # Iterate over each category and its topics
    for category, topic_list in topics.items():
        # Calculate topic frequencies using Counter
        topic_frequencies[category] = Counter(topic_list)
    return topic_frequencies

def visualize_topic_frequencies(topic_frequencies, num_topics=10):
    """
    Visualize the frequency of topics in each category.

    Parameters:
    topic_frequencies (dict): A dictionary with categories as keys and dictionaries of topic frequencies as values.
    num_topics (int): The number of top topics to display.
    """
    # Iterate over each category and its topic frequencies
    for category, frequencies in topic_frequencies.items():
        # Get the top N topics
        top_topics = frequencies.most_common(num_topics)
        # Separate topics and frequencies
        topics, freqs = zip(*top_topics)
        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(topics, freqs)
        plt.xlabel('Topic')
        plt.ylabel('Frequency')
        plt.title(f'Top {num_topics} Topics in {category} Category')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

def main():
    # Load blog data
    file_path = 'blog_data.csv'  # replace with your file path
    data = load_blog_data(file_path)
    if data is not None:
        # Extract topics
        category_column = 'category'  # replace with your category column name
        text_column = 'text'  # replace with your text column name
        topics = extract_topics(data, category_column, text_column)
        # Calculate topic frequencies
        topic_frequencies = calculate_topic_frequencies(topics)
        # Visualize topic frequencies
        visualize_topic_frequencies(topic_frequencies)

if __name__ == "__main__":
    main()
```
