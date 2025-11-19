"""
Generated Code Metadata:
========================
Original URL: https://rewards-steth.com
Prompt: Suggest a method to analyze trends in user discussions from the "자유게시판" section using natural language processing (NLP).
Generated: DETERMINISTIC_ae57d93eeaa86776
Batch ID: 20250612_153527
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
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
import re
import warnings
warnings.filterwarnings('ignore')

class DiscussionAnalyzer:
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path
        """
        self.data_path = data_path
        self.okt = Okt()
        self.stopwords = ['은', '는', '이', '가', '을', '를', '에', '에서', '의', '과', '와', '으로', '하다', '하다가', '하지만', '그리고', '그러나']
        
    def load_data(self):
        """
        Load discussion data from CSV file
        Expected columns: 'post_id', 'title', 'content', 'date', 'author'
        """
        try:
            self.df = pd.read_csv(self.data_path)
            self.df['text'] = self.df['title'] + ' ' + self.df['content']
            self.df['date'] = pd.to_datetime(self.df['date'])
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def preprocess_text(self, text):
        """
        Clean and tokenize Korean text
        """
        # Remove special characters and numbers
        text = re.sub(r'[^가-힣\s]', '', text)
        # Tokenize and remove stopwords
        tokens = self.okt.morphs(text, stem=True)
        tokens = [token for token in tokens if token not in self.stopwords and len(token) > 1]
        return ' '.join(tokens)
    
    def analyze_word_frequency(self, top_n=20):
        """
        Analyze word frequency and generate word cloud
        """
        if not hasattr(self, 'df'):
            print("Data not loaded. Call load_data() first.")
            return None
        
        self.df['processed_text'] = self.df['text'].apply(self.preprocess_text)
        all_words = ' '.join(self.df['processed_text']).split()
        word_counts = Counter(all_words)
        
        # Generate word cloud
        wordcloud = WordCloud(font_path='malgun.ttf', 
                            width=800, 
                            height=400, 
                            background_color='white').generate_from_frequencies(word_counts)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        
        return word_counts.most_common(top_n)
    
    def analyze_temporal_trends(self, time_period='M'):
        """
        Analyze trends over time (daily, weekly, monthly)
        """
        if not hasattr(self, 'df'):
            print("Data not loaded. Call load_data() first.")
            return None
        
        temporal_df = self.df.copy()
        temporal_df.set_index('date', inplace=True)
        temporal_df = temporal_df.resample(time_period).size()
        
        plt.figure(figsize=(12, 6))
        temporal_df.plot(kind='line', marker='o')
        plt.title(f'Discussion Activity Over Time ({time_period})')
        plt.xlabel('Date')
        plt.ylabel('Number of Posts')
        plt.grid(True)
        plt.show()
        
        return temporal_df
    
    def analyze_topics(self, n_topics=5, n_words=5):
        """
        Perform topic modeling using LDA
        """
        if not hasattr(self, 'df'):
            print("Data not loaded. Call load_data() first.")
            return None
        
        if 'processed_text' not in self.df.columns:
            self.df['processed_text'] = self.df['text'].apply(self.preprocess_text)
        
        # Create TF-IDF matrix
        tfidf = TfidfVectorizer(max_df=0.95, min_df=2)
        tfidf_matrix = tfidf.fit_transform(self.df['processed_text'])
        
        # Perform LDA
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(tfidf_matrix)
        
        # Display topics
        feature_names = tfidf.get_feature_names_out()
        topics = []
        
        for topic_idx, topic in enumerate(lda.components_):
            top_features = [feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]]
            topics.append((f"Topic {topic_idx + 1}", top_features))
        
        return topics
    
    def analyze_sentiment_trends(self):
        """
        Basic sentiment analysis (positive/negative) based on sentiment words
        """
        if not hasattr(self, 'df'):
            print("Data not loaded. Call load_data() first.")
            return None
        
        # Simple sentiment dictionary (in practice, use a more comprehensive one)
        positive_words = ['좋다', '행복', '감사', '사랑', '기쁘다']
        negative_words = ['나쁘다', '슬프다', '화나다', '실망', '아쉽다']
        
        self.df['sentiment'] = self.df['processed_text'].apply(
            lambda x: 'positive' if any(word in x for word in positive_words) 
                     else ('negative' if any(word in x for word in negative_words) 
                           else 'neutral')
        )
        
        sentiment_counts = self.df['sentiment'].value_counts(normalize=True)
        
        plt.figure(figsize=(8, 6))
        sentiment_counts.plot(kind='bar')
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Percentage')
        plt.show()
        
        return sentiment_counts
    
    def cluster_discussions(self, n_clusters=5):
        """
        Cluster discussions using K-means
        """
        if not hasattr(self, 'df'):
            print("Data not loaded. Call load_data() first.")
            return None
        
        if 'processed_text' not in self.df.columns:
            self.df['processed_text'] = self.df['text'].apply(self.preprocess_text)
        
        tfidf = TfidfVectorizer(max_df=0.95, min_df=2)
        tfidf_matrix = tfidf.fit_transform(self.df['processed_text'])
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(tfidf_matrix)
        
        self.df['cluster'] = clusters
        
        # Get top words per cluster
        cluster_top_words = {}
        for i in range(n_clusters):
            cluster_texts = self.df[self.df['cluster'] == i]['processed_text']
            all_words = ' '.join(cluster_texts).split()
            word_counts = Counter(all_words)
            cluster_top_words[f'Cluster {i}'] = word_counts.most_common(10)
        
        return cluster_top_words

# Example usage
if __name__ == "__main__":
    analyzer = DiscussionAnalyzer('free_board_posts.csv')
    if analyzer.load_data():
        # Word frequency analysis
        top_words = analyzer.analyze_word_frequency()
        print("Top 20 words:", top_words)
        
        # Temporal trends
        monthly_trends = analyzer.analyze_temporal_trends('M')
        
        # Topic modeling
        topics = analyzer.analyze_topics()
        print("Discovered topics:")
        for topic in topics:
            print(f"{topic[0]}: {', '.join(topic[1])}")
        
        # Sentiment analysis
        sentiment = analyzer.analyze_sentiment_trends()
        
        # Clustering
        clusters = analyzer.cluster_discussions()
        print("Cluster top words:")
        for cluster, words in clusters.items():
            print(f"{cluster}: {words}")
```
