"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Develop a Python script to analyze employee performance data and recommend career development plans, inspired by Videtis Consultores' outplacement program.
Generated: DETERMINISTIC_85c5d56b05759121
Batch ID: 20250612_153517
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
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import warnings
from typing import Dict, List, Tuple, Optional

# Suppress sklearn warnings
warnings.filterwarnings('ignore')

class EmployeePerformanceAnalyzer:
    """
    A class to analyze employee performance data and recommend career development plans.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with employee performance data.
        
        Args:
            data_path (str): Path to the employee performance data file (CSV format)
        """
        self.data_path = data_path
        self.data = None
        self.scaler = StandardScaler()
        self.model = None
        self.cluster_labels = None
        self.cluster_centers = None
        
    def load_data(self) -> None:
        """
        Load and preprocess employee performance data.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            
            # Basic data validation
            if self.data.empty:
                raise ValueError("Empty dataset provided")
                
            required_columns = ['employee_id', 'performance_score', 'skills_score', 
                              'engagement_score', 'tenure', 'training_hours']
            if not all(col in self.data.columns for col in required_columns):
                missing = [col for col in required_columns if col not in self.data.columns]
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert scores to numeric if they aren't
            score_columns = ['performance_score', 'skills_score', 'engagement_score']
            self.data[score_columns] = self.data[score_columns].apply(pd.to_numeric, errors='coerce')
            
            # Drop rows with missing values
            self.data.dropna(inplace=True)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def preprocess_data(self) -> pd.DataFrame:
        """
        Preprocess data for clustering analysis.
        
        Returns:
            pd.DataFrame: Preprocessed data with selected features
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Select relevant features for clustering
        features = ['performance_score', 'skills_score', 'engagement_score', 'training_hours']
        X = self.data[features].copy()
        
        # Standardize features
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled
    
    def find_optimal_clusters(self, X: np.ndarray, max_clusters: int = 10) -> int:
        """
        Determine the optimal number of clusters using silhouette score.
        
        Args:
            X (np.ndarray): Scaled feature matrix
            max_clusters (int): Maximum number of clusters to try
            
        Returns:
            int: Optimal number of clusters
        """
        best_score = -1
        optimal_clusters = 2
        
        for n_clusters in range(2, max_clusters + 1):
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(X)
            silhouette_avg = silhouette_score(X, cluster_labels)
            
            if silhouette_avg > best_score:
                best_score = silhouette_avg
                optimal_clusters = n_clusters
                
        return optimal_clusters
    
    def cluster_employees(self) -> None:
        """
        Cluster employees based on performance metrics.
        """
        try:
            X = self.preprocess_data()
            optimal_clusters = self.find_optimal_clusters(X)
            
            self.model = KMeans(n_clusters=optimal_clusters, random_state=42)
            self.cluster_labels = self.model.fit_predict(X)
            self.cluster_centers = self.model.cluster_centers_
            
            # Add cluster labels to original data
            self.data['cluster'] = self.cluster_labels
            
        except Exception as e:
            raise Exception(f"Error during clustering: {str(e)}")
    
    def analyze_clusters(self) -> Dict[int, Dict[str, float]]:
        """
        Analyze cluster characteristics.
        
        Returns:
            Dict[int, Dict[str, float]]: Dictionary with cluster characteristics
        """
        if self.cluster_labels is None:
            raise ValueError("Clustering not performed. Call cluster_employees() first.")
            
        cluster_stats = {}
        features = ['performance_score', 'skills_score', 'engagement_score', 'training_hours']
        
        for cluster in sorted(self.data['cluster'].unique()):
            cluster_data = self.data[self.data['cluster'] == cluster]
            stats = {
                'size': len(cluster_data),
                'performance_avg': cluster_data['performance_score'].mean(),
                'skills_avg': cluster_data['skills_score'].mean(),
                'engagement_avg': cluster_data['engagement_score'].mean(),
                'training_avg': cluster_data['training_hours'].mean()
            }
            cluster_stats[cluster] = stats
            
        return cluster_stats
    
    def generate_recommendations(self) -> Dict[int, List[str]]:
        """
        Generate career development recommendations for each cluster.
        
        Returns:
            Dict[int, List[str]]: Dictionary of recommendations per cluster
        """
        if self.cluster_labels is None:
            raise ValueError("Clustering not performed. Call cluster_employees() first.")
            
        recommendations = {}
        cluster_stats = self.analyze_clusters()
        
        for cluster, stats in cluster_stats.items():
            cluster_recs = []
            
            # High performers with high skills
            if stats['performance_avg'] > 0.8 and stats['skills_avg'] > 0.8:
                cluster_recs.extend([
                    "Leadership development program",
                    "Mentorship opportunities",
                    "Cross-functional project assignments"
                ])
            # High performers with moderate skills
            elif stats['performance_avg'] > 0.8 and stats['skills_avg'] > 0.6:
                cluster_recs.extend([
                    "Advanced skills training",
                    "Specialization courses",
                    "Stretch assignments"
                ])
            # Moderate performers with high engagement
            elif stats['performance_avg'] > 0.6 and stats['engagement_avg'] > 0.7:
                cluster_recs.extend([
                    "Performance coaching",
                    "Targeted skill development",
                    "Job rotation opportunities"
                ])
            # Low performers with low engagement
            elif stats['performance_avg'] < 0.5 and stats['engagement_avg'] < 0.5:
                cluster_recs.extend([
                    "Performance improvement plan",
                    "Basic skills training",
                    "Career counseling"
                ])
            # All others
            else:
                cluster_recs.extend([
                    "General professional development",
                    "Team-building activities",
                    "Regular feedback sessions"
                ])
                
            # Add training recommendation based on training hours
            if stats['training_avg'] < 20:
                cluster_recs.append("Increase training participation")
                
            recommendations[cluster] = cluster_recs
            
        return recommendations
    
    def get_employee_recommendations(self, employee_id: str) -> Tuple[List[str], Optional[int]]:
        """
        Get personalized recommendations for a specific employee.
        
        Args:
            employee_id (str): Employee ID to get recommendations for
            
        Returns:
            Tuple[List[str], Optional[int]]: (recommendations, cluster) or ([], None) if not found
        """
        if self.cluster_labels is None:
            raise ValueError("Clustering not performed. Call cluster_employees() first.")
            
        if employee_id not in self.data['employee_id'].values:
            return [], None
            
        cluster_recs = self.generate_recommendations()
        employee_cluster = self.data[self.data['employee_id'] == employee_id]['cluster'].values[0]
        
        return cluster_recs.get(employee_cluster, []), employee_cluster
    
    def save_results(self, output_path: str) -> None:
        """
        Save analysis results to a CSV file.
        
        Args:
            output_path (str): Path to save the results
        """
        if self.cluster_labels is None:
            raise ValueError("Clustering not performed. Call cluster_employees() first.")
            
        try:
            results = self.data.copy()
            cluster_recs = self.generate_recommendations()
            
            # Add recommendations to each employee
            results['recommendations'] = results['cluster'].apply(
                lambda x: "; ".join(cluster_recs.get(x, []))
            )
            
            results.to_csv(output_path, index=False)
            
        except Exception as e:
            raise Exception(f"Error saving results: {str(e)}")


def main():
    """
    Main execution function for the employee performance analyzer.
    """
    try:
        # Initialize analyzer with data path
        analyzer = EmployeePerformanceAnalyzer('employee_performance.csv')
        
        # Load and process data
        analyzer.load_data()
        analyzer.cluster_employees()
        
        # Generate and display recommendations
        recommendations = analyzer.generate_recommendations()
        print("Cluster Recommendations:")
        for cluster, recs in recommendations.items():
            print(f"\nCluster {cluster}:")
            for rec in recs:
