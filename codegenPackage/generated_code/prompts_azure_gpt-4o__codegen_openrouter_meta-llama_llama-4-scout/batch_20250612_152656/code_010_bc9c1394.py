"""
Generated Code Metadata:
========================
Original URL: https://trekk.com
Prompt: Write code to analyze customer data for personalized marketing campaigns, referencing Trekk's use of variable data publishing.
Generated: DETERMINISTIC_bc9c139428e1ad3e
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a function to analyze customer data
def analyze_customer_data(customer_data):
    """
    Analyze customer data for personalized marketing campaigns.

    Args:
        customer_data (pd.DataFrame): A DataFrame containing customer data.

    Returns:
        dict: A dictionary containing insights and recommendations for personalized marketing campaigns.
    """

    # Check if customer data is not empty
    if customer_data.empty:
        raise ValueError("Customer data is empty")

    # Define features (X) and target variable (y)
    try:
        X = customer_data.drop(['purchase_history'], axis=1) # Features
        y = customer_data['purchase_history'] # Target variable
    except KeyError:
        raise ValueError("Customer data must contain 'purchase_history' column")

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a linear regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    # Create a dictionary to store insights and recommendations
    insights = {
        'mean_absolute_error': mae,
        'mean_squared_error': mse,
        'root_mean_squared_error': rmse,
        'recommendations': get_recommendations(customer_data, model)
    }

    return insights

# Define a function to generate recommendations
def get_recommendations(customer_data, model):
    """
    Generate recommendations for personalized marketing campaigns.

    Args:
        customer_data (pd.DataFrame): A DataFrame containing customer data.
        model (LinearRegression): A trained linear regression model.

    Returns:
        list: A list of recommendations for personalized marketing campaigns.
    """

    # Use the model to predict customer purchase history
    predictions = model.predict(customer_data.drop(['purchase_history'], axis=1))

    # Create a list to store recommendations
    recommendations = []

    # Iterate over customers and their predictions
    for index, prediction in enumerate(predictions):
        customer_id = customer_data.index[index]
        if prediction > 0:
            recommendations.append({
                'customer_id': customer_id,
                'campaign': 'targeted_email',
                'product': get_product_recommendation(customer_data, customer_id)
            })
        else:
            recommendations.append({
                'customer_id': customer_id,
                'campaign': 'general_email',
                'product': None
            })

    return recommendations

# Define a function to get product recommendations
def get_product_recommendation(customer_data, customer_id):
    """
    Get product recommendations for a customer.

    Args:
        customer_data (pd.DataFrame): A DataFrame containing customer data.
        customer_id (int): The ID of the customer.

    Returns:
        str: A product recommendation for the customer.
    """

    # Get customer purchase history
    purchase_history = customer_data.loc[customer_id, 'purchase_history']

    # Use a simple collaborative filtering approach to get product recommendations
    similar_customers = customer_data[customer_data['purchase_history'] == purchase_history]
    recommended_product = similar_customers['product'].mode().values[0]

    return recommended_product

# Example usage
if __name__ == "__main__":
    # Create sample customer data
    data = {
        'customer_id': [1, 2, 3, 4, 5],
        'age': [25, 30, 35, 40, 45],
        'purchase_history': [100, 200, 300, 400, 500],
        'product': ['A', 'B', 'C', 'D', 'E']
    }
    customer_data = pd.DataFrame(data)

    # Analyze customer data
    insights = analyze_customer_data(customer_data)

    # Print insights and recommendations
    print("Insights:")
    print(f"Mean Absolute Error: {insights['mean_absolute_error']}")
    print(f"Mean Squared Error: {insights['mean_squared_error']}")
    print(f"Root Mean Squared Error: {insights['root_mean_squared_error']}")
    print("Recommendations:")
    for recommendation in insights['recommendations']:
        print(recommendation)
```
