"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Based on the 3rd & Taylor strategy for bridging the gap between sales and marketing, write code to analyze customer data and create targeted campaigns that improve conversions.
Generated: DETERMINISTIC_725aa8fea441e57e
Batch ID: 20250612_154432
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
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

def load_customer_data(file_path):
    """Load customer data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def preprocess_data(data):
    """Preprocess the customer data by handling missing values and encoding categorical variables."""
    # Fill missing values with median for numerical columns
    data.fillna(data.median(), inplace=True)
    
    # Encode categorical features
    categorical_cols = data.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    for col in categorical_cols:
        data[col] = le.fit_transform(data[col])
        logging.info(f"Encoded column: {col}")

    return data

def train_model(features, target):
    """Train a Random Forest Classifier."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(features, target)
    logging.info("Model training completed.")
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model using classification report."""
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions)
    logging.info("Model evaluation completed.")
    logging.info(f"Classification Report:\n{report}")

def create_targeted_campaigns(data):
    """Create targeted marketing campaigns based on customer segments."""
    # Example segmentation logic based on hypothetical features
    campaigns = {}
    campaigns['high_value'] = data[data['purchase_amount'] > 1000]
    campaigns['loyal_customers'] = data[data['customer_since_year'] < 5]
    logging.info("Targeted campaigns created based on segmentation.")
    return campaigns

def main(file_path):
    """Main function to execute the customer data analysis and campaign creation."""
    # Load customer data
    data = load_customer_data(file_path)

    # Preprocess the data
    processed_data = preprocess_data(data)

    # Define features and target
    features = processed_data.drop('conversion', axis=1)
    target = processed_data['conversion']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Create targeted campaigns
    targeted_campaigns = create_targeted_campaigns(processed_data)

    # Output the campaigns
    logging.info(f"Targeted Campaigns: {targeted_campaigns}")

if __name__ == "__main__":
    main("customer_data.csv")
```
