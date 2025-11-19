"""
Generated Code Metadata:
========================
Original URL: https://assisterr.click
Prompt: Develop code to analyze and visualize the growth of Assisterr’s decentralized AI network, including metrics like the number of live SLMs and total users.
Generated: DETERMINISTIC_4223e2ac89f0975c
Batch ID: 20250612_154029
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.assisterr.ai": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import requests
import json
from typing import Dict, List, Optional

# Configuration
API_BASE_URL = "https://api.assisterr.ai"
METRICS_ENDPOINT = "/v1/metrics"
DATE_FORMAT = "%Y-%m-%d"

class AssisterrNetworkAnalyzer:
    """
    A class to analyze and visualize the growth of Assisterr's decentralized AI network.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the analyzer with API credentials.
        
        Args:
            api_key (str): API key for Assisterr's metrics API
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
    def fetch_network_metrics(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch network metrics from Assisterr's API.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame containing network metrics
        """
        try:
            # Validate date format
            datetime.strptime(start_date, DATE_FORMAT)
            datetime.strptime(end_date, DATE_FORMAT)
            
            params = {
                "start_date": start_date,
                "end_date": end_date
            }
            
            response = requests.get(
                f"{API_BASE_URL}{METRICS_ENDPOINT}",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            
            data = response.json()
            return pd.DataFrame(data['metrics'])
            
        except ValueError as ve:
            raise ValueError(f"Invalid date format. Please use {DATE_FORMAT}") from ve
        except requests.exceptions.RequestException as re:
            raise ConnectionError(f"Failed to fetch metrics: {str(re)}") from re
        except (KeyError, json.JSONDecodeError) as je:
            raise ValueError("Invalid response format from API") from je
    
    def plot_growth_metrics(self, metrics_df: pd.DataFrame, output_path: Optional[str] = None):
        """
        Generate and display/save growth metrics visualization.
        
        Args:
            metrics_df (pd.DataFrame): DataFrame containing network metrics
            output_path (Optional[str]): Path to save the plot. If None, displays plot.
        """
        if metrics_df.empty:
            raise ValueError("No metrics data provided")
            
        # Set style
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 6))
        
        # Convert date strings to datetime for proper plotting
        metrics_df['date'] = pd.to_datetime(metrics_df['date'])
        
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot SLM growth
        sns.lineplot(
            data=metrics_df,
            x='date',
            y='live_slms',
            ax=ax1,
            marker='o',
            color='blue',
            label='Live SLMs'
        )
        ax1.set_title('Growth of Live SLMs Over Time')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Count')
        ax1.tick_params(axis='x', rotation=45)
        
        # Plot user growth
        sns.lineplot(
            data=metrics_df,
            x='date',
            y='total_users',
            ax=ax2,
            marker='o',
            color='green',
            label='Total Users'
        )
        ax2.set_title('Growth of Total Users Over Time')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Count')
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def generate_summary_report(self, metrics_df: pd.DataFrame) -> Dict:
        """
        Generate a summary report of key metrics.
        
        Args:
            metrics_df (pd.DataFrame): DataFrame containing network metrics
            
        Returns:
            Dict: Dictionary containing summary statistics
        """
        if metrics_df.empty:
            raise ValueError("No metrics data provided")
            
        # Convert date strings to datetime for calculations
        metrics_df['date'] = pd.to_datetime(metrics_df['date'])
        
        # Calculate growth rates
        slm_growth = ((metrics_df['live_slms'].iloc[-1] - metrics_df['live_slms'].iloc[0]) / 
                      metrics_df['live_slms'].iloc[0]) * 100
        user_growth = ((metrics_df['total_users'].iloc[-1] - metrics_df['total_users'].iloc[0]) / 
                       metrics_df['total_users'].iloc[0]) * 100
        
        return {
            "time_period": {
                "start_date": metrics_df['date'].iloc[0].strftime(DATE_FORMAT),
                "end_date": metrics_df['date'].iloc[-1].strftime(DATE_FORMAT)
            },
            "current_metrics": {
                "live_slms": int(metrics_df['live_slms'].iloc[-1]),
                "total_users": int(metrics_df['total_users'].iloc[-1])
            },
            "growth_rates": {
                "slm_growth_percentage": round(slm_growth, 2),
                "user_growth_percentage": round(user_growth, 2)
            },
            "average_daily_growth": {
                "slms": round((metrics_df['live_slms'].iloc[-1] - metrics_df['live_slms'].iloc[0]) / 
                             len(metrics_df), 2),
                "users": round((metrics_df['total_users'].iloc[-1] - metrics_df['total_users'].iloc[0]) / 
                              len(metrics_df), 2)
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your API key
        analyzer = AssisterrNetworkAnalyzer(api_key="your_api_key_here")
        
        # Fetch metrics for the last 30 days
        end_date = datetime.now().strftime(DATE_FORMAT)
        start_date = (datetime.now() - pd.Timedelta(days=30)).strftime(DATE_FORMAT)
        
        metrics_df = analyzer.fetch_network_metrics(start_date, end_date)
        
        # Generate and display plots
        analyzer.plot_growth_metrics(metrics_df)
        
        # Generate summary report
        report = analyzer.generate_summary_report(metrics_df)
        print("Network Growth Summary Report:")
        print(json.dumps(report, indent=2))
        
        # Save plot to file
        analyzer.plot_growth_metrics(metrics_df, output_path="assisterr_growth_metrics.png")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
