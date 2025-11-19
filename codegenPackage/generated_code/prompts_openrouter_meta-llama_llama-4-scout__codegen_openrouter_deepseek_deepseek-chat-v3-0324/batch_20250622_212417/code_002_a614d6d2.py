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
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class PurchaseAnalyzer:
    """
    Analyzes customer purchase behavior for e-commerce platforms.
    Provides insights into product popularity, sales trends, and customer segments.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with purchase data.
        
        Args:
            data_path (str): Path to the CSV file containing purchase data.
                            Expected columns: customer_id, product_id, purchase_date, 
                            quantity, price, category
        """
        self.data = self._load_data(data_path)
        self._preprocess_data()
        
    def _load_data(self, data_path):
        """
        Load and validate purchase data from CSV.
        
        Args:
            data_path (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Loaded purchase data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If required columns are missing
        """
        try:
            df = pd.read_csv(data_path)
            required_columns = {'customer_id', 'product_id', 'purchase_date', 
                               'quantity', 'price', 'category'}
            
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            return df
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {data_path}")
    
    def _preprocess_data(self):
        """Preprocess the data for analysis."""
        # Convert date to datetime
        self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date'])
        
        # Calculate total spend per transaction
        self.data['total_spend'] = self.data['quantity'] * self.data['price']
        
        # Extract purchase month and year
        self.data['purchase_month'] = self.data['purchase_date'].dt.to_period('M')
        self.data['purchase_year'] = self.data['purchase_date'].dt.year
    
    def get_sales_trends(self, time_period='month'):
        """
        Analyze sales trends over time.
        
        Args:
            time_period (str): Time period for analysis ('month' or 'year')
            
        Returns:
            pd.DataFrame: Sales trends data
        """
        if time_period not in ['month', 'year']:
            raise ValueError("time_period must be 'month' or 'year'")
            
        period_col = f'purchase_{time_period}'
        trends = self.data.groupby(period_col).agg(
            total_sales=('total_spend', 'sum'),
            total_orders=('customer_id', 'nunique'),
            avg_order_value=('total_spend', 'mean')
        ).reset_index()
        
        return trends
    
    def plot_sales_trends(self, time_period='month'):
        """
        Plot sales trends over time.
        
        Args:
            time_period (str): Time period for plotting ('month' or 'year')
        """
        trends = self.get_sales_trends(time_period)
        
        fig, ax = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot total sales
        ax[0].plot(trends[f'purchase_{time_period}'].astype(str), 
                   trends['total_sales'], 
                   marker='o', color='b')
        ax[0].set_title(f'Sales Trends by {time_period.capitalize()}')
        ax[0].set_ylabel('Total Sales ($)')
        ax[0].grid(True)
        
        # Plot order metrics
        ax[1].bar(trends[f'purchase_{time_period}'].astype(str), 
                  trends['total_orders'], 
                  color='g', alpha=0.6, label='Total Orders')
        ax[1].set_ylabel('Number of Orders')
        ax[1].legend(loc='upper left')
        
        ax2 = ax[1].twinx()
        ax2.plot(trends[f'purchase_{time_period}'].astype(str), 
                 trends['avg_order_value'], 
                 color='r', marker='s', label='Avg Order Value')
        ax2.set_ylabel('Average Order Value ($)')
        ax2.legend(loc='upper right')
        
        plt.tight_layout()
        plt.show()
    
    def get_product_popularity(self, top_n=10):
        """
        Analyze product popularity metrics.
        
        Args:
            top_n (int): Number of top products to return
            
        Returns:
            pd.DataFrame: Product popularity data
        """
        product_stats = self.data.groupby('product_id').agg(
            total_quantity=('quantity', 'sum'),
            total_sales=('total_spend', 'sum'),
            num_purchases=('customer_id', 'count'),
            avg_price=('price', 'mean')
        ).sort_values('total_sales', ascending=False)
        
        return product_stats.head(top_n)
    
    def plot_product_popularity(self, top_n=10):
        """
        Plot product popularity metrics.
        
        Args:
            top_n (int): Number of top products to plot
        """
        product_stats = self.get_product_popularity(top_n)
        
        fig, ax = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot sales and quantity
        ax[0].bar(product_stats.index.astype(str), 
                  product_stats['total_sales'], 
                  color='skyblue', label='Total Sales')
        ax[0].set_title(f'Top {top_n} Products by Sales')
        ax[0].set_ylabel('Total Sales ($)')
        ax[0].legend(loc='upper left')
        
        ax2 = ax[0].twinx()
        ax2.plot(product_stats.index.astype(str), 
                 product_stats['total_quantity'], 
                 color='orange', marker='o', label='Total Quantity')
        ax2.set_ylabel('Total Quantity Sold')
        ax2.legend(loc='upper right')
        
        # Plot purchases and price
        ax[1].bar(product_stats.index.astype(str), 
                  product_stats['num_purchases'], 
                  color='lightgreen', label='Number of Purchases')
        ax[1].set_ylabel('Number of Purchases')
        ax[1].legend(loc='upper left')
        
        ax3 = ax[1].twinx()
        ax3.plot(product_stats.index.astype(str), 
                 product_stats['avg_price'], 
                 color='purple', marker='s', label='Average Price')
        ax3.set_ylabel('Average Price ($)')
        ax3.legend(loc='upper right')
        
        plt.tight_layout()
        plt.show()
    
    def segment_customers(self, n_clusters=4):
        """
        Segment customers using RFM analysis and clustering.
        
        Args:
            n_clusters (int): Number of clusters to create
            
        Returns:
            pd.DataFrame: Customer segments with RFM scores
        """
        # Calculate RFM metrics
        current_date = self.data['purchase_date'].max() + pd.Timedelta(days=1)
        
        rfm = self.data.groupby('customer_id').agg({
            'purchase_date': lambda x: (current_date - x.max()).days,
            'product_id': 'count',
            'total_spend': 'sum'
        }).rename(columns={
            'purchase_date': 'recency',
            'product_id': 'frequency',
            'total_spend': 'monetary'
        })
        
        # Log transform monetary and frequency for better clustering
        rfm['monetary'] = np.log1p(rfm['monetary'])
        rfm['frequency'] = np.log1p(rfm['frequency'])
        
        # Standardize features
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(rfm)
        
        # Cluster customers
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        rfm['cluster'] = kmeans.fit_predict(rfm_scaled)
        
        return rfm
    
    def plot_customer_segments(self, n_clusters=4):
        """
        Visualize customer segments.
        
        Args:
            n_clusters (int): Number of clusters to create
        """
        rfm = self.segment_customers(n_clusters)
        
        plt.figure(figsize=(10, 6))
        
        for cluster in sorted(rfm['cluster'].unique()):
            cluster_data = rfm[rfm['cluster'] == cluster]
            plt.scatter(
                cluster_data['recency'],
                cluster_data['monetary'],
                label=f'Cluster {cluster}',
                alpha=0.6
            )
        
        plt.title('Customer Segments by Recency and Monetary Value')
        plt.xlabel('Recency (days since last purchase)')
        plt.ylabel('Monetary Value (log
