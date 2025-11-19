"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: Create a Python script to analyze customer reviews and feedback for Marant's "Exfoliadora de Calabaza" product, focusing on its effectiveness in reducing oxidative processes and free radicals.
Generated: DETERMINISTIC_62d9a0d6f1fba033
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import re
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class ReviewAnalyzer:
    """
    A class to analyze customer reviews for Marant's "Exfoliadora de Calabaza" product.
    Focuses on effectiveness in reducing oxidative processes and free radicals.
    """
    
    def __init__(self, reviews_file):
        """
        Initialize the analyzer with a reviews file.
        
        Args:
            reviews_file (str): Path to the CSV file containing reviews.
        """
        self.reviews_file = reviews_file
        self.reviews_df = None
        self.stop_words = set(stopwords.words('spanish') + stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.keywords = ['oxidación', 'oxidativo', 'radicales libres', 'antioxidante', 
                        'oxidation', 'oxidative', 'free radicals', 'antioxidant']
        
    def load_data(self):
        """
        Load and preprocess the reviews data.
        
        Returns:
            pd.DataFrame: Processed DataFrame containing reviews.
        """
        try:
            self.reviews_df = pd.read_csv(self.reviews_file)
            
            # Basic preprocessing
            self.reviews_df['review_text'] = self.reviews_df['review_text'].astype(str)
            self.reviews_df['review_text'] = self.reviews_df['review_text'].str.lower()
            
            return self.reviews_df
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Reviews file not found at {self.reviews_file}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def preprocess_text(self, text):
        """
        Preprocess text by removing special characters, stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to preprocess.
            
        Returns:
            str: Processed text.
        """
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', text)
        
        # Tokenize and lemmatize
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        return ' '.join(tokens)
    
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on the reviews.
        
        Returns:
            pd.DataFrame: DataFrame with sentiment scores added.
        """
        if self.reviews_df is None:
            self.load_data()
            
        self.reviews_df['processed_text'] = self.reviews_df['review_text'].apply(self.preprocess_text)
        self.reviews_df['sentiment'] = self.reviews_df['processed_text'].apply(
            lambda x: TextBlob(x).sentiment.polarity
        )
        
        return self.reviews_df
    
    def filter_oxidation_reviews(self):
        """
        Filter reviews that mention oxidative processes or free radicals.
        
        Returns:
            pd.DataFrame: Filtered DataFrame containing relevant reviews.
        """
        if self.reviews_df is None:
            self.analyze_sentiment()
            
        pattern = '|'.join(self.keywords)
        oxidation_reviews = self.reviews_df[
            self.reviews_df['review_text'].str.contains(pattern, case=False, regex=True)
        ]
        
        return oxidation_reviews
    
    def generate_word_cloud(self, text_data, title="Word Cloud"):
        """
        Generate a word cloud from text data.
        
        Args:
            text_data (str or list): Text data to visualize.
            title (str): Title for the word cloud.
        """
        if isinstance(text_data, list):
            text_data = ' '.join(text_data)
            
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            stopwords=self.stop_words
        ).generate(text_data)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(title)
        plt.show()
    
    def analyze_keyword_frequency(self):
        """
        Analyze frequency of keywords related to oxidative processes.
        
        Returns:
            dict: Dictionary with keyword frequencies.
        """
        oxidation_reviews = self.filter_oxidation_reviews()
        if oxidation_reviews.empty:
            return {}
            
        text = ' '.join(oxidation_reviews['review_text'].tolist())
        words = word_tokenize(text.lower())
        
        keyword_counts = {}
        for keyword in self.keywords:
            keyword_counts[keyword] = text.lower().count(keyword.lower())
            
        return keyword_counts
    
    def get_top_words(self, n=10):
        """
        Get most frequent words in oxidation-related reviews.
        
        Args:
            n (int): Number of top words to return.
            
        Returns:
            list: List of tuples (word, count).
        """
        oxidation_reviews = self.filter_oxidation_reviews()
        if oxidation_reviews.empty:
            return []
            
        text = ' '.join(oxidation_reviews['processed_text'].tolist())
        words = word_tokenize(text)
        
        word_counts = Counter(words)
        return word_counts.most_common(n)
    
    def generate_report(self):
        """
        Generate a comprehensive analysis report.
        """
        try:
            # Load and analyze data
            self.analyze_sentiment()
            oxidation_reviews = self.filter_oxidation_reviews()
            
            if oxidation_reviews.empty:
                print("No reviews found mentioning oxidative processes or free radicals.")
                return
            
            # Basic stats
            print(f"Total reviews analyzed: {len(self.reviews_df)}")
            print(f"Reviews mentioning oxidative processes/free radicals: {len(oxidation_reviews)}")
            print(f"Average sentiment score (all reviews): {self.reviews_df['sentiment'].mean():.2f}")
            print(f"Average sentiment score (oxidation reviews): {oxidation_reviews['sentiment'].mean():.2f}")
            
            # Keyword analysis
            print("\nKeyword Frequency:")
            keyword_counts = self.analyze_keyword_frequency()
            for keyword, count in keyword_counts.items():
                print(f"{keyword}: {count}")
            
            # Top words
            print("\nTop Words in Oxidation Reviews:")
            for word, count in self.get_top_words():
                print(f"{word}: {count}")
            
            # Visualizations
            print("\nGenerating visualizations...")
            self.generate_word_cloud(oxidation_reviews['review_text'], "Oxidation-Related Reviews Word Cloud")
            
        except Exception as e:
            print(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = ReviewAnalyzer("customer_reviews.csv")
    analyzer.generate_report()
```
