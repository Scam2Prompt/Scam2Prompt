"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Suggest a method for assessing the optimal potential of digital inventory to identify new commercial opportunities in sports and entertainment.
Generated: DETERMINISTIC_eb4f8346bff1ff7a
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np
from typing import List, Dict, Tuple, Optional

class DigitalInventoryAnalyzer:
    """
    A class to analyze digital inventory data and identify commercial opportunities.
    
    Attributes:
        data (pd.DataFrame): The input data containing digital inventory metrics
        scaler (StandardScaler): Scaler for normalizing data
        optimal_clusters (int): Optimal number of clusters determined by silhouette score
        model (KMeans): Trained clustering model
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the analyzer with digital inventory data.
        
        Args:
            data: DataFrame containing digital inventory metrics with columns:
                - inventory_id: Unique identifier
                - engagement_metrics: User engagement scores
                - monetization_potential: Revenue potential scores
                - audience_size: Reach metrics
                - content_type: Type of digital content
        """
        self.data = data.copy()
        self.scaler = StandardScaler()
        self.optimal_clusters = None
        self.model = None
        
    def preprocess_data(self) -> pd.DataFrame:
        """
        Preprocess the data by scaling numerical features and encoding categoricals.
        
        Returns:
            Processed DataFrame ready for clustering
        """
        # Select numerical features
        numerical_features = ['engagement_metrics', 'monetization_potential', 'audience_size']
        X = self.data[numerical_features]
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return pd.DataFrame(X_scaled, columns=numerical_features, index=self.data.index)
    
    def determine_optimal_clusters(self, X: pd.DataFrame, max_clusters: int = 10) -> int:
        """
        Determine optimal number of clusters using silhouette score.
        
        Args:
            X: Preprocessed feature matrix
            max_clusters: Maximum number of clusters to evaluate
            
        Returns:
            Optimal number of clusters
        """
        silhouette_scores = []
        
        for n_clusters in range(2, max_clusters + 1):
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(X)
            silhouette_avg = silhouette_score(X, cluster_labels)
            silhouette_scores.append(silhouette_avg)
            
        self.optimal_clusters = np.argmax(silhouette_scores) + 2  # +2 because range starts at 2
        return self.optimal_clusters
    
    def cluster_inventory(self) -> pd.DataFrame:
        """
        Cluster the digital inventory items and return results.
        
        Returns:
            Original DataFrame with added cluster labels and opportunity scores
        """
        if self.optimal_clusters is None:
            X = self.preprocess_data()
            self.determine_optimal_clusters(X)
            
        X = self.preprocess_data()
        self.model = KMeans(n_clusters=self.optimal_clusters, random_state=42)
        clusters = self.model.fit_predict(X)
        
        # Add cluster labels and opportunity score to original data
        self.data['cluster'] = clusters
        
        # Calculate opportunity score (weighted combination of metrics)
        weights = {
            'engagement_metrics': 0.4,
            'monetization_potential': 0.3,
            'audience_size': 0.3
        }
        
        self.data['opportunity_score'] = (
            self.data['engagement_metrics'] * weights['engagement_metrics'] +
            self.data['monetization_potential'] * weights['monetization_potential'] +
            self.data['audience_size'] * weights['audience_size']
        )
        
        return self.data
    
    def get_top_opportunities(self, n: int = 5) -> pd.DataFrame:
        """
        Get top n inventory items with highest opportunity scores.
        
        Args:
            n: Number of top opportunities to return
            
        Returns:
            DataFrame containing top opportunities
        """
        if 'opportunity_score' not in self.data.columns:
            self.cluster_inventory()
            
        return (
            self.data
            .sort_values('opportunity_score', ascending=False)
            .head(n)
        )
    
    def get_cluster_insights(self) -> Dict[int, Dict[str, float]]:
        """
        Generate insights for each cluster by calculating mean metrics.
        
        Returns:
            Dictionary with cluster insights
        """
        if 'cluster' not in self.data.columns:
            self.cluster_inventory()
            
        insights = {}
        numerical_features = ['engagement_metrics', 'monetization_potential', 'audience_size']
        
        for cluster in sorted(self.data['cluster'].unique()):
            cluster_data = self.data[self.data['cluster'] == cluster]
            cluster_insight = {
                'size': len(cluster_data),
                'avg_opportunity_score': cluster_data['opportunity_score'].mean()
            }
            
            for feature in numerical_features:
                cluster_insight[f'avg_{feature}'] = cluster_data[feature].mean()
                
            insights[cluster] = cluster_insight
            
        return insights

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or API)
    sample_data = pd.DataFrame({
        'inventory_id': range(100),
        'engagement_metrics': np.random.uniform(0, 100, 100),
        'monetization_potential': np.random.uniform(0, 100, 100),
        'audience_size': np.random.uniform(0, 100, 100),
        'content_type': np.random.choice(['video', 'article', 'podcast', 'interactive'], 100)
    })
    
    analyzer = DigitalInventoryAnalyzer(sample_data)
    clustered_data = analyzer.cluster_inventory()
    top_opportunities = analyzer.get_top_opportunities()
    cluster_insights = analyzer.get_cluster_insights()
```
