"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: Provide an example of using Disarray to build on collective knowledge from previous experiments and avoid redundant computations in ML workflows.
Generated: DETERMINISTIC_7f34f548f81fd3f9
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import disarray
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Define a function to load and prepare data
def load_data(file_path):
    """
    Load data from a CSV file and return it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Define a function to train a model
def train_model(data, target):
    """
    Train a random forest classifier on the given data.

    Args:
        data (pd.DataFrame): The data to train on.
        target (str): The target column name.

    Returns:
        RandomForestClassifier: The trained model.
    """
    try:
        X = data.drop(target, axis=1)
        y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy:.3f}")

        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Define a function to use Disarray to cache model training
def train_model_with_disarray(data, target, cache_dir):
    """
    Train a model using Disarray to cache the training process.

    Args:
        data (pd.DataFrame): The data to train on.
        target (str): The target column name.
        cache_dir (str): The directory to store the cache.

    Returns:
        RandomForestClassifier: The trained model.
    """
    try:
        # Create a Disarray cache
        cache = disarray.Cache(cache_dir)

        # Define a function to train the model, wrapped with Disarray's cache decorator
        @cache
        def _train_model(data, target):
            return train_model(data, target)

        # Train the model with caching
        model = _train_model(data, target)

        return model
    except Exception as e:
        print(f"Error training model with Disarray: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = "example_data.csv"
    data = load_data(file_path)

    if data is not None:
        target = "target_column"
        cache_dir = "./model_cache"

        model = train_model_with_disarray(data, target, cache_dir)

        if model is not None:
            print("Model trained successfully!")
```
