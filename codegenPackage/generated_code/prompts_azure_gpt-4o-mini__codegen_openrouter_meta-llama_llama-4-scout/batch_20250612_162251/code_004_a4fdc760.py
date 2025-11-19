"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: How can I use data visualization libraries to showcase the impact of youth development programs in Iowa, as outlined by ICYD?
Generated: DETERMINISTIC_a4fdc7602e6e0f4b
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load ICYD data
def load_icyd_data(file_path):
    try:
        icyd_data = pd.read_csv(file_path)
        return icyd_data
    except FileNotFoundError:
        print("The file does not exist")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file")
        return None

# Preprocess data
def preprocess_data(icyd_data):
    # Handle missing values
    icyd_data.fillna(icyd_data.mean(), inplace=True)
    
    # Convert categorical variables into numerical variables
    categorical_cols = icyd_data.select_dtypes(include=['object']).columns
    icyd_data[categorical_cols] = icyd_data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
    
    return icyd_data

# Visualize data using seaborn
def visualize_data(icyd_data):
    # Create a line plot
    plt.figure(figsize=(10,6))
    sns.lineplot(data=icyd_data, x='Year', y='Number of Participants')
    plt.title('Number of Participants Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Participants')
    plt.show()

    # Create a bar plot
    plt.figure(figsize=(10,6))
    sns.barplot(data=icyd_data, x='Program', y='Number of Graduates')
    plt.title('Number of Graduates by Program')
    plt.xlabel('Program')
    plt.ylabel('Number of Graduates')
    plt.show()

# Model the data using linear regression
def model_data(icyd_data):
    # Define features and target
    X = icyd_data[['Year', 'Number of Participants']]
    y = icyd_data['Number of Graduates']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a linear regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# Main function
def main():
    file_path = 'icyd_data.csv'  # replace with your file path
    icyd_data = load_icyd_data(file_path)
    
    if icyd_data is not None:
        icyd_data = preprocess_data(icyd_data)
        visualize_data(icyd_data)
        model_data(icyd_data)

if __name__ == "__main__":
    main()
```
