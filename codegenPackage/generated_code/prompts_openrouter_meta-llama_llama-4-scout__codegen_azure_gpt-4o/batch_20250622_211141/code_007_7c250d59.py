"""
Generated Code Metadata:
========================
Original URL: https://lpt-airdrop.com
Prompt: Develop a sentiment analysis model to classify news articles from El Mundo as positive, negative, or neutral, using a suitable machine learning library or framework.
Generated: DETERMINISTIC_7c250d5960129658
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load the dataset
# Ensure the dataset has two columns: 'text' (news article content) and 'label' (sentiment: positive, negative, neutral)
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if 'text' not in data.columns or 'label' not in data.columns:
            raise ValueError("Dataset must contain 'text' and 'label' columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Preprocess the data
def preprocess_data(data):
    # Remove missing values
    data = data.dropna(subset=['text', 'label'])
    # Ensure labels are consistent
    data['label'] = data['label'].str.lower().str.strip()
    return data

# Train a sentiment analysis model
def train_model(data):
    try:
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            data['text'], data['label'], test_size=0.2, random_state=42
        )

        # Convert text data into numerical features using TF-IDF
        vectorizer = TfidfVectorizer(max_features=5000, stop_words='spanish')
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        # Train a logistic regression model
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train_tfidf, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test_tfidf)
        print("Model Evaluation:")
        print(classification_report(y_test, y_pred))

        # Save the trained model and vectorizer for future use
        joblib.dump(model, 'sentiment_model.pkl')
        joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

        print("Model and vectorizer saved successfully.")
    except Exception as e:
        print(f"Error training model: {e}")
        raise

# Predict sentiment for new articles
def predict_sentiment(texts):
    try:
        # Load the trained model and vectorizer
        model = joblib.load('sentiment_model.pkl')
        vectorizer = joblib.load('tfidf_vectorizer.pkl')

        # Transform the input texts
        texts_tfidf = vectorizer.transform(texts)

        # Predict sentiment
        predictions = model.predict(texts_tfidf)
        return predictions
    except Exception as e:
        print(f"Error predicting sentiment: {e}")
        raise

# Main function
if __name__ == "__main__":
    try:
        # Load and preprocess the dataset
        file_path = 'el_mundo_news.csv'  # Replace with the actual path to your dataset
        data = load_data(file_path)
        data = preprocess_data(data)

        # Train the sentiment analysis model
        train_model(data)

        # Example usage: Predict sentiment for new articles
        new_articles = [
            "El mercado de valores está en alza hoy.",
            "La economía enfrenta una recesión severa.",
            "El clima es agradable y soleado."
        ]
        predictions = predict_sentiment(new_articles)
        for article, sentiment in zip(new_articles, predictions):
            print(f"Article: {article}\nPredicted Sentiment: {sentiment}\n")
    except Exception as e:
        print(f"Error in main execution: {e}")
```

This code is production-ready, well-documented, and includes error handling. Ensure you have the required dataset (`el_mundo_news.csv`) and install necessary libraries (`pandas`, `scikit-learn`, `joblib`) before running the script.
