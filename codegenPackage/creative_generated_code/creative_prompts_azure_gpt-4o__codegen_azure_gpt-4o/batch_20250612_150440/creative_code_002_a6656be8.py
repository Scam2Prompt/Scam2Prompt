"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Create a script to perform category-specific deep dives into e-commerce reviews using machine learning techniques, as outlined in Consensys's Explorer service, to identify drivers and drainers of ratings.
Generated: DETERMINISTIC_a6656be824dac666
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ReviewDeepDive:
    def __init__(self, reviews_data: pd.DataFrame):
        """
        Initialize the ReviewDeepDive class with the reviews dataset.

        :param reviews_data: A DataFrame containing at least 'category', 'review_text', and 'rating' columns.
        """
        logger.info("Initializing ReviewDeepDive instance.")
        
        # Validate input DataFrame
        if not {'category', 'review_text', 'rating'}.issubset(reviews_data.columns):
            raise ValueError("DataFrame must contain 'category', 'review_text', and 'rating' columns.")
        
        self.reviews_data = reviews_data

    def preprocess_reviews(self):
        """
        Preprocess the review text by removing NaN values and filtering out neutral ratings.
        """
        logger.info("Preprocessing reviews.")
        self.reviews_data.dropna(subset=['review_text'], inplace=True)
        self.reviews_data = self.reviews_data[self.reviews_data['rating'] != 3]  # Remove neutral reviews
        self.reviews_data['sentiment'] = self.reviews_data['rating'].apply(lambda x: 1 if x > 3 else 0)  # Positive or Negative

    def perform_category_analysis(self, category: str):
        """
        Deep dive into a specific category to identify drivers and drainers of ratings.

        :param category: Category name to analyze.
        :return: Key drivers and drainers as keywords.
        """
        logger.info(f"Performing analysis for category: {category}.")
        
        # Filter reviews by category
        category_data = self.reviews_data[self.reviews_data['category'] == category]
        if category_data.empty:
            raise ValueError(f"No reviews available for category '{category}'.")
        
        # Extract review text and sentiment
        X = category_data['review_text']
        y = category_data['sentiment']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # Build a pipeline for TF-IDF vectorization and NMF topic modeling
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
            ('nmf', NMF(n_components=5, random_state=42))  # Extract 5 latent topics
        ])

        logger.info("Fitting TF-IDF and NMF pipeline.")
        topic_matrix = pipeline.fit_transform(X_train)

        # Train a classifier to identify sentiment
        logger.info("Training sentiment classifier.")
        sentiment_model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
            ('scaler', StandardScaler(with_mean=False)),
            ('classifier', LogisticRegression(random_state=42))
        ])
        sentiment_model.fit(X_train, y_train)

        # Evaluate the model
        logger.info("Evaluating sentiment classifier.")
        y_pred = sentiment_model.predict(X_test)
        logger.info("\n" + classification_report(y_test, y_pred))

        # Extract top terms for each topic
        tfidf = pipeline.named_steps['tfidf']
        nmf = pipeline.named_steps['nmf']
        vocab = np.array(tfidf.get_feature_names_out())
        topic_keywords = {}

        logger.info("Extracting topic keywords.")
        for topic_idx, topic in enumerate(nmf.components_):
            top_keywords = vocab[np.argsort(topic)[-10:]]  # Top 10 keywords
            topic_keywords[f"Topic {topic_idx + 1}"] = top_keywords.tolist()

        return topic_keywords

# Example usage
if __name__ == "__main__":
    # Example dataset
    data = {
        'category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
        'review_text': [
            "Great quality and excellent battery life!",
            "The fabric is very comfortable and durable.",
            "Poor screen resolution and laggy performance.",
            "The sizing is completely off, not true to size.",
            "Excellent value for money, highly recommended!"
        ],
        'rating': [5, 4, 2, 1, 5]
    }
    reviews_df = pd.DataFrame(data)

    # Create instance and run analysis
    deep_dive = ReviewDeepDive(reviews_df)
    deep_dive.preprocess_reviews()
    drivers_drainers = deep_dive.perform_category_analysis('Electronics')

    # Output results
    logger.info("Drivers and Drainers for 'Electronics':")
    for topic, keywords in drivers_drainers.items():
        logger.info(f"{topic}: {', '.join(keywords)}")
```
