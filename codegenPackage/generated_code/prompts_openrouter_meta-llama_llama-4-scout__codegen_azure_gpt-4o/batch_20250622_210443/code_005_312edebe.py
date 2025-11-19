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
import re
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import nltk

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    """
    Preprocesses the input text by:
    - Converting to lowercase
    - Removing special characters and numbers
    - Tokenizing words
    - Removing stopwords
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize words
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return filtered_tokens

# Function to analyze keyword frequency
def analyze_keyword_frequency(titles):
    """
    Analyzes the frequency of keywords in a list of titles.
    Returns a frequency distribution of keywords.
    """
    all_tokens = []
    
    # Preprocess each title and collect tokens
    for title in titles:
        tokens = preprocess_text(title)
        all_tokens.extend(tokens)
    
    # Calculate frequency distribution
    freq_dist = FreqDist(all_tokens)
    return freq_dist

# Function to visualize keyword frequency
def visualize_keyword_frequency(freq_dist, top_n=20):
    """
    Visualizes the top N keywords using a bar chart and a word cloud.
    """
    # Get the most common keywords
    common_keywords = freq_dist.most_common(top_n)
    keywords, frequencies = zip(*common_keywords)
    
    # Bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, frequencies, color='skyblue')
    plt.title('Top Keywords in Titles')
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

# Main script
if __name__ == "__main__":
    # Example list of titles (replace with actual data)
    titles = [
        "Introduction to Machine Learning",
        "Deep Learning for Natural Language Processing",
        "Understanding Artificial Intelligence",
        "Data Science and Analytics",
        "Machine Learning Applications in Healthcare",
        "Natural Language Processing with Python",
        "AI Ethics and Responsible AI",
        "Big Data and Cloud Computing",
        "Python Programming for Beginners",
        "Advanced Topics in Data Science"
    ]
    
    try:
        # Analyze keyword frequency
        freq_dist = analyze_keyword_frequency(titles)
        
        # Visualize keyword frequency
        visualize_keyword_frequency(freq_dist)
    except Exception as e:
        print(f"An error occurred: {e}")
```
