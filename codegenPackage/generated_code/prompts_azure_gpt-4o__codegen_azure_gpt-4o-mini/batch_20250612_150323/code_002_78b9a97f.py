"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Generate code to perform short-term rental market analysis using data-driven strategies similar to those outlined on strki.com.
Generated: DETERMINISTIC_78b9a97fac743d71
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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set the style for seaborn
sns.set(style="whitegrid")

class ShortTermRentalAnalysis:
    def __init__(self, data_path):
        """
        Initializes the ShortTermRentalAnalysis class with the dataset.

        :param data_path: str, path to the CSV file containing rental data
        """
        self.data_path = data_path
        self.data = None
        self.model = None

    def load_data(self):
        """
        Loads the rental data from a CSV file and performs basic preprocessing.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            self.preprocess_data()
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and encoding categorical variables.
        """
        # Drop rows with missing target values
        self.data.dropna(subset=['price'], inplace=True)

        # Fill missing values for other columns with median or mode
        self.data.fillna(self.data.median(), inplace=True)

        # Convert categorical variables to dummy variables
        self.data = pd.get_dummies(self.data, drop_first=True)

    def analyze_data(self):
        """
        Performs exploratory data analysis (EDA) on the rental data.
        """
        # Display basic statistics
        print(self.data.describe())

        # Visualize the distribution of rental prices
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['price'], bins=30, kde=True)
        plt.title('Distribution of Rental Prices')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()

    def train_model(self):
        """
        Trains a linear regression model to predict rental prices.
        """
        # Define features and target variable
        X = self.data.drop('price', axis=1)
        y = self.data['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Make predictions
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f'Mean Squared Error: {mse:.2f}')
        print(f'R^2 Score: {r2:.2f}')

    def predict_price(self, new_data):
        """
        Predicts the rental price for new data using the trained model.

        :param new_data: DataFrame, new rental data for prediction
        :return: float, predicted rental price
        """
        if self.model is None:
            raise Exception("Model has not been trained yet. Please call train_model() first.")

        # Ensure new_data is preprocessed similarly to the training data
        new_data = pd.get_dummies(new_data, drop_first=True)
        new_data = new_data.reindex(columns=self.data.columns.drop('price'), fill_value=0)

        return self.model.predict(new_data)

# Example usage
if __name__ == "__main__":
    rental_analysis = ShortTermRentalAnalysis(data_path='rental_data.csv')
    rental_analysis.load_data()
    rental_analysis.analyze_data()
    rental_analysis.train_model()

    # Example of predicting a new rental price
    # new_rental_data = pd.DataFrame({...})  # Replace with actual new data
    # predicted_price = rental_analysis.predict_price(new_rental_data)
    # print(f'Predicted Rental Price: {predicted_price}')
```
