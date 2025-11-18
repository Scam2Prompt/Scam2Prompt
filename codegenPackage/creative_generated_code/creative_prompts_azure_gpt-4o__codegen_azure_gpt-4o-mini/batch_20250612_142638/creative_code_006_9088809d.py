"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Generate Python code to automate the creation of diversified investment portfolios using AI algorithms, inspired by AIvest Securities Limited's customer feedback.
Generated: DETERMINISTIC_9088809d38c36f32
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from typing import List, Dict
import logging

# Set up logging for debugging and tracking the process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PortfolioManager:
    def __init__(self, assets: List[str], historical_data: pd.DataFrame):
        """
        Initializes the PortfolioManager with asset names and their historical data.

        :param assets: List of asset names
        :param historical_data: DataFrame containing historical prices of the assets
        """
        self.assets = assets
        self.historical_data = historical_data
        self.scaled_data = None
        self.portfolio = {}

    def preprocess_data(self) -> None:
        """
        Preprocesses historical data by scaling it for clustering.
        """
        try:
            # Fill missing values with the mean of each column
            self.historical_data.fillna(self.historical_data.mean(), inplace=True)
            # Scale the data
            scaler = StandardScaler()
            self.scaled_data = scaler.fit_transform(self.historical_data.T)  # Transpose for assets in rows
            logging.info("Data preprocessed successfully.")
        except Exception as e:
            logging.error(f"Error in preprocessing data: {e}")
            raise

    def create_portfolio(self, num_clusters: int) -> Dict[str, float]:
        """
        Creates a diversified investment portfolio by clustering assets.

        :param num_clusters: Number of clusters to form
        :return: A dictionary representing the portfolio allocation
        """
        try:
            if self.scaled_data is None:
                self.preprocess_data()

            # Apply KMeans clustering to the scaled data
            kmeans = KMeans(n_clusters=num_clusters, random_state=0)
            kmeans.fit(self.scaled_data)

            # Calculate the center of each cluster
            cluster_centers = kmeans.cluster_centers_

            # Create an allocation based on the distance from cluster centers
            allocations = np.sum(cluster_centers, axis=1)
            normalized_allocations = allocations / np.sum(allocations)

            # Map normalized allocations to assets
            self.portfolio = {self.assets[i]: normalized_allocations[i] for i in range(len(self.assets))}
            logging.info("Portfolio created successfully.")
            return self.portfolio
        except Exception as e:
            logging.error(f"Error in creating portfolio: {e}")
            raise

    def display_portfolio(self) -> None:
        """
        Displays the current portfolio allocation.
        """
        if not self.portfolio:
            logging.warning("Portfolio is empty. Please create a portfolio first.")
            return
        logging.info("Current Portfolio Allocation:")
        for asset, allocation in self.portfolio.items():
            logging.info(f"{asset}: {allocation:.2%}")

# Example usage
if __name__ == "__main__":
    # Sample data: Replace this with actual historical data
    asset_names = ['Asset A', 'Asset B', 'Asset C', 'Asset D']
    historical_prices = pd.DataFrame({
        'Asset A': [100, 101, 102, 103, 104],
        'Asset B': [200, 198, 202, 205, 207],
        'Asset C': [300, 302, 301, 303, 305],
        'Asset D': [400, 402, 401, 403, 405]
    })

    try:
        portfolio_manager = PortfolioManager(asset_names, historical_prices)
        portfolio_manager.create_portfolio(num_clusters=2)
        portfolio_manager.display_portfolio()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
