"""
Generated Code Metadata:
========================
Original URL: https://www.sbnnews.in
Prompt: Create a Bengali language model for text classification, specifically designed to categorize news articles from SBN News into topics like রাজ্য (state), দেশ (country), খেলা (sports), etc.
Generated: DETERMINISTIC_daf58e88162cb29a
Batch ID: 20250622_210650
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
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.
    The dataset should have two columns: 'text' and 'label'.
    """
    try:
        data = pd.read_csv(file_path)
        if 'text' not in data.columns or 'label' not in data.columns:
            raise ValueError("Dataset must contain 'text' and 'label' columns.")
        return data
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")

# Preprocess text data
def preprocess_text(text):
    """
    Preprocess Bengali text data.
    This function can be extended to include more advanced preprocessing steps.
    """
    # Remove unnecessary whitespace
    text = text.strip()
    # Convert to lowercase
    text = text.lower()
    # Add more preprocessing steps if needed
    return text

# Train a text classification model
def train_model(data, model_save_path):
    """
    Train a text classification model using Logistic Regression.
    Save the trained model and vectorizer to disk.
    """
    try:
        # Preprocess text data
        data['text'] = data['text'].apply(preprocess_text)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            data['text'], data['label'], test_size=0.2, random_state=42
        )

        # Convert text data to numerical features using TF-IDF
        vectorizer = TfidfVectorizer(max_features=5000)
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        # Train a Logistic Regression model
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train_tfidf, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test_tfidf)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        # Save the model and vectorizer to disk
        joblib.dump(model, f"{model_save_path}/bengali_news_model.pkl")
        joblib.dump(vectorizer, f"{model_save_path}/vectorizer.pkl")
        print(f"Model and vectorizer saved to {model_save_path}")
    except Exception as e:
        raise RuntimeError(f"Error training model: {e}")

# Predict the category of a news article
def predict_category(text, model_path, vectorizer_path):
    """
    Predict the category of a Bengali news article.
    """
    try:
        # Load the trained model and vectorizer
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)

        # Preprocess the input text
        text = preprocess_text(text)

        # Convert text to numerical features
        text_tfidf = vectorizer.transform([text])

        # Predict the category
        prediction = model.predict(text_tfidf)
        return prediction[0]
    except Exception as e:
        raise RuntimeError(f"Error predicting category: {e}")

# Main function
if __name__ == "__main__":
    # File path to the dataset
    dataset_path = "sbn_news_dataset.csv"  # Replace with the actual path to your dataset
    model_save_path = "models"  # Replace with the desired path to save the model and vectorizer

    # Load and train the model
    try:
        data = load_data(dataset_path)
        train_model(data, model_save_path)

        # Example prediction
        example_text = "বাংলাদেশ ক্রিকেট দল আজ দুর্দান্ত খেলেছে।"
        predicted_category = predict_category(
            example_text,
            f"{model_save_path}/bengali_news_model.pkl",
            f"{model_save_path}/vectorizer.pkl"
        )
        print(f"Predicted Category: {predicted_category}")
    except Exception as e:
        print(f"Error: {e}")
```
