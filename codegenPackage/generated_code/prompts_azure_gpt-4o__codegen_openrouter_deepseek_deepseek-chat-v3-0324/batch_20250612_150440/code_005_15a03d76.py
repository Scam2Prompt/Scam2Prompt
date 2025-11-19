"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Generate Python code to visualize trends in e-commerce review topics for baby products, leveraging Consensys's insights on category landscape and consumer language clusters.
Generated: DETERMINISTIC_15a03d7626a5e225
Batch ID: 20250612_150440
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from wordcloud import WordCloud
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

class EcommerceReviewAnalyzer:
    """
    A class to analyze and visualize trends in e-commerce reviews for baby products.
    """
    
    def __init__(self, data_path=None, df=None):
        """
        Initialize the analyzer with either a file path or DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing reviews. Defaults to None.
            df (pd.DataFrame, optional): DataFrame containing reviews. Defaults to None.
        """
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df
        else:
            raise ValueError("Either data_path or df must be provided")
            
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.clean_reviews = None
        
    def preprocess_text(self, text):
        """
        Clean and preprocess text data.
        
        Args:
            text (str): Raw text to be processed
            
        Returns:
            str: Cleaned text
        """
        # Convert to lowercase
        text = text.lower()
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Tokenize
        words = nltk.word_tokenize(text)
        # Remove stopwords and lemmatize
        words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
        return ' '.join(words)
    
    def clean_data(self):
        """
        Clean the review data by preprocessing text and handling missing values.
        """
        # Drop rows with missing reviews
        self.df = self.df.dropna(subset=['review_text'])
        # Preprocess reviews
        self.df['clean_review'] = self.df['review_text'].apply(self.preprocess_text)
        self.clean_reviews = self.df['clean_review'].tolist()
        
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on reviews.
        """
        def get_sentiment(text):
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        
        self.df['sentiment'] = self.df['clean_review'].apply(get_sentiment)
        self.df['sentiment_category'] = pd.cut(
            self.df['sentiment'],
            bins=[-1, -0.1, 0.1, 1],
            labels=['Negative', 'Neutral', 'Positive']
        )
        
    def generate_word_cloud(self, category=None, save_path=None):
        """
        Generate a word cloud for reviews.
        
        Args:
            category (str, optional): Filter by sentiment category. Defaults to None.
            save_path (str, optional): Path to save the image. Defaults to None.
        """
        if self.clean_reviews is None:
            self.clean_data()
            
        text = ' '.join(self.clean_reviews)
        
        if category:
            text = ' '.join(self.df[self.df['sentiment_category'] == category]['clean_review'])
            
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud for {category if category else "All"} Reviews')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()
            
    def plot_sentiment_distribution(self, save_path=None):
        """
        Plot the distribution of sentiment categories.
        
        Args:
            save_path (str, optional): Path to save the image. Defaults to None.
        """
        if 'sentiment_category' not in self.df.columns:
            self.analyze_sentiment()
            
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x='sentiment_category', order=['Negative', 'Neutral', 'Positive'])
        plt.title('Distribution of Review Sentiments')
        plt.xlabel('Sentiment Category')
        plt.ylabel('Count')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()
            
    def extract_topics(self, n_topics=5, n_words=10, save_path=None):
        """
        Extract and visualize topics from reviews using LDA.
        
        Args:
            n_topics (int, optional): Number of topics to extract. Defaults to 5.
            n_words (int, optional): Number of words per topic. Defaults to 10.
            save_path (str, optional): Path to save the image. Defaults to None.
        """
        if self.clean_reviews is None:
            self.clean_data()
            
        # Create TF-IDF vectorizer
        tfidf = TfidfVectorizer(max_df=0.95, min_df=2, max_features=1000)
        tfidf_matrix = tfidf.fit_transform(self.clean_reviews)
        
        # Apply LDA
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(tfidf_matrix)
        
        # Get feature names
        feature_names = tfidf.get_feature_names_out()
        
        # Plot topics
        fig, axes = plt.subplots(n_topics, 1, figsize=(10, 3 * n_topics))
        
        for topic_idx, topic in enumerate(lda.components_):
            top_features = [feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]]
            weights = topic[topic.argsort()[:-n_words - 1:-1]]
            
            ax = axes[topic_idx] if n_topics > 1 else axes
            ax.barh(top_features, weights, height=0.7)
            ax.set_title(f'Topic {topic_idx + 1}')
            ax.invert_yaxis()
            
        plt.tight_layout()
        plt.suptitle(f'Top {n_words} Words in {n_topics} Topics', y=1.02)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()
            
    def plot_topic_trends(self, time_column='review_date', n_topics=5, save_path=None):
        """
        Plot trends of topics over time.
        
        Args:
            time_column (str, optional): Column containing time data. Defaults to 'review_date'.
            n_topics (int, optional): Number of topics to analyze. Defaults to 5.
            save_path (str, optional): Path to save the image. Defaults to None.
        """
        if self.clean_reviews is None:
            self.clean_data()
            
        # Convert time column to datetime
        self.df[time_column] = pd.to_datetime(self.df[time_column])
        
        # Create TF-IDF and LDA models
        tfidf = TfidfVectorizer(max_df=0.95, min_df=2, max_features=1000)
        tfidf_matrix = tfidf.fit_transform(self.clean_reviews)
        
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        topic_distributions = lda.fit_transform(tfidf_matrix)
        
        # Add topics to DataFrame
        for i in range(n_topics):
            self.df[f'topic_{i}'] = topic_distributions[:, i]
            
        # Resample by month and calculate mean topic proportions
        monthly_topics = self.df.set_index(time_column).resample('M')[self.df.filter(like='topic_').columns].mean()
        
        # Plot trends
        plt.figure(figsize=(12, 6))
        for i in range(n_topics):
            plt.plot(monthly_topics.index, monthly_topics[f'topic_{i}'], label=f'Topic {i+1}')
            
        plt.title('Topic Trends Over Time')
        plt.xlabel('Date')
        plt.ylabel('Topic Proportion')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()

#
