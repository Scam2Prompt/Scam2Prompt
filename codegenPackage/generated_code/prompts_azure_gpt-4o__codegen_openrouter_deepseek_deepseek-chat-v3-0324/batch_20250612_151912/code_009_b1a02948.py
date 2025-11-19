"""
Generated Code Metadata:
========================
Original URL: https://bettermost.net
Prompt: Generate code to create a visualization of the most popular topics discussed in the "Anything Goes" section using Python and word cloud libraries.
Generated: DETERMINISTIC_b1a029481a3bc1f2
Batch ID: 20250612_151912
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
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess text by removing special characters, stopwords, and tokenizing.
    """
    if not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    
    return ' '.join(filtered_tokens)

def generate_word_cloud(text_data, title="Popular Topics"):
    """
    Generate and display a word cloud from text data.
    """
    # Combine all text data
    combined_text = ' '.join(text_data)
    
    # Generate word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords=STOPWORDS,
        max_words=100,
        colormap='viridis'
    ).generate(combined_text)
    
    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=20)
    plt.tight_layout()
    plt.show()

def get_top_words(text_data, n=20):
    """
    Get the top n most frequent words from text data.
    """
    combined_text = ' '.join(text_data)
    tokens = word_tokenize(combined_text.lower())
    filtered_tokens = [word for word in tokens if word not in STOPWORDS and len(word) > 2]
    
    word_counts = Counter(filtered_tokens)
    return word_counts.most_common(n)

def visualize_topics(csv_file, text_column='content'):
    """
    Main function to load data, preprocess, and visualize topics.
    """
    try:
        # Load data
        df = pd.read_csv(csv_file)
        
        # Check if text column exists
        if text_column not in df.columns:
            raise ValueError(f"Column '{text_column}' not found in the CSV file.")
        
        # Preprocess text
        df['processed_text'] = df[text_column].apply(preprocess_text)
        
        # Generate word cloud
        generate_word_cloud(df['processed_text'].tolist())
        
        # Print top words
        top_words = get_top_words(df['processed_text'].tolist())
        print("\nTop 20 Most Frequent Words:")
        for word, count in top_words:
            print(f"{word}: {count}")
            
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual CSV file path and column name
    csv_file = "anything_goes_posts.csv"
    text_column = "content"
    
    visualize_topics(csv_file, text_column)
```
