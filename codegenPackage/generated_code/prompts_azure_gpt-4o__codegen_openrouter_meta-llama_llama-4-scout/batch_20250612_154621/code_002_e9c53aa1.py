"""
Generated Code Metadata:
========================
Original URL: https://itab.com
Prompt: Generate code to analyze consumer buying behavior in a grocery store setting, referencing ITAB's sector experience and focus on increasing conversions and sales.
Generated: DETERMINISTIC_e9c53aa1864f281c
Batch ID: 20250612_154621
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
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Define a function to analyze consumer buying behavior
def analyze_buying_behavior(data):
    """
    Analyze consumer buying behavior in a grocery store setting.

    Parameters:
    data (pandas DataFrame): A DataFrame containing consumer data, including:
        - 'customer_id' (int): Unique customer ID
        - 'purchase_history' (list): List of previous purchases
        - 'demographics' (dict): Customer demographics (e.g. age, location)
        - 'purchase_amount' (float): Total amount spent in current purchase
        - 'converted' (bool): Whether the customer made a purchase (1) or not (0)

    Returns:
    A dictionary containing analysis results, including:
        - 'conversion_rate' (float): Overall conversion rate
        - 'average_purchase_amount' (float): Average purchase amount
        - 'top_products' (list): Top 5 products purchased
        - 'demographic_insights' (dict): Demographic insights (e.g. age, location)
    """

    # Check if data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")

    # Calculate conversion rate
    conversion_rate = data['converted'].mean()

    # Calculate average purchase amount
    avg_purchase_amount = data['purchase_amount'].mean()

    # Get top 5 products purchased
    top_products = data['purchase_history'].explode().value_counts().head(5).index.tolist()

    # Get demographic insights
    demographic_insights = {}
    for demographic, values in data['demographics'].apply(pd.Series).iterrows():
        demographic_insights[demographic] = values.mean()

    # Prepare data for logistic regression
    X = data[['purchase_history', 'demographics']]
    y = data['converted']

    # Convert purchase history to numerical values
    X['purchase_history'] = X['purchase_history'].apply(lambda x: len(x))

    # Convert demographics to numerical values
    X['demographics'] = X['demographics'].apply(lambda x: list(x.values())).apply(lambda x: np.mean(x))

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model performance
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)

    # Return analysis results
    return {
        'conversion_rate': conversion_rate,
        'average_purchase_amount': avg_purchase_amount,
        'top_products': top_products,
        'demographic_insights': demographic_insights,
        'model_performance': {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall
        }
    }

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5],
        'purchase_history': [['milk', 'eggs'], ['bread', 'cheese'], ['milk', 'bread'], ['eggs', 'cheese'], ['milk', 'eggs']],
        'demographics': [{'age': 25, 'location': 'urban'}, {'age': 30, 'location': 'suburban'}, {'age': 35, 'location': 'urban'}, {'age': 20, 'location': 'suburban'}, {'age': 40, 'location': 'urban'}],
        'purchase_amount': [10.99, 20.99, 15.99, 30.99, 25.99],
        'converted': [1, 1, 1, 0, 1]
    })

    # Analyze buying behavior
    results = analyze_buying_behavior(data)

    # Print results
    print("Conversion Rate:", results['conversion_rate'])
    print("Average Purchase Amount:", results['average_purchase_amount'])
    print("Top Products:", results['top_products'])
    print("Demographic Insights:", results['demographic_insights'])
    print("Model Performance:")
    print("  Accuracy:", results['model_performance']['accuracy'])
    print("  Precision:", results['model_performance']['precision'])
    print("  Recall:", results['model_performance']['recall'])
```
