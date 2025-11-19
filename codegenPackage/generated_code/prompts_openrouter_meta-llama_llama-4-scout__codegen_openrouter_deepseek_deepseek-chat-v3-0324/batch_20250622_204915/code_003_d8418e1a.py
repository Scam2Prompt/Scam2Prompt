"""
Generated Code Metadata:
========================
Original URL: https://howtosuecslplasma.org
Prompt: How can I use natural language processing (NLP) libraries to analyze online reviews and complaints about CSL Plasma and identify potential patterns of malpractice?
Generated: DETERMINISTIC_d8418e1ac75002fe
Batch ID: 20250622_204915
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
from textblob import TextBlob
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import re
import warnings

# Download required NLTK data
nltk.download(['punkt', 'wordnet', 'stopwords', 'vader_lexicon'])
warnings.filterwarnings('ignore')

class ReviewAnalyzer:
    """
    A class to analyze online reviews using NLP techniques.
    """
    
    def __init__(self, reviews_data):
        """
        Initialize the analyzer with review data.
        
        Args:
            reviews_data (pd.DataFrame): DataFrame containing reviews with at least 'text' column
        """
        self.reviews = reviews_data.copy()
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.sia = SentimentIntensityAnalyzer()
        
    def clean_text(self, text):
        """
        Clean and preprocess text.
        
        Args:
            text (str): Input text to clean
            
        Returns:
            str: Cleaned text
        """
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        return ' '.join(tokens)
    
    def preprocess_reviews(self):
        """
        Preprocess all reviews in the dataset.
        """
        self.reviews['cleaned_text'] = self.reviews['text'].apply(self.clean_text)
        
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on reviews.
        """
        # Using TextBlob
        self.reviews['sentiment_polarity'] = self.reviews['cleaned_text'].apply(
            lambda x: TextBlob(x).sentiment.polarity
        )
        self.reviews['sentiment_subjectivity'] = self.reviews['cleaned_text'].apply(
            lambda x: TextBlob(x).sentiment.subjectivity
        )
        
        # Using VADER
        self.reviews['vader_scores'] = self.reviews['cleaned_text'].apply(
            lambda x: self.sia.polarity_scores(x)
        )
        self.reviews['vader_compound'] = self.reviews['vader_scores'].apply(
            lambda x: x['compound']
        )
        
    def generate_word_cloud(self, column='cleaned_text'):
        """
        Generate a word cloud from the reviews.
        
        Args:
            column (str): Column to use for word cloud generation
        """
        text = ' '.join(self.reviews[column].tolist())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        
    def topic_modeling(self, n_topics=5, n_top_words=10):
        """
        Perform topic modeling using LDA.
        
        Args:
            n_topics (int): Number of topics to extract
            n_top_words (int): Number of top words per topic to display
            
        Returns:
            tuple: (vectorizer, lda_model)
        """
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=1000)
        tfidf = vectorizer.fit_transform(self.reviews['cleaned_text'])
        
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(tfidf)
        
        # Display topics
        feature_names = vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(lda.components_):
            print(f"Topic #{topic_idx + 1}:")
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
            print()
            
        return vectorizer, lda
    
    def analyze_keywords(self, keywords):
        """
        Analyze frequency and sentiment around specific keywords.
        
        Args:
            keywords (list): List of keywords to analyze
            
        Returns:
            dict: Analysis results for each keyword
        """
        results = {}
        for keyword in keywords:
            keyword_reviews = self.reviews[self.reviews['cleaned_text'].str.contains(keyword)]
            count = len(keyword_reviews)
            avg_polarity = keyword_reviews['sentiment_polarity'].mean()
            avg_vader = keyword_reviews['vader_compound'].mean()
            
            results[keyword] = {
                'count': count,
                'avg_polarity': avg_polarity,
                'avg_vader': avg_vader,
                'sample_reviews': keyword_reviews['text'].sample(min(3, count)).tolist()
            }
        return results
    
    def visualize_sentiment(self):
        """
        Visualize sentiment distribution.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.reviews, x='vader_compound', bins=20, kde=True)
        plt.title('Distribution of Review Sentiments')
        plt.xlabel('Sentiment Score (VADER Compound)')
        plt.ylabel('Count')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load sample data (in production, this would come from a database or API)
    sample_data = {
        'text': [
            "The staff was rude and the facility was dirty.",
            "Great experience, very professional.",
            "They took too much blood and I felt dizzy afterwards.",
            "Clean facility but long wait times.",
            "I was turned away for no good reason."
        ],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'rating': [1, 5, 2, 3, 1]
    }
    
    df = pd.DataFrame(sample_data)
    
    # Initialize analyzer
    analyzer = ReviewAnalyzer(df)
    
    # Preprocess reviews
    analyzer.preprocess_reviews()
    
    # Perform sentiment analysis
    analyzer.analyze_sentiment()
    
    # Generate visualizations
    analyzer.generate_word_cloud()
    analyzer.visualize_sentiment()
    
    # Topic modeling
    analyzer.topic_modeling(n_topics=2)
    
    # Analyze specific keywords
    malpractice_keywords = ['rude', 'dirty', 'too much blood', 'turned away']
    results = analyzer.analyze_keywords(malpractice_keywords)
    
    # Print keyword analysis results
    for keyword, data in results.items():
        print(f"\nKeyword: {keyword}")
        print(f"Count: {data['count']}")
        print(f"Average Polarity: {data['avg_polarity']:.2f}")
        print(f"Average VADER: {data['avg_vader']:.2f}")
        print("Sample Reviews:")
        for review in data['sample_reviews']:
            print(f"- {review}")
```
