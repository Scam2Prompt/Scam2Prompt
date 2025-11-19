"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Write a script to analyze the effectiveness of training programs for grassroots women leaders, incorporating metrics like advocacy communication skills and organizational sustainability.
Generated: DETERMINISTIC_abb7decdbb25fea3
Batch ID: 20250612_150653
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
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class TrainingProgramAnalyzer:
    """
    A class to analyze the effectiveness of training programs for grassroots women leaders.
    Metrics include advocacy communication skills and organizational sustainability.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing training program data
        """
        self.data = pd.read_csv(data_path)
        self.scaler = MinMaxScaler()
        self._preprocess_data()
        
    def _preprocess_data(self):
        """Preprocess the data by handling missing values and normalizing metrics."""
        # Fill missing values with median
        self.data.fillna(self.data.median(numeric_only=True), inplace=True)
        
        # Normalize metrics (0-1 scaling)
        metrics = ['advocacy_skills', 'communication_skills', 'org_sustainability']
        self.data[metrics] = self.scaler.fit_transform(self.data[metrics])
        
    def calculate_effectiveness_score(self):
        """
        Calculate an overall effectiveness score for each participant.
        The score is a weighted average of the metrics.
        
        Returns:
            pd.Series: Effectiveness scores for each participant
        """
        weights = {
            'advocacy_skills': 0.4,
            'communication_skills': 0.3,
            'org_sustainability': 0.3
        }
        
        self.data['effectiveness_score'] = (
            self.data['advocacy_skills'] * weights['advocacy_skills'] +
            self.data['communication_skills'] * weights['communication_skills'] +
            self.data['org_sustainability'] * weights['org_sustainability']
        )
        
        return self.data['effectiveness_score']
    
    def cluster_participants(self, n_clusters=3):
        """
        Cluster participants based on their metrics using K-means.
        
        Args:
            n_clusters (int): Number of clusters to create
            
        Returns:
            pd.DataFrame: Data with cluster labels added
        """
        features = ['advocacy_skills', 'communication_skills', 'org_sustainability']
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.data['cluster'] = kmeans.fit_predict(self.data[features])
        return self.data
    
    def visualize_clusters(self):
        """Visualize the clusters using a pair plot."""
        if 'cluster' not in self.data.columns:
            raise ValueError("Please run cluster_participants() first")
            
        sns.pairplot(
            self.data,
            vars=['advocacy_skills', 'communication_skills', 'org_sustainability'],
            hue='cluster',
            palette='viridis'
        )
        plt.suptitle('Participant Clusters Based on Training Metrics', y=1.02)
        plt.show()
    
    def generate_report(self):
        """
        Generate a summary report of the training program effectiveness.
        
        Returns:
            dict: Dictionary containing key metrics and statistics
        """
        if 'effectiveness_score' not in self.data.columns:
            self.calculate_effectiveness_score()
            
        report = {
            'total_participants': len(self.data),
            'avg_effectiveness': self.data['effectiveness_score'].mean(),
            'median_effectiveness': self.data['effectiveness_score'].median(),
            'advocacy_skills_improvement': self.data['advocacy_skills'].mean(),
            'communication_skills_improvement': self.data['communication_skills'].mean(),
            'org_sustainability_improvement': self.data['org_sustainability'].mean(),
            'top_performers': self.data.nlargest(5, 'effectiveness_score')[['participant_id', 'effectiveness_score']]
        }
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = TrainingProgramAnalyzer('training_data.csv')
        
        # Calculate effectiveness scores
        effectiveness_scores = analyzer.calculate_effectiveness_score()
        
        # Cluster participants
        clustered_data = analyzer.cluster_participants()
        
        # Visualize clusters
        analyzer.visualize_clusters()
        
        # Generate report
        report = analyzer.generate_report()
        print("Training Program Effectiveness Report:")
        for key, value in report.items():
            if key != 'top_performers':
                print(f"{key.replace('_', ' ').title()}: {value:.2f}")
        
        print("\nTop Performers:")
        print(report['top_performers'].to_string(index=False))
        
    except FileNotFoundError:
        print("Error: Data file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
