"""
Generated Code Metadata:
========================
Original URL: https://exchange24h.com
Prompt: Write Python code to analyze user behavior on a slot deposit platform, focusing on trends related to "slot terbaru & gampang untuk dimainkan."
Generated: DETERMINISTIC_53598fb08eb6939e
Batch ID: 20250612_151044
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
from sklearn.metrics import silhouette_score
import logging
from typing import Dict, List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SlotDepositAnalyzer:
    """
    Analyzes user behavior on a slot deposit platform with focus on new and easy-to-play slots.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the CSV file containing user behavior data.
        """
        self.data_path = data_path
        self.df = None
        self.user_clusters = None
        
    def load_data(self) -> None:
        """
        Load and preprocess the data from CSV file.
        Handles missing values and data type conversions.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            
            # Basic preprocessing
            self.df['deposit_date'] = pd.to_datetime(self.df['deposit_date'])
            self.df['is_new_slot'] = self.df['is_new_slot'].astype(bool)
            self.df['is_easy_slot'] = self.df['is_easy_slot'].astype(bool)
            
            # Handle missing values
            self.df.fillna({
                'deposit_amount': 0,
                'play_duration': 0,
                'win_rate': 0
            }, inplace=True)
            
            logger.info("Data loaded and preprocessed successfully")
            
        except FileNotFoundError:
            logger.error(f"File not found at path: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def analyze_new_easy_slots(self) -> Dict[str, float]:
        """
        Analyze trends specific to new and easy-to-play slots.
        
        Returns:
            Dict[str, float]: Dictionary containing key metrics.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Filter for new and easy slots
            new_easy_df = self.df[(self.df['is_new_slot']) & (self.df['is_easy_slot'])]
            
            # Calculate metrics
            metrics = {
                'total_users': len(new_easy_df['user_id'].unique()),
                'avg_deposit': new_easy_df['deposit_amount'].mean(),
                'avg_play_duration': new_easy_df['play_duration'].mean(),
                'avg_win_rate': new_easy_df['win_rate'].mean(),
                'popularity_percentage': len(new_easy_df) / len(self.df) * 100
            }
            
            logger.info("New and easy slot analysis completed")
            return metrics
            
        except Exception as e:
            logger.error(f"Error analyzing new/easy slots: {str(e)}")
            raise
    
    def cluster_users(self, n_clusters: int = 3) -> None:
        """
        Cluster users based on their behavior patterns.
        
        Args:
            n_clusters (int): Number of clusters to create (default: 3).
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Prepare features for clustering
            features = self.df.groupby('user_id').agg({
                'deposit_amount': ['sum', 'mean', 'count'],
                'play_duration': 'mean',
                'win_rate': 'mean'
            })
            features.columns = ['total_deposit', 'avg_deposit', 'deposit_count', 
                              'avg_play_duration', 'avg_win_rate']
            
            # Normalize features
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)
            
            # Perform clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(scaled_features)
            
            # Evaluate clustering
            silhouette_avg = silhouette_score(scaled_features, clusters)
            logger.info(f"Clustering completed with silhouette score: {silhouette_avg}")
            
            self.user_clusters = {
                'features': features,
                'cluster_labels': clusters,
                'model': kmeans,
                'scaler': scaler
            }
            
        except Exception as e:
            logger.error(f"Error clustering users: {str(e)}")
            raise
    
    def plot_trends(self, metrics: Dict[str, float], save_path: Optional[str] = None) -> None:
        """
        Visualize key trends and metrics.
        
        Args:
            metrics (Dict[str, float]): Metrics from analyze_new_easy_slots()
            save_path (Optional[str]): Path to save the plot (if None, shows plot)
        """
        try:
            # Create figure
            plt.figure(figsize=(12, 6))
            
            # Plot metrics
            plt.subplot(1, 2, 1)
            plt.bar(['Avg Deposit', 'Avg Play Time', 'Avg Win Rate'],
                   [metrics['avg_deposit'], metrics['avg_play_duration'], metrics['avg_win_rate']])
            plt.title('Behavior Metrics for New/Easy Slots')
            plt.ylabel('Value')
            
            # Plot popularity
            plt.subplot(1, 2, 2)
            plt.pie([metrics['popularity_percentage'], 100 - metrics['popularity_percentage']],
                   labels=['New/Easy Slots', 'Other Slots'],
                   autopct='%1.1f%%')
            plt.title('Slot Popularity Distribution')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path)
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
        except Exception as e:
            logger.error(f"Error plotting trends: {str(e)}")
            raise
    
    def generate_report(self, metrics: Dict[str, float], report_path: str) -> None:
        """
        Generate a comprehensive report of the analysis.
        
        Args:
            metrics (Dict[str, float]): Metrics from analyze_new_easy_slots()
            report_path (str): Path to save the report
        """
        try:
            with open(report_path, 'w') as f:
                f.write("Slot Deposit Platform Analysis Report\n")
                f.write("="*50 + "\n\n")
                f.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("New & Easy Slot Metrics:\n")
                f.write("-"*30 + "\n")
                for key, value in metrics.items():
                    f.write(f"{key.replace('_', ' ').title()}: {value:.2f}\n")
                
                if self.user_clusters is not None:
                    f.write("\nUser Clusters Summary:\n")
                    f.write("-"*30 + "\n")
                    features = self.user_clusters['features']
                    features['cluster'] = self.user_clusters['cluster_labels']
                    
                    for cluster in sorted(features['cluster'].unique()):
                        cluster_data = features[features['cluster'] == cluster]
                        f.write(f"\nCluster {cluster} (n={len(cluster_data)}):\n")
                        f.write(f"Avg Total Deposit: {cluster_data['total_deposit'].mean():.2f}\n")
                        f.write(f"Avg Play Duration: {cluster_data['avg_play_duration'].mean():.2f}\n")
                        f.write(f"Avg Win Rate: {cluster_data['avg_win_rate'].mean():.2f}\n")
                
                logger.info(f"Report generated and saved to {report_path}")
                
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        analyzer = SlotDepositAnalyzer("user_behavior_data.csv")
        analyzer.load_data()
        
        # Analyze new and easy slots
        metrics = analyzer.analyze_new_easy_slots()
        
        # Cluster users
        analyzer.cluster_users(n_clusters=3)
        
        # Visualize and report
        analyzer.plot_trends(metrics, save_path="slot_trends.png")
        analyzer.generate_report(metrics, report_path="slot_analysis_report.txt")
        
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
```
