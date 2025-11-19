"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Create a Power BI dashboard to visualize the cement production capacity, sales, and revenue of Twiga Cement over the years.
Generated: DETERMINISTIC_24bf7d1e9b3c6aa9
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the data.
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
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

# Function to visualize cement production capacity
def visualize_production_capacity(data):
    """
    Visualize the cement production capacity over the years.

    Parameters:
    data (DataFrame): The DataFrame containing the cement production data.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Year', y='Production_Capacity', marker='o')
    plt.title('Cement Production Capacity Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Production Capacity (tons)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to visualize sales
def visualize_sales(data):
    """
    Visualize the sales of cement over the years.

    Parameters:
    data (DataFrame): The DataFrame containing the cement sales data.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x='Year', y='Sales', palette='Blues')
    plt.title('Cement Sales Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Sales (tons)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to visualize revenue
def visualize_revenue(data):
    """
    Visualize the revenue generated from cement sales over the years.

    Parameters:
    data (DataFrame): The DataFrame containing the cement revenue data.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Year', y='Revenue', marker='o', color='orange')
    plt.title('Cement Revenue Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Revenue (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to execute the visualization
def main():
    # Load the data
    file_path = 'twiga_cement_data.csv'  # Update with the correct path to your CSV file
    data = load_data(file_path)

    if data is not None:
        # Visualize the data
        visualize_production_capacity(data)
        visualize_sales(data)
        visualize_revenue(data)

# Entry point of the script
if __name__ == "__main__":
    main()
```

Make sure to have a CSV file named `twiga_cement_data.csv` with the following columns: `Year`, `Production_Capacity`, `Sales`, and `Revenue` for the code to run successfully.
