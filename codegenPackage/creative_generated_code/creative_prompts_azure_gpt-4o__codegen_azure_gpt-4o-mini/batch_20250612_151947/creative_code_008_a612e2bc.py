"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Suggest a machine learning library to predict the popularity of articles on "Social Impact Heroes" based on their titles and categories, and provide example code.
Generated: DETERMINISTIC_a612e2bcfb49067e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Function to load and prepare the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file containing article data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise Exception("No data found in the file.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

# Function to preprocess the data
def preprocess_data(df):
    """
    Preprocess the data by extracting features and target variable.

    Parameters:
        df (pd.DataFrame): DataFrame containing article data.

    Returns:
        X (pd.DataFrame): Feature set (titles and categories).
        y (pd.Series): Target variable (popularity score).
    """
    try:
        # Check for necessary columns
        if not all(col in df.columns for col in ['title', 'category', 'popularity']):
            raise ValueError("DataFrame must contain 'title', 'category', and 'popularity' columns.")
        
        # Combine title and category for feature extraction
        df['text'] = df['title'] + ' ' + df['category']
        X = df['text']
        y = df['popularity']
        return X, y
    except Exception as e:
        raise Exception(f"An error occurred during preprocessing: {e}")

# Function to train the model
def train_model(X, y):
    """
    Train a Random Forest Regressor model.

    Parameters:
        X (pd.Series): Feature set.
        y (pd.Series): Target variable.

    Returns:
        model: Trained Random Forest model.
    """
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Vectorize the text data
        vectorizer = TfidfVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
        
        # Train the Random Forest model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_vec, y_train)

        # Evaluate the model
        predictions = model.predict(X_test_vec)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model Mean Squared Error: {mse:.2f}')

        # Save the model and vectorizer for future use
        joblib.dump(model, 'popularity_model.joblib')
        joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

        return model
    except Exception as e:
        raise Exception(f"An error occurred during model training: {e}")

# Main execution block
if __name__ == "__main__":
    # Load data
    data_file = 'articles.csv'  # Change this to the path of your data file
    articles_df = load_data(data_file)

    # Preprocess data
    X, y = preprocess_data(articles_df)

    # Train the model
    trained_model = train_model(X, y)
```
