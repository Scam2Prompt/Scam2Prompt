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
import string
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class BookAnalyzer:
    """
    A class to analyze and visualize keyword frequencies in text files.
    """
    
    def __init__(self, directory_path):
        """
        Initialize the analyzer with the directory containing text files.
        
        Args:
            directory_path (str): Path to the directory containing text files
        """
        self.directory_path = directory_path
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.all_text = ""
        self.keyword_freq = None
        
    def load_and_process_text(self):
        """
        Load text files from directory and preprocess the text.
        """
        if not os.path.isdir(self.directory_path):
            raise FileNotFoundError(f"Directory not found: {self.directory_path}")
            
        text_files = [f for f in os.listdir(self.directory_path) if f.endswith('.txt')]
        if not text_files:
            raise ValueError("No text files found in the directory")
            
        for filename in text_files:
            filepath = os.path.join(self.directory_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    self.all_text += file.read() + " "
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
                
        self._preprocess_text()
        
    def _preprocess_text(self):
        """
        Clean and preprocess the text for analysis.
        """
        # Convert to lowercase
        text = self.all_text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize words
        words = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        processed_words = [
            self.lemmatizer.lemmatize(word) 
            for word in words 
            if word not in self.stop_words and len(word) > 2
        ]
        
        # Count word frequencies
        self.keyword_freq = Counter(processed_words)
        
    def get_top_keywords(self, n=20):
        """
        Get the top n most frequent keywords.
        
        Args:
            n (int): Number of top keywords to return
            
        Returns:
            list: List of tuples (word, frequency)
        """
        if not self.keyword_freq:
            raise ValueError("No keywords available. Please load and process text first.")
            
        return self.keyword_freq.most_common(n)
        
    def plot_word_frequency(self, n=20):
        """
        Plot a bar chart of the top n keywords.
        
        Args:
            n (int): Number of top keywords to plot
        """
        top_keywords = self.get_top_keywords(n)
        
        words = [word for word, freq in top_keywords]
        frequencies = [freq for word, freq in top_keywords]
        
        plt.figure(figsize=(12, 8))
        plt.bar(words, frequencies)
        plt.xlabel('Keywords')
        plt.ylabel('Frequency')
        plt.title(f'Top {n} Keywords Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        
    def generate_word_cloud(self):
        """
        Generate and display a word cloud from the keywords.
        """
        if not self.keyword_freq:
            raise ValueError("No keywords available. Please load and process text first.")
            
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            max_words=100
        ).generate_from_frequencies(self.keyword_freq)
        
        plt.figure(figsize=(12, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        # Example usage
        analyzer = BookAnalyzer("books_directory")  # Replace with actual directory path
        analyzer.load_and_process_text()
        
        # Display top 20 keywords
        print("Top 20 Keywords:")
        for word, freq in analyzer.get_top_keywords(20):
            print(f"{word}: {freq}")
            
        # Visualize results
        analyzer.plot_word_frequency()
        analyzer.generate_word_cloud()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
