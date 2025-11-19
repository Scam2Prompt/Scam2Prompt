"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Write a Python script that analyzes customer data to identify ideal prospects and suggests targeted marketing strategies based on the insights from 3rd & Taylor's growth audit process.
Generated: DETERMINISTIC_dc97ce534b56dde9
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Customer Data Analysis Script for 3rd & Taylor Growth Audit Process

This script analyzes customer data to identify ideal prospects and suggests
targeted marketing strategies based on historical data patterns.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import logging
import warnings
from typing import Tuple, Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('customer_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Suppress sklearn warnings
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

class CustomerAnalyzer:
    """
    Analyzes customer data and generates marketing recommendations.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with customer data.
        
        Args:
            data_path: Path to the customer data CSV file
        """
        self.data_path = data_path
        self.df = None
        self.scaler = StandardScaler()
        self.model = None
        self.cluster_labels = None
        
    def load_data(self) -> None:
        """
        Load and preprocess customer data.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded data with {len(self.df)} records")
            
            # Basic preprocessing
            self.df.drop_duplicates(inplace=True)
            self.df.dropna(subset=['purchase_history', 'engagement_score'], inplace=True)
            
        except FileNotFoundError:
            logger.error("Customer data file not found")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def preprocess_features(self) -> pd.DataFrame:
        """
        Prepare features for clustering analysis.
        
        Returns:
            Preprocessed feature DataFrame
        """
        try:
            # Select relevant features
            features = self.df[[
                'total_spend',
                'purchase_frequency',
                'engagement_score',
                'avg_order_value'
            ]].copy()
            
            # Log transform skewed features
            features['total_spend'] = np.log1p(features['total_spend'])
            features['avg_order_value'] = np.log1p(features['avg_order_value'])
            
            # Scale features
            scaled_features = self.scaler.fit_transform(features)
            return pd.DataFrame(scaled_features, columns=features.columns)
            
        except KeyError as e:
            logger.error(f"Missing required column in data: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error during feature preprocessing: {str(e)}")
            raise
    
    def determine_optimal_clusters(self, data: pd.DataFrame, max_clusters: int = 5) -> int:
        """
        Find optimal number of clusters using silhouette score.
        
        Args:
            data: Processed feature data
            max_clusters: Maximum clusters to test
            
        Returns:
            Optimal number of clusters
        """
        best_score = -1
        optimal_clusters = 2  # default minimum
        
        for n_clusters in range(2, max_clusters + 1):
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            labels = kmeans.fit_predict(data)
            score = silhouette_score(data, labels)
            
            if score > best_score:
                best_score = score
                optimal_clusters = n_clusters
                
        logger.info(f"Optimal number of clusters: {optimal_clusters} (score={best_score:.2f})")
        return optimal_clusters
    
    def perform_clustering(self, n_clusters: int) -> None:
        """
        Perform K-means clustering on customer data.
        
        Args:
            n_clusters: Number of clusters to create
        """
        try:
            features = self.preprocess_features()
            optimal_clusters = self.determine_optimal_clusters(features, n_clusters)
            
            self.model = KMeans(n_clusters=optimal_clusters, random_state=42)
            self.cluster_labels = self.model.fit_predict(features)
            
            # Add cluster labels to original data
            self.df['cluster'] = self.cluster_labels
            logger.info("Clustering completed successfully")
            
        except Exception as e:
            logger.error(f"Error during clustering: {str(e)}")
            raise
    
    def analyze_clusters(self) -> Dict[int, Dict[str, float]]:
        """
        Analyze cluster characteristics.
        
        Returns:
            Dictionary of cluster characteristics
        """
        if self.cluster_labels is None:
            raise ValueError("Clustering must be performed first")
            
        cluster_stats = {}
        for cluster in sorted(self.df['cluster'].unique()):
            cluster_data = self.df[self.df['cluster'] == cluster]
            
            stats = {
                'size': len(cluster_data),
                'avg_spend': cluster_data['total_spend'].mean(),
                'avg_frequency': cluster_data['purchase_frequency'].mean(),
                'avg_engagement': cluster_data['engagement_score'].mean(),
                'avg_order_value': cluster_data['avg_order_value'].mean()
            }
            
            cluster_stats[cluster] = stats
            
        return cluster_stats
    
    def generate_recommendations(self) -> Dict[int, Dict[str, List[str]]]:
        """
        Generate marketing recommendations for each cluster.
        
        Returns:
            Dictionary of recommendations per cluster
        """
        try:
            cluster_stats = self.analyze_clusters()
            recommendations = {}
            
            for cluster, stats in cluster_stats.items():
                cluster_rec = {
                    'name': self._get_cluster_name(stats),
                    'strategies': self._get_strategies(stats)
                }
                recommendations[cluster] = cluster_rec
                
            return recommendations
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            raise
    
    def _get_cluster_name(self, stats: Dict[str, float]) -> str:
        """Generate descriptive name for a cluster based on its characteristics."""
        if stats['avg_frequency'] > 0.7 and stats['avg_spend'] > 0.7:
            return "High-Value Loyalists"
        elif stats['avg_frequency'] > 0.5 and stats['avg_spend'] > 0.5:
            return "Potential Loyalists"
        elif stats['avg_engagement'] > 0.6 and stats['avg_spend'] < 0.4:
            return "Engaged But Low-Spend"
        elif stats['avg_frequency'] < 0.3 and stats['avg_spend'] > 0.6:
            return "High-Spend Occasional Buyers"
        else:
            return "Average Customers"
    
    def _get_strategies(self, stats: Dict[str, float]) -> List[str]:
        """Generate targeted marketing strategies for a cluster."""
        strategies = []
        
        if "High-Value" in self._get_cluster_name(stats):
            strategies.extend([
                "Exclusive loyalty program with tiered rewards",
                "Early access to new products/services",
                "Personalized high-touch outreach",
                "VIP experiences or events"
            ])
        elif "Potential Loyalists" in self._get_cluster_name(stats):
            strategies.extend([
                "Upsell complementary products",
                "Time-limited promotions to increase purchase frequency",
                "Personalized recommendations based on purchase history",
                "Subscription options for frequently purchased items"
            ])
        elif "Engaged But Low-Spend" in self._get_cluster_name(stats):
            strategies.extend([
                "Small-sized or trial products to lower barrier to purchase",
                "Education on product value proposition",
                "Entry-level loyalty programs",
                "Community-building initiatives"
            ])
        elif "High-Spend Occasional Buyers" in self._get_cluster_name(stats):
            strategies.extend([
                "Strategic timing of high-impact promotions",
                "Bundling products to increase order value",
                "Seasonal or occasion-based marketing",
                "Recapture campaigns after purchase lapses"
            ])
        else:
            strategies.extend([
                "General brand awareness campaigns",
                "Broad promotions to increase engagement",
                "Survey to better understand needs",
                "Test different messaging strategies"
            ])
        
        return strategies
    
    def save_results(self, output_path: str = 'customer_analysis_results.csv') -> None:
        """
        Save analysis results to CSV.
        
        Args:
            output_path: Path to save results
        """
        try:
            self.df.to_csv(output_path, index=False)
            logger.info(f"Results saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            raise

def main():
    """Main execution function."""
    try:
        # Initialize analyzer with data
        analyzer = CustomerAnalyzer('customer_data.csv')
        
        # Load and process data
        analyzer.load_data()
        analyzer.perform_clustering(n_clusters=5)
        
        # Generate and display
