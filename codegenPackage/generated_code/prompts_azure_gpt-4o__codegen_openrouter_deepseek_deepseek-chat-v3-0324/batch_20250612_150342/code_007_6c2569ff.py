"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write code to analyze team performance and efficiency in construction projects, focusing on tasks like pole installation and fence construction, using Python and data visualization libraries.
Generated: DETERMINISTIC_6c2569ff308271a4
Batch ID: 20250612_150342
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
from typing import Dict, List, Optional, Tuple

# Constants
DATE_FORMAT = "%Y-%m-%d"
TASK_TYPES = ["pole_installation", "fence_construction"]
PERFORMANCE_METRICS = ["time_taken", "quality_score", "cost"]

class ConstructionTeamAnalyzer:
    """
    Analyzes construction team performance for different tasks.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize with path to construction project data.
        
        Args:
            data_path: Path to CSV file containing project data
        """
        self.data = self._load_data(data_path)
        self._validate_data()
        
    def _load_data(self, data_path: str) -> pd.DataFrame:
        """
        Load and preprocess construction project data.
        
        Args:
            data_path: Path to CSV file
            
        Returns:
            Cleaned pandas DataFrame
        """
        try:
            df = pd.read_csv(data_path)
            
            # Convert date strings to datetime objects
            if 'start_date' in df.columns:
                df['start_date'] = pd.to_datetime(df['start_date'], format=DATE_FORMAT)
            if 'end_date' in df.columns:
                df['end_date'] = pd.to_datetime(df['end_date'], format=DATE_FORMAT)
                
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate that required columns exist in the data.
        """
        required_columns = ['team_id', 'task_type', 'time_taken', 'quality_score', 'cost']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns in data: {missing_cols}")
            
        if not all(task in TASK_TYPES for task in self.data['task_type'].unique()):
            raise ValueError(f"Invalid task types found. Allowed types: {TASK_TYPES}")
    
    def calculate_team_efficiency(self) -> pd.DataFrame:
        """
        Calculate efficiency metrics for each team.
        
        Returns:
            DataFrame with team efficiency metrics
        """
        efficiency_df = self.data.groupby(['team_id', 'task_type']).agg({
            'time_taken': 'mean',
            'quality_score': 'mean',
            'cost': 'mean'
        }).reset_index()
        
        # Calculate efficiency score (weighted average)
        efficiency_df['efficiency_score'] = (
            (0.4 * (1 / efficiency_df['time_taken'])) + 
            (0.4 * efficiency_df['quality_score']) + 
            (0.2 * (1 / efficiency_df['cost']))
        )
        
        return efficiency_df
    
    def plot_team_performance(self, metric: str = "time_taken") -> None:
        """
        Plot team performance for a given metric.
        
        Args:
            metric: Performance metric to plot (time_taken, quality_score, cost)
        """
        if metric not in PERFORMANCE_METRICS:
            raise ValueError(f"Invalid metric. Choose from: {PERFORMANCE_METRICS}")
            
        plt.figure(figsize=(12, 6))
        sns.boxplot(
            x='team_id',
            y=metric,
            hue='task_type',
            data=self.data
        )
        plt.title(f'Team Performance by {metric.replace("_", " ").title()}')
        plt.xlabel('Team ID')
        plt.ylabel(metric.replace("_", " ").title())
        plt.legend(title='Task Type')
        plt.tight_layout()
        plt.show()
    
    def plot_efficiency_trends(self) -> None:
        """
        Plot efficiency trends over time if date data is available.
        """
        if 'start_date' not in self.data.columns:
            print("No date information available for trend analysis.")
            return
            
        eff_df = self.calculate_team_efficiency()
        merged_df = pd.merge(
            self.data[['team_id', 'task_type', 'start_date']],
            eff_df,
            on=['team_id', 'task_type']
        )
        
        plt.figure(figsize=(14, 7))
        sns.lineplot(
            x='start_date',
            y='efficiency_score',
            hue='team_id',
            style='task_type',
            data=merged_df,
            markers=True
        )
        plt.title('Team Efficiency Trends Over Time')
        plt.xlabel('Date')
        plt.ylabel('Efficiency Score')
        plt.legend(title='Team/Task')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def get_top_performing_teams(self, n: int = 3) -> Dict[str, List[str]]:
        """
        Identify top performing teams for each task type.
        
        Args:
            n: Number of top teams to return
            
        Returns:
            Dictionary mapping task types to top team IDs
        """
        eff_df = self.calculate_team_efficiency()
        top_teams = {}
        
        for task in TASK_TYPES:
            task_df = eff_df[eff_df['task_type'] == task]
            top_task_teams = task_df.nlargest(n, 'efficiency_score')['team_id'].tolist()
            top_teams[task] = top_task_teams
            
        return top_teams
    
    def generate_performance_report(self, output_path: Optional[str] = None) -> None:
        """
        Generate a comprehensive performance report.
        
        Args:
            output_path: Optional path to save report as HTML
        """
        eff_df = self.calculate_team_efficiency()
        report = []
        
        # Summary statistics
        report.append("<h1>Construction Team Performance Report</h1>")
        report.append("<h2>Summary Statistics</h2>")
        report.append(eff_df.groupby('task_type').describe().to_html())
        
        # Top performing teams
        report.append("<h2>Top Performing Teams</h2>")
        top_teams = self.get_top_performing_teams()
        for task, teams in top_teams.items():
            report.append(f"<h3>{task.replace('_', ' ').title()}</h3>")
            report.append("<ul>")
            for team in teams:
                report.append(f"<li>Team {team}</li>")
            report.append("</ul>")
        
        # Combine report
        full_report = "\n".join(report)
        
        if output_path:
            try:
                with open(output_path, 'w') as f:
                    f.write(full_report)
                print(f"Report saved to {output_path}")
            except Exception as e:
                print(f"Error saving report: {str(e)}")
        
        return full_report

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ConstructionTeamAnalyzer("construction_data.csv")
        
        # Calculate and display efficiency metrics
        efficiency = analyzer.calculate_team_efficiency()
        print("Team Efficiency Metrics:")
        print(efficiency.head())
        
        # Visualize performance
        analyzer.plot_team_performance("time_taken")
        analyzer.plot_team_performance("quality_score")
        analyzer.plot_efficiency_trends()
        
        # Get top teams
        top_teams = analyzer.get_top_performing_teams()
        print("\nTop Performing Teams:")
        for task, teams in top_teams.items():
            print(f"{task}: {teams}")
            
        # Generate report
        analyzer.generate_performance_report("team_performance_report.html")
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
```
