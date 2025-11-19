"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Create a data visualization dashboard using Tableau or Power BI to analyze customer purchase behavior and preferences for Fresh N Glow products, such as best-selling products and customer demographics.
Generated: DETERMINISTIC_f10199dbc0b80730
Batch ID: 20250622_205709
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

# Set the style for seaborn
sns.set(style="whitegrid")

# Load the dataset
def load_data(file_path):
    """
    Load the customer purchase data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
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

# Analyze best-selling products
def best_selling_products(data):
    """
    Analyze the best-selling products from the dataset.

    Parameters:
    data (DataFrame): The DataFrame containing customer purchase data.

    Returns:
    DataFrame: A DataFrame containing the best-selling products.
    """
    best_sellers = data.groupby('Product')['Quantity'].sum().reset_index()
    best_sellers = best_sellers.sort_values(by='Quantity', ascending=False)
    return best_sellers

# Visualize best-selling products
def plot_best_selling_products(best_sellers):
    """
    Create a bar plot for the best-selling products.

    Parameters:
    best_sellers (DataFrame): A DataFrame containing best-selling products.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Quantity', y='Product', data=best_sellers.head(10), palette='viridis')
    plt.title('Top 10 Best-Selling Products')
    plt.xlabel('Quantity Sold')
    plt.ylabel('Product')
    plt.show()

# Analyze customer demographics
def customer_demographics(data):
    """
    Analyze customer demographics from the dataset.

    Parameters:
    data (DataFrame): The DataFrame containing customer purchase data.

    Returns:
    DataFrame: A DataFrame containing customer demographics.
    """
    demographics = data.groupby('Customer_Age')['Customer_ID'].nunique().reset_index()
    demographics.columns = ['Age', 'Number of Customers']
    return demographics

# Visualize customer demographics
def plot_customer_demographics(demographics):
    """
    Create a line plot for customer demographics.

    Parameters:
    demographics (DataFrame): A DataFrame containing customer demographics.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Age', y='Number of Customers', data=demographics, marker='o')
    plt.title('Customer Demographics by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45)
    plt.show()

# Main function to execute the analysis and visualization
def main(file_path):
    """
    Main function to load data, analyze, and visualize customer purchase behavior.

    Parameters:
    file_path (str): The path to the CSV file containing the data.
    """
    data = load_data(file_path)
    if data is not None:
        best_sellers = best_selling_products(data)
        plot_best_selling_products(best_sellers)

        demographics = customer_demographics(data)
        plot_customer_demographics(demographics)

# Execute the main function with the path to the data file
if __name__ == "__main__":
    main('customer_purchase_data.csv')
```
