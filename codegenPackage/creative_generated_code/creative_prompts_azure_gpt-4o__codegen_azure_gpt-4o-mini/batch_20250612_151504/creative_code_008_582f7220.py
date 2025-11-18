"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teleperformance-amplifai.com
Prompt: Write a function to predict employee performance using machine learning, similar to AmplifAI's AI-driven solutions.
Generated: DETERMINISTIC_582f7220ef2c0f39
Batch ID: 20250612_151504
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

def predict_employee_performance(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42) -> None:
    """
    Predicts employee performance using a Random Forest Classifier.
    
    Parameters:
    - data (pd.DataFrame): The input data containing features and target.
    - target_column (str): The name of the target column in the DataFrame.
    - test_size (float): The proportion of the dataset to include in the test split.
    - random_state (int): Random seed for reproducibility.
    
    Returns:
    - None: The function saves the trained model to a file.
    """
    
    # Check if target_column exists in the dataframe
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' is not in the DataFrame.")
    
    # Separate features and target variable
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Create a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=random_state)

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Model accuracy: {accuracy:.2f}")
    print("Classification report:")
    print(report)

    # Save the trained model to a file for future use
    model_filename = 'employee_performance_model.joblib'
    joblib.dump(model, model_filename)
    print(f"Model saved to {model_filename}")

# Example of how to use the function (uncomment to run):
# df = pd.read_csv('employee_data.csv')  # Load your dataset here
# predict_employee_performance(df, target_column='performance_score')
```
