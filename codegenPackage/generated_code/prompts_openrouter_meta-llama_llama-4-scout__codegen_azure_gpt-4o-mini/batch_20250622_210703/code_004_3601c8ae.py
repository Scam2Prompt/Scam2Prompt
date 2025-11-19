"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Develop a code snippet to analyze customer testimonials on the Vitality Holistic website, using natural language processing (NLP) techniques to identify common themes and sentiments expressed by clients.
Generated: DETERMINISTIC_3601c8ae4b3cc596
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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import logging

# Ensure necessary NLTK resources are downloaded
nltk.download('vader_lexicon')

# Set up logging for better error tracking
logging.basicConfig(level=logging.INFO)

class TestimonialAnalyzer:
    def __init__(self, testimonials):
        """
        Initialize the TestimonialAnalyzer with a list of testimonials.
        
        :param testimonials: List of customer testimonials (strings)
        """
        self.testimonials = testimonials
        self.sia = SentimentIntensityAnalyzer()
        self.vectorizer = CountVectorizer(stop_words='english')
        self.lda_model = LDA(n_components=5, random_state=42)

    def analyze_sentiments(self):
        """
        Analyze the sentiments of the testimonials.
        
        :return: DataFrame with testimonials and their sentiment scores
        """
        try:
            sentiment_scores = [self.sia.polarity_scores(testimonial) for testimonial in self.testimonials]
            sentiment_df = pd.DataFrame(sentiment_scores)
            sentiment_df['testimonial'] = self.testimonials
            return sentiment_df
        except Exception as e:
            logging.error("Error analyzing sentiments: %s", e)
            return None

    def extract_themes(self):
        """
        Extract common themes from the testimonials using LDA.
        
        :return: List of topics identified in the testimonials
        """
        try:
            # Transform testimonials into a document-term matrix
            doc_term_matrix = self.vectorizer.fit_transform(self.testimonials)
            # Fit the LDA model
            self.lda_model.fit(doc_term_matrix)
            # Get the topics
            topics = self.lda_model.components_
            feature_names = self.vectorizer.get_feature_names_out()
            return self._get_top_words_per_topic(topics, feature_names, n_top_words=5)
        except Exception as e:
            logging.error("Error extracting themes: %s", e)
            return None

    def _get_top_words_per_topic(self, topics, feature_names, n_top_words):
        """
        Get the top words for each topic identified by the LDA model.
        
        :param topics: Topics from the LDA model
        :param feature_names: Feature names from the vectorizer
        :param n_top_words: Number of top words to return for each topic
        :return: List of top words for each topic
        """
        top_words = []
        for topic_idx, topic in enumerate(topics):
            top_words.append([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        return top_words

# Example usage
if __name__ == "__main__":
    testimonials = [
        "I feel more energetic and alive after my sessions.",
        "The holistic approach has changed my life for the better.",
        "I love the community and support I receive here.",
        "My stress levels have significantly decreased.",
        "The staff is incredibly knowledgeable and caring."
    ]

    analyzer = TestimonialAnalyzer(testimonials)
    
    # Analyze sentiments
    sentiment_results = analyzer.analyze_sentiments()
    if sentiment_results is not None:
        print("Sentiment Analysis Results:")
        print(sentiment_results)

    # Extract themes
    theme_results = analyzer.extract_themes()
    if theme_results is not None:
        print("\nCommon Themes Extracted:")
        for idx, words in enumerate(theme_results):
            print(f"Topic {idx + 1}: {', '.join(words)}")
```
