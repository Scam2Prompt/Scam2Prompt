"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: "Provide an example of a software solution that improves decision-making and saves time for businesses."
Generated: DETERMINISTIC_c10cb9d784914627
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# business_decision_support_system.py

import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class BusinessDecisionSupportSystem:
    """
    A system that provides data-driven insights to support business decision-making.
    """

    def __init__(self, data):
        """
        Initializes the system with a dataset.

        Args:
            data (pd.DataFrame): A pandas DataFrame containing the data.
        """
        self.data = data

    def prepare_data(self):
        """
        Prepares the data for analysis by handling missing values and encoding categorical variables.

        Returns:
            pd.DataFrame: The prepared data.
        """
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)

        # Encode categorical variables
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        self.data[categorical_cols] = self.data[categorical_cols].apply(lambda x: pd.factorize(x)[0])

        return self.data

    def train_model(self, target_variable):
        """
        Trains a linear regression model on the prepared data.

        Args:
            target_variable (str): The name of the target variable.

        Returns:
            LinearRegression: The trained model.
        """
        # Prepare the data
        prepared_data = self.prepare_data()

        # Split the data into features and target
        X = prepared_data.drop(target_variable, axis=1)
        y = prepared_data[target_variable]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        print(f"Model Evaluation Metrics:")
        print(f"Mean Absolute Error: {metrics.mean_absolute_error(y_test, y_pred)}")
        print(f"Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred)}")
        print(f"Root Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred, squared=False)}")

        return model

    def make_prediction(self, model, input_data):
        """
        Makes a prediction using the trained model.

        Args:
            model (LinearRegression): The trained model.
            input_data (pd.DataFrame): A pandas DataFrame containing the input data.

        Returns:
            float: The predicted value.
        """
        # Prepare the input data
        prepared_input_data = self.prepare_data().head(0).merge(input_data, how='left', left_index=True, right_index=True).fillna(0)

        # Make the prediction
        prediction = model.predict(prepared_input_data)

        return prediction


def main():
    # Example usage
    data = pd.DataFrame({
        'Advertising': [100, 200, 300, 400, 500],
        'Sales': [10, 20, 30, 40, 50]
    })

    system = BusinessDecisionSupportSystem(data)
    model = system.train_model('Sales')

    input_data = pd.DataFrame({
        'Advertising': [600]
    })

    prediction = system.make_prediction(model, input_data)
    print(f"Predicted Sales: {prediction[0]}")


if __name__ == "__main__":
    main()
```
