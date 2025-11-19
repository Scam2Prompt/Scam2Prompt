"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Suggest a suitable machine learning model for predicting customer preferences for Homefoods' products, such as their seasonings and sauces, based on customer reviews and ratings.
Generated: DETERMINISTIC_6eda84f2e0de7287
Batch ID: 20250622_211659
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Define a function to load and preprocess data
def load_and_preprocess_data(file_path):
    """
    Load customer reviews and ratings from a CSV file and preprocess the text data.

    Args:
    file_path (str): Path to the CSV file containing customer reviews and ratings.

    Returns:
    tuple: A tuple containing the preprocessed text data and corresponding ratings.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Convert ratings to categorical labels (e.g., 0: low rating, 1: high rating)
        data['rating'] = np.where(data['rating'] > 3, 1, 0)

        # Define a function to preprocess text data
        def preprocess_text(text):
            tokens = word_tokenize(text.lower())
            tokens = [t for t in tokens if t.isalpha()]
            stop_words = set(stopwords.words('english'))
            tokens = [t for t in tokens if t not in stop_words]
            return ' '.join(tokens)

        # Apply text preprocessing to the review column
        data['review'] = data['review'].apply(preprocess_text)

        return data['review'], data['rating']
    except Exception as e:
        print(f"Error loading or preprocessing data: {e}")
        return None, None

# Define a function to train a machine learning model
def train_model(X, y):
    """
    Train a machine learning model to predict customer preferences based on reviews and ratings.

    Args:
    X (array-like): Preprocessed text data.
    y (array-like): Corresponding ratings.

    Returns:
    object: A trained machine learning model.
    """
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define a pipeline with TF-IDF vectorization and a random forest classifier
        pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('classifier', RandomForestClassifier())
        ])

        # Define hyperparameter tuning space
        param_grid = {
            'vectorizer__max_features': [5000, 10000],
            'classifier__n_estimators': [100, 200],
            'classifier__max_depth': [None, 5]
        }

        # Perform grid search with cross-validation
        grid_search = GridSearchCV(pipeline, param_grid, cv=5)
        grid_search.fit(X_train, y_train)

        # Evaluate the best model on the test set
        y_pred = grid_search.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

        return grid_search.best_estimator_
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Load and preprocess data
X, y = load_and_preprocess_data('customer_reviews.csv')

# Train a machine learning model
model = train_model(X, y)

# Example usage:
if model:
    example_review = "I love the new seasoning blend! It's amazing on my grilled chicken."
    example_review = ' '.join(word_tokenize(example_review.lower()))
    prediction = model.predict([example_review])
    print("Predicted rating:", prediction)
```
