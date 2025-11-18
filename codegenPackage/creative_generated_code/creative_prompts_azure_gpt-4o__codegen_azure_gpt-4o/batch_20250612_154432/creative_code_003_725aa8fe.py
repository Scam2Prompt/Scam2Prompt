"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Based on the 3rd & Taylor strategy for bridging the gap between sales and marketing, write code to analyze customer data and create targeted campaigns that improve conversions.
Generated: DETERMINISTIC_725aa8fea441e57e
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import logging

# Setup logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CampaignAnalyzer:
    """
    Class to analyze customer data and create targeted campaigns
    based on clustering and segmentation techniques.
    """

    def __init__(self, data):
        """
        Initialize the CampaignAnalyzer with customer data.

        :param data: DataFrame containing customer data
                     Expected columns: ['CustomerID', 'Age', 'Income', 'SpendScore']
        """
        self.data = data
        self.processed_data = None
        self.cluster_model = None

    def preprocess_data(self):
        """
        Preprocess the customer data:
        - Remove invalid entries
        - Standardize numerical features
        """
        try:
            logging.info("Preprocessing data...")
            
            # Drop rows with missing values
            self.data.dropna(inplace=True)
            
            # Select numerical columns for clustering
            numerical_data = self.data[['Age', 'Income', 'SpendScore']]
            
            # Standardize the data
            scaler = StandardScaler()
            self.processed_data = scaler.fit_transform(numerical_data)
            logging.info("Data preprocessing completed successfully.")
        except Exception as e:
            logging.error(f"Error in preprocessing data: {e}")
            raise

    def perform_clustering(self, n_clusters=4):
        """
        Perform customer segmentation using K-Means clustering.

        :param n_clusters: Number of clusters to segment the customers into
        """
        try:
            logging.info("Performing clustering...")
            
            # Run K-Means clustering
            self.cluster_model = KMeans(n_clusters=n_clusters, random_state=42)
            self.data['Cluster'] = self.cluster_model.fit_predict(self.processed_data)
            
            logging.info("Clustering completed successfully.")
        except Exception as e:
            logging.error(f"Error in clustering: {e}")
            raise

    def generate_campaigns(self):
        """
        Generate targeted campaigns based on clusters.
        
        :return: Dictionary mapping cluster IDs to campaign strategies
        """
        try:
            logging.info("Generating campaigns...")
            
            campaigns = {}
            cluster_groups = self.data.groupby('Cluster')
            
            for cluster_id, group in cluster_groups:
                # Analyze cluster data to determine campaign strategy
                avg_age = group['Age'].mean()
                avg_income = group['Income'].mean()
                avg_spend_score = group['SpendScore'].mean()
                
                if avg_spend_score > 75:
                    campaigns[cluster_id] = "Upsell premium products"
                elif avg_income < 50000:
                    campaigns[cluster_id] = "Offer discounts"
                elif avg_age < 30:
                    campaigns[cluster_id] = "Target with social media ads"
                else:
                    campaigns[cluster_id] = "Focus on loyalty programs"
            
            logging.info("Campaign generation completed successfully.")
            return campaigns
        except Exception as e:
            logging.error(f"Error in generating campaigns: {e}")
            raise


# Example Usage
if __name__ == "__main__":
    try:
        # Load customer data
        logging.info("Loading customer data...")
        customer_data = pd.DataFrame({
            'CustomerID': [1, 2, 3, 4, 5],
            'Age': [25, 40, 30, 22, 35],
            'Income': [40000, 50000, 60000, 30000, 45000],
            'SpendScore': [90, 60, 75, 85, 70]
        })

        # Analyze data and create campaigns
        analyzer = CampaignAnalyzer(customer_data)
        analyzer.preprocess_data()
        analyzer.perform_clustering(n_clusters=3)
        campaigns = analyzer.generate_campaigns()

        # Display the campaigns
        for cluster_id, strategy in campaigns.items():
            print(f"Cluster {cluster_id}: {strategy}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
