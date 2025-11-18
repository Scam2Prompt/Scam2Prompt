"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Write a Python script using the Pandas library to analyze product data from an e-commerce site and generate insights, such as the most popular categories and average prices for each category.
Generated: DETERMINISTIC_089be26911ab0e5b
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Function to analyze product data
def analyze_product_data(file_path):
    """
    Analyzes the product data from the given CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing product data.

    Returns:
    pd.DataFrame: A DataFrame containing insights about categories and average prices.
    """
    try:
        # Load the product data
        product_data = pd.read_csv(file_path)

        # Display the first few rows of the dataset for initial inspection
        print("Initial data preview:")
        print(product_data.head())

        # Check for necessary columns
        if 'category' not in product_data.columns or 'price' not in product_data.columns:
            raise ValueError("Input data must contain 'category' and 'price' columns.")

        # Calculate the average price for each category
        average_price_per_category = product_data.groupby('category')['price'].mean().reset_index()

        # Count the number of products in each category
        product_count_per_category = product_data['category'].value_counts().reset_index()
        product_count_per_category.columns = ['category', 'product_count']

        # Merge average price data with product count data
        insights = pd.merge(average_price_per_category, product_count_per_category, on='category')

        # Rename columns for clarity
        insights.columns = ['Category', 'Average Price', 'Product Count']

        # Sort insights by product count in descending order
        insights = insights.sort_values(by='Product Count', ascending=False).reset_index(drop=True)

        # Print the insights DataFrame
        print("\nInsights on product categories:")
        print(insights)

        return insights

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'product_data.csv' with the actual path to your CSV file
    file_path = 'product_data.csv'
    analyze_product_data(file_path)
```
