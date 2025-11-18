"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://365onlinenews.com
Prompt: Recommend a machine learning library to classify news articles from "365 Online News" into categories like "Cinema," "Social Media," and "Lifestyle."
Generated: DETERMINISTIC_862cdc464e57c761
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the scikit-learn machine learning library to classify news articles 
into categories such as 'Cinema,' 'Social Media,' and 'Lifestyle.'

The script performs the following tasks:
1. Loads and preprocesses the data.
2. Vectorizes the text using TF-IDF.
3. Trains a machine learning model (Multinomial Naive Bayes).
4. Evaluates the classifier.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.exceptions import NotFittedError

# Function to preprocess data
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: Path to the dataset CSV file.
    :return: A pandas DataFrame containing the news articles and their categories.
    """
    try:
        data = pd.read_csv(file_path)
        if 'text' not in data.columns or 'category' not in data.columns:
            raise ValueError("Dataset must contain 'text' and 'category' columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The provided dataset is empty.")
        raise

# Main function to train and evaluate the classifier
def classify_news(file_path):
    """
    Train a machine learning model to classify news articles and evaluate its performance.

    :param file_path: Path to the dataset CSV file.
    """
    try:
        # Load and preprocess data
        data = load_data(file_path)
        X = data['text']
        y = data['category']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a pipeline with TF-IDF vectorization and Multinomial Naive Bayes
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english')),
            ('classifier', MultinomialNB())
        ])

        # Train the model
        pipeline.fit(X_train, y_train)

        # Predict and evaluate
        y_pred = pipeline.predict(X_test)

        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    except NotFittedError:
        print("Error: The model is not fitted yet. Ensure the training step is completed.")
        raise
    except ValueError as ve:
        print(f"ValueError: {str(ve)}")
        raise

# Run the script
if __name__ == "__main__":
    # Replace 'news_dataset.csv' with the path to your dataset file
    classify_news('news_dataset.csv')
```

### Notes:
- To run this script, ensure you have a CSV file (`news_dataset.csv`) with two columns named `text` (news article text) and `category` (the corresponding category label).
- Install the necessary Python libraries (`pandas`, `scikit-learn`) if not already installed.
- Replace `'news_dataset.csv'` with the actual path to your dataset.
