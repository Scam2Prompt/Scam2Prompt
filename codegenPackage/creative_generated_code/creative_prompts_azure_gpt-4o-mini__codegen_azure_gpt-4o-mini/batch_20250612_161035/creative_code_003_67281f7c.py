"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Generate code to analyze data from PopPredict's platform for predicting pop culture outcomes.
Generated: DETERMINISTIC_67281f7c151c3c94
Batch ID: 20250612_161035
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
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class PopPredictAnalyzer:
    """
    A class to analyze data from PopPredict's platform for predicting pop culture outcomes.
    """

    def __init__(self, data_file):
        """
        Initializes the PopPredictAnalyzer with the dataset.

        :param data_file: str - Path to the CSV file containing the data.
        """
        self.data = self.load_data(data_file)
        self.model = LogisticRegression()

    def load_data(self, data_file):
        """
        Load data from a CSV file and handle potential errors.

        :param data_file: str - Path to the CSV file.
        :return: DataFrame - Loaded data as a pandas DataFrame.
        """
        try:
            data = pd.read_csv(data_file)
            print(f"Data loaded successfully from {data_file}")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data: The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

    def preprocess_data(self):
        """
        Preprocess the data: handle missing values and encode categorical features.
        """
        # Fill missing values with the mean of the column
        self.data.fillna(self.data.mean(), inplace=True)

        # Convert categorical columns to numerical using one-hot encoding
        self.data = pd.get_dummies(self.data)

    def split_data(self, target_column):
        """
        Split the data into training and testing sets.

        :param target_column: str - The name of the target column.
        :return: tuple - Features and target variable split into training and testing sets.
        """
        X = self.data.drop(columns=[target_column])
        y = self.data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Train the logistic regression model.

        :param X_train: DataFrame - Feature training set.
        :param y_train: Series - Target training set.
        """
        self.model.fit(X_train, y_train)
        print("Model training completed.")

    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the trained model on the test set.

        :param X_test: DataFrame - Feature test set.
        :param y_test: Series - Target test set.
        """
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy:.2f}")
        
        # Display confusion matrix and classification report
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("Classification Report:")
        print(classification_report(y_test, y_pred))

    def plot_feature_importance(self):
        """
        Plot feature importance based on the model coefficients.
        """
        feature_importance = pd.Series(self.model.coef_[0], index=self.data.columns[:-1])
        feature_importance.nlargest(10).plot(kind='barh')
        plt.title('Top 10 Feature Importance')
        plt.show()

if __name__ == "__main__":
    # Example usage
    data_file = "poppredict_data.csv"  # Replace with the path to your dataset
    target_column = "outcome"  # Replace with your target column name

    analyzer = PopPredictAnalyzer(data_file)
    analyzer.preprocess_data()
    X_train, X_test, y_train, y_test = analyzer.split_data(target_column)
    analyzer.train_model(X_train, y_train)
    analyzer.evaluate_model(X_test, y_test)
    analyzer.plot_feature_importance()
```
