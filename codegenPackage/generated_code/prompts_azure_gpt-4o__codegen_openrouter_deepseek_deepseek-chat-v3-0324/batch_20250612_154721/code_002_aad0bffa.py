"""
Generated Code Metadata:
========================
Original URL: https://get-link.io
Prompt: Generate code to analyze regional innovation trends using patent and company data, inspired by the study on U.S. universities driving innovation.
Generated: DETERMINISTIC_aad0bffaf2b5110d
Batch ID: 20250612_154721
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
from sqlalchemy import create_engine
import logging
from typing import Tuple, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InnovationAnalyzer:
    """
    A class to analyze regional innovation trends using patent and company data.
    """
    
    def __init__(self, db_connection_string: str = None):
        """
        Initialize the InnovationAnalyzer with optional database connection.
        
        Args:
            db_connection_string (str, optional): Database connection string. Defaults to None.
        """
        self.db_engine = None
        if db_connection_string:
            try:
                self.db_engine = create_engine(db_connection_string)
                logger.info("Database connection established successfully")
            except Exception as e:
                logger.error(f"Failed to establish database connection: {e}")
                raise
        
        self.patent_data = None
        self.company_data = None
        self.merged_data = None
        
    def load_data_from_db(self, patent_query: str, company_query: str) -> None:
        """
        Load data from database using SQL queries.
        
        Args:
            patent_query (str): SQL query to fetch patent data
            company_query (str): SQL query to fetch company data
            
        Raises:
            ValueError: If database engine is not initialized
        """
        if not self.db_engine:
            raise ValueError("Database connection not initialized")
            
        try:
            self.patent_data = pd.read_sql(patent_query, self.db_engine)
            self.company_data = pd.read_sql(company_query, self.db_engine)
            logger.info("Data loaded successfully from database")
        except Exception as e:
            logger.error(f"Error loading data from database: {e}")
            raise
    
    def load_data_from_files(self, patent_file: str, company_file: str) -> None:
        """
        Load data from CSV files.
        
        Args:
            patent_file (str): Path to patent data CSV file
            company_file (str): Path to company data CSV file
        """
        try:
            self.patent_data = pd.read_csv(patent_file)
            self.company_data = pd.read_csv(company_file)
            logger.info("Data loaded successfully from files")
        except Exception as e:
            logger.error(f"Error loading data from files: {e}")
            raise
    
    def preprocess_data(self) -> None:
        """
        Preprocess and merge patent and company data.
        """
        if self.patent_data is None or self.company_data is None:
            raise ValueError("Data not loaded. Please load data first.")
            
        try:
            # Clean patent data
            self.patent_data['filing_date'] = pd.to_datetime(self.patent_data['filing_date'])
            self.patent_data['year'] = self.patent_data['filing_date'].dt.year
            self.patent_data = self.patent_data.dropna(subset=['region', 'assignee_id'])
            
            # Clean company data
            self.company_data = self.company_data.dropna(subset=['company_id', 'region'])
            
            # Merge data
            self.merged_data = pd.merge(
                self.patent_data,
                self.company_data,
                left_on='assignee_id',
                right_on='company_id',
                how='inner'
            )
            
            logger.info("Data preprocessing completed successfully")
        except Exception as e:
            logger.error(f"Error during data preprocessing: {e}")
            raise
    
    def calculate_innovation_metrics(self) -> pd.DataFrame:
        """
        Calculate regional innovation metrics.
        
        Returns:
            pd.DataFrame: DataFrame with calculated innovation metrics by region
        """
        if self.merged_data is None:
            raise ValueError("Data not processed. Please preprocess data first.")
            
        try:
            # Calculate basic metrics
            metrics = self.merged_data.groupby(['region', 'year']).agg({
                'patent_id': 'count',
                'citation_count': 'sum',
                'company_id': pd.Series.nunique
            }).reset_index()
            
            metrics.columns = ['region', 'year', 'patent_count', 'total_citations', 'unique_companies']
            
            # Calculate derived metrics
            metrics['citations_per_patent'] = metrics['total_citations'] / metrics['patent_count']
            metrics['patents_per_company'] = metrics['patent_count'] / metrics['unique_companies']
            
            # Calculate 3-year moving averages
            metrics.sort_values(['region', 'year'], inplace=True)
            metrics['patent_count_ma'] = metrics.groupby('region')['patent_count'].transform(
                lambda x: x.rolling(3, min_periods=1).mean()
            )
            
            logger.info("Innovation metrics calculated successfully")
            return metrics
        except Exception as e:
            logger.error(f"Error calculating innovation metrics: {e}")
            raise
    
    def cluster_regions(self, metrics: pd.DataFrame, n_clusters: int = 4) -> Tuple[pd.DataFrame, Dict[int, str]]:
        """
        Cluster regions based on innovation metrics.
        
        Args:
            metrics (pd.DataFrame): DataFrame with innovation metrics
            n_clusters (int, optional): Number of clusters. Defaults to 4.
            
        Returns:
            Tuple[pd.DataFrame, Dict[int, str]]: Tuple containing:
                - DataFrame with cluster labels
                - Dictionary mapping cluster numbers to descriptions
        """
        try:
            # Prepare data for clustering
            cluster_data = metrics.groupby('region').agg({
                'patent_count': 'mean',
                'citations_per_patent': 'mean',
                'patents_per_company': 'mean'
            }).reset_index()
            
            # Standardize features
            scaler = StandardScaler()
            features = ['patent_count', 'citations_per_patent', 'patents_per_company']
            X = scaler.fit_transform(cluster_data[features])
            
            # Determine optimal number of clusters using silhouette score
            best_score = -1
            best_k = n_clusters
            
            if len(cluster_data) > 10:  # Only try multiple k if we have enough regions
                for k in range(2, min(10, len(cluster_data))):
                    kmeans = KMeans(n_clusters=k, random_state=42)
                    labels = kmeans.fit_predict(X)
                    score = silhouette_score(X, labels)
                    if score > best_score:
                        best_score = score
                        best_k = k
            
            # Perform clustering with best k
            kmeans = KMeans(n_clusters=best_k, random_state=42)
            cluster_data['cluster'] = kmeans.fit_predict(X)
            
            # Create cluster descriptions
            cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
            cluster_descriptions = {}
            
            for i, center in enumerate(cluster_centers):
                desc = []
                for j, feature in enumerate(features):
                    desc.append(f"{feature}: {center[j]:.2f}")
                cluster_descriptions[i] = ", ".join(desc)
            
            logger.info(f"Regions clustered into {best_k} groups successfully")
            return cluster_data, cluster_descriptions
        except Exception as e:
            logger.error(f"Error during clustering: {e}")
            raise
    
    def visualize_trends(self, metrics: pd.DataFrame, output_file: str = None) -> None:
        """
        Visualize innovation trends over time.
        
        Args:
            metrics (pd.DataFrame): DataFrame with innovation metrics
            output_file (str, optional): Path to save the plot. If None, plot is displayed.
        """
        try:
            plt.figure(figsize=(12, 8))
            
            # Plot patent count trends
            plt.subplot(2, 2, 1)
            sns.lineplot(data=metrics, x='year', y='patent_count', hue='region', estimator='sum')
            plt.title('Patent Count by Region')
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            
            # Plot citation trends
            plt.subplot(2, 2, 2)
            sns.lineplot(data=metrics, x='year', y='citations_per_patent', hue='region')
            plt.title('Citations per Patent by Region')
            
            # Plot company participation
            plt.subplot(2, 2, 3)
            sns.lineplot(data=metrics, x='year', y='unique_companies', hue='region', estimator='sum')
            plt.title('Unique Companies by Region')
            
            # Plot patents per company
            plt.subplot(2, 2, 4)
            sns.lineplot(data=metrics, x='year', y='patents_per_company', hue='region')
            plt.title('Patents per Company by Region')
