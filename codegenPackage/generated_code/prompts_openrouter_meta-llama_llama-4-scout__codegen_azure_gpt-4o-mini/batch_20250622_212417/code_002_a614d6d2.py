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
import seaborn as sns

class CustomerPurchaseAnalyzer:
    """
    A class to analyze customer purchase behavior for an e-commerce platform.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: str, path to the CSV file containing purchase data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the purchase data from a CSV file.

        :return: DataFrame containing the purchase data
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by converting date columns and handling missing values.
        """
        # Convert 'purchase_date' to datetime
        self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date'], errors='coerce')
        
        # Drop rows with missing values in critical columns
        self.data.dropna(subset=['product_id', 'purchase_date'], inplace=True)

    def analyze_product_popularity(self):
        """
        Analyzes product popularity based on the number of purchases.
        
        :return: DataFrame with product popularity
        """
        product_popularity = self.data['product_id'].value_counts().reset_index()
        product_popularity.columns = ['product_id', 'purchase_count']
        return product_popularity

    def analyze_sales_trends(self):
        """
        Analyzes sales trends over time.

        :return: DataFrame with sales trends
        """
        sales_trends = self.data.groupby(self.data['purchase_date'].dt.to_period('M')).size().reset_index(name='sales_count')
        sales_trends['purchase_date'] = sales_trends['purchase_date'].dt.to_timestamp()
        return sales_trends

    def visualize_product_popularity(self, product_popularity):
        """
        Visualizes product popularity using a bar chart.

        :param product_popularity: DataFrame containing product popularity data
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(x='purchase_count', y='product_id', data=product_popularity.head(10), palette='viridis')
        plt.title('Top 10 Most Popular Products')
        plt.xlabel('Number of Purchases')
        plt.ylabel('Product ID')
        plt.show()

    def visualize_sales_trends(self, sales_trends):
        """
        Visualizes sales trends over time using a line chart.

        :param sales_trends: DataFrame containing sales trends data
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='purchase_date', y='sales_count', data=sales_trends, marker='o')
        plt.title('Sales Trends Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Runs the complete analysis and visualizations.
        """
        self.preprocess_data()
        product_popularity = self.analyze_product_popularity()
        sales_trends = self.analyze_sales_trends()
        
        self.visualize_product_popularity(product_popularity)
        self.visualize_sales_trends(sales_trends)

if __name__ == "__main__":
    # Replace 'purchase_data.csv' with the path to your actual data file
    analyzer = CustomerPurchaseAnalyzer('purchase_data.csv')
    analyzer.run_analysis()
```
