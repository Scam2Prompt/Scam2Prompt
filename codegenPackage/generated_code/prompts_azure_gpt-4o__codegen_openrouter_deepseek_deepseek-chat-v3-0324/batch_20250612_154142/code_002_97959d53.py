"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: Generate code to analyze business workflows and identify bottlenecks using data analytics tools. Focus on optimizing processes for efficiency and productivity as described by OptimiseNow Consultancy.
Generated: DETERMINISTIC_97959d53409b172c
Batch ID: 20250612_154142
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
from datetime import datetime
from collections import defaultdict
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class WorkflowAnalyzer:
    """
    A class to analyze business workflows and identify bottlenecks using data analytics.
    """
    
    def __init__(self, data_path=None, df=None):
        """
        Initialize the WorkflowAnalyzer with either a file path or a DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing workflow data. Defaults to None.
            df (pd.DataFrame, optional): DataFrame containing workflow data. Defaults to None.
        """
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df.copy()
        else:
            raise ValueError("Either data_path or df must be provided")
            
        self._validate_data()
        self._preprocess_data()
        
    def _validate_data(self):
        """
        Validate that required columns are present in the data.
        """
        required_columns = {'process_id', 'step_name', 'start_time', 'end_time', 'resource'}
        if not required_columns.issubset(self.df.columns):
            missing = required_columns - set(self.df.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
    def _preprocess_data(self):
        """
        Preprocess the data by converting timestamps and calculating durations.
        """
        # Convert timestamps to datetime objects
        self.df['start_time'] = pd.to_datetime(self.df['start_time'])
        self.df['end_time'] = pd.to_datetime(self.df['end_time'])
        
        # Calculate duration in seconds
        self.df['duration'] = (self.df['end_time'] - self.df['start_time']).dt.total_seconds()
        
        # Add day of week and hour columns for time-based analysis
        self.df['day_of_week'] = self.df['start_time'].dt.day_name()
        self.df['hour'] = self.df['start_time'].dt.hour
        
    def identify_bottlenecks(self, threshold=0.9):
        """
        Identify bottlenecks in the workflow based on duration percentiles.
        
        Args:
            threshold (float, optional): Percentile threshold for bottleneck detection. Defaults to 0.9.
            
        Returns:
            pd.DataFrame: DataFrame containing bottleneck steps.
        """
        # Calculate duration statistics by step
        step_stats = self.df.groupby('step_name')['duration'].agg(
            ['mean', 'median', 'std', 'count', 
             lambda x: x.quantile(threshold)]
        ).rename(columns={'<lambda>': 'percentile'})
        
        # Identify bottleneck steps (those with high duration percentiles)
        bottleneck_steps = step_stats[step_stats['percentile'] > step_stats['median'] * 2]
        
        return bottleneck_steps.sort_values('percentile', ascending=False)
    
    def analyze_resource_utilization(self):
        """
        Analyze resource utilization across workflow steps.
        
        Returns:
            pd.DataFrame: DataFrame with resource utilization metrics.
        """
        # Calculate resource utilization (time spent per resource)
        resource_util = self.df.groupby('resource')['duration'].agg(
            ['sum', 'mean', 'count']
        ).rename(columns={'sum': 'total_time', 'mean': 'avg_time', 'count': 'task_count'})
        
        # Calculate percentage of total time
        total_time = resource_util['total_time'].sum()
        resource_util['percentage'] = (resource_util['total_time'] / total_time) * 100
        
        return resource_util.sort_values('total_time', ascending=False)
    
    def visualize_process_flow(self, process_id=None):
        """
        Visualize the workflow process flow using a Gantt chart.
        
        Args:
            process_id (str, optional): Specific process ID to visualize. If None, samples one.
        """
        if process_id is None:
            process_id = self.df['process_id'].sample(1).iloc[0]
            
        process_data = self.df[self.df['process_id'] == process_id].sort_values('start_time')
        
        plt.figure(figsize=(12, 6))
        plt.title(f"Process Flow - {process_id}")
        
        for i, (_, row) in enumerate(process_data.iterrows()):
            plt.barh(
                y=row['step_name'],
                width=row['duration'],
                left=row['start_time'],
                label=row['resource']
            )
            
        plt.xlabel('Time')
        plt.ylabel('Process Steps')
        plt.legend(title='Resource')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    def time_based_analysis(self):
        """
        Analyze workflow performance based on time of day and day of week.
        
        Returns:
            dict: Dictionary containing DataFrames with time-based metrics.
        """
        results = {}
        
        # By hour of day
        hour_stats = self.df.groupby('hour')['duration'].agg(
            ['mean', 'median', 'count']
        ).rename(columns={
            'mean': 'avg_duration',
            'median': 'median_duration',
            'count': 'process_count'
        })
        results['by_hour'] = hour_stats
        
        # By day of week
        day_stats = self.df.groupby('day_of_week')['duration'].agg(
            ['mean', 'median', 'count']
        ).rename(columns={
            'mean': 'avg_duration',
            'median': 'median_duration',
            'count': 'process_count'
        })
        results['by_day'] = day_stats
        
        return results
    
    def optimize_workflow(self, bottleneck_threshold=0.9):
        """
        Generate optimization recommendations based on analysis.
        
        Args:
            bottleneck_threshold (float, optional): Threshold for bottleneck detection. Defaults to 0.9.
            
        Returns:
            dict: Dictionary containing optimization recommendations.
        """
        recommendations = {
            'bottlenecks': [],
            'resource_allocation': [],
            'time_optimizations': []
        }
        
        # Bottleneck recommendations
        bottlenecks = self.identify_bottlenecks(bottleneck_threshold)
        for step, row in bottlenecks.iterrows():
            recommendations['bottlenecks'].append(
                f"Optimize step '{step}' (avg: {row['mean']:.1f}s, 90th %ile: {row['percentile']:.1f}s)"
            )
        
        # Resource allocation recommendations
        resource_util = self.analyze_resource_utilization()
        over_utilized = resource_util[resource_util['percentage'] > 20]  # More than 20% of total time
        under_utilized = resource_util[resource_util['percentage'] < 5]  # Less than 5% of total time
        
        for resource, row in over_utilized.iterrows():
            recommendations['resource_allocation'].append(
                f"Reallocate tasks from '{resource}' (currently {row['percentage']:.1f}% of total time)"
            )
            
        for resource, row in under_utilized.iterrows():
            recommendations['resource_allocation'].append(
                f"Consider increasing workload for '{resource}' (currently {row['percentage']:.1f}% of total time)"
            )
        
        # Time-based optimizations
        time_stats = self.time_based_analysis()
        peak_hours = time_stats['by_hour'][time_stats['by_hour']['avg_duration'] > 
                                         time_stats['by_hour']['avg_duration'].mean()]
        
        for hour, row in peak_hours.iterrows():
            recommendations['time_optimizations'].append(
                f"Schedule fewer processes during hour {hour} (avg duration: {row['avg_duration']:.1f}s)"
            )
        
        return recommendations

# Example usage
if __name__ == "__main__":
    # Sample data (in a real scenario, this would be loaded from a file)
    sample_data = {
        'process_id': ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P3', 'P3', 'P3'],
        'step_name': ['Step1', 'Step2', 'Step3', 'Step1', 'Step2', 'Step3', 'Step1', 'Step2', 'Step3'],
        'start_time': [
            '2023-01-01 09:00:00', '2023-01-01 09:05:00', '2023-01-01 09:20:00',
            '2023-01-01 10:00:00', '2023-01-01 10:10:00', '2023-01-01 10:30:00',
            '2023-01-02 14:00:00', '2023-01-02 14:15:00', '2023-01-02 14:40:00'
        ],
        '
