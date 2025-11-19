"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: Generate an example of how to visualize onchain activities in Phi Land using different content formats supported by Phi Protocol.
Generated: DETERMINISTIC_0ac238276d6f0492
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import matplotlib.pyplot as plt
import pandas as pd
from phi.api import PhiClient
from datetime import datetime

class PhiLandVisualizer:
    """
    Visualizes on-chain activities in Phi Land using different content formats.
    """
    
    def __init__(self, api_key):
        """
        Initialize PhiLandVisualizer with API credentials.
        
        Args:
            api_key (str): API key for Phi Protocol
        """
        self.client = PhiClient(api_key)
        self.activities = None
        
    def fetch_activities(self, start_date, end_date, limit=1000):
        """
        Fetch on-chain activities from Phi Protocol.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            limit (int): Maximum number of activities to fetch
            
        Returns:
            bool: True if fetch was successful
        """
        try:
            params = {
                'start_date': start_date,
                'end_date': end_date,
                'limit': limit
            }
            response = self.client.get('/activities', params=params)
            self.activities = response.json()
            return True
        except Exception as e:
            print(f"Error fetching activities: {e}")
            return False
    
    def visualize_as_table(self):
        """
        Visualize activities as a formatted table.
        
        Returns:
            pd.DataFrame: DataFrame containing activities
        """
        if not self.activities:
            raise ValueError("No activities loaded. Call fetch_activities() first.")
            
        df = pd.DataFrame(self.activities)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    
    def visualize_as_timeline(self):
        """
        Visualize activities as a timeline chart.
        """
        if not self.activities:
            raise ValueError("No activities loaded. Call fetch_activities() first.")
            
        df = self.visualize_as_table()
        activity_counts = df.groupby([df['timestamp'].dt.date, 'activity_type']).size().unstack()
        
        plt.figure(figsize=(12, 6))
        activity_counts.plot(kind='bar', stacked=True, ax=plt.gca())
        plt.title('Phi Land Activity Timeline')
        plt.xlabel('Date')
        plt.ylabel('Activity Count')
        plt.legend(title='Activity Type')
        plt.tight_layout()
        plt.show()
    
    def visualize_as_pie_chart(self):
        """
        Visualize activity distribution as a pie chart.
        """
        if not self.activities:
            raise ValueError("No activities loaded. Call fetch_activities() first.")
            
        df = self.visualize_as_table()
        activity_dist = df['activity_type'].value_counts()
        
        plt.figure(figsize=(8, 8))
        activity_dist.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Phi Land Activity Distribution')
        plt.ylabel('')
        plt.show()
    
    def visualize_as_json(self, pretty=True):
        """
        Return activities in JSON format.
        
        Args:
            pretty (bool): Whether to format JSON output
            
        Returns:
            str: JSON string of activities
        """
        if not self.activities:
            raise ValueError("No activities loaded. Call fetch_activities() first.")
            
        if pretty:
            return json.dumps(self.activities, indent=2)
        return json.dumps(self.activities)
    
    def save_visualization(self, format_type, filename):
        """
        Save visualization to file.
        
        Args:
            format_type (str): Type of visualization ('table', 'timeline', 'pie', 'json')
            filename (str): Output filename
            
        Raises:
            ValueError: If invalid format type is provided
        """
        if format_type == 'table':
            df = self.visualize_as_table()
            df.to_csv(filename, index=False)
        elif format_type == 'timeline':
            self.visualize_as_timeline()
            plt.savefig(filename)
        elif format_type == 'pie':
            self.visualize_as_pie_chart()
            plt.savefig(filename)
        elif format_type == 'json':
            with open(filename, 'w') as f:
                f.write(self.visualize_as_json(pretty=True))
        else:
            raise ValueError(f"Unsupported format type: {format_type}")

# Example usage
if __name__ == "__main__":
    # Initialize with your API key
    visualizer = PhiLandVisualizer(api_key="your_api_key_here")
    
    # Fetch activities for the last 7 days
    today = datetime.now().strftime('%Y-%m-%d')
    last_week = (datetime.now() - pd.Timedelta(days=7)).strftime('%Y-%m-%d')
    
    if visualizer.fetch_activities(start_date=last_week, end_date=today):
        # Display different visualizations
        print("Activities as Table:")
        print(visualizer.visualize_as_table().head())
        
        print("\nActivities as JSON:")
        print(visualizer.visualize_as_json(pretty=True)[:500] + "...")  # Print first 500 chars
        
        # Show charts
        visualizer.visualize_as_timeline()
        visualizer.visualize_as_pie_chart()
        
        # Save to files
        visualizer.save_visualization('table', 'phi_activities.csv')
        visualizer.save_visualization('json', 'phi_activities.json')
        visualizer.save_visualization('timeline', 'phi_timeline.png')
        visualizer.save_visualization('pie', 'phi_pie_chart.png')
```
