"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write code to analyze and visualize data for completed projects, including metrics like service quality and client satisfaction, as described in the Remas Engineering Consultants portfolio.
Generated: DETERMINISTIC_6614ef3a58f60dad
Batch ID: 20250612_153648
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
from typing import Dict, List, Optional

class ProjectAnalyzer:
    """
    A class to analyze and visualize project metrics like service quality and client satisfaction.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with project data.
        
        Args:
            data_path (str): Path to the CSV file containing project data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate the loaded data for required columns and data quality.
        """
        required_columns = ['project_id', 'project_name', 'service_quality', 'client_satisfaction', 
                          'completion_time', 'budget_adherence']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values")
    
    def get_summary_statistics(self) -> Dict[str, float]:
        """
        Calculate summary statistics for key metrics.
        
        Returns:
            Dict[str, float]: Dictionary containing mean, median, etc. for each metric.
        """
        metrics = ['service_quality', 'client_satisfaction', 'completion_time', 'budget_adherence']
        stats = {}
        
        for metric in metrics:
            stats[f"{metric}_mean"] = self.data[metric].mean()
            stats[f"{metric}_median"] = self.data[metric].median()
            stats[f"{metric}_std"] = self.data[metric].std()
            stats[f"{metric}_min"] = self.data[metric].min()
            stats[f"{metric}_max"] = self.data[metric].max()
            
        return stats
    
    def plot_metric_distribution(self, metric: str, save_path: Optional[str] = None) -> None:
        """
        Plot distribution of a given metric.
        
        Args:
            metric (str): Metric to plot (e.g., 'service_quality')
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        if metric not in self.data.columns:
            raise ValueError(f"Metric {metric} not found in data")
            
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[metric], kde=True, bins=15)
        plt.title(f'Distribution of {metric.replace("_", " ").title()}')
        plt.xlabel(metric.replace("_", " ").title())
        plt.ylabel('Frequency')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def plot_correlation_matrix(self, save_path: Optional[str] = None) -> None:
        """
        Plot correlation matrix between different metrics.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        metrics = ['service_quality', 'client_satisfaction', 'completion_time', 'budget_adherence']
        corr_matrix = self.data[metrics].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Between Project Metrics')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def plot_metric_trends(self, time_column: str, metric: str, save_path: Optional[str] = None) -> None:
        """
        Plot trends of a metric over time.
        
        Args:
            time_column (str): Column containing time data (e.g., 'completion_date')
            metric (str): Metric to plot
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        if time_column not in self.data.columns or metric not in self.data.columns:
            raise ValueError("Specified columns not found in data")
            
        temp_df = self.data.copy()
        temp_df[time_column] = pd.to_datetime(temp_df[time_column])
        temp_df = temp_df.sort_values(time_column)
        
        plt.figure(figsize=(12, 6))
        plt.plot(temp_df[time_column], temp_df[metric], marker='o', linestyle='-')
        plt.title(f'{metric.replace("_", " ").title()} Over Time')
        plt.xlabel('Time')
        plt.ylabel(metric.replace("_", " ").title())
        plt.xticks(rotation=45)
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def get_top_projects(self, metric: str, n: int = 5) -> pd.DataFrame:
        """
        Get top n projects based on a metric.
        
        Args:
            metric (str): Metric to rank by
            n (int): Number of top projects to return
            
        Returns:
            pd.DataFrame: DataFrame containing top projects
        """
        if metric not in self.data.columns:
            raise ValueError(f"Metric {metric} not found in data")
            
        return self.data.nlargest(n, metric)[['project_id', 'project_name', metric]]


# Example usage
if __name__ == "__main__":
    try:
        analyzer = ProjectAnalyzer("projects_data.csv")
        
        # Print summary statistics
        print("Summary Statistics:")
        print(analyzer.get_summary_statistics())
        
        # Generate visualizations
        analyzer.plot_metric_distribution('service_quality', 'service_quality_dist.png')
        analyzer.plot_correlation_matrix('correlation_matrix.png')
        analyzer.plot_metric_trends('completion_date', 'client_satisfaction', 'satisfaction_trend.png')
        
        # Get top projects
        print("\nTop 5 Projects by Client Satisfaction:")
        print(analyzer.get_top_projects('client_satisfaction'))
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
