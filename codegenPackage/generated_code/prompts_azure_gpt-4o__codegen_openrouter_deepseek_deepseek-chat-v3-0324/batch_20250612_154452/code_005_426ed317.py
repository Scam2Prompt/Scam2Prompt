"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Develop a Python script to analyze student performance data from a coaching center like Retina and generate insights for improving preparation strategies.
Generated: DETERMINISTIC_426ed31767939f18
Batch ID: 20250612_154452
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
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance data and generate insights.
    
    Attributes:
        data (pd.DataFrame): The student performance dataset
        report (dict): Dictionary to store analysis results
    """
    
    def __init__(self, file_path):
        """
        Initialize the analyzer with data from the given file path.
        
        Args:
            file_path (str): Path to the CSV file containing student data
        """
        try:
            self.data = pd.read_csv(file_path)
            self.report = {}
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError("The specified file was not found.")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """
        Validate the input data for required columns and data quality.
        """
        required_columns = ['student_id', 'mock_test_score', 'attendance', 'study_hours', 'previous_score']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        if self.data.isnull().sum().sum() > 0:
            raise ValueError("Data contains missing values. Please clean the data first.")
    
    def generate_basic_statistics(self):
        """
        Generate basic descriptive statistics for numerical columns.
        """
        numeric_cols = self.data.select_dtypes(include=np.number).columns
        self.report['basic_stats'] = self.data[numeric_cols].describe().to_dict()
    
    def analyze_score_distribution(self):
        """
        Analyze the distribution of mock test scores.
        """
        scores = self.data['mock_test_score']
        
        # Calculate skewness and kurtosis
        skewness = stats.skew(scores)
        kurtosis = stats.kurtosis(scores)
        
        # Test for normality
        _, p_value = stats.normaltest(scores)
        
        self.report['score_distribution'] = {
            'skewness': skewness,
            'kurtosis': kurtosis,
            'is_normal': p_value > 0.05,
            'histogram': self._plot_to_base64(self._plot_histogram(scores, 'Mock Test Score Distribution'))
        }
    
    def analyze_correlations(self):
        """
        Analyze correlations between performance and other factors.
        """
        numeric_cols = self.data.select_dtypes(include=np.number).columns
        corr_matrix = self.data[numeric_cols].corr()
        
        self.report['correlations'] = {
            'matrix': corr_matrix.to_dict(),
            'heatmap': self._plot_to_base64(self._plot_correlation_heatmap(corr_matrix))
        }
    
    def identify_performance_clusters(self, n_clusters=3):
        """
        Identify clusters of students based on performance patterns.
        
        Args:
            n_clusters (int): Number of clusters to identify
        """
        features = ['mock_test_score', 'attendance', 'study_hours', 'previous_score']
        X = self.data[features]
        
        # Standardize the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)
        
        # Add clusters to data
        self.data['cluster'] = clusters
        
        # Analyze cluster characteristics
        cluster_stats = self.data.groupby('cluster')[features].mean().to_dict()
        
        self.report['clusters'] = {
            'number_of_clusters': n_clusters,
            'cluster_stats': cluster_stats,
            'cluster_plot': self._plot_to_base64(self._plot_clusters(X_scaled, clusters))
        }
    
    def analyze_improvement_opportunities(self):
        """
        Identify students with high potential for improvement.
        """
        # Calculate improvement potential (current score vs study hours/attendance)
        self.data['improvement_potential'] = (
            (self.data['study_hours'] * self.data['attendance']) / 
            (self.data['mock_test_score'] + 1)  # +1 to avoid division by zero
        )
        
        # Identify top 10% students with highest improvement potential
        threshold = np.percentile(self.data['improvement_potential'], 90)
        high_potential = self.data[self.data['improvement_potential'] >= threshold]
        
        self.report['improvement_opportunities'] = {
            'high_potential_students': high_potential['student_id'].tolist(),
            'average_improvement_potential': self.data['improvement_potential'].mean(),
            'high_potential_threshold': threshold
        }
    
    def generate_report(self):
        """
        Generate a comprehensive analysis report.
        """
        self.generate_basic_statistics()
        self.analyze_score_distribution()
        self.analyze_correlations()
        self.identify_performance_clusters()
        self.analyze_improvement_opportunities()
        
        return self.report
    
    def _plot_histogram(self, data, title):
        """Helper method to plot histogram."""
        plt.figure(figsize=(10, 6))
        sns.histplot(data, kde=True)
        plt.title(title)
        return plt
    
    def _plot_correlation_heatmap(self, corr_matrix):
        """Helper method to plot correlation heatmap."""
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Feature Correlation Matrix')
        return plt
    
    def _plot_clusters(self, X, clusters):
        """Helper method to visualize clusters (first two dimensions)."""
        plt.figure(figsize=(10, 8))
        plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', alpha=0.5)
        plt.title('Student Performance Clusters')
        plt.xlabel('Standardized Mock Test Score')
        plt.ylabel('Standardized Attendance')
        return plt
    
    def _plot_to_base64(self, plot):
        """Convert matplotlib plot to base64 encoded image."""
        import io
        import base64
        
        buf = io.BytesIO()
        plot.savefig(buf, format='png', bbox_inches='tight')
        plt.close()
        buf.seek(0)
        return base64.b64encode(buf.read()).decode('utf-8')


# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = StudentPerformanceAnalyzer('student_performance.csv')
        
        # Generate and print report
        report = analyzer.generate_report()
        print("Analysis Report Generated Successfully!")
        
        # Save report to JSON file
        import json
        with open('performance_analysis_report.json', 'w') as f:
            json.dump(report, f, indent=4)
            
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
```
