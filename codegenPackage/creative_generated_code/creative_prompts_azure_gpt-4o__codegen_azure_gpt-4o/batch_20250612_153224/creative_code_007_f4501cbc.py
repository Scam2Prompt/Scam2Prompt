"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Generate Python code to analyze sales data for products like "Intense Coffee Blend" and generate a report on the most popular items in the "Coffee" category.
Generated: DETERMINISTIC_f4501cbc38bd3475
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_sales_data(file_path):
    """
    Analyzes sales data to generate a report on the most popular items in the 'Coffee' category.

    Args:
        file_path (str): Path to the sales data CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the most popular 'Coffee' products sorted by sales quantity.
    """
    try:
        # Load the sales data from the CSV file into a DataFrame
        sales_data = pd.read_csv(file_path)
        
        # Ensure required columns are present
        required_columns = {'Product Name', 'Category', 'Quantity Sold'}
        if not required_columns.issubset(sales_data.columns):
            raise ValueError(f"Missing required columns. Expected columns: {required_columns}")

        # Filter data to include only products in the 'Coffee' category
        coffee_data = sales_data[sales_data['Category'].str.lower() == 'coffee']

        # Aggregate sales data by product name
        coffee_sales_summary = coffee_data.groupby('Product Name', as_index=False).sum()

        # Sort products by quantity sold in descending order
        coffee_sales_summary = coffee_sales_summary.sort_values(
            by='Quantity Sold', ascending=False
        )

        # Generate top-selling products report
        print("Top-selling Coffee products:")
        print(coffee_sales_summary)

        # Return the summary DataFrame for further processing if needed
        return coffee_sales_summary

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'. Please check the file location.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid sales data file.")
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Example usage:
# Replace 'sales_data.csv' with the actual path to your sales data file.
if __name__ == "__main__":
    file_path = 'sales_data.csv'
    top_coffee_products = analyze_sales_data(file_path)
```
