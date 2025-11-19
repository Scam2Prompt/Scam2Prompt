"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Generate a list of keywords and tags for categorizing and searching luxury furniture products on a website like origines-decoration.com, using techniques like natural language processing and machine learning."
Generated: DETERMINISTIC_451e9a6afb6aafa4
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Download required NLTK data
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

class LuxuryFurnitureCategorizer:
    def __init__(self, products_df):
        """
        Initialize the LuxuryFurnitureCategorizer class.

        Args:
        - products_df (pd.DataFrame): A DataFrame containing luxury furniture product information.
            It should have a 'description' column for product descriptions.
        """
        self.products_df = products_df
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        """
        Preprocess a product description by tokenizing, removing stop words, and lemmatizing.

        Args:
        - text (str): The product description.

        Returns:
        - list: A list of preprocessed tokens.
        """
        tokens = nltk.word_tokenize(text.lower())
        tokens = [t for t in tokens if t.isalpha() and t not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]
        return tokens

    def extract_keywords(self, product_description, num_keywords=10):
        """
        Extract keywords from a product description.

        Args:
        - product_description (str): The product description.
        - num_keywords (int): The number of keywords to extract.

        Returns:
        - list: A list of extracted keywords.
        """
        tokens = self.preprocess_text(product_description)
        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform([' '.join(tokens)])
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = tfidf.toarray()[0]
        top_indices = tfidf_scores.argsort()[-num_keywords:]
        return [feature_names[i] for i in top_indices]

    def categorize_products(self):
        """
        Categorize luxury furniture products based on their descriptions.

        Returns:
        - pd.DataFrame: A DataFrame with a 'keywords' column added to the original products_df.
        """
        self.products_df['keywords'] = self.products_df['description'].apply(self.extract_keywords)
        return self.products_df

    def generate_tags(self, product_description, num_tags=5):
        """
        Generate tags for a product description.

        Args:
        - product_description (str): The product description.
        - num_tags (int): The number of tags to generate.

        Returns:
        - list: A list of generated tags.
        """
        keywords = self.extract_keywords(product_description, num_tags * 2)
        return keywords[:num_tags]

    def search_products(self, query, num_results=10):
        """
        Search luxury furniture products based on a query.

        Args:
        - query (str): The search query.
        - num_results (int): The number of search results to return.

        Returns:
        - pd.DataFrame: A DataFrame with search results.
        """
        query_keywords = self.preprocess_text(query)
        products_tfidf = TfidfVectorizer().fit_transform(self.products_df['description'])
        query_tfidf = TfidfVectorizer().fit_transform([' '.join(query_keywords)])
        similarities = cosine_similarity(query_tfidf, products_tfidf).flatten()
        top_indices = similarities.argsort()[-num_results:]
        return self.products_df.iloc[top_indices]

# Example usage
if __name__ == "__main__":
    # Sample products DataFrame
    products_data = {
        'id': [1, 2, 3],
        'description': [
            'Luxury modern sofa with high-density foam cushioning.',
            'Elegant wooden coffee table with intricate carvings.',
            'Comfortable velvet armchair with sturdy metal legs.'
        ]
    }
    products_df = pd.DataFrame(products_data)

    categorizer = LuxuryFurnitureCategorizer(products_df)
    categorized_df = categorizer.categorize_products()
    print(categorized_df)

    query = 'modern sofa'
    search_results = categorizer.search_products(query)
    print(search_results)
```
