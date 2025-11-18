"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Write code to automate the process of categorizing news articles based on human rights violations, inspired by Jusoor International's media advocacy efforts.
Generated: DETERMINISTIC_0d9bbe8773c12f45
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import re
from typing import List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.exceptions import NotFittedError
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Ensure necessary NLTK data files are downloaded
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

class NewsCategorizer:
    """
    Automates the categorization of news articles based on human rights violations.
    """
    def __init__(self, num_categories: int = 5):
        """
        Initialize the categorizer with the number of categories.
        :param num_categories: Number of categories for clustering (default: 5).
        """
        self.num_categories = num_categories
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=1000)
        self.model = KMeans(n_clusters=self.num_categories, random_state=42)
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text: str) -> str:
        """
        Preprocess the text for analysis.
        - Tokenize sentences
        - Remove special characters and stopwords
        - Lemmatize words
        :param text: Raw text of an article.
        :return: Cleaned and processed text.
        """
        sentences = sent_tokenize(text)
        processed_sentences = []
        for sentence in sentences:
            # Remove special characters and numbers
            sentence = re.sub(r"[^\w\s]", "", sentence)
            sentence = re.sub(r"\d+", "", sentence)
            # Tokenize words and remove stopwords
            words = [
                self.lemmatizer.lemmatize(word.lower())
                for word in sentence.split()
                if word.lower() not in self.stop_words
            ]
            processed_sentences.append(" ".join(words))
        return " ".join(processed_sentences)

    def fit(self, articles: List[str]) -> None:
        """
        Fit the categorization model on a list of articles.
        :param articles: List of news articles (raw text).
        """
        # Preprocess all articles
        processed_articles = [self.preprocess_text(article) for article in articles]

        # Vectorize the articles
        try:
            vectors = self.vectorizer.fit_transform(processed_articles)
        except ValueError as ve:
            raise ValueError("Error during vectorization. Ensure articles are not empty.") from ve

        # Train KMeans clustering model
        self.model.fit(vectors)

    def predict(self, article: str) -> int:
        """
        Predict the category of a single article.
        :param article: Raw text of the article.
        :return: Predicted category index.
        """
        processed_article = self.preprocess_text(article)
        try:
            vector = self.vectorizer.transform([processed_article])
        except NotFittedError as nfe:
            raise NotFittedError("The model has not been fitted yet. Call `fit` first.") from nfe

        return self.model.predict(vector)[0]

    def save_model(self, file_path: str) -> None:
        """
        Save the model and vectorizer to a file.
        :param file_path: Path to save the model.
        """
        model_data = {
            "num_categories": self.num_categories,
            "model": self.model,
            "vectorizer": self.vectorizer
        }
        with open(file_path, "wb") as file:
            json.dump(model_data, file)

    def load_model(self, file_path: str) -> None:
        """
        Load the model and vectorizer from a file.
        :param file_path: Path to the saved model file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        with open(file_path, "rb") as file:
            model_data = json.load(file)
        self.num_categories = model_data["num_categories"]
        self.model = model_data["model"]
        self.vectorizer = model_data["vectorizer"]


# Example usage
if __name__ == "__main__":
    try:
        articles = [
            "Article about human rights violations in country X.",
            "A report regarding child labor issues in region Y.",
            "News on gender inequality and discrimination.",
            "Information about freedom of speech suppression.",
            "Coverage on refugee crises and displacement."
        ]

        categorizer = NewsCategorizer(num_categories=3)
        categorizer.fit(articles)

        new_article = "Discussing suppression of freedom of speech in country Z."
        predicted_category = categorizer.predict(new_article)

        print(f"Predicted category: {predicted_category}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
