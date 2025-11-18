"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.gtempus.com
Prompt: Suggest a machine learning model for Grupo de Seguros Tempus to predict customer retention based on historical data, including factors like claim frequency and policy type.
Generated: DETERMINISTIC_7b5af74d5c2b9ba3
Batch ID: 20250612_150917
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import joblib

# Load the data
# Replace 'data.csv' with the path to your dataset
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("Error: Data file not found.")
    exit()

# Data preprocessing
# Check for missing values and handle them (e.g., filling or dropping)
if data.isnull().sum().sum() > 0:
    print("Warning: Missing data detected. Filling missing values with column means.")
    data.fillna(data.mean(), inplace=True)

# Encode categorical variables (e.g., policy type)
categorical_columns = data.select_dtypes(include=['object']).columns
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Separate features (X) and target (y)
X = data.drop(columns=['customer_retained'])  # Replace 'customer_retained' with the actual target column name
y = data['customer_retained']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (optional, depends on the model)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the model
# Using RandomForestClassifier as a baseline model
model = RandomForestClassifier(random_state=42, n_estimators=100)

try:
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the model and scaler for future use
    joblib.dump(model, 'customer_retention_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("Model and scaler saved successfully.")
except Exception as e:
    print(f"Error occurred during model training or evaluation: {e}")
```

Make sure to replace placeholders like `'data.csv'` and `'customer_retained'` with the actual file path and column names from your dataset.
