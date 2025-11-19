"""
Generated Code Metadata:
========================
Original URL: https://lqeth.com
Prompt: Suggest a suitable machine learning model for classifying sports news articles from GiveMeSport into categories (e.g., transfer news, match results, analysis).
Generated: DETERMINISTIC_1aa6a1f2e1242f24
Batch ID: 20250622_205948
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
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str, path to the CSV file containing the sports news articles
    :return: DataFrame, containing the articles and their corresponding categories
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    """
    Preprocess the data by dropping missing values and ensuring correct data types.

    :param data: DataFrame, the raw data
    :return: DataFrame, cleaned data
    """
    data = data.dropna(subset=['article', 'category'])
    return data

# Train the model
def train_model(X_train, y_train):
    """
    Train a Naive Bayes model using TF-IDF vectorization.

    :param X_train: Series, the training articles
    :param y_train: Series, the training categories
    :return: model, the trained machine learning model
    """
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test set.

    :param model: the trained model
    :param X_test: Series, the test articles
    :param y_test: Series, the test categories
    """
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))

# Save the model
def save_model(model, file_name):
    """
    Save the trained model to a file.

    :param model: the trained model
    :param file_name: str, the name of the file to save the model
    """
    joblib.dump(model, file_name)

# Main function to execute the workflow
def main(file_path):
    """
    Main function to load data, train the model, evaluate it, and save the model.

    :param file_path: str, path to the CSV file containing the sports news articles
    """
    # Load and preprocess data
    data = load_data(file_path)
    if data is None:
        return

    data = preprocess_data(data)

    # Split the data into training and testing sets
    X = data['article']
    y = data['category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model for future use
    save_model(model, 'sports_news_classifier.joblib')

# Entry point of the script
if __name__ == "__main__":
    # Specify the path to the dataset
    dataset_path = 'sports_news_articles.csv'
    main(dataset_path)
```
