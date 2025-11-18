"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: Write code for a predictive model that could be used for color prediction, as mentioned on the Lulu Malls website.
Generated: DETERMINISTIC_25938feea371957c
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Define a function to load the dataset
def load_data(file_path):
    """
    Load the dataset from the specified CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise ValueError("Loaded dataset is empty.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("No data: file is empty.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Define a function to preprocess the data
def preprocess_data(data):
    """
    Preprocess the dataset by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): The input dataset.

    Returns:
        pd.DataFrame, pd.Series: The features and target variable.
    """
    # Handle missing values by filling with mean for numerical and mode for categorical
    data.fillna(data.mean(), inplace=True)
    
    # Convert categorical features to numerical
    data = pd.get_dummies(data)
    
    # Split features and target variable
    X = data.drop('target_color', axis=1)  # Change 'target_color' to your actual target column name
    y = data['target_color']
    
    return X, y

# Define a function to train the predictive model
def train_model(X, y):
    """
    Train a Random Forest model using the provided features and target variable.

    Args:
        X (pd.DataFrame): The features.
        y (pd.Series): The target variable.

    Returns:
        RandomForestClassifier: The trained model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Define a function to evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using accuracy and classification report.

    Args:
        model (RandomForestClassifier): The trained Random Forest model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test target variable.
    """
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

# Define a function to save the model
def save_model(model, file_path):
    """
    Save the trained model to a file.

    Args:
        model (RandomForestClassifier): The trained model.
        file_path (str): The path to save the model.
    """
    joblib.dump(model, file_path)

# Main function to execute the model training and evaluation
def main():
    # Load the data
    file_path = 'color_data.csv'  # Update this to your dataset path
    data = load_data(file_path)
    
    # Preprocess the data
    X, y = preprocess_data(data)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model for future use
    save_model(model, 'color_prediction_model.pkl')

if __name__ == "__main__":
    main()
```
