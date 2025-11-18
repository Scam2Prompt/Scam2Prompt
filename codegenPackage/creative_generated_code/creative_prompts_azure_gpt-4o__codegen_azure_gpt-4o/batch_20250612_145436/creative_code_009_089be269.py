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

def analyze_ecommerce_data(file_path):
    """
    Analyze product data from an e-commerce site and generate insights such as 
    the most popular categories and average prices for each category.

    Args:
        file_path (str): Path to the CSV file containing product data.

    Returns:
        dict: A dictionary containing insights about the product data.
    """
    try:
        # Load the product data into a Pandas DataFrame
        data = pd.read_csv(file_path)

        # Ensure required columns exist
        required_columns = {'category', 'price', 'product_id'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Input data must contain the following columns: {', '.join(required_columns)}")

        # Drop rows with missing or invalid data in critical columns
        data = data.dropna(subset=['category', 'price'])
        data = data[data['price'] >= 0]  # Ensure prices are non-negative

        # Calculate average price for each category
        avg_price_per_category = data.groupby('category')['price'].mean().sort_values(ascending=False)

        # Calculate the most popular categories based on product counts
        popular_categories = data['category'].value_counts()

        # Prepare insights
        insights = {
            "average_price_per_category": avg_price_per_category.to_dict(),
            "most_popular_categories": popular_categories.to_dict()
        }

        return insights

    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file path.")
        return {}
    except pd.errors.EmptyDataError:
        print("Error: The input file is empty or corrupted.")
        return {}
    except ValueError as ve:
        print(f"Error: {ve}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

if __name__ == "__main__":
    # Example usage
    # Replace 'data/products.csv' with the path to your actual CSV file
    file_path = 'data/products.csv'
    insights = analyze_ecommerce_data(file_path)

    if insights:
        print("Insights from the e-commerce data:")
        print("\nAverage Price per Category:")
        for category, avg_price in insights["average_price_per_category"].items():
            print(f"  {category}: ${avg_price:.2f}")

        print("\nMost Popular Categories:")
        for category, count in insights["most_popular_categories"].items():
            print(f"  {category}: {count} products")
```
