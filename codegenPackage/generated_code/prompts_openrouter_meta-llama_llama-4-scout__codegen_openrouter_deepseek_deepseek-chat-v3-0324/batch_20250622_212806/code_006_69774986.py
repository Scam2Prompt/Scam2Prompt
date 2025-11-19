"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: "Write a Python script to analyze customer testimonials and feedback for an insurance company like GTempus, using natural language processing techniques to identify common themes and sentiment patterns."
Generated: DETERMINISTIC_6977498640ec57de
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TestimonialAnalyzer:
    """
    A class to analyze customer testimonials using NLP techniques.
    """
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.custom_stopwords = {'gtempus', 'insurance', 'company', 'like', 'would', 'get'}
    
    def preprocess_text(self, text):
        """
        Clean and preprocess text data.
        """
        if not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        processed_tokens = [
            self.lemmatizer.lemmatize(token) 
            for token in tokens 
            if token not in self.stop_words and token not in self.custom_stopwords and len(token) > 2
        ]
        
        return ' '.join(processed_tokens)
    
    def analyze_sentiment(self, text):
        """
        Perform sentiment analysis on text.
        Returns polarity and subjectivity scores.
        """
        analysis = TextBlob(text)
        return {
            'polarity': analysis.sentiment.polarity,
            'subjectivity': analysis.sentiment.subjectivity
        }
    
    def categorize_sentiment(self, polarity_score):
        """
        Categorize sentiment based on polarity score.
        """
        if polarity_score > 0.1:
            return 'Positive'
        elif polarity_score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'
    
    def get_top_keywords(self, texts, n=10):
        """
        Extract top n keywords from texts.
        """
        all_words = ' '.join(texts).split()
        word_counts = Counter(all_words)
        return word_counts.most_common(n)
    
    def generate_wordcloud(self, texts, filename='wordcloud.png'):
        """
        Generate and save a word cloud from texts.
        """
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(texts))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
    
    def analyze_testimonials(self, data_path, output_dir='output'):
        """
        Main analysis pipeline for customer testimonials.
        """
        try:
            # Load data
            df = pd.read_csv(data_path)
            
            # Check required columns
            if 'testimonial' not in df.columns:
                raise ValueError("Input data must contain a 'testimonial' column")
            
            # Preprocess text
            df['processed_text'] = df['testimonial'].apply(self.preprocess_text)
            
            # Sentiment analysis
            sentiment_results = df['processed_text'].apply(self.analyze_sentiment).apply(pd.Series)
            df = pd.concat([df, sentiment_results], axis=1)
            df['sentiment_category'] = df['polarity'].apply(self.categorize_sentiment)
            
            # Generate visualizations
            os.makedirs(output_dir, exist_ok=True)
            
            # Sentiment distribution
            plt.figure(figsize=(8, 6))
            sns.countplot(data=df, x='sentiment_category', order=['Positive', 'Neutral', 'Negative'])
            plt.title('Customer Sentiment Distribution')
            plt.savefig(f'{output_dir}/sentiment_distribution.png')
            plt.close()
            
            # Polarity distribution
            plt.figure(figsize=(8, 6))
            sns.histplot(data=df, x='polarity', bins=20, kde=True)
            plt.title('Sentiment Polarity Distribution')
            plt.savefig(f'{output_dir}/polarity_distribution.png')
            plt.close()
            
            # Top keywords
            top_keywords = self.get_top_keywords(df['processed_text'].tolist())
            keywords_df = pd.DataFrame(top_keywords, columns=['Keyword', 'Count'])
            keywords_df.to_csv(f'{output_dir}/top_keywords.csv', index=False)
            
            # Word cloud
            self.generate_wordcloud(df['processed_text'].tolist(), f'{output_dir}/wordcloud.png')
            
            # Save processed data
            df.to_csv(f'{output_dir}/processed_testimonials.csv', index=False)
            
            return {
                'status': 'success',
                'message': f'Analysis completed. Results saved in {output_dir}',
                'sentiment_distribution': df['sentiment_category'].value_counts().to_dict(),
                'average_polarity': df['polarity'].mean(),
                'average_subjectivity': df['subjectivity'].mean(),
                'top_keywords': dict(top_keywords)
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

# Example usage
if __name__ == "__main__":
    import os
    
    analyzer = TestimonialAnalyzer()
    
    # Example with sample data (replace with actual data path)
    sample_data = {
        'testimonial': [
            "GTempus provided excellent service during my claim process.",
            "The premium rates are too high compared to competitors.",
            "Average experience, nothing special.",
            "Very responsive customer support team!",
            "I had issues with claim settlement."
        ]
    }
    
    # Create sample CSV if it doesn't exist
    if not os.path.exists('sample_testimonials.csv'):
        pd.DataFrame(sample_data).to_csv('sample_testimonials.csv', index=False)
    
    # Run analysis
    results = analyzer.analyze_testimonials('sample_testimonials.csv')
    print(results)
```
