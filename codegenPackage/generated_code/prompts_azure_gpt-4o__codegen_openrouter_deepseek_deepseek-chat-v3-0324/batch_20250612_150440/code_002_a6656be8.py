"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Create a script to perform category-specific deep dives into e-commerce reviews using machine learning techniques, as outlined in Consensys's Explorer service, to identify drivers and drainers of ratings.
Generated: DETERMINISTIC_a6656be824dac666
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class ReviewAnalyzer:
    """
    A class to perform category-specific deep dives into e-commerce reviews
    using machine learning techniques to identify drivers and drainers of ratings.
    """
    
    def __init__(self, data_path, category_column='category', review_column='review', rating_column='rating'):
        """
        Initialize the ReviewAnalyzer with data path and column names.
        
        Args:
            data_path (str): Path to the CSV file containing reviews data
            category_column (str): Name of the column containing categories
            review_column (str): Name of the column containing review text
            rating_column (str): Name of the column containing ratings
        """
        self.data_path = data_path
        self.category_column = category_column
        self.review_column = review_column
        self.rating_column = rating_column
        self.data = None
        self.vectorizer = None
        self.lda_model = None
        self.classifier = None
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
    def load_data(self):
        """Load and preprocess the review data."""
        try:
            self.data = pd.read_csv(self.data_path)
            # Basic data validation
            if not all(col in self.data.columns for col in [self.category_column, self.review_column, self.rating_column]):
                raise ValueError("Required columns not found in the data")
            # Drop rows with missing values
            self.data = self.data.dropna(subset=[self.category_column, self.review_column, self.rating_column])
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def preprocess_text(self, text):
        """
        Preprocess text by removing special characters, stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            str: Preprocessed text
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
    
    def analyze_sentiment(self):
        """Add sentiment analysis columns to the data."""
        def get_sentiment(text):
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        
        self.data['sentiment'] = self.data[self.review_column].apply(get_sentiment)
        self.data['sentiment_label'] = self.data['sentiment'].apply(
            lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral'
        )
    
    def extract_topics(self, n_topics=5, max_features=1000):
        """
        Extract topics from reviews using LDA.
        
        Args:
            n_topics (int): Number of topics to extract
            max_features (int): Maximum number of features for vectorizer
        """
        # Preprocess all reviews
        processed_reviews = self.data[self.review_column].apply(self.preprocess_text)
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
        tfidf_matrix = self.vectorizer.fit_transform(processed_reviews)
        
        # Apply LDA
        self.lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda_output = self.lda_model.fit_transform(tfidf_matrix)
        
        # Add topic probabilities to data
        for i in range(n_topics):
            self.data[f'topic_{i}'] = lda_output[:, i]
        
        # Get top words for each topic
        self.topic_words = {}
        feature_names = self.vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(self.lda_model.components_):
            top_words_idx = topic.argsort()[-10:][::-1]
            top_words = [feature_names[i] for i in top_words_idx]
            self.topic_words[f'topic_{topic_idx}'] = top_words
    
    def train_rating_classifier(self, test_size=0.2, random_state=42):
        """
        Train a classifier to predict ratings based on review topics and sentiment.
        
        Args:
            test_size (float): Proportion of data to use for testing
            random_state (int): Random seed for reproducibility
        """
        # Prepare features and target
        topic_cols = [col for col in self.data.columns if col.startswith('topic_')]
        X = self.data[topic_cols + ['sentiment']]
        y = self.data[self.rating_column].apply(lambda x: 1 if x >= 4 else 0)  # Binary classification (high/low rating)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        # Train classifier
        self.classifier = RandomForestClassifier(random_state=random_state)
        self.classifier.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.classifier.predict(X_test)
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        print("\nConfusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
    
    def analyze_category(self, category):
        """
        Perform deep dive analysis for a specific category.
        
        Args:
            category (str): Category to analyze
        """
        if category not in self.data[self.category_column].unique():
            print(f"Category '{category}' not found in data")
            return
        
        category_data = self.data[self.data[self.category_column] == category]
        
        # Rating distribution
        plt.figure(figsize=(10, 6))
        sns.countplot(x=self.rating_column, data=category_data)
        plt.title(f'Rating Distribution for {category}')
        plt.show()
        
        # Sentiment distribution
        plt.figure(figsize=(10, 6))
        sns.countplot(x='sentiment_label', data=category_data)
        plt.title(f'Sentiment Distribution for {category}')
        plt.show()
        
        # Topic importance
        topic_cols = [col for col in category_data.columns if col.startswith('topic_')]
        topic_means = category_data[topic_cols].mean().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        topic_means.plot(kind='bar')
        plt.title(f'Average Topic Probabilities for {category}')
        plt.ylabel('Probability')
        plt.show()
        
        # Print top words for important topics
        print("\nTop Words for Important Topics:")
        for topic in topic_means.index[:3]:
            print(f"\n{topic}: {self.topic_words[topic]}")
    
    def get_drivers_drainers(self, category, top_n=3):
        """
        Identify top drivers and drainers for a category.
        
        Args:
            category (str): Category to analyze
            top_n (int): Number of drivers/drainers to return
            
        Returns:
            tuple: (drivers, drainers) - lists of top features
        """
        if category not in self.data[self.category_column].unique():
            print(f"Category '{category}' not found in data")
            return None, None
        
        category_data = self.data[self.data[self.category_column] == category]
        
        # Separate high and low ratings
        high_ratings = category_data[category_data[self.rating_column] >= 4]
        low_ratings = category_data[category_data[self.rating_column] < 3]
        
        # Get mean topic probabilities for each group
        topic_cols = [col for col in category_data.columns if col.startswith('topic_')]
        high_means = high_ratings[topic_cols].mean()
        low_means = low_ratings[topic_cols].mean()
        
        # Calculate difference between high and low ratings
        topic_diff = high_means - low_means
        
        # Get drivers (topics
