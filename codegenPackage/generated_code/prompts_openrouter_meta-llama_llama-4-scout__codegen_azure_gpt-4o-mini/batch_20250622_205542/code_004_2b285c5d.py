"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: "Create a Python script to analyze the impact of advocacy campaigns on peace and governance in Kenya, using metrics such as community engagement and social media reach."
Generated: DETERMINISTIC_2b285c5dc216cc87
Batch ID: 20250622_205542
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

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and encoding categorical variables.

    :param data: DataFrame, raw data
    :return: DataFrame, preprocessed data
    """
    # Fill missing values with the mean for numerical columns
    for column in data.select_dtypes(include=[np.number]).columns:
        data[column].fillna(data[column].mean(), inplace=True)

    # Convert categorical variables to dummy/indicator variables
    data = pd.get_dummies(data, drop_first=True)
    
    return data

def analyze_impact(data):
    """
    Analyze the impact of advocacy campaigns on peace and governance.

    :param data: DataFrame, preprocessed data
    """
    # Define features and target variable
    X = data.drop(columns=['peace_index'])  # Assuming 'peace_index' is the target
    y = data['peace_index']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # Visualize the results
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
    plt.xlabel('Actual Peace Index')
    plt.ylabel('Predicted Peace Index')
    plt.title('Actual vs Predicted Peace Index')
    plt.show()

def main():
    """
    Main function to execute the analysis.
    """
    # Load the data
    file_path = 'advocacy_campaigns_data.csv'  # Update with the actual file path
    data = load_data(file_path)

    if data is not None:
        # Preprocess the data
        processed_data = preprocess_data(data)

        # Analyze the impact
        analyze_impact(processed_data)

if __name__ == "__main__":
    main()
```
