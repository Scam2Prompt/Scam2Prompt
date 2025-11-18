"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-link.io
Prompt: Suggest tools or libraries to model the economic impact of new manufacturing technologies, as highlighted in MIT's Initiative for New Manufacturing.
Generated: DETERMINISTIC_341c2550fb516096
Batch ID: 20250612_154721
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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Define a class for Economic Impact Modeling
class EconomicImpactModel:
    """
    A class to model the economic impact of new manufacturing technologies.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing relevant economic data.
    """

    def __init__(self, data_path):
        """
        Initializes the EconomicImpactModel with data from the specified CSV file.

        Parameters:
            data_path (str): The file path to the CSV file containing economic data.
        """
        try:
            self.data = pd.read_csv(data_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file at {data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """Preprocess the data by handling missing values and encoding categorical variables."""
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)
        
        # Convert categorical columns to numeric if necessary
        self.data = pd.get_dummies(self.data, drop_first=True)

    def train_model(self, target_variable):
        """
        Train a linear regression model to predict economic impact.

        Parameters:
            target_variable (str): The name of the target variable in the dataset.
        
        Returns:
            model (LinearRegression): The trained linear regression model.
            X_test (pd.DataFrame): The test dataset for predictions.
            y_test (pd.Series): The actual values for the target variable in the test dataset.
        """
        # Split into features and target
        X = self.data.drop(columns=[target_variable])
        y = self.data[target_variable]
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predictions
        predictions = model.predict(X_test)

        # Evaluate the model
        self.evaluate_model(y_test, predictions)

        return model, X_test, y_test

    @staticmethod
    def evaluate_model(y_true, y_pred):
        """
        Evaluate the performance of the model using RMSE and R-squared metrics.

        Parameters:
            y_true (pd.Series): The actual values for the target variable.
            y_pred (np.ndarray): The predicted values from the model.
        """
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        r2 = r2_score(y_true, y_pred)
        print(f"Root Mean Squared Error: {rmse:.2f}")
        print(f"R-squared: {r2:.2f}")

    def visualize_data(self):
        """Visualize the economic data using seaborn."""
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Heatmap of Economic Data')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Path to the economic data CSV file
    data_file = 'economic_data.csv'
    
    # Create an instance of EconomicImpactModel
    model = EconomicImpactModel(data_file)
    
    # Preprocess the data
    model.preprocess_data()
    
    # Train the model and specify the target variable
    trained_model, test_data, actual_values = model.train_model(target_variable='economic_impact')

    # Visualize the data
    model.visualize_data()
```
