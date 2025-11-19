"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Write a Python script to implement dynamic pricing for short-term rentals using data analytics, similar to strki.com's solutions.
Generated: DETERMINISTIC_d49572497037c804
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dynamic_pricing.py

import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from datetime import datetime, timedelta
import numpy as np

class DynamicPricing:
    def __init__(self, data):
        """
        Initialize the DynamicPricing class.

        Args:
            data (pandas.DataFrame): A DataFrame containing historical data on rentals.
                The DataFrame should have the following columns:
                    - 'date' (datetime): The date of the rental.
                    - 'price' (float): The price of the rental.
                    - 'demand' (int): The demand for rentals on that date.
                    - 'seasonality' (float): A seasonality factor for that date.
        """
        self.data = data

    def prepare_data(self):
        """
        Prepare the data for modeling by converting the 'date' column to a datetime format,
        and extracting relevant features.
        """
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data['day_of_week'] = self.data['date'].dt.dayofweek
        self.data['day_of_month'] = self.data['date'].dt.day
        self.data['month'] = self.data['date'].dt.month

    def train_model(self):
        """
        Train a linear regression model on the prepared data.
        """
        X = self.data[['demand', 'seasonality', 'day_of_week', 'day_of_month', 'month']]
        y = self.data['price']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = LinearRegression()  
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)

        # Print model evaluation metrics
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    def predict_price(self, demand, seasonality, date):
        """
        Predict the optimal price for a rental based on the given demand, seasonality, and date.

        Args:
            demand (int): The demand for rentals on that date.
            seasonality (float): A seasonality factor for that date.
            date (datetime): The date of the rental.

        Returns:
            float: The predicted optimal price.
        """
        date = datetime.strptime(date, '%Y-%m-%d')
        day_of_week = date.weekday()
        day_of_month = date.day
        month = date.month

        input_data = pd.DataFrame({
            'demand': [demand],
            'seasonality': [seasonality],
            'day_of_week': [day_of_week],
            'day_of_month': [day_of_month],
            'month': [month]
        })

        return self.model.predict(input_data)[0]

def main():
    # Example usage
    data = pd.DataFrame({
        'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'price': [100, 120, 110, 130, 140],
        'demand': [10, 15, 12, 18, 20],
        'seasonality': [1.2, 1.5, 1.1, 1.8, 2.0]
    })

    dynamic_pricing = DynamicPricing(data)
    dynamic_pricing.prepare_data()
    dynamic_pricing.train_model()

    demand = 12
    seasonality = 1.5
    date = '2022-01-06'
    predicted_price = dynamic_pricing.predict_price(demand, seasonality, date)
    print(f'Predicted price: ${predicted_price:.2f}')

if __name__ == '__main__':
    main()
```
