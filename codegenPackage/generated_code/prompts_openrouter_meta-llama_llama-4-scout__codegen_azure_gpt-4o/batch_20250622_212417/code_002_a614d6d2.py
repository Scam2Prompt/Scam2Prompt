"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Generate a Python script that analyzes customer purchase behavior for an e-commerce platform like Cody Alt's ventures, with insights into product popularity and sales trends.
Generated: DETERMINISTIC_a614d6d2c8cbd428
Batch ID: 20250622_212417
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='purchase_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file_path):
    """
    Load purchase data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the purchase data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
    except pd.errors.EmptyDataError:
        logging.error("File is empty: %s", file_path)
        raise
    except Exception as e:
        logging.error("Error loading data: %s", str(e))
        raise

def preprocess_data(data):
    """
    Preprocess the purchase data.

    Args:
        data (pd.DataFrame): Raw purchase data.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Ensure required columns exist
        required_columns = ['product_id', 'product_name', 'quantity', 'price', 'purchase_date']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Convert purchase_date to datetime
        data['purchase_date'] = pd.to_datetime(data['purchase_date'], errors='coerce')

        # Drop rows with invalid dates or missing values
        data = data.dropna(subset=['purchase_date', 'product_id', 'product_name', 'quantity', 'price'])

        # Ensure quantity and price are numeric
        data['quantity'] = pd.to_numeric(data['quantity'], errors='coerce')
        data['price'] = pd.to_numeric(data['price'], errors='coerce')

        # Drop rows with invalid numeric values
        data = data.dropna(subset=['quantity', 'price'])

        logging.info("Data preprocessing completed successfully")
        return data
    except Exception as e:
        logging.error("Error during preprocessing: %s", str(e))
        raise

def analyze_product_popularity(data):
    """
    Analyze product popularity based on quantity sold.

    Args:
        data (pd.DataFrame): Preprocessed purchase data.

    Returns:
        pd.DataFrame: DataFrame containing product popularity insights.
    """
    try:
        popularity = data.groupby(['product_id', 'product_name'])['quantity'].sum().reset_index()
        popularity = popularity.sort_values(by='quantity', ascending=False)
        logging.info("Product popularity analysis completed successfully")
        return popularity
    except Exception as e:
        logging.error("Error during product popularity analysis: %s", str(e))
        raise

def analyze_sales_trends(data):
    """
    Analyze sales trends over time.

    Args:
        data (pd.DataFrame): Preprocessed purchase data.

    Returns:
        pd.DataFrame: DataFrame containing sales trends insights.
    """
    try:
        data['sales'] = data['quantity'] * data['price']
        trends = data.groupby(data['purchase_date'].dt.to_period('M'))['sales'].sum().reset_index()
        trends['purchase_date'] = trends['purchase_date'].dt.to_timestamp()
        logging.info("Sales trends analysis completed successfully")
        return trends
    except Exception as e:
        logging.error("Error during sales trends analysis: %s", str(e))
        raise

def plot_product_popularity(popularity):
    """
    Plot product popularity.

    Args:
        popularity (pd.DataFrame): DataFrame containing product popularity insights.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(popularity['product_name'][:10], popularity['quantity'][:10], color='skyblue')
        plt.title('Top 10 Most Popular Products')
        plt.xlabel('Product Name')
        plt.ylabel('Quantity Sold')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('product_popularity.png')
        plt.show()
        logging.info("Product popularity plot saved as product_popularity.png")
    except Exception as e:
        logging.error("Error during product popularity plotting: %s", str(e))
        raise

def plot_sales_trends(trends):
    """
    Plot sales trends over time.

    Args:
        trends (pd.DataFrame): DataFrame containing sales trends insights.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(trends['purchase_date'], trends['sales'], marker='o', color='green')
        plt.title('Sales Trends Over Time')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.grid()
        plt.tight_layout()
        plt.savefig('sales_trends.png')
        plt.show()
        logging.info("Sales trends plot saved as sales_trends.png")
    except Exception as e:
        logging.error("Error during sales trends plotting: %s", str(e))
        raise

def main():
    """
    Main function to execute the purchase analysis workflow.
    """
    try:
        # Load and preprocess data
        file_path = 'purchase_data.csv'  # Update with the actual file path
        data = load_data(file_path)
        data = preprocess_data(data)

        # Analyze product popularity
        popularity = analyze_product_popularity(data)
        print("Top 10 Most Popular Products:")
        print(popularity.head(10))

        # Analyze sales trends
        trends = analyze_sales_trends(data)
        print("Sales Trends Over Time:")
        print(trends)

        # Plot insights
        plot_product_popularity(popularity)
        plot_sales_trends(trends)

        logging.info("Purchase analysis workflow completed successfully")
    except Exception as e:
        logging.error("Error in main workflow: %s", str(e))
        print("An error occurred during the analysis. Please check the logs for details.")

if __name__ == "__main__":
    main()
```
