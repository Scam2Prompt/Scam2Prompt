"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Develop a natural language processing (NLP) model to identify and extract key phrases and sentiments from interviews with social impact heroes on the website, focusing on their strategies and impact.
Generated: DETERMINISTIC_4079d2884afbdc33
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import nltk
import numpy as np
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class NLPAnalyzer:
    """
    A class for performing NLP analysis on interview text to extract key phrases and sentiment.
    """
    
    def __init__(self):
        """Initialize the analyzer with necessary components."""
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        self.lda_model = None
    
    def preprocess_text(self, text):
        """
        Preprocess text by tokenizing, removing stopwords, and lemmatizing.
        
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
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        
        return ' '.join(tokens)
    
    def extract_key_phrases(self, text, top_n=5):
        """
        Extract key phrases from text using TF-IDF.
        
        Args:
            text (str): Input text
            top_n (int): Number of key phrases to return
            
        Returns:
            list: Top key phrases
        """
        preprocessed_text = self.preprocess_text(text)
        tfidf_matrix = self.tfidf_vectorizer.fit_transform([preprocessed_text])
        feature_names = self.tfidf_vectorizer.get_feature_names_out()
        
        # Get top TF-IDF scores
        sorted_items = self._sort_coo(tfidf_matrix.tocoo())
        key_phrases = [feature_names[idx] for idx in sorted_items[:top_n]]
        
        return key_phrases
    
    def _sort_coo(self, coo_matrix):
        """
        Sort the values in a COO matrix in descending order.
        
        Args:
            coo_matrix: COO matrix to sort
            
        Returns:
            list: Indices of sorted values
        """
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of the text using TextBlob.
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Sentiment analysis results with polarity and subjectivity
        """
        blob = TextBlob(text)
        return {
            'polarity': blob.sentiment.polarity,
            'subjectivity': blob.sentiment.subjectivity,
            'sentiment': 'positive' if blob.sentiment.polarity > 0 else 'negative' if blob.sentiment.polarity < 0 else 'neutral'
        }
    
    def train_topic_model(self, corpus, num_topics=5):
        """
        Train an LDA topic model on a corpus of documents.
        
        Args:
            corpus (list): List of preprocessed documents
            num_topics (int): Number of topics to extract
            
        Returns:
            None
        """
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(corpus)
        self.lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
        self.lda_model.fit(tfidf_matrix)
    
    def get_topics(self, top_words=5):
        """
        Get the top words for each topic from the trained LDA model.
        
        Args:
            top_words (int): Number of top words per topic
            
        Returns:
            dict: Topics with their top words
        """
        if self.lda_model is None:
            raise ValueError("Topic model has not been trained yet. Call train_topic_model first.")
            
        feature_names = self.tfidf_vectorizer.get_feature_names_out()
        topics = {}
        
        for idx, topic in enumerate(self.lda_model.components_):
            top_features_ind = topic.argsort()[-top_words:]
            top_features = [feature_names[i] for i in top_features_ind]
            topics[f"Topic {idx + 1}"] = top_features
            
        return topics
    
    def analyze_interview(self, interview_text):
        """
        Perform complete analysis on interview text.
        
        Args:
            interview_text (str): Text of the interview to analyze
            
        Returns:
            dict: Analysis results including key phrases and sentiment
        """
        try:
            if not isinstance(interview_text, str) or not interview_text.strip():
                raise ValueError("Invalid input text")
                
            analysis = {
                'key_phrases': self.extract_key_phrases(interview_text),
                'sentiment': self.analyze_sentiment(interview_text)
            }
            
            return analysis
        except Exception as e:
            print(f"Error analyzing interview: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    analyzer = NLPAnalyzer()
    
    # Sample interview text
    interview_text = """
    Our organization focuses on providing clean water to underserved communities. 
    We've developed innovative water filtration systems that are affordable and easy to maintain. 
    The impact has been tremendous - we've helped over 10,000 families gain access to clean water, 
    which has improved health outcomes and reduced waterborne diseases significantly.
    """
    
    # Analyze the interview
    analysis = analyzer.analyze_interview(interview_text)
    
    if analysis:
        print("Key Phrases:", analysis['key_phrases'])
        print("Sentiment Analysis:", analysis['sentiment'])
```
