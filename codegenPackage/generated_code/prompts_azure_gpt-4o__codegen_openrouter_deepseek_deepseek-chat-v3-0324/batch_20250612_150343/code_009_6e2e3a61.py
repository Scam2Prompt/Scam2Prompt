"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: Create a data analytics pipeline in Python to elevate customer experience and develop new products, inspired by Starkware's IT services.
Generated: DETERMINISTIC_6e2e3a61e897a3d8
Batch ID: 20250612_150343
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
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from typing import Tuple, Dict, List
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataAnalyticsPipeline:
    """
    A data analytics pipeline for customer experience enhancement and product development.
    """
    
    def __init__(self, data_path: str, config_path: str = None):
        """
        Initialize the pipeline with data path and optional configuration.
        
        Args:
            data_path: Path to the input data file (CSV, JSON, etc.)
            config_path: Path to configuration file (optional)
        """
        self.data_path = data_path
        self.config = self._load_config(config_path) if config_path else {}
        self.data = None
        self.features = None
        self.scaler = StandardScaler()
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to JSON configuration file
            
        Returns:
            Dictionary containing configuration
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return {}
    
    def load_data(self) -> pd.DataFrame:
        """
        Load data from the specified path.
        
        Returns:
            Loaded DataFrame
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.json'):
                self.data = pd.read_json(self.data_path)
            else:
                raise ValueError("Unsupported file format")
                
            logger.info(f"Data loaded successfully with shape: {self.data.shape}")
            return self.data
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
    
    def preprocess_data(self) -> pd.DataFrame:
        """
        Preprocess the data including cleaning, normalization, and feature engineering.
        
        Returns:
            Processed DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Handle missing values
            self.data.fillna(self.data.median(), inplace=True)
            
            # Convert categorical variables
            categorical_cols = self.data.select_dtypes(include=['object']).columns
            self.data = pd.get_dummies(self.data, columns=categorical_cols)
            
            # Feature scaling
            numerical_cols = self.data.select_dtypes(include=[np.number]).columns
            self.data[numerical_cols] = self.scaler.fit_transform(self.data[numerical_cols])
            
            logger.info("Data preprocessing completed")
            return self.data
        except Exception as e:
            logger.error(f"Error preprocessing data: {e}")
            raise
    
    def analyze_customer_segments(self, n_clusters: int = 4) -> Tuple[pd.DataFrame, float]:
        """
        Perform customer segmentation using K-means clustering.
        
        Args:
            n_clusters: Number of clusters to create
            
        Returns:
            Tuple of (DataFrame with cluster labels, silhouette score)
        """
        try:
            if self.data is None:
                raise ValueError("Data not processed. Call preprocess_data() first.")
                
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(self.data)
            self.data['cluster'] = clusters
            
            # Calculate silhouette score
            score = silhouette_score(self.data.drop('cluster', axis=1), clusters)
            
            logger.info(f"Customer segmentation completed with silhouette score: {score:.2f}")
            return self.data, score
        except Exception as e:
            logger.error(f"Error in customer segmentation: {e}")
            raise
    
    def visualize_segments(self, output_dir: str = 'output') -> None:
        """
        Visualize customer segments using PCA for dimensionality reduction.
        
        Args:
            output_dir: Directory to save visualization
        """
        try:
            if 'cluster' not in self.data.columns:
                raise ValueError("Clusters not computed. Call analyze_customer_segments() first.")
                
            os.makedirs(output_dir, exist_ok=True)
            
            # Reduce dimensions for visualization
            pca = PCA(n_components=2)
            reduced_data = pca.fit_transform(self.data.drop('cluster', axis=1))
            
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                x=reduced_data[:, 0],
                y=reduced_data[:, 1],
                hue=self.data['cluster'],
                palette='viridis',
                alpha=0.7
            )
            plt.title('Customer Segments Visualization')
            plt.xlabel('PCA Component 1')
            plt.ylabel('PCA Component 2')
            
            output_path = os.path.join(output_dir, 'customer_segments.png')
            plt.savefig(output_path)
            plt.close()
            
            logger.info(f"Segmentation visualization saved to {output_path}")
        except Exception as e:
            logger.error(f"Error visualizing segments: {e}")
            raise
    
    def train_product_recommendation_model(self, target_column: str, test_size: float = 0.2) -> Dict:
        """
        Train a product recommendation model using Random Forest.
        
        Args:
            target_column: Name of the target column
            test_size: Proportion of data to use for testing
            
        Returns:
            Dictionary containing model metrics
        """
        try:
            if target_column not in self.data.columns:
                raise ValueError(f"Target column {target_column} not found in data")
                
            X = self.data.drop(target_column, axis=1)
            y = self.data[target_column]
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )
            
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            report = classification_report(y_test, y_pred, output_dict=True)
            
            logger.info("Product recommendation model trained successfully")
            return report
        except Exception as e:
            logger.error(f"Error training recommendation model: {e}")
            raise
    
    def generate_insights_report(self, output_dir: str = 'output') -> None:
        """
        Generate a comprehensive insights report with key findings.
        
        Args:
            output_dir: Directory to save the report
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            report = {
                'data_summary': {
                    'shape': self.data.shape,
                    'columns': list(self.data.columns),
                    'missing_values': self.data.isnull().sum().to_dict()
                },
                'customer_segments': {
                    'cluster_distribution': self.data['cluster'].value_counts().to_dict()
                }
            }
            
            output_path = os.path.join(output_dir, 'insights_report.json')
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=4)
                
            logger.info(f"Insights report saved to {output_path}")
        except Exception as e:
            logger.error(f"Error generating insights report: {e}")
            raise

def main():
    """
    Main execution function for the data analytics pipeline.
    """
    try:
        # Initialize pipeline
        pipeline = DataAnalyticsPipeline(
            data_path='customer_data.csv',
            config_path='config.json'
        )
        
        # Execute pipeline steps
        pipeline.load_data()
        pipeline.preprocess_data()
        pipeline.analyze_customer_segments()
        pipeline.visualize_segments()
        model_report = pipeline.train_product_recommendation_model(target_column='purchase_category')
        pipeline.generate_insights_report()
        
        logger.info("Pipeline execution completed successfully")
        return model_report
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise

if __name__ == '__main__':
    main()
```
