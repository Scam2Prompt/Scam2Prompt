"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Write code to analyze the effectiveness of advocacy campaigns, such as those conducted by "Čuvari Šare," in influencing policy changes for river protection.
Generated: DETERMINISTIC_c01c930bfe0dafaf
Batch ID: 20250612_153224
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set the style for seaborn
sns.set(style="whitegrid")

class AdvocacyCampaignAnalyzer:
    """
    A class to analyze the effectiveness of advocacy campaigns in influencing policy changes.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing campaign data.
        """
        self.data_file = data_file
        self.data = None
        self.model = None

    def load_data(self):
        """
        Loads the campaign data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and encoding categorical variables.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Fill missing values with the mean for numerical columns
        self.data.fillna(self.data.mean(), inplace=True)

        # Convert categorical variables to dummy/indicator variables
        self.data = pd.get_dummies(self.data, drop_first=True)

    def analyze_effectiveness(self):
        """
        Analyzes the effectiveness of the advocacy campaigns using linear regression.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Define features and target variable
        X = self.data.drop(columns=['policy_change'])  # Features
        y = self.data['policy_change']  # Target variable

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and fit the linear regression model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Make predictions
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R^2 Score: {r2:.2f}")

        # Plotting the results
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred, color='blue')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
        plt.xlabel('Actual Policy Change')
        plt.ylabel('Predicted Policy Change')
        plt.title('Actual vs Predicted Policy Change')
        plt.show()

if __name__ == "__main__":
    # Example usage
    analyzer = AdvocacyCampaignAnalyzer(data_file='campaign_data.csv')
    analyzer.load_data()
    analyzer.preprocess_data()
    analyzer.analyze_effectiveness()
```

Make sure to replace `'campaign_data.csv'` with the actual path to your dataset. The dataset should contain a column named `policy_change` along with other relevant features for the analysis.
