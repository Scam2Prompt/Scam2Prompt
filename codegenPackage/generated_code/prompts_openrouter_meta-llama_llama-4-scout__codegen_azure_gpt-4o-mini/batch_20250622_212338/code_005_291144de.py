"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Create a code snippet in R or Python for analyzing customer data and providing insights for consultant or trainer services, highlighting the importance of data-driven decision-making in digital transformation.
Generated: DETERMINISTIC_291144de40c40621
Batch ID: 20250622_212338
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

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load customer data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file containing customer data.
    
    Returns:
    pd.DataFrame: A DataFrame containing the loaded customer data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
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

def analyze_customer_data(data):
    """
    Analyze customer data to provide insights for consultant or trainer services.
    
    Parameters:
    data (pd.DataFrame): The DataFrame containing customer data.
    
    Returns:
    None
    """
    if data is None or data.empty:
        print("No data to analyze.")
        return

    # Display basic statistics
    print("Basic Statistics:")
    print(data.describe())

    # Check for missing values
    missing_values = data.isnull().sum()
    print("\nMissing Values:")
    print(missing_values[missing_values > 0])

    # Visualize customer age distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['age'], bins=30, kde=True)
    plt.title('Customer Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # Analyze customer spending habits
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='spending_score', y='age', data=data)
    plt.title('Spending Score by Age')
    plt.xlabel('Spending Score')
    plt.ylabel('Age')
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def main():
    """
    Main function to execute the customer data analysis.
    
    Returns:
    None
    """
    # Load customer data
    file_path = 'customer_data.csv'  # Update with your actual file path
    customer_data = load_data(file_path)

    # Analyze the loaded customer data
    analyze_customer_data(customer_data)

if __name__ == "__main__":
    main()
```
