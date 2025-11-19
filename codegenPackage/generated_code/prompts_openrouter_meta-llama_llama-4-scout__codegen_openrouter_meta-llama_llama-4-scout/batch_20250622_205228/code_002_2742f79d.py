"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Generate a code snippet to categorize and analyze e-commerce reviews using machine learning techniques, such as topic modeling and sentiment analysis.
Generated: DETERMINISTIC_2742f79d5876f3ff
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download required NLTK data
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class ReviewAnalyzer:
    def __init__(self, reviews_df):
        """
        Initialize the ReviewAnalyzer class.

        Args:
            reviews_df (pd.DataFrame): A DataFrame containing e-commerce reviews.
                It should have two columns: 'review' and 'rating' (or 'sentiment').
        """
        self.reviews_df = reviews_df

    def preprocess_reviews(self):
        """
        Preprocess the reviews by tokenizing, removing stopwords, and lemmatizing.

        Returns:
            list: A list of preprocessed reviews.
        """
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))

        preprocessed_reviews = []
        for review in self.reviews_df['review']:
            tokens = nltk.word_tokenize(review.lower())
            tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
            tokens = [lemmatizer.lemmatize(t) for t in tokens]
            preprocessed_reviews.append(' '.join(tokens))

        return preprocessed_reviews

    def topic_modeling(self, num_topics):
        """
        Perform topic modeling using Latent Dirichlet Allocation (LDA).

        Args:
            num_topics (int): The number of topics to extract.

        Returns:
            pd.DataFrame: A DataFrame containing the topic distribution for each review.
        """
        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform(self.preprocess_reviews())

        lda = LatentDirichletAllocation(n_components=num_topics)
        topic_distribution = lda.fit_transform(tfidf)

        return pd.DataFrame(topic_distribution.toarray())

    def sentiment_analysis(self):
        """
        Perform sentiment analysis using the VADER sentiment intensity analyzer.

        Returns:
            pd.DataFrame: A DataFrame containing the sentiment scores for each review.
        """
        sia = SentimentIntensityAnalyzer()

        sentiment_scores = []
        for review in self.reviews_df['review']:
            scores = sia.polarity_scores(review)
            sentiment_scores.append({
                'compound': scores['compound'],
                'pos': scores['pos'],
                'neu': scores['neu'],
                'neg': scores['neg']
            })

        return pd.DataFrame(sentiment_scores)

    def train_sentiment_classifier(self):
        """
        Train a sentiment classifier using a Multinomial Naive Bayes classifier.

        Returns:
            tuple: A tuple containing the trained classifier and the vectorizer.
        """
        X = self.preprocess_reviews()
        y = np.where(self.reviews_df['rating'] > 3, 1, 0)  # Binary sentiment classification

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        vectorizer = TfidfVectorizer()
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        clf = MultinomialNB()
        clf.fit(X_train_tfidf, y_train)

        y_pred = clf.predict(X_test_tfidf)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        return clf, vectorizer

# Example usage
if __name__ == "__main__":
    reviews_data = {
        'review': [
            "I loved the product! It's amazing.",
            "The product was okay, but not great.",
            "I'm so disappointed with the product.",
            "The product is perfect for my needs.",
            "I'm not sure about the product..."
        ],
        'rating': [5, 3, 1, 5, 3]
    }

    reviews_df = pd.DataFrame(reviews_data)

    analyzer = ReviewAnalyzer(reviews_df)
    preprocessed_reviews = analyzer.preprocess_reviews()
    print("Preprocessed Reviews:")
    print(preprocessed_reviews)

    topic_distribution = analyzer.topic_modeling(num_topics=2)
    print("\nTopic Distribution:")
    print(topic_distribution)

    sentiment_scores = analyzer.sentiment_analysis()
    print("\nSentiment Scores:")
    print(sentiment_scores)

    clf, vectorizer = analyzer.train_sentiment_classifier()
```
