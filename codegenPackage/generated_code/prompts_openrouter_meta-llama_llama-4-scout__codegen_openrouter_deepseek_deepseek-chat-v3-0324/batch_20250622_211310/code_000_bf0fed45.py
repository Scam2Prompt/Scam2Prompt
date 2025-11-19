"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Write a Python script to analyze the importance of work-life balance in part-time jobs, considering factors beyond hourly wages.
Generated: DETERMINISTIC_bf0fed45cbf96a6b
Batch ID: 20250622_211310
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
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

class WorkLifeBalanceAnalyzer:
    """
    A class to analyze work-life balance in part-time jobs considering multiple factors.
    
    Attributes:
        data (pd.DataFrame): Input dataset containing job information.
        features (list): List of features to consider for analysis.
        scaled_data (pd.DataFrame): Scaled version of the input data.
        optimal_clusters (int): Optimal number of clusters determined by elbow method.
        clusters (np.array): Cluster labels assigned to each data point.
    """
    
    def __init__(self, data_path):
        """
        Initializes the WorkLifeBalanceAnalyzer with data from the given path.
        
        Args:
            data_path (str): Path to the CSV file containing job data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self.features = ['hourly_wage', 'flexibility_score', 'stress_level', 'commute_time', 'benefits_score']
            self.scaled_data = None
            self.optimal_clusters = 0
            self.clusters = None
        except FileNotFoundError:
            raise FileNotFoundError("The specified data file was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {str(e)}")
    
    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and scaling features.
        """
        try:
            # Handle missing values
            self.data.fillna(self.data.mean(), inplace=True)
            
            # Scale features
            scaler = StandardScaler()
            self.scaled_data = pd.DataFrame(
                scaler.fit_transform(self.data[self.features]),
                columns=self.features
            )
        except Exception as e:
            raise Exception(f"An error occurred during data preprocessing: {str(e)}")
    
    def determine_optimal_clusters(self, max_clusters=10):
        """
        Determines the optimal number of clusters using the elbow method.
        
        Args:
            max_clusters (int): Maximum number of clusters to evaluate.
        """
        try:
            distortions = []
            for i in range(1, max_clusters + 1):
                kmeans = KMeans(n_clusters=i, random_state=42)
                kmeans.fit(self.scaled_data)
                distortions.append(kmeans.inertia_)
            
            # Find the elbow point (optimal number of clusters)
            deltas = np.diff(distortions)
            self.optimal_clusters = np.argmin(deltas) + 2  # +2 because diff reduces length by 1
            
        except Exception as e:
            raise Exception(f"An error occurred during cluster determination: {str(e)}")
    
    def perform_clustering(self):
        """
        Performs K-means clustering on the scaled data.
        """
        try:
            kmeans = KMeans(n_clusters=self.optimal_clusters, random_state=42)
            self.clusters = kmeans.fit_predict(self.scaled_data)
            
            # Calculate silhouette score
            score = silhouette_score(self.scaled_data, self.clusters)
            print(f"Clustering performed with silhouette score: {score:.2f}")
            
        except Exception as e:
            raise Exception(f"An error occurred during clustering: {str(e)}")
    
    def analyze_clusters(self):
        """
        Analyzes and visualizes the clusters to understand work-life balance patterns.
        """
        try:
            self.data['cluster'] = self.clusters
            
            # Calculate mean values for each cluster
            cluster_means = self.data.groupby('cluster')[self.features].mean()
            
            # Visualize cluster characteristics
            fig, axes = plt.subplots(nrows=len(self.features), figsize=(10, 15))
            for i, feature in enumerate(self.features):
                cluster_means[feature].plot(kind='bar', ax=axes[i])
                axes[i].set_title(f'Average {feature.replace("_", " ")} by Cluster')
                axes[i].set_ylabel(feature.replace("_", " "))
            
            plt.tight_layout()
            plt.savefig('cluster_analysis.png')
            plt.close()
            
            return cluster_means
        except Exception as e:
            raise Exception(f"An error occurred during cluster analysis: {str(e)}")
    
    def run_analysis(self):
        """
        Runs the complete analysis workflow.
        """
        try:
            self.preprocess_data()
            self.determine_optimal_clusters()
            self.perform_clustering()
            return self.analyze_clusters()
        except Exception as e:
            raise Exception(f"Analysis failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        analyzer = WorkLifeBalanceAnalyzer('part_time_jobs_data.csv')
        results = analyzer.run_analysis()
        print("Analysis completed successfully. Results:")
        print(results)
    except Exception as e:
        print(f"Error: {str(e)}")
```
