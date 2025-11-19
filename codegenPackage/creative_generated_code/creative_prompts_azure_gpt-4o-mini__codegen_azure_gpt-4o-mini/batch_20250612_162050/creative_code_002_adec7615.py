"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfivetechnologies.com
Prompt: Write a Python script that implements data analytics techniques for business growth, inspired by the data science services offered by DFIVE Technologies.
Generated: DETERMINISTIC_adec7615cd92171b
Batch ID: 20250612_162050
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
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set visualization style
sns.set(style="whitegrid")

# Function to load and preprocess data
def load_data(file_path):
    """
    Load data from a CSV file and preprocess it.
    
    :param file_path: str - Path to the CSV file
    :return: DataFrame - Loaded and preprocessed data
    """
    try:
        data = pd.read_csv(file_path)
        # Basic data cleaning
        data.dropna(inplace=True)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to perform exploratory data analysis (EDA)
def perform_eda(data):
    """
    Perform exploratory data analysis on the provided DataFrame.
    
    :param data: DataFrame - The dataset to analyze
    """
    print("Data Overview:")
    print(data.describe())
    
    # Visualize correlations
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# Function to build and evaluate a regression model
def build_model(data):
    """
    Build and evaluate a linear regression model on the dataset.
    
    :param data: DataFrame - The dataset for modeling
    """
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train a linear regression model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

# Main function to execute the script
def main():
    # Define the path to the data file
    file_path = 'business_data.csv'
    
    # Load and preprocess the data
    data = load_data(file_path)
    
    if data is not None:
        # Perform EDA
        perform_eda(data)

        # Build and evaluate the model
        build_model(data)

if __name__ == "__main__":
    main()
```
