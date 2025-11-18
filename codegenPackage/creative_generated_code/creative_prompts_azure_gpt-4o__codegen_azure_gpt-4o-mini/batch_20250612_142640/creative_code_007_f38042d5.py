"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Develop a machine learning model to predict the best financing options for businesses based on asset type and industry sector, using examples like those provided by Rhino Asset Finance.
Generated: DETERMINISTIC_f38042d545070e6d
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
def load_data(file_path):
    """Load dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    """Preprocess the data for the machine learning model."""
    # Encode categorical variables
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    # Split features and target
    X = data.drop('financing_option', axis=1)  # Change 'financing_option' to your target variable
    y = data['financing_option']
    return X, y, label_encoders

# Train the model
def train_model(X_train, y_train):
    """Train a Random Forest model."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    y_pred = model.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the model
def save_model(model, filename):
    """Save the trained model to a file."""
    try:
        joblib.dump(model, filename)
        print(f"Model saved to {filename}.")
    except Exception as e:
        print(f"Error saving model: {e}")

# Main function
def main():
    """Main function to run the modeling process."""
    # Load and preprocess the data
    file_path = 'business_financing_data.csv'  # Path to your dataset
    data = load_data(file_path)
    
    if data is None:
        return

    X, y, label_encoders = preprocess_data(data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, 'financing_model.joblib')

if __name__ == "__main__":
    main()
```
