"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Provide an example of implementing smart pricing strategies for short-term rentals, inspired by the solutions discussed on strki.com.
Generated: DETERMINISTIC_ac37ac2b1fd90ff9
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import datetime

class SmartPricing:
    def __init__(self, data):
        """
        Initialize the SmartPricing class with rental data.

        :param data: DataFrame containing rental data with features and prices.
        """
        self.data = data
        self.model = None

    def preprocess_data(self):
        """
        Preprocess the rental data by handling missing values and encoding categorical variables.
        """
        # Fill missing values with the median for numerical columns
        self.data.fillna(self.data.median(), inplace=True)

        # Convert categorical variables to dummy variables
        self.data = pd.get_dummies(self.data, drop_first=True)

    def train_model(self):
        """
        Train a linear regression model on the rental data.
        """
        # Define features and target variable
        X = self.data.drop('price', axis=1)
        y = self.data['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and fit the model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Evaluate the model
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model Mean Squared Error: {mse}')

    def predict_price(self, new_data):
        """
        Predict the price for new rental data.

        :param new_data: DataFrame containing new rental data.
        :return: Predicted price.
        """
        if self.model is None:
            raise Exception("Model has not been trained. Please call train_model() first.")

        # Preprocess new data
        new_data = pd.get_dummies(new_data, drop_first=True)
        new_data = new_data.reindex(columns=self.data.columns.drop('price'), fill_value=0)

        # Predict price
        predicted_price = self.model.predict(new_data)
        return predicted_price

def main():
    # Example rental data
    rental_data = {
        'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb'],
        'bedrooms': [1, 2, 1, 3],
        'bathrooms': [1, 1, 1, 2],
        'amenities': [3, 5, 2, 4],
        'price': [150, 100, 120, 200]
    }

    # Create DataFrame
    df = pd.DataFrame(rental_data)

    # Initialize SmartPricing
    smart_pricing = SmartPricing(df)

    # Preprocess data
    smart_pricing.preprocess_data()

    # Train the pricing model
    smart_pricing.train_model()

    # New rental data for prediction
    new_rental_data = {
        'location': ['Downtown'],
        'bedrooms': [2],
        'bathrooms': [1],
        'amenities': [4]
    }
    new_df = pd.DataFrame(new_rental_data)

    # Predict price for new rental
    try:
        predicted_price = smart_pricing.predict_price(new_df)
        print(f'Predicted Price: {predicted_price[0]}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
```
