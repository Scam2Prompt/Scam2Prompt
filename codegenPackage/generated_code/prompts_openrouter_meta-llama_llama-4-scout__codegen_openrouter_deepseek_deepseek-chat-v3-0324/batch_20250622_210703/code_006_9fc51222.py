"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Write a script to analyze customer reviews and ratings for a tire and wheel services company, using natural language processing techniques to identify common feedback themes.
Generated: DETERMINISTIC_9fc512220d3f5364
Batch ID: 20250622_210703
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
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class ReviewAnalyzer:
    """
    A class to analyze customer reviews for tire and wheel services using NLP techniques.
    """
    
    def __init__(self, file_path):
        """
        Initialize the analyzer with the path to the review data.
        
        Args:
            file_path (str): Path to the CSV file containing reviews
        """
        self.file_path = file_path
        self.reviews_df = None
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.custom_stopwords = {'service', 'tire', 'wheel', 'car', 'vehicle', 'shop', 'store'}
        
    def load_data(self):
        """
        Load and preprocess the review data.
        """
        try:
            self.reviews_df = pd.read_csv(self.file_path)
            # Basic data validation
            required_columns = {'review_text', 'rating'}
            if not required_columns.issubset(self.reviews_df.columns):
                raise ValueError("CSV must contain 'review_text' and 'rating' columns")
                
            # Clean text data
            self.reviews_df['cleaned_text'] = self.reviews_df['review_text'].apply(self._clean_text)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {self.file_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _clean_text(self, text):
        """
        Clean and preprocess text.
        
        Args:
            text (str): Raw text to clean
            
        Returns:
            str: Cleaned text
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
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens 
                 if word not in self.stop_words and word not in self.custom_stopwords]
        return ' '.join(tokens)
    
    def analyze_ratings(self):
        """
        Analyze rating distribution.
        
        Returns:
            dict: Summary statistics of ratings
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        rating_stats = {
            'average': np.mean(self.reviews_df['rating']),
            'median': np.median(self.reviews_df['rating']),
            'min': np.min(self.reviews_df['rating']),
            'max': np.max(self.reviews_df['rating']),
            'std_dev': np.std(self.reviews_df['rating'])
        }
        return rating_stats
    
    def generate_word_cloud(self, save_path=None):
        """
        Generate a word cloud from reviews.
        
        Args:
            save_path (str, optional): Path to save the word cloud image
            
        Returns:
            matplotlib figure: Word cloud visualization
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        all_text = ' '.join(self.reviews_df['cleaned_text'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            
        return plt.gcf()
    
    def identify_topics(self, num_topics=5, num_words=10):
        """
        Identify common themes using LDA topic modeling.
        
        Args:
            num_topics (int): Number of topics to identify
            num_words (int): Number of words to show per topic
            
        Returns:
            list: List of topics with their top words
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Vectorize text using TF-IDF
        vectorizer = TfidfVectorizer(max_features=1000)
        X = vectorizer.fit_transform(self.reviews_df['cleaned_text'])
        
        # Apply LDA
        lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
        lda.fit(X)
        
        # Get top words for each topic
        feature_names = vectorizer.get_feature_names_out()
        topics = []
        
        for topic_idx, topic in enumerate(lda.components_):
            top_words_idx = topic.argsort()[-num_words:][::-1]
            top_words = [feature_names[i] for i in top_words_idx]
            topics.append({
                'topic_id': topic_idx,
                'top_words': top_words,
                'word_weights': topic[top_words_idx].tolist()
            })
            
        return topics
    
    def get_common_phrases(self, n=10, min_phrase_length=2):
        """
        Get most common phrases in reviews.
        
        Args:
            n (int): Number of phrases to return
            min_phrase_length (int): Minimum words in a phrase
            
        Returns:
            list: Most common phrases with counts
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        phrases = []
        for text in self.reviews_df['cleaned_text']:
            words = text.split()
            for i in range(len(words) - min_phrase_length + 1):
                phrase = ' '.join(words[i:i+min_phrase_length])
                phrases.append(phrase)
                
        phrase_counts = Counter(phrases)
        return phrase_counts.most_common(n)
    
    def analyze_sentiment_by_rating(self):
        """
        Analyze sentiment correlation with ratings.
        
        Returns:
            dict: Sentiment analysis results
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Simple sentiment analysis based on positive/negative words
        positive_words = ['great', 'excellent', 'good', 'awesome', 'fantastic', 'perfect']
        negative_words = ['bad', 'poor', 'terrible', 'awful', 'horrible', 'disappointed']
        
        results = []
        for _, row in self.reviews_df.iterrows():
            text = row['cleaned_text']
            pos_count = sum(1 for word in text.split() if word in positive_words)
            neg_count = sum(1 for word in text.split() if word in negative_words)
            sentiment = 'neutral'
            if pos_count > neg_count:
                sentiment = 'positive'
            elif neg_count > pos_count:
                sentiment = 'negative'
                
            results.append({
                'rating': row['rating'],
                'sentiment': sentiment,
                'positive_words': pos_count,
                'negative_words': neg_count
            })
            
        return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ReviewAnalyzer('tire_reviews.csv')
        analyzer.load_data()
        
        # Get rating statistics
        rating_stats = analyzer.analyze_ratings()
        print("Rating Statistics:", rating_stats)
        
        # Generate word cloud
        analyzer.generate_word_cloud('wordcloud.png')
        
        # Identify topics
        topics = analyzer.identify_topics()
        print("\nIdentified Topics:")
        for topic in topics:
            print(f"Topic {topic['topic_id']}: {', '.join(topic['top_words'])}")
            
        # Get common phrases
        common_phrases = analyzer.get_common_phrases()
        print("\nCommon Phrases:", common_phrases)
        
        # Analyze sentiment
        sentiment_results = analyzer.analyze_sentiment_by_rating()
        print("\nSentiment Analysis:")
        print(sentiment_results.groupby(['rating', 'sentiment']).size().unstack())
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
