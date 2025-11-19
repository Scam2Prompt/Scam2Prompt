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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class KeywordAnalyzer:
    """
    A class to analyze and visualize keyword frequencies in resource titles.
    """
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.custom_stopwords = {'metis', 'data', 'science', 'learning', 'machine', 'ai', 'artificial', 'intelligence'}
        
    def preprocess_text(self, text):
        """
        Clean and preprocess text by:
        1. Lowercasing
        2. Removing special characters
        3. Tokenizing
        4. Removing stopwords
        5. Lemmatizing
        """
        try:
            # Lowercase and remove special characters
            text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
            
            # Tokenize
            tokens = word_tokenize(text)
            
            # Remove stopwords and custom stopwords
            tokens = [word for word in tokens if word not in self.stop_words and word not in self.custom_stopwords]
            
            # Lemmatize
            tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
            
            return ' '.join(tokens)
        except Exception as e:
            print(f"Error preprocessing text: {e}")
            return ""
    
    def analyze_keywords(self, titles):
        """
        Analyze keyword frequencies from a list of titles.
        Returns a DataFrame with keywords and their counts.
        """
        try:
            # Preprocess all titles
            processed_titles = [self.preprocess_text(title) for title in titles]
            
            # Vectorize the text
            vectorizer = CountVectorizer(ngram_range=(1, 2), max_features=50)
            X = vectorizer.fit_transform(processed_titles)
            
            # Get feature names and counts
            feature_names = vectorizer.get_feature_names_out()
            counts = np.asarray(X.sum(axis=0)).ravel()
            
            # Create DataFrame
            df = pd.DataFrame({
                'keyword': feature_names,
                'count': counts
            }).sort_values('count', ascending=False)
            
            return df
        except Exception as e:
            print(f"Error analyzing keywords: {e}")
            return pd.DataFrame()
    
    def visualize_keywords(self, keyword_df, top_n=20):
        """
        Visualize the top N keywords using a horizontal bar chart.
        """
        try:
            if keyword_df.empty:
                print("No data to visualize.")
                return
            
            plt.figure(figsize=(10, 8))
            sns.barplot(
                x='count',
                y='keyword',
                data=keyword_df.head(top_n),
                palette='viridis'
            )
            plt.title(f'Top {top_n} Keywords in Resource Titles')
            plt.xlabel('Frequency')
            plt.ylabel('Keyword')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing keywords: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data (replace with actual Metis resource titles)
    sample_titles = [
        "Introduction to Data Science",
        "Machine Learning Fundamentals",
        "Deep Learning for Computer Vision",
        "Natural Language Processing Techniques",
        "The Future of AI in Healthcare",
        "Data Visualization Best Practices",
        "Python for Data Analysis",
        "Statistics for Machine Learning",
        "Building Recommender Systems",
        "Time Series Forecasting Methods"
    ]
    
    analyzer = KeywordAnalyzer()
    keyword_df = analyzer.analyze_keywords(sample_titles)
    
    if not keyword_df.empty:
        print("Top Keywords:")
        print(keyword_df.head(20))
        analyzer.visualize_keywords(keyword_df)
    else:
        print("Keyword analysis failed.")
```
