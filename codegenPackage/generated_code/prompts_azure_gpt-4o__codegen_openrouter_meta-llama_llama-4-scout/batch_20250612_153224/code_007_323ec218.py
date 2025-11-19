"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: Develop a recommendation system using machine learning to match buyers with suppliers listed on PRGMEA’s platform based on product categories and certifications.
Generated: DETERMINISTIC_323ec218fb11d5db
Batch ID: 20250612_153224
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Define a function to load and preprocess data
def load_and_preprocess_data(buyers_df, suppliers_df):
    """
    Load and preprocess buyer and supplier data.

    Args:
        buyers_df (pd.DataFrame): Buyer data.
        suppliers_df (pd.DataFrame): Supplier data.

    Returns:
        pd.DataFrame: Preprocessed buyer data.
        pd.DataFrame: Preprocessed supplier data.
    """
    try:
        # Merge buyer and supplier data on product categories
        merged_df = pd.merge(buyers_df, suppliers_df, on='product_category')

        # Encode certifications using LabelEncoder
        le = LabelEncoder()
        merged_df['buyer_certification'] = le.fit_transform(merged_df['buyer_certification'])
        merged_df['supplier_certification'] = le.transform(merged_df['supplier_certification'])

        return merged_df

    except Exception as e:
        print(f"Error loading and preprocessing data: {str(e)}")

# Define a function to train a recommendation model
def train_recommendation_model(data_df):
    """
    Train a recommendation model using a random forest classifier.

    Args:
        data_df (pd.DataFrame): Preprocessed data.

    Returns:
        RandomForestClassifier: Trained recommendation model.
    """
    try:
        # Define features (X) and target (y)
        X = data_df[['buyer_certification', 'supplier_certification', 'product_category']]
        y = data_df['match']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate model performance
        y_pred = model.predict(X_test)
        print("Model Performance:")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

        return model

    except Exception as e:
        print(f"Error training recommendation model: {str(e)}")

# Define a function to make recommendations
def make_recommendations(model, buyer_df, suppliers_df):
    """
    Make recommendations for a buyer based on their certifications and product category.

    Args:
        model (RandomForestClassifier): Trained recommendation model.
        buyer_df (pd.DataFrame): Buyer data.
        suppliers_df (pd.DataFrame): Supplier data.

    Returns:
        pd.DataFrame: Recommended suppliers.
    """
    try:
        # Encode buyer certifications
        le = LabelEncoder()
        buyer_df['buyer_certification'] = le.fit_transform(buyer_df['buyer_certification'])

        # Define features (X) for recommendation
        X = buyer_df[['buyer_certification', 'product_category']]

        # Make predictions
        predictions = model.predict_proba(X)

        # Get recommended suppliers
        recommended_suppliers = suppliers_df[predictions > 0.5]

        return recommended_suppliers

    except Exception as e:
        print(f"Error making recommendations: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample buyer and supplier data
    buyers_df = pd.DataFrame({
        'buyer_id': [1, 2, 3],
        'buyer_certification': ['ISO 9001', 'ISO 14001', 'ISO 45001'],
        'product_category': ['Electronics', 'Fashion', 'Electronics']
    })

    suppliers_df = pd.DataFrame({
        'supplier_id': [101, 102, 103],
        'supplier_certification': ['ISO 9001', 'ISO 14001', 'ISO 45001'],
        'product_category': ['Electronics', 'Fashion', 'Electronics'],
        'match': [1, 0, 1]  # 1 indicates a match, 0 indicates no match
    })

    # Load and preprocess data
    data_df = load_and_preprocess_data(buyers_df, suppliers_df)

    # Train a recommendation model
    model = train_recommendation_model(data_df)

    # Make recommendations for a buyer
    buyer_df = pd.DataFrame({
        'buyer_id': [1],
        'buyer_certification': ['ISO 9001'],
        'product_category': ['Electronics']
    })

    recommended_suppliers = make_recommendations(model, buyer_df, suppliers_df)
    print("Recommended Suppliers:")
    print(recommended_suppliers)
```
