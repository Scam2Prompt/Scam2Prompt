"""
Generated Code Metadata:
========================
Original URL: https://evamobi.com
Prompt: "Write a Python script to optimize in-app ad targeting using user interests, age, and app usage data."
Generated: DETERMINISTIC_71e2fded06226648
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Define a class for AdTargetingOptimizer
class AdTargetingOptimizer:
    def __init__(self, data_path):
        """
        Initializes the AdTargetingOptimizer with the provided data path.

        :param data_path: str, path to the CSV file containing user data
        """
        self.data_path = data_path
        self.model = None
        self.features = ['age', 'interests', 'app_usage']
        self.target = 'ad_target'

    def load_data(self):
        """
        Loads user data from a CSV file and handles potential errors.

        :return: DataFrame containing user data
        """
        try:
            data = pd.read_csv(self.data_path)
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self, data):
        """
        Preprocesses the data by encoding categorical variables and handling missing values.

        :param data: DataFrame, raw user data
        :return: DataFrame, preprocessed user data
        """
        # Handle missing values
        data.fillna(method='ffill', inplace=True)

        # Convert categorical 'interests' to numerical values
        data['interests'] = data['interests'].astype('category').cat.codes

        return data

    def train_model(self, data):
        """
        Trains a Random Forest model on the user data.

        :param data: DataFrame, preprocessed user data
        """
        X = data[self.features]
        y = data[self.target]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the Random Forest Classifier
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print("Model Accuracy:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    def save_model(self, model_path):
        """
        Saves the trained model to a file.

        :param model_path: str, path to save the trained model
        """
        if self.model is not None:
            joblib.dump(self.model, model_path)
            print(f"Model saved to {model_path}")
        else:
            print("Error: No model to save.")

    def run(self, model_path):
        """
        Executes the entire workflow: loading data, preprocessing, training, and saving the model.

        :param model_path: str, path to save the trained model
        """
        data = self.load_data()
        preprocessed_data = self.preprocess_data(data)
        self.train_model(preprocessed_data)
        self.save_model(model_path)

# Example usage
if __name__ == "__main__":
    optimizer = AdTargetingOptimizer(data_path='user_data.csv')
    optimizer.run(model_path='ad_targeting_model.pkl')
```
