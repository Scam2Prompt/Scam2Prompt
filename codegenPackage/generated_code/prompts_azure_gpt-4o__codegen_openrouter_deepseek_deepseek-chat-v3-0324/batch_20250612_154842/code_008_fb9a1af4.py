"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: Write code to analyze and visualize customer journey data, focusing on maximizing lifetime value as described by Swell Creative Management's strategy services.
Generated: DETERMINISTIC_fb9a1af466701a3c
Batch ID: 20250612_154842
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
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from datetime import datetime
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class CustomerJourneyAnalyzer:
    """
    A class to analyze and visualize customer journey data with focus on maximizing lifetime value.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with customer journey data.
        
        Args:
            data_path (str): Path to the customer journey data file (CSV format expected)
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
            print("Data loaded and preprocessed successfully.")
        except Exception as e:
            print(f"Error initializing analyzer: {str(e)}")
            raise
    
    def _validate_data(self):
        """
        Validate that required columns are present in the data.
        """
        required_columns = {'customer_id', 'timestamp', 'event_type', 'revenue'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def _preprocess_data(self):
        """
        Preprocess the data by converting timestamps and calculating derived metrics.
        """
        # Convert timestamp to datetime
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
        
        # Calculate days since first purchase
        first_purchase = self.data.groupby('customer_id')['timestamp'].min().reset_index()
        first_purchase.columns = ['customer_id', 'first_purchase_date']
        self.data = self.data.merge(first_purchase, on='customer_id')
        self.data['days_since_first_purchase'] = (self.data['timestamp'] - self.data['first_purchase_date']).dt.days
        
        # Calculate cumulative revenue per customer
        self.data['cumulative_revenue'] = self.data.groupby('customer_id')['revenue'].cumsum()
        
        # Calculate purchase frequency
        purchase_counts = self.data[self.data['event_type'] == 'purchase'].groupby('customer_id').size().reset_index()
        purchase_counts.columns = ['customer_id', 'purchase_count']
        self.data = self.data.merge(purchase_counts, on='customer_id', how='left')
        
        # Fill NA for customers with no purchases
        self.data['purchase_count'] = self.data['purchase_count'].fillna(0)
    
    def calculate_clv(self, time_horizon=365, discount_rate=0.1):
        """
        Calculate Customer Lifetime Value (CLV) for each customer.
        
        Args:
            time_horizon (int): Time horizon in days for CLV calculation (default: 365)
            discount_rate (float): Discount rate for future revenue (default: 0.1)
            
        Returns:
            pd.DataFrame: DataFrame with CLV for each customer
        """
        try:
            # Filter data within the time horizon
            filtered_data = self.data[self.data['days_since_first_purchase'] <= time_horizon]
            
            # Calculate average purchase value
            avg_purchase_value = filtered_data.groupby('customer_id')['revenue'].mean().reset_index()
            avg_purchase_value.columns = ['customer_id', 'avg_purchase_value']
            
            # Calculate purchase frequency
            purchase_freq = filtered_data[filtered_data['event_type'] == 'purchase'].groupby('customer_id').size().reset_index()
            purchase_freq.columns = ['customer_id', 'purchase_freq']
            
            # Calculate customer lifespan (days between first and last purchase)
            lifespan = filtered_data.groupby('customer_id')['days_since_first_purchase'].max().reset_index()
            lifespan.columns = ['customer_id', 'lifespan']
            
            # Merge metrics
            clv_data = avg_purchase_value.merge(purchase_freq, on='customer_id', how='left')
            clv_data = clv_data.merge(lifespan, on='customer_id', how='left')
            
            # Fill NA values
            clv_data['purchase_freq'] = clv_data['purchase_freq'].fillna(0)
            clv_data['lifespan'] = clv_data['lifespan'].fillna(0)
            
            # Calculate CLV
            clv_data['clv'] = (clv_data['avg_purchase_value'] * 
                              clv_data['purchase_freq'] * 
                              (clv_data['lifespan'] / time_horizon) / 
                              (1 + discount_rate))
            
            return clv_data.sort_values('clv', ascending=False)
        
        except Exception as e:
            print(f"Error calculating CLV: {str(e)}")
            raise
    
    def segment_customers(self, n_clusters=4):
        """
        Segment customers using K-means clustering based on RFM metrics.
        
        Args:
            n_clusters (int): Number of clusters to create (default: 4)
            
        Returns:
            pd.DataFrame: DataFrame with customer segments
        """
        try:
            # Calculate RFM metrics
            now = datetime.now()
            
            # Recency
            recency = self.data.groupby('customer_id')['timestamp'].max().reset_index()
            recency['recency'] = (now - recency['timestamp']).dt.days
            
            # Frequency
            frequency = self.data[self.data['event_type'] == 'purchase'].groupby('customer_id').size().reset_index()
            frequency.columns = ['customer_id', 'frequency']
            
            # Monetary
            monetary = self.data.groupby('customer_id')['revenue'].sum().reset_index()
            monetary.columns = ['customer_id', 'monetary']
            
            # Merge RFM metrics
            rfm = recency.merge(frequency, on='customer_id', how='left')
            rfm = rfm.merge(monetary, on='customer_id', how='left')
            rfm.fillna(0, inplace=True)
            
            # Log transform to handle skewness
            rfm['recency_log'] = np.log1p(rfm['recency'])
            rfm['frequency_log'] = np.log1p(rfm['frequency'])
            rfm['monetary_log'] = np.log1p(rfm['monetary'])
            
            # Standardize the data
            scaler = StandardScaler()
            rfm_scaled = scaler.fit_transform(rfm[['recency_log', 'frequency_log', 'monetary_log']])
            
            # K-means clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(rfm_scaled)
            
            # Add clusters to RFM data
            rfm['segment'] = clusters
            
            # Calculate silhouette score
            score = silhouette_score(rfm_scaled, clusters)
            print(f"Segmentation complete. Silhouette Score: {score:.2f}")
            
            return rfm
        
        except Exception as e:
            print(f"Error segmenting customers: {str(e)}")
            raise
    
    def plot_journey_paths(self, top_n_customers=10):
        """
        Visualize the journey paths of top customers by CLV.
        
        Args:
            top_n_customers (int): Number of top customers to visualize (default: 10)
        """
        try:
            # Get top customers by CLV
            clv_data = self.calculate_clv()
            top_customers = clv_data.head(top_n_customers)['customer_id'].tolist()
            
            # Filter data for top customers
            top_data = self.data[self.data['customer_id'].isin(top_customers)]
            
            # Create event sequence plot
            plt.figure(figsize=(12, 8))
            sns.lineplot(data=top_data, 
                        x='days_since_first_purchase', 
                        y='cumulative_revenue', 
                        hue='customer_id',
                        palette='viridis',
                        linewidth=2)
            
            plt.title(f'Customer Journey Paths (Top {top_n_customers} by CLV)')
            plt.xlabel('Days Since First Purchase')
            plt.ylabel('Cumulative Revenue')
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting journey paths: {str(e)}")
            raise
    
    def plot_segments(self, rfm_data):
        """
        Visualize customer segments in 3D space.
        
        Args:
            rfm_data (pd.DataFrame): DataFrame containing segment data from segment_customers()
        """
        try:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Plot each segment
            for segment in sorted(rfm_data['segment'].unique()):
                segment_data = rfm_data[rfm_data['segment'] == segment]
                ax.sc
