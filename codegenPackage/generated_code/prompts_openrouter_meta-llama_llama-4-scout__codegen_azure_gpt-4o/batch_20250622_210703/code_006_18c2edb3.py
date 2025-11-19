"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Develop a machine learning model to recommend knitting or crochet patterns based on a user's skill level, yarn preferences, and project type.
Generated: DETERMINISTIC_18c2edb3fa117d15
Batch ID: 20250622_210703
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load and preprocess the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file and preprocess it.
    :param file_path: Path to the dataset file.
    :return: Preprocessed DataFrame.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)

        # Check for missing values and handle them
        data = data.dropna()

        # Convert categorical columns to numerical using one-hot encoding
        data = pd.get_dummies(data, columns=['skill_level', 'yarn_type', 'project_type'])

        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Train the machine learning model
def train_model(data):
    """
    Train a Random Forest Classifier to recommend patterns.
    :param data: Preprocessed DataFrame.
    :return: Trained model and test data for evaluation.
    """
    try:
        # Separate features and target variable
        X = data.drop(columns=['pattern_id'])  # Assuming 'pattern_id' is the target column
        y = data['pattern_id']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the Random Forest Classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        return model, X_test, y_test
    except Exception as e:
        print(f"Error training model: {e}")
        raise

# Save the trained model to a file
def save_model(model, file_path):
    """
    Save the trained model to a file using pickle.
    :param model: Trained model.
    :param file_path: Path to save the model.
    """
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(model, f)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

# Load the trained model from a file
def load_model(file_path):
    """
    Load a trained model from a file using pickle.
    :param file_path: Path to the model file.
    :return: Loaded model.
    """
    try:
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
        print(f"Model loaded from {file_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

# Predict patterns based on user input
def recommend_pattern(model, user_input):
    """
    Recommend a knitting or crochet pattern based on user input.
    :param model: Trained model.
    :param user_input: Dictionary containing user preferences.
    :return: Recommended pattern ID.
    """
    try:
        # Convert user input to DataFrame
        user_df = pd.DataFrame([user_input])

        # Ensure the input matches the model's feature set
        user_df = pd.get_dummies(user_df)
        user_df = user_df.reindex(columns=model.feature_names_in_, fill_value=0)

        # Predict the pattern
        pattern_id = model.predict(user_df)[0]
        return pattern_id
    except Exception as e:
        print(f"Error recommending pattern: {e}")
        raise

# Main function to execute the workflow
if __name__ == "__main__":
    # File paths
    dataset_path = "patterns_dataset.csv"  # Replace with your dataset file path
    model_path = "pattern_recommendation_model.pkl"

    # Load and preprocess the data
    data = load_data(dataset_path)

    # Train the model
    model, X_test, y_test = train_model(data)

    # Save the model
    save_model(model, model_path)

    # Load the model (optional, for demonstration purposes)
    loaded_model = load_model(model_path)

    # Example user input for prediction
    user_input = {
        "skill_level": "beginner",
        "yarn_type": "cotton",
        "project_type": "scarf"
    }

    # Recommend a pattern
    recommended_pattern = recommend_pattern(loaded_model, user_input)
    print(f"Recommended Pattern ID: {recommended_pattern}")
```

**Note:** Replace `"patterns_dataset.csv"` with the actual path to your dataset file. Ensure the dataset contains columns like `skill_level`, `yarn_type`, `project_type`, and `pattern_id`. Adjust the code as needed based on your dataset structure.
