"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Provide Python code to model silver demand trends, incorporating industrial uses and safe-haven asset appeal, as outlined in Brexphil Inc.'s precious metals investment section.
Generated: DETERMINISTIC_ff5ef63536e39032
Batch ID: 20250612_150446
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
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class SilverDemandModel:
    """
    A class to model silver demand trends incorporating industrial uses
    and safe-haven asset appeal.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SilverDemandModel with a DataFrame containing demand data.

        Parameters:
        data (pd.DataFrame): DataFrame containing columns for 'Year', 'Industrial_Uses',
                             'Investment_Demand', and 'Total_Demand'.
        """
        self.data = data
        self.model = LinearRegression()

    def preprocess_data(self):
        """Prepares the data for modeling by splitting into features and target."""
        try:
            # Ensure required columns exist
            required_columns = ['Year', 'Industrial_Uses', 'Investment_Demand', 'Total_Demand']
            for col in required_columns:
                if col not in self.data.columns:
                    raise ValueError(f"Missing required column: {col}")

            # Features and target variable
            X = self.data[['Industrial_Uses', 'Investment_Demand']]
            y = self.data['Total_Demand']

            return X, y
        except Exception as e:
            print(f"Error in preprocessing data: {e}")
            raise

    def train_model(self) -> None:
        """Trains the linear regression model on the demand data."""
        try:
            X, y = self.preprocess_data()
            # Split data into training and test sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Fit the model
            self.model.fit(X_train, y_train)

            # Evaluate the model
            score = self.model.score(X_test, y_test)
            print(f"Model training complete. R^2 score: {score:.4f}")
        except Exception as e:
            print(f"Error in training model: {e}")
            raise

    def predict_demand(self, industrial_use: float, investment_demand: float) -> float:
        """
        Predicts the total silver demand based on industrial uses and investment demand.

        Parameters:
        industrial_use (float): Projected industrial use for silver.
        investment_demand (float): Projected investment demand for silver.

        Returns:
        float: Predicted total silver demand.
        """
        try:
            input_data = np.array([[industrial_use, investment_demand]])
            prediction = self.model.predict(input_data)
            return prediction[0]
        except Exception as e:
            print(f"Error in predicting demand: {e}")
            raise

    def plot_demand_trends(self) -> None:
        """Plots the demand trends over the years."""
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(self.data['Year'], self.data['Total_Demand'], label='Total Demand', marker='o')
            plt.plot(self.data['Year'], self.data['Industrial_Uses'], label='Industrial Uses', marker='o')
            plt.plot(self.data['Year'], self.data['Investment_Demand'], label='Investment Demand', marker='o')
            plt.title('Silver Demand Trends')
            plt.xlabel('Year')
            plt.ylabel('Demand (in tons)')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error in plotting demand trends: {e}")
            raise

# Usage example (assuming data is available in a DataFrame):
# data = pd.DataFrame({
#     'Year': [2020, 2021, 2022, 2023],
#     'Industrial_Uses': [500, 550, 600, 650],
#     'Investment_Demand': [300, 400, 450, 500],
#     'Total_Demand': [800, 950, 1050, 1150]
# })

# model = SilverDemandModel(data)
# model.train_model()
# prediction = model.predict_demand(700, 600)
# print(f"Predicted Total Demand: {prediction:.2f} tons")
# model.plot_demand_trends()
```
