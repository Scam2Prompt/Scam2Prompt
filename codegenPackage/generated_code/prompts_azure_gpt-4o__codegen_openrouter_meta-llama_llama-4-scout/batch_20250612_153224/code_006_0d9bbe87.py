"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Write code to automate the process of categorizing news articles based on human rights violations, inspired by Jusoor International's media advocacy efforts.
Generated: DETERMINISTIC_0d9bbe8773c12f45
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Define a function to load and preprocess data
def load_data(file_path):
    """
    Load news articles data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the news articles data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

# Define a function to categorize news articles
def categorize_news_articles(data):
    """
    Categorize news articles based on human rights violations.

    Args:
        data (pandas.DataFrame): DataFrame containing the news articles data.

    Returns:
        tuple: Trained model, vectorizer, and categorized data.
    """
    # Check if required columns exist
    required_columns = ['article_text', 'category']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['article_text'], data['category'], test_size=0.2, random_state=42)

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')

    # Fit the vectorizer to the training data and transform both the training and testing data
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    # Train a Multinomial Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X_train_vectorized, y_train)

    # Make predictions on the testing data
    y_pred = model.predict(X_test_vectorized)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.3f}")
    print("Classification Report:\n", report)

    # Use the trained model to categorize new news articles
    def categorize_new_article(article_text):
        article_vectorized = vectorizer.transform([article_text])
        predicted_category = model.predict(article_vectorized)
        return predicted_category[0]

    return model, vectorizer, categorize_new_article

# Example usage
if __name__ == "__main__":
    # Load data
    data = load_data('news_articles.csv')

    if data is not None:
        # Categorize news articles
        model, vectorizer, categorize_new_article = categorize_news_articles(data)

        # Test the categorization function
        new_article_text = "A recent report highlighted the ongoing issue of freedom of speech in a certain country."
        predicted_category = categorize_new_article(new_article_text)
        print(f"Predicted Category for new article: {predicted_category}")
```
