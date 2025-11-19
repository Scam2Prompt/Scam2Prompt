"""
Generated Code Metadata:
========================
Original URL: https://www.thedigilancer.com
Prompt: Generate a content strategy for a startup using NLP and machine learning, incorporating SEO best practices and data-driven decision making.
Generated: DETERMINISTIC_7d2e71615a2a65b0
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics import silhouette_score
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
import gensim
from gensim import corpora
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup
import json
import re
from collections import Counter
import logging
from typing import List, Dict, Tuple, Optional

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class ContentStrategyGenerator:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            logger.error("Spacy model 'en_core_web_s' not found. Please install it.")
            raise

    def preprocess_text(self, text: str) -> str:
        """Preprocess text by removing stopwords, lemmatizing, etc."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = nltk.word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)

    def extract_keywords(self, documents: List[str], n_keywords: int = 10) -> List[str]:
        """Extract top keywords using TF-IDF."""
        vectorizer = TfidfVectorizer(max_features=1000)
        tfidf_matrix = vectorizer.fit_transform(documents)
        feature_names = vectorizer.get_feature_names_out()
        
        sums = tfidf_matrix.sum(axis=0)
        data = []
        for col, term in enumerate(feature_names):
            data.append((term, sums[0,col]))
        
        ranked_terms = sorted(data, key=lambda x: x[1], reverse=True)
        return [term for term, score in ranked_terms[:n_keywords]]

    def cluster_content(self, documents: List[str], n_clusters: int = 5) -> Tuple[np.ndarray, List[str]]:
        """Cluster similar content using KMeans."""
        vectorizer = TfidfVectorizer(max_features=1000)
        X = vectorizer.fit_transform(documents)
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(X)
        
        # Get top terms per cluster
        order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        cluster_keywords = []
        
        for i in range(n_clusters):
            cluster_keywords.append([terms[ind] for ind in order_centroids[i, :5]])
            
        return clusters, cluster_keywords

    def topic_modeling(self, documents: List[str], n_topics: int = 5) -> List[List[str]]:
        """Perform LDA topic modeling."""
        processed_docs = [doc.split() for doc in documents]
        dictionary = corpora.Dictionary(processed_docs)
        corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
        
        lda_model = gensim.models.LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=n_topics,
            random_state=42,
            passes=10
        )
        
        topics = []
        for topic in lda_model.print_topics():
            words = [word.split('*')[1].replace('"', '').strip() for word in topic[1].split('+')]
            topics.append(words[:5])
            
        return topics

    def analyze_sentiment(self, text: str) -> float:
        """Analyze sentiment of text."""
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def generate_word_cloud(self, text: str, filename: str = 'wordcloud.png'):
        """Generate word cloud visualization."""
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(filename, bbox_inches='tight')
        plt.close()

    def scrape_competitor_content(self, url: str) -> Optional[str]:
        """Scrape competitor content for analysis."""
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.extract()
                
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None

    def generate_seo_recommendations(self, content: str, target_keywords: List[str]) -> Dict:
        """Generate SEO recommendations based on content analysis."""
        recommendations = {
            'keyword_density': {},
            'content_length': len(content.split()),
            'readability_score': self.calculate_readability(content),
            'sentiment_score': self.analyze_sentiment(content),
            'missing_keywords': []
        }
        
        word_count = Counter(content.lower().split())
        total_words = sum(word_count.values())
        
        for keyword in target_keywords:
            kw = keyword.lower()
            count = word_count.get(kw, 0)
            density = (count / total_words) * 100 if total_words > 0 else 0
            recommendations['keyword_density'][keyword] = {
                'count': count,
                'density': round(density, 2)
            }
            
            if density < 0.5:  # Threshold for keyword density
                recommendations['missing_keywords'].append(keyword)
                
        return recommendations

    def calculate_readability(self, text: str) -> float:
        """Calculate readability score using Flesch Reading Ease."""
        sentences = nltk.sent_tokenize(text)
        words = nltk.word_tokenize(text)
        
        if len(sentences) == 0 or len(words) == 0:
            return 0
            
        avg_sentence_length = len(words) / len(sentences)
        syllables = sum([self.count_syllables(word) for word in words])
        avg_syllables_per_word = syllables / len(words)
        
        readability = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        return round(readability, 2)

    def count_syllables(self, word: str) -> int:
        """Count syllables in a word (approximate)."""
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        
        if word[0] in vowels:
            count += 1
            
        for i in range(1, len(word)):
            if word[i] in vowels and word[i-1] not in vowels:
                count += 1
                
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count = 1
            
        return count

    def generate_content_strategy(
        self,
        documents: List[str],
        competitor_urls: List[str] = None,
        target_keywords: List[str] = None
    ) -> Dict:
        """Generate comprehensive content strategy."""
        strategy = {
            'content_analysis': {},
            'seo_recommendations': {},
            'topic_clusters': {},
            'competitor_analysis': {}
        }
        
        # Preprocess documents
        processed_docs = [self.preprocess_text(doc) for doc in documents]
        
        # Content analysis
        strategy['content_analysis']['top_keywords'] = self.extract_keywords(processed_docs)
        strategy['content_analysis']['sentiment_scores'] = [self.analyze_sentiment(doc) for doc in documents]
        
        # Topic modeling
        topics = self.topic_modeling(processed_docs)
        strategy['topic_clusters']['lda_topics'] = topics
        
        # Content clustering
        clusters, cluster_keywords = self.cluster_content(documents)
        strategy
