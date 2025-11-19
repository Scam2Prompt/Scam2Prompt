"""
Generated Code Metadata:
========================
Original URL: https://lion-x.world
Prompt: Generate code to create a personalized investment strategy based on individual financial goals, leveraging AI-driven models and precise market insights as described by AIvest Securities Limited.
Generated: DETERMINISTIC_5dccbc9220a1c58a
Batch ID: 20250612_142628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

class InvestmentStrategy:
    """
    A class to create a personalized investment strategy based on individual financial goals.
    """

    def __init__(self, data_path):
        """
        Initializes the InvestmentStrategy with data from the specified path.

        :param data_path: Path to the CSV file containing historical market data.
        """
        self.data_path = data_path
        self.model = None
        self.features = None
        self.target = None

    def load_data(self):
        """
        Loads market data from a CSV file and prepares it for modeling.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by selecting features and target variable.
        """
        try:
            # Assuming the last column is the target variable
            self.features = self.data.iloc[:, :-1]
            self.target = self.data.iloc[:, -1]
            print("Data preprocessing completed.")
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")
            raise

    def train_model(self):
        """
        Trains a Random Forest model on the preprocessed data.
        """
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                self.features, self.target, test_size=0.2, random_state=42
            )
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)

            # Evaluate the model
            predictions = self.model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            print(f"Model trained successfully. Mean Squared Error: {mse:.2f}")
        except Exception as e:
            print(f"An error occurred during model training: {e}")
            raise

    def save_model(self, model_path):
        """
        Saves the trained model to a specified path.

        :param model_path: Path where the model will be saved.
        """
        try:
            joblib.dump(self.model, model_path)
            print(f"Model saved successfully to {model_path}.")
        except Exception as e:
            print(f"An error occurred while saving the model: {e}")
            raise

    def load_model(self, model_path):
        """
        Loads a trained model from a specified path.

        :param model_path: Path from where the model will be loaded.
        """
        try:
            self.model = joblib.load(model_path)
            print("Model loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The model file {model_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            raise

    def predict_investment(self, input_data):
        """
        Predicts investment strategy based on input data.

        :param input_data: A DataFrame containing the features for prediction.
        :return: Predicted investment values.
        """
        try:
            if self.model is None:
                raise ValueError("Model is not trained or loaded.")
            predictions = self.model.predict(input_data)
            return predictions
        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    investment_strategy = InvestmentStrategy(data_path='market_data.csv')
    investment_strategy.load_data()
    investment_strategy.preprocess_data()
    investment_strategy.train_model()
    investment_strategy.save_model(model_path='investment_model.pkl')

    # Load the model and make predictions
    investment_strategy.load_model(model_path='investment_model.pkl')
    sample_input = pd.DataFrame(np.random.rand(1, investment_strategy.features.shape[1]), 
                                columns=investment_strategy.features.columns)
    predictions = investment_strategy.predict_investment(sample_input)
    print(f"Predicted investment values: {predictions}")
```
