"""
Generated Code Metadata:
========================
Original URL: https://liquideth-gift.org
Prompt: Develop a machine learning model using Python and scikit-learn to classify posts from a humor website into different categories, such as funny, serious, or thought-provoking.
Generated: DETERMINISTIC_d4556f11f422c7f4
Batch ID: 20250622_211628
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
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import os

# Constants
RANDOM_STATE = 42
MODEL_SAVE_PATH = 'humor_classifier.pkl'
VECTORIZER_SAVE_PATH = 'tfidf_vectorizer.pkl'

def load_data(filepath):
    """
    Load dataset from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded dataset
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {filepath}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def preprocess_data(data, text_column='text', label_column='label'):
    """
    Preprocess the data by cleaning and splitting into features and labels.
    
    Args:
        data (pandas.DataFrame): Input data
        text_column (str): Name of the text column
        label_column (str): Name of the label column
        
    Returns:
        tuple: (X, y) where X is the text data and y is the labels
    """
    if text_column not in data.columns or label_column not in data.columns:
        raise ValueError("Specified columns not found in the dataset")
    
    # Drop rows with missing values
    data = data.dropna(subset=[text_column, label_column])
    
    X = data[text_column]
    y = data[label_column]
    
    return X, y

def train_model(X_train, y_train):
    """
    Train a text classification model using TF-IDF and LinearSVC.
    
    Args:
        X_train (pandas.Series): Training text data
        y_train (pandas.Series): Training labels
        
    Returns:
        tuple: (model, vectorizer) trained model and vectorizer
    """
    # Create a pipeline with TF-IDF vectorizer and LinearSVC classifier
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])
    
    # Define parameter grid for GridSearch
    param_grid = {
        'tfidf__max_features': [5000, 10000, None],
        'tfidf__ngram_range': [(1, 1), (1, 2)],
        'clf__C': [0.1, 1, 10]
    }
    
    # Perform grid search with cross-validation
    grid_search = GridSearchCV(
        pipeline,
        param_grid,
        cv=5,
        n_jobs=-1,
        verbose=1
    )
    
    grid_search.fit(X_train, y_train)
    
    # Get the best model and vectorizer
    best_model = grid_search.best_estimator_
    vectorizer = best_model.named_steps['tfidf']
    
    return best_model, vectorizer

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on test data.
    
    Args:
        model: Trained model
        X_test: Test text data
        y_test: Test labels
        
    Returns:
        dict: Evaluation metrics
    """
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)
    
    return {
        'accuracy': accuracy,
        'report': report
    }

def save_artifacts(model, vectorizer):
    """
    Save the trained model and vectorizer to disk.
    
    Args:
        model: Trained model
        vectorizer: Fitted vectorizer
    """
    try:
        joblib.dump(model, MODEL_SAVE_PATH)
        joblib.dump(vectorizer, VECTORIZER_SAVE_PATH)
    except Exception as e:
        raise Exception(f"Error saving artifacts: {str(e)}")

def load_artifacts():
    """
    Load the saved model and vectorizer from disk.
    
    Returns:
        tuple: (model, vectorizer) if found, else (None, None)
    """
    if not os.path.exists(MODEL_SAVE_PATH) or not os.path.exists(VECTORIZER_SAVE_PATH):
        return None, None
    
    try:
        model = joblib.load(MODEL_SAVE_PATH)
        vectorizer = joblib.load(VECTORIZER_SAVE_PATH)
        return model, vectorizer
    except Exception as e:
        raise Exception(f"Error loading artifacts: {str(e)}")

def main():
    """
    Main function to execute the training pipeline.
    """
    try:
        # Load data (replace with your actual data path)
        data = load_data('humor_posts.csv')
        
        # Preprocess data
        X, y = preprocess_data(data)
        
        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=RANDOM_STATE
        )
        
        # Train model
        model, vectorizer = train_model(X_train, y_train)
        
        # Evaluate model
        evaluation = evaluate_model(model, X_test, y_test)
        print(f"Accuracy: {evaluation['accuracy']:.2f}")
        print("Classification Report:")
        print(pd.DataFrame(evaluation['report']).transpose())
        
        # Save artifacts
        save_artifacts(model, vectorizer)
        print("Model and vectorizer saved successfully.")
        
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
        raise

if __name__ == '__main__':
    main()
```
